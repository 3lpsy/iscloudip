# Check IPs agains Official Cloud Provider IP Ranges


## Help

```
usage: main.py [-h] [-i IP] [-s] [-p PROVIDER] [-f FORCE] [-v VERBOSE]
               [-c CLEAR] [--drop] [-d]

A solar system wide communication protocol

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        IP/CIDR
  -s, --sync            Sync Provider
  -p PROVIDER, --provider PROVIDER
                        Provider
  -f FORCE, --force FORCE
                        Force Installation
  -v VERBOSE, --verbose VERBOSE
                        Verbose
  -c CLEAR, --clear CLEAR
                        Clear Database Cache
  --drop                Drop Databases
  -d, --debug           Debug Mode
  ```

## Example

```
$ python3 main.py -h

# sync a single provider's ranges
$ python3 main.py --sync --provider aws

# clear cached database of ip ranges

$ python3 main.py --clear

# drop database tables

$ python3 main.py --drop

$ python3 main.py -i 127.0.0.1 -p aws # not implemented
```
