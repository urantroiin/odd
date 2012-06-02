# -*- coding: utf-8 -*-

from db import *

#获取问题的标签，插入tags表中，重复的tag自动忽略
sql = 'insert ignore into tags (tag,create_time) select distinct tag, now() from question_tags'
curs.execute(sql)
