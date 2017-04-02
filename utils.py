__author__ = 'lihy'
import sys
from PyQt4 import QtCore, QtGui

def _char2utf8(Str):
    return unicode(Str.toUtf8(),'utf8', 'ignore')