import requests
from app.utils import str_to_xml

class CommonProvider(object):
    def pull_data(self):
        r = requests.get(self.data_url)
        data_format = self.data_format
        if data_format == 'json':
            return self._parse_json_request(r)
        if data_format == 'xml':
            return self._parse_xml_request(r)
        return r.text

    def get_ranges(self):
        raw_data = self.pull_data()
        parsed_data = self.parse_data(raw_data)
        return parsed_data

    def _parse_json_request(self, r):
        return r.json()

    def _parse_xml_request(self, r):
        return str_to_xml(r.text)
