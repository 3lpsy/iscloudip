from .common import CommonProvider

class AwsProvider(CommonProvider):
    name = 'aws'
    description = "Amazon Web Services"
    data_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    data_format = 'json'

    def parse_datum(self, unparsed):
        parsed = {}
        parsed['cidr'] = unparsed['ip_prefix']
        parsed['description'] = "{}: {} - {}".format(self.name.upper(), unparsed['service'], unparsed['region'])
        parsed['provider'] = self.name
        if 'ipv6_prefix' in unparsed:
            parsed['ip_version'] = 'ipv6'
        else:
            parsed['ip_version'] = 'ipv4'
        return parsed

    def parse_data(self, data):
        prefixes = data['prefixes']
        data = []
        for prefix in prefixes:
            data.append(self.parse_datum(prefix))
        return data
