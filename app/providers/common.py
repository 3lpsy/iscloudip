import requests

class CommonProvider(object):

    def pull_data(self):
        r = requests.get(self.data_url)
        form = self.data_format
        if form == 'json':
            return r.json()

    def get_ranges(self):
        raw_data = self.pull_data()
        parsed_data = self.parse_data(raw_data)
        return parsed_data
