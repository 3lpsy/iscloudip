from app.providers import default_loader
from app.db import db

class ProviderManager(object):
    def __init__(self):
        self.providers = {}

    def get(self, name):
        return self.providers[name]

    def all(self):
        return self.providers

    def get_names(self):
        names = []
        for key, val in self.providers.items():
            names.append(key)
        return names

    def load_default_providers(self):
        defaults = default_loader()
        for provider in defaults:
            self.register_provider(provider())

    def load_custom_providers(self):
        return

    def register_provider(self, provider):
        if not db.provider_exists(provider.name):
            db.add_provider(provider.name, provider.description)
        self.providers[provider.name] = provider
