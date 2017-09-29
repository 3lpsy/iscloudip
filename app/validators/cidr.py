import ipaddress

from .common import CommonValidator

class CidrValidator(CommonValidator):

    @classmethod
    def validate(self, cidr):
        try:
            network = ipaddress.ip_network(cidr)
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError) as e:
            raise ValidatorException("Invalid CIDR: {}".format(cidr))
