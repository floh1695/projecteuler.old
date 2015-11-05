#!/usr/bin/python2

from __future__ import (absolute_import,
                        print_function)


class DictManager:
    def __init__(self, filename, key_type, value_type):
        self.filename = filename
        self.key_type = key_type
        self.value_type = value_type
        self.map = {}
        self.update()

    def update(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line[:-1]
                    key, value = line.split(',')
                    self.map[self.key_type(key)] = self.value_type(value)
        except IOError:
            pass  # There probably isn't a file to read yet

    def write(self):
        write_string = ''
        for key, value in self.map.iteritems():
            write_string += '{},{}\n'.format(key, value)
        with open(self.filename, 'w') as f:
            f.write(write_string)

    def get(self, key):
        try:
            return self.map[key]
        except KeyError:
            self.update()
        return self.map[key]

    def add(self, key, value):
        self.map[key] = value
        self.write()
