#!/usr/bin/python2

from __future__ import (absolute_import,
                        print_function)


class DictManager:
    def __init__(self, filename):
        self.filename = filename
        self.map = {}
        self.update()

    def update(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    key, value = line.split(',')
                    self.map[int(key)] = int(value)
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
