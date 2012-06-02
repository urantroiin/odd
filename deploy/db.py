# -*- coding: utf-8 -*-

import oursql

conn = oursql.connect(host='127.0.0.1', user='odd', passwd='odd', db='odd', port=3306)
curs = conn.cursor(oursql.DictCursor)
