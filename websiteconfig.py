# -*- coding: utf-8 -*-

'''
test environment
'''
#host
HOST = '127.0.0.1'
PORT = 5000
DEBUG_ON = True

#DB
DATABASE_URI = 'mysql+oursql://root:123456@localhost/odd'
DATABASE_CONNECT_OPTIONS = {}

'''
load production environment
'''
from os.path import isfile
if isfile('config.py'):
    from config import *
