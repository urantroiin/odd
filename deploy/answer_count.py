# -*- coding: utf-8 -*-

from db import *

#获取每个问题的答案个数
sql = 'select question_id, count(1) as count from answers group by question_id'
curs.execute(sql)
rs = curs.fetchall()

#更新问题的answer_count
sql = 'update questions set answer_count=? where id=?'
for r in rs:
    curs.execute(sql,(r['count'],r['question_id']))

