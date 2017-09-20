from .store import Store
from .config import Config
from .providers import provider_loader

class App(object):
    def __init__(self, data=None):
        self.config = Config(data)
        self.db = Store(self.conf('DB_PATH'), force=self.conf('FORCE', default=False), debug=self.conf("DEBUG", default="False"), migrate= self.conf("LOAD"))
        self.providers = {}
        if self.conf("LOAD"):
            self.collect_providers()

    def collect_providers(self):
        for provider in provider_loader():
            self.add_provider(provider())

    def get_providers(self):
        return self.providers

    def get_provider(self, name):
        return self.providers[name]

    def conf(self, key, value='NOT_SET', default='NOT_SET'):
        # using NOT_SET is not a great a approach
        if value != 'NOT_SET':
            return self.config.set(key, value)
        if default == 'NOT_SET':
            default = None
        return self.config.get(key, default)

    # External Commands
    def add_provider(self, provider):
        if not self.db.provider_exists(provider.name):
            self.db.add_provider(provider.name, provider.description)
        self.providers[provider.name] = provider

    def sync_all(self):
        for provider in self.get_providers():
            self.sync(provider.name)
        return True

    def sync(self, name):
        provider = self.get_provider(name)
        ranges = provider.get_ranges()
        self.db.add_ranges(ranges)
        return True

    def clear_all(self):
        for provider in self.get_providers():
            self.clear(provider)
        return True

    def clear(self, name):
        provider = self.get_provider(name)
        self.db.clear_provider_ranges(name)
        return True

    def drop_all(self):
        self.db.drop_all()
