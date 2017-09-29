from .aws import AwsProvider
from .azure import AzureProvider

def default_loader():
    providers = []
    providers.append(AwsProvider)
    providers.append(AzureProvider)
    # do fancy imports based on config for custom providers?
    # check for conflicting names
    return providers

def custom_loader():
    return []
