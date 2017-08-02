#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''doc'''

def singleton(cls):
    '''doc'''
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class Data():
    '''doc'''
    def __init__(self):
        self.data = {}
    def set(self, key, val):
        '''doc'''
        self.data[key] = val
    def get(self, key):
        '''doc'''
        return self.data[key]
