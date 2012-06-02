# -*- coding: utf-8 -*-

from os.path import splitext, join
from subprocess import call

from odd import app

def file_type(file_name):
    ext = splitext(file_name)[1][1:].lower()
    return ext

def save_img(uid, img):
    photo_path = app.static_folder+'/photo'
    ext = file_type(img.filename)
    img_name = '%d.%s' % (uid, ext)
    path = join(photo_path, img_name)
    img.save(path)
    cv = 'convert -size 20x20 %s -resize 20x20 %s/%d-20.jpg;convert -size 90x90 %s -resize 90x90 %s/%d-90.jpg'
    call(cv % (path, photo_path, uid, path, photo_path, uid), shell=True)

