from .aws import AwsProvider
from .azure import AzureProvider

def provider_loader():
    providers = []
    providers.append(AwsProvider)
    providers.append(AzureProvider)
    # do fancy imports based on config for custom providers?
    # check for conflicting names
    return providers
