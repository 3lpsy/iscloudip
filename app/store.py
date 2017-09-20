import os
import json
import sys
import sqlite3
from .utils import confirm

class Grammar(object):
    def __init__(self):
        file_dir = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(file_dir, "sql.json")
        with open(path) as sql_statments:
            self.sql = json.load(sql_statments)

    def get(self, name):
        return self.sql[name]

class Store(object):
    def __init__(self, path, force=False, debug=False, migrate=True):
        self.grammar = Grammar()
        self.debug = debug
        self.path = path
        if not os.path.isfile(path):
            self.create_db_file(path, force)
        self.conn = sqlite3.connect(path)
        if migrate:
            self.migrate()

    def execute(self, grammar, params, many=False):
        cur = self.conn.cursor()
        statement = self.grammar.get(grammar)
        if self.debug:
            print("Debug: Executing '{}'".format(statement))
            if params:
                print("Debug: Parameters '{}'".format(params))
        if many:
            cur.executemany(statement, params)
        else:
            cur.execute(statement, params)
        return cur

    def perform(self, grammar, many=False, **kwargs):
        if many:
            data = kwargs['data']
            c = self.execute(grammar, data, many=True)
        else:
            c = self.execute(grammar, kwargs, many=False)
        self.conn.commit()

    def get(self, grammar, **kwargs):
        c = self.execute(grammar, kwargs)
        return c.fetchone()

    def all(self, grammar, **kwargs):
        c = self.execute(grammar, kwargs)
        return c.fetchall()

    def create_db_file(self, path, force):
        if not force:
            if not confirm("Database File Does Not Exist. Do you want to install it?"):
                return sys.exit(print("Cannot continue without database Installation", file=sys.stderr))
        open(path, 'x')

    def migrate(self):
        self.perform("CREATE_PROVIDERS_IF_NOT_EXISTS")
        self.perform("CREATE_RANGES_IF_NOT_EXISTS")

    def drop_all(self):
        self.drop('ranges')
        self.drop('providers')

    def drop(self, table):
        self.perform("DROP_" + table.upper() + "_TABLE")

    def provider_exists(self, name):
        provider = self.get_provider(name)
        return True if provider else False

    def get_provider(self, name):
        return self.get("GET_PROVIDER", name=name)

    def add_provider(self, name, description):
        return self.perform("INSERT_PROVIDER", name=name, description=description)

    def add_ranges(self, ranges):
        return self.perform('INSERT_RANGES', True, data=ranges)

    def clear_provider_ranges(self, name):
        self.perform('DELETE_RANGES_FOR_PROVIDER', provider=name)
