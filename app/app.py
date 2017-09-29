from .enums import verbosities
from .validators import IpValidator, CidrValidator, Ipv4Validator, Ipv6Validator
from .exceptions import NotImplementedException
from .utils import find_ip_in_ranges
from .logger import logger
from .db import db
from .config import config
from .provider import provider_manager
from .utils import confirm
class App(object):
    def __init__(self, data=None):
        config.load(data)
        db.load(config.get('DB_PATH'), force=config.get('FORCE', default=False), debug=config.get("DEBUG", default="False"), migrate= config.get("LOAD"))
        if config.get("DEBUG") == True:
            logger.level = verbosities.DEBUG
        elif config.get("VERBOSE") == True:
            logger.level = verbosities.VERBOSE
        elif config.get("SILENT") == True:
            logger.level = verbosities.SILENT
        else:
            logger.level = verbosities.INFO
        logger.path = config.get("DATA_DIR")
        if config.get("LOAD"):
            provider_manager.load_default_providers()
            provider_manager.load_custom_providers()
        if db.get_ranges_count() < 1:
            if config.get('FORCE') or confirm("You have no ranges loaded in your database. Do you want to sync?"):
                self.sync_all()
    # External Commands
    def find(self, ip, provider=None):
        if IpValidator.is_valid(ip):
            return self.find_ip(ip, provider)
        elif CidrValidator.is_valid(ip):
            return self.find_cidr(ip, provider)
        raise Exception("Invalid IP or CIDR")

    def find_ip(self, ip, provider=None):
        if provider:
            ranges = db.get_ranges(provider=provider)
        else:
            ranges = db.get_ranges()
        ip_range = find_ip_in_ranges(ip, ranges)
        if not ip_range:
            logger.not_found_ip(ip, provider)
        if ip_range:
            logger.found_ip(ip_range)

    def find_cidr(self, cidr, provider=None):
        raise NotImplementedException("find_cidr")

    def sync_all(self):
        logger.log("Syncing All Providers")
        for name in provider_manager.get_names():
            self.sync(name)
        return True

    def sync(self, name):
        self.clear(name)
        logger.log("Syncing Provider: {}".format(name))
        provider = provider_manager.get(name)
        ranges = provider.get_ranges()
        logger.log("... {} Ranges Pulled".format(len(ranges)))
        db.add_ranges(ranges)
        count = db.get_ranges_count(name)
        logger.log("... {} Ranges Saved".format(count))
        return True

    def clear_all(self):
        logger.log("Clearing All Provider Ranges")
        for name in provider_manager.get_names():
            self.clear(name)
        return True

    def clear(self, name):
        logger.log("Clearing Provider Ranges: {}".format(name))
        count = db.get_ranges_count(name)
        provider = provider_manager.get(name)
        logger.log("... {} Ranges Cleared".format(count))
        db.clear_provider_ranges(name)
        return True

    def drop_all(self):
        db.drop_all()

    def list_providers(self):
        for name, provider in provider_manager.all().items():
            self.list_provider(name)
        return True

    def list_provider(self, name):
        provider = provider_manager.get(name)
        logger.loaded_provider(provider)
        return True

    def list_ranges(self, provider = None):
        if provider:
            ranges = db.get_ranges(provider=provider)
        else:
            ranges = db.get_ranges()
        for ip_range in ranges:
            logger.output(ip_range)
