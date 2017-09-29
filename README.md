# Check IPs against Official Cloud Provider IP Ranges

The iscloudip app a command line python application that allows you to search Cloud Provider's publicly listed IP ranges to determine if a given IP falls within their network.

This is useful for determining who the hosting provider of different web applications. While a typically method of completing this task could be to check DNS records, this instead app relies on lists of IP ranges publicly provided by Cloud Services.

The tools requires python3 but does not require any additional pip packages so setting up a virtualenv or pulling 3rd party code will not be required. In addition, the package itself will create a local sqlite database and cache the IP ranges in order to make searching faster.


## Help

```
usage: main.py [-h] [-i IP] [--ranges] [-s] [-p PROVIDER] [-f] [-c]
               [--list-providers] [--debug] [-v] [--silent] [--drop]

A Command Line Application to Compare an IP Against a Cloud Provider's publicly available list of IPs

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IP/Range
  --ranges              List Available IP Ranges
  -s, --sync            Sync Provider
  -p PROVIDER, --provider PROVIDER
                        Provider
  -f, --force           Force Installation
  -c, --clear           Clear Database Cache
  --list-providers      List Available Providers
  --debug               Debug Mode
  -v, --verbose         Verbose Mode
  --silent              Silent Mode
  --drop                Drop Databases
  ```

## Example

```
$ python3 main.py -h

# search for an IP
# on the first one, the app will ask you if you want to sync
$ python3 main.py -i 52.222.128.3
You have no ranges loaded in your database. Do you want to sync? [y/n] y
Syncing All Providers
Clearing Provider Ranges: aws
... 0 Ranges Cleared
Syncing Provider: aws
... 909 Ranges Pulled
... 909 Ranges Saved
Clearing Provider Ranges: azure
... 0 Ranges Cleared
Syncing Provider: azure
... 3469 Ranges Pulled
... 3469 Ranges Saved
Found: 52.222.128.0/17 (AWS) GLOBAL: AMAZON

# search for an ip with a specific providers
$ python3 main.py -i 52.222.128.3 -p aws

# list available providers
$ python3 main.py --list-providers
Provider: aws | Amazon Web Services
Provider: azure | Azure Cloud Hosting

# manually sync all providers
$ python3 main.py -s

# sync a specific provider
$ python3 main.py -s -p aws

# list all ranges currently in the database
$ python3 main.py --ranges

# list all ranges for a provider
$ python3 main.py --ranges -p -azure

# clear cached database of ip ranges
$ python3 main.py --clear

# drop database tables
$ python3 main.py --drop

```

# TODO

- [ ] Update Comments
- [ ] Use logger service instead of print
- [ ] Incorporate verbosity
- [ ] Provide file logging for debugging
- [ ] Allow setting up a manual provider
- [ ] Allow manually importing IPs to manual provider
- [ ] Let user import their own python3 providers
- [ ] Let user configure whether to clear cache on sync or not
