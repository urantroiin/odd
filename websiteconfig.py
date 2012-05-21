# -*- coding: utf-8 -*-

'''
test environment
'''
#host
HOST = '127.0.0.1'
PORT = 5000

#debug
DEBUG = True

#secret key
SECRET_KEY = r"42a3e1376f8852d1c0620a3235886bcd712879a3"

#DB
DATABASE_URI = 'mysql+oursql://root:123456@localhost/odd'
DATABASE_CONNECT_OPTIONS = {}

'''
load production environment
'''
from os.path import isfile
if isfile('config.py'):
    from config import *
