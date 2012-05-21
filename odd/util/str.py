# -*- coding: utf-8 -*-

from os.path import splitext

ext_map = {
        'py':'python',
        'php':'php-script'
        }


def strip_text(data):
    """
    去除WTForm数据的前后空白部分
    """
    if isinstance(data, unicode):
        data = data.strip()
    return data

def file_type(file_name):
    ext = splitext(file_name)[1][1:]
    if ext in ext_map.keys():
        return ext_map[ext]
    return ext
