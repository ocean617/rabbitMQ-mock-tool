# coding=utf-8
__author__ = 'lihy'

import execjs
try:
    ctx = execjs.compile(u"function add(x, y) { return x +'中国人' ;} " )
    print ctx.call("add",3,4)
except Exception as err:
    print unicode(err)
