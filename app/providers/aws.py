from .common import CommonProvider

class AwsProvider(CommonProvider):
    name = 'aws'
    description = "Amazon Web Services"
    data_url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    data_format = 'json'

    def _parse_one(self, unparsed):
        parsed = {}
        parsed['cidr'] = unparsed['ip_prefix']
        parsed['description'] = "{}: {}".format(unparsed['region'], unparsed['service'])
        parsed['provider'] = self.name
        if 'ipv6_prefix' in unparsed:
            parsed['ip_version'] = 'ipv6'
        else:
            parsed['ip_version'] = 'ipv4'
        return parsed

    def parse_data(self, data):
        prefixes = data['prefixes']
        parsed_data = []
        for prefix in prefixes:
            parsed_data.append(self._parse_one(prefix))
        return parsed_data
