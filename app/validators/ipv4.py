import ipaddress

from .common import CommonValidator
from app.exceptions import ValidatorException

class Ipv4Validator(CommonValidator):

    @classmethod
    def validate(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            if ip.__class__.__name__ != 'IPv4Address':
                raise ValidatorException("Invalid IPV4: {}".format(ip))
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError) as e:
            raise ValidatorException("Invalid IPV4: {}".format(ip))
