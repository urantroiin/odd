# -*- coding: utf-8 -*-

from os.path import splitext, join

from odd import app

def file_type(file_name):
    ext = splitext(file_name)[1][1:].lower()
    return ext

def save_img(uid, img):
    photo_path = app.static_folder+'/photo'
    img_name = '%d.%s' % (uid,file_type(img.filename))
    path = join(photo_path, img_name)
    img.save(path)
