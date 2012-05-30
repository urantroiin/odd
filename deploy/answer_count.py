# -*- coding: utf-8 -*-

import oursql

conn = oursql.connect(host='127.0.0.1', user='odd', passwd='odd', db='odd', port=3306)
curs = conn.cursor(oursql.DictCursor)

#获取每个问题的答案个数
sql = 'select question_id, count(1) as count from answers group by question_id'
curs.execute(sql)
rs = curs.fetchall()

#更新问题的answer_count
sql = 'update questions set answer_count=? where id=?'
for r in rs:
    curs.execute(sql,(r['count'],r['question_id']))

