# -*- coding: utf-8 -*-

from os.path import splitext, join
from subprocess import call

from odd import app

def file_type(file_name):
    ext = splitext(file_name)[1][1:].lower()
    return ext

def save_photo(id, img):
    photo_path = app.static_folder+'/photo'
    ext = file_type(img.filename)
    if not ext in app.config['ALLOWED_IMGS']:
        return False
    img_name = '%d.%s' % (id, ext)
    path = join(photo_path, img_name)
    img.save(path)
    cv = 'convert -size 20x20 %s -resize 20x20 %s/%d-20.jpg;convert -size 90x90 %s -resize 90x90 %s/%d-90.jpg'
    call(cv % (path, photo_path, id, path, photo_path, id), shell=True)

def save_tag_photo(id, img):
    photo_path = app.static_folder+'/tag_photo'
    ext = file_type(img.filename)
    if not ext in app.config['ALLOWED_IMGS']:
        return False
    img_name = '%d.%s' % (id, ext)
    path = join(photo_path, img_name)
    img.save(path)
    cv = 'convert -size 20x20 %s -resize 20x20 %s/%d-20.jpg;convert -size 90x90 %s -resize 90x90 %s/%d-90.jpg'
    call(cv % (path, photo_path, id, path, photo_path, id), shell=True)
