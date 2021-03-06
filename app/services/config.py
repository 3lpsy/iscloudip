
class Config(object):
    def __init__(self, data=None):
        self.data = data or {}

    def load(self, data):
        for key, value in data.items():
            self.data[key] = value

    def get(self, key, default='NOT_SET'):
        if key not in self.data and default != 'NOT_SET':
            raise Exception("Error: Config Key {} Does Not Exist".format(key))
        elif key not in self.data:
            return default
        return self.data[key]

    def set(self, key, value):
        self.data[key] = value
        return value
