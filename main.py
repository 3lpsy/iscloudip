#!/usr/bin/env python3

import argparse
import os
import sys

from app.app import App

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

def get_db_path():
    return os.path.join(get_data_dir(),  "db.sqlite")

def get_parser():
    parser = argparse.ArgumentParser(description='A Command Line Application to Compare an IP Against a Cloud Provider\'s publicly available list of IPs')
    parser.add_argument('-i', '--ip', help='IP/Range')
    parser.add_argument('--ranges', action='store_true', help='List Available IP Ranges')
    parser.add_argument('-s', '--sync', help='Sync Provider', action='store_true')
    parser.add_argument('-p', '--provider', help='Provider')
    parser.add_argument('-f', '--force', action='store_true', help='Force Installation')
    parser.add_argument('-c', '--clear', action='store_true', help='Clear Database Cache')
    parser.add_argument('--list-providers', action='store_true', help='List Available Providers')
    parser.add_argument('--debug', action='store_true', help='Debug Mode')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose Mode')
    parser.add_argument('--silent', action='store_true', help='Silent Mode')
    parser.add_argument('--drop', action='store_true', help='Drop Databases')
    return parser

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    load = not args.drop

    config = {
        "DEBUG": args.debug or False,
        "FORCE": args.force or False,
        "VERBOSE": args.verbose or False,
        "SILENT": args.silent or False,
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
    elif args.ranges:
        if not args.provider:
            sys.exit(app.list_ranges())
        else:
            provider = args.provider
            sys.exit(app.list_ranges(provider))
    elif args.list_providers:
        if not args.provider:
            app.list_providers()
        else:
            provider = args.provider
            sys.exit(app.list_provider(provider))
    elif not args.ip:
        parser.print_help()
    else:
        sys.exit(app.find(args.ip, args.provider))
