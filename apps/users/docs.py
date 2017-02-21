#_*_coding:utf-8_*_
from mongoengine import *
import datetime
connect('mxonline',host='127.0.0.1')
class Page(Document):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)
