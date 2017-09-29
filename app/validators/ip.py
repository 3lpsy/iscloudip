import ipaddress

from .common import CommonValidator
from app.exceptions import ValidatorException

class IpValidator(CommonValidator):

    @classmethod
    def validate(self, ip):
        try:
            ip = ipaddress.ip_address(ip)
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError) as e:
            raise ValidatorException("Invalid IP: {}".format(cidr))
