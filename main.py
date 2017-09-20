#!/bin/bash/python3

import argparse
import os
import sys
from app.app import App

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

def get_db_path():
    return os.path.join(get_data_dir(),  "db/db.sqlite")


def get_args():
    parser = argparse.ArgumentParser(description='A solar system wide communication protocol')
    parser.add_argument('-i', '--ip', help='IP/CIDR')
    parser.add_argument('-l', '--list', action='store_true', help='List Available Providers')
    parser.add_argument('-s', '--sync', help='Sync Provider', action='store_true')
    parser.add_argument('-p', '--provider', help='Provider', default="aws")
    parser.add_argument('-f', '--force', action='store_true', help='Force Installation')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose')
    parser.add_argument('-c', '--clear', help='Clear Database Cache')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug Mode')
    parser.add_argument('--drop', action='store_true', help='Drop Databases')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    load = not args.drop
    config = {
        "DEBUG": args.debug or False,
        "FORCE": args.force or False,
        "VERBOSE": args.verbose or False,
        "DATA_DIR": get_data_dir(),
        "DB_PATH": get_db_path(),
        "LOAD": load
    }

    if args.drop:
        app = App(config)
        sys.exit(app.drop_all())
    else:
        app = App(config)


    if args.sync:
        if not args.provider:
            app.sync_all()
        else:
            provider = args.provider
            sys.exit(app.sync(provider))
    elif args.clear:
        if not args.provider:
            app.clear_all()
        else:
            provider = args.provider
            sys.exit(app.clear(provider))
    elif args.list:
        sys.exit(app.list())
    elif not args.ip:
        sys.exit(print("Please enter an IP or CIDR", file=sys.stderr))
    else:
        sys.exit(app.check(ip, args.provider))
