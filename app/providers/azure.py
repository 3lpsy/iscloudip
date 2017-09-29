from .common import CommonProvider
from app.utils import print_xml_elem
class AzureProvider(CommonProvider):
    name = 'azure'
    description = "Azure Cloud Hosting"
    data_url = "https://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPs_20170925.xml"
    data_format = "xml"


    def parse_data(self, data):
        public_ip_address = data
        parsed_data = []
        for region in public_ip_address.getchildren():
            region_name = region.get('Name')
            for ip_range in region.getchildren():
                cidr = ip_range.get("Subnet")
                parsed = {}
                parsed['cidr'] = cidr
                parsed['description'] = "{}".format(region_name)
                parsed['provider'] = self.name
                parsed['ip_version'] = 'ipv4'
                parsed_data.append(parsed)
        return parsed_data
