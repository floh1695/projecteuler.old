#!/usr/bin/python2

from __future__ import (absolute_import,
                        print_function)


class DictManager:
    def __init__(self):
        self.map = {}

    def get(self, key):
        return self.map[key]

    def add(self, key, value):
        self.map[key] = value
