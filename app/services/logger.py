
class Logger(object):
    def __init__(self, path=None, level=0):
        self.path = path
        self.level = level

    def log(self, message, level=None):
        message_level = self.level
        if level:
            message_level = level
        if message_level > 0:
            print(message)

    def range(self, ip_range):
        self.log(self.format_range(ip_range))

    def format_range(self, ip_range):
        return "{} ({}) {}".format(ip_range['cidr'], ip_range['provider'].upper(), ip_range['description'])

    def loaded_provider(self, provider):
        self.log("Provider: {} | {}".format(provider.name, provider.description))

    def found_ip(self, ip_range):
            self.log("Found: " + self.format_range(ip_range))

    def not_found_ip(self, ip, provider=None):
        if provider:
            self.log("Not Found: {} in Provider {}".format(ip, provider))
        else:
            self.log("Not Found: {}".format(ip))
