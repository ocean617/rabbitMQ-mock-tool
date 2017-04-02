# coding=utf-8

# rabbitMQ Mock工具
import sys
import logging
import utils
import MqUtil
import pika
import threading
import execjs

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# 主界面类
class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(995, 701)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 991, 621))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_sender = QtGui.QWidget()
        self.tab_sender.setObjectName(_fromUtf8("tab_sender"))
        self.groupBox = QtGui.QGroupBox(self.tab_sender)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 961, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(274, 34, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(437, 30, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.serverEdt = QtGui.QLineEdit(self.groupBox)
        self.serverEdt.setGeometry(QtCore.QRect(64, 27, 113, 20))
        self.serverEdt.setMaxLength(50)
        self.serverEdt.setObjectName(_fromUtf8("serverEdt"))
        self.portEdt = QtGui.QLineEdit(self.groupBox)
        self.portEdt.setGeometry(QtCore.QRect(220, 27, 51, 20))
        self.portEdt.setMaxLength(50)
        self.portEdt.setObjectName(_fromUtf8("portEdt"))
        self.unameEdt = QtGui.QLineEdit(self.groupBox)
        self.unameEdt.setGeometry(QtCore.QRect(316, 30, 111, 20))
        self.unameEdt.setMaxLength(50)
        self.unameEdt.setObjectName(_fromUtf8("unameEdt"))
        self.passEdt = QtGui.QLineEdit(self.groupBox)
        self.passEdt.setGeometry(QtCore.QRect(470, 30, 131, 20))
        self.passEdt.setInputMask(_fromUtf8(""))
        self.passEdt.setText(_fromUtf8("guest"))
        self.passEdt.setMaxLength(50)
        self.passEdt.setEchoMode(QtGui.QLineEdit.Password)
        self.passEdt.setObjectName(_fromUtf8("passEdt"))
        self.connectBtn = QtGui.QPushButton(self.groupBox)
        self.connectBtn.setGeometry(QtCore.QRect(824, 22, 121, 23))
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(609, 33, 31, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.VhostEdt = QtGui.QLineEdit(self.groupBox)
        self.VhostEdt.setGeometry(QtCore.QRect(643, 31, 91, 20))
        self.VhostEdt.setMaxLength(50)
        self.VhostEdt.setObjectName(_fromUtf8("VhostEdt"))
        self.httpChk = QtGui.QCheckBox(self.groupBox)
        self.httpChk.setGeometry(QtCore.QRect(760, 30, 51, 16))
        self.httpChk.setObjectName(_fromUtf8("httpChk"))
        self.sendBox = QtGui.QGroupBox(self.tab_sender)
        self.sendBox.setGeometry(QtCore.QRect(10, 80, 961, 511))
        self.sendBox.setTitle(_fromUtf8(""))
        self.sendBox.setObjectName(_fromUtf8("sendBox"))
        self.label_6 = QtGui.QLabel(self.sendBox)
        self.label_6.setGeometry(QtCore.QRect(10, 14, 331, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.scrollArea = QtGui.QScrollArea(self.sendBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 531, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 449))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.sendContentTxtEdt = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.sendContentTxtEdt.setGeometry(QtCore.QRect(0, 0, 531, 451))
        self.sendContentTxtEdt.setObjectName(_fromUtf8("sendContentTxtEdt"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_7 = QtGui.QLabel(self.sendBox)
        self.label_7.setGeometry(QtCore.QRect(550, 15, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.sendBox)
        self.label_8.setGeometry(QtCore.QRect(550, 44, 61, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.sendBox)
        self.label_9.setGeometry(QtCore.QRect(550, 72, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.exchageNameEdt = QtGui.QLineEdit(self.sendBox)
        self.exchageNameEdt.setGeometry(QtCore.QRect(630, 14, 121, 20))
        self.exchageNameEdt.setText(_fromUtf8(""))
        self.exchageNameEdt.setMaxLength(50)
        self.exchageNameEdt.setObjectName(_fromUtf8("exchageNameEdt"))
        self.QueueEdt = QtGui.QLineEdit(self.sendBox)
        self.QueueEdt.setGeometry(QtCore.QRect(630, 40, 321, 20))
        self.QueueEdt.setText(_fromUtf8(""))
        self.QueueEdt.setMaxLength(50)
        self.QueueEdt.setObjectName(_fromUtf8("QueueEdt"))
        self.RtKeyEdt = QtGui.QLineEdit(self.sendBox)
        self.RtKeyEdt.setGeometry(QtCore.QRect(630, 70, 321, 20))
        self.RtKeyEdt.setText(_fromUtf8(""))
        self.RtKeyEdt.setMaxLength(50)
        self.RtKeyEdt.setObjectName(_fromUtf8("RtKeyEdt"))
        self.replaceTag_group = QtGui.QGroupBox(self.sendBox)
        self.replaceTag_group.setGeometry(QtCore.QRect(550, 110, 401, 231))
        self.replaceTag_group.setObjectName(_fromUtf8("replaceTag_group"))
        self.label_11 = QtGui.QLabel(self.replaceTag_group)
        self.label_11.setGeometry(QtCore.QRect(130, 30, 61, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.replaceTag_group)
        self.label_12.setGeometry(QtCore.QRect(254, 30, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.replaceTag_group)
        self.label_13.setGeometry(QtCore.QRect(324, 30, 61, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.replaceTag_group)
        self.label_14.setGeometry(QtCore.QRect(12, 31, 61, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tagPreEdt11 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt11.setGeometry(QtCore.QRect(130, 60, 121, 20))
        self.tagPreEdt11.setText(_fromUtf8(""))
        self.tagPreEdt11.setMaxLength(50)
        self.tagPreEdt11.setObjectName(_fromUtf8("tagPreEdt11"))
        self.tagSpBox11_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox11_1.setGeometry(QtCore.QRect(254, 60, 61, 22))
        self.tagSpBox11_1.setMinimum(1)
        self.tagSpBox11_1.setObjectName(_fromUtf8("tagSpBox11_1"))
        self.tagSpBox11_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox11_2.setGeometry(QtCore.QRect(321, 60, 71, 22))
        self.tagSpBox11_2.setMinimum(1)
        self.tagSpBox11_2.setMaximum(1000000)
        self.tagSpBox11_2.setObjectName(_fromUtf8("tagSpBox11_2"))
        self.tagSpBox12_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox12_1.setGeometry(QtCore.QRect(254, 84, 61, 22))
        self.tagSpBox12_1.setMinimum(1)
        self.tagSpBox12_1.setObjectName(_fromUtf8("tagSpBox12_1"))
        self.tagSpBox12_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox12_2.setGeometry(QtCore.QRect(321, 84, 71, 22))
        self.tagSpBox12_2.setMinimum(1)
        self.tagSpBox12_2.setMaximum(1000000)
        self.tagSpBox12_2.setObjectName(_fromUtf8("tagSpBox12_2"))
        self.tagPreEdt12 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt12.setGeometry(QtCore.QRect(130, 84, 121, 20))
        self.tagPreEdt12.setText(_fromUtf8(""))
        self.tagPreEdt12.setMaxLength(50)
        self.tagPreEdt12.setObjectName(_fromUtf8("tagPreEdt12"))
        self.tagSpBox13_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox13_1.setGeometry(QtCore.QRect(254, 109, 61, 22))
        self.tagSpBox13_1.setMinimum(1)
        self.tagSpBox13_1.setObjectName(_fromUtf8("tagSpBox13_1"))
        self.tagSpBox13_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox13_2.setGeometry(QtCore.QRect(321, 109, 71, 22))
        self.tagSpBox13_2.setMinimum(1)
        self.tagSpBox13_2.setMaximum(1000000)
        self.tagSpBox13_2.setObjectName(_fromUtf8("tagSpBox13_2"))
        self.tagSpBox14_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox14_2.setGeometry(QtCore.QRect(321, 133, 71, 22))
        self.tagSpBox14_2.setMinimum(1)
        self.tagSpBox14_2.setMaximum(1000000)
        self.tagSpBox14_2.setObjectName(_fromUtf8("tagSpBox14_2"))
        self.tagPreEdt13 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt13.setGeometry(QtCore.QRect(130, 109, 121, 20))
        self.tagPreEdt13.setText(_fromUtf8(""))
        self.tagPreEdt13.setMaxLength(50)
        self.tagPreEdt13.setObjectName(_fromUtf8("tagPreEdt13"))
        self.tagPreEdt14 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt14.setGeometry(QtCore.QRect(130, 133, 121, 20))
        self.tagPreEdt14.setText(_fromUtf8(""))
        self.tagPreEdt14.setMaxLength(50)
        self.tagPreEdt14.setObjectName(_fromUtf8("tagPreEdt14"))
        self.tagSpBox14_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox14_1.setGeometry(QtCore.QRect(254, 133, 61, 22))
        self.tagSpBox14_1.setMinimum(1)
        self.tagSpBox14_1.setObjectName(_fromUtf8("tagSpBox14_1"))
        self.tagSpBox16_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox16_1.setGeometry(QtCore.QRect(254, 184, 61, 22))
        self.tagSpBox16_1.setMinimum(1)
        self.tagSpBox16_1.setObjectName(_fromUtf8("tagSpBox16_1"))
        self.tagPreEdt16 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt16.setGeometry(QtCore.QRect(130, 184, 121, 20))
        self.tagPreEdt16.setText(_fromUtf8(""))
        self.tagPreEdt16.setMaxLength(50)
        self.tagPreEdt16.setObjectName(_fromUtf8("tagPreEdt16"))
        self.tagPreEdt15 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagPreEdt15.setGeometry(QtCore.QRect(130, 160, 121, 20))
        self.tagPreEdt15.setText(_fromUtf8(""))
        self.tagPreEdt15.setMaxLength(50)
        self.tagPreEdt15.setObjectName(_fromUtf8("tagPreEdt15"))
        self.tagSpBox15_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox15_2.setGeometry(QtCore.QRect(321, 160, 71, 22))
        self.tagSpBox15_2.setMinimum(1)
        self.tagSpBox15_2.setMaximum(1000000)
        self.tagSpBox15_2.setObjectName(_fromUtf8("tagSpBox15_2"))
        self.tagSpBox16_2 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox16_2.setGeometry(QtCore.QRect(321, 184, 71, 22))
        self.tagSpBox16_2.setMinimum(1)
        self.tagSpBox16_2.setMaximum(1000000)
        self.tagSpBox16_2.setObjectName(_fromUtf8("tagSpBox16_2"))
        self.tagSpBox15_1 = QtGui.QSpinBox(self.replaceTag_group)
        self.tagSpBox15_1.setGeometry(QtCore.QRect(254, 160, 61, 22))
        self.tagSpBox15_1.setMinimum(1)
        self.tagSpBox15_1.setObjectName(_fromUtf8("tagSpBox15_1"))
        self.tagEdt15 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt15.setGeometry(QtCore.QRect(10, 160, 110, 20))
        self.tagEdt15.setText(_fromUtf8(""))
        self.tagEdt15.setMaxLength(50)
        self.tagEdt15.setObjectName(_fromUtf8("tagEdt15"))
        self.tagEdt16 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt16.setGeometry(QtCore.QRect(10, 184, 110, 20))
        self.tagEdt16.setText(_fromUtf8(""))
        self.tagEdt16.setMaxLength(50)
        self.tagEdt16.setObjectName(_fromUtf8("tagEdt16"))
        self.tagEdt14 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt14.setGeometry(QtCore.QRect(10, 133, 110, 20))
        self.tagEdt14.setText(_fromUtf8(""))
        self.tagEdt14.setMaxLength(50)
        self.tagEdt14.setObjectName(_fromUtf8("tagEdt14"))
        self.tagEdt13 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt13.setGeometry(QtCore.QRect(10, 109, 110, 20))
        self.tagEdt13.setText(_fromUtf8(""))
        self.tagEdt13.setMaxLength(50)
        self.tagEdt13.setObjectName(_fromUtf8("tagEdt13"))
        self.tagEdt11 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt11.setGeometry(QtCore.QRect(10, 60, 110, 20))
        self.tagEdt11.setText(_fromUtf8(""))
        self.tagEdt11.setMaxLength(50)
        self.tagEdt11.setObjectName(_fromUtf8("tagEdt11"))
        self.tagEdt12 = QtGui.QLineEdit(self.replaceTag_group)
        self.tagEdt12.setGeometry(QtCore.QRect(10, 84, 110, 20))
        self.tagEdt12.setText(_fromUtf8(""))
        self.tagEdt12.setMaxLength(50)
        self.tagEdt12.setObjectName(_fromUtf8("tagEdt12"))
        self.sendCountSpBox = QtGui.QSpinBox(self.sendBox)
        self.sendCountSpBox.setGeometry(QtCore.QRect(640, 357, 151, 22))
        self.sendCountSpBox.setMinimum(1)
        self.sendCountSpBox.setMaximum(1000000)
        self.sendCountSpBox.setProperty("value", 1)
        self.sendCountSpBox.setObjectName(_fromUtf8("sendCountSpBox"))
        self.label_15 = QtGui.QLabel(self.sendBox)
        self.label_15.setGeometry(QtCore.QRect(550, 360, 81, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.sendMsgBtn = QtGui.QPushButton(self.sendBox)
        self.sendMsgBtn.setGeometry(QtCore.QRect(810, 356, 121, 23))
        self.sendMsgBtn.setObjectName(_fromUtf8("sendMsgBtn"))
        self.sendLogChk = QtGui.QCheckBox(self.sendBox)
        self.sendLogChk.setGeometry(QtCore.QRect(550, 400, 241, 16))
        self.sendLogChk.setObjectName(_fromUtf8("sendLogChk"))
        self.send_status_lbl = QtGui.QLabel(self.sendBox)
        self.send_status_lbl.setGeometry(QtCore.QRect(550, 430, 401, 16))
        self.send_status_lbl.setWordWrap(True)
        self.send_status_lbl.setObjectName(_fromUtf8("send_status_lbl"))
        self.label_32 = QtGui.QLabel(self.sendBox)
        self.label_32.setGeometry(QtCore.QRect(764, 14, 81, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.exchangeTypeCmb = QtGui.QComboBox(self.sendBox)
        self.exchangeTypeCmb.setGeometry(QtCore.QRect(848, 10, 101, 22))
        self.exchangeTypeCmb.setObjectName(_fromUtf8("exchangeTypeCmb"))
        self.exchangeTypeCmb.addItem(_fromUtf8(""))
        self.exchangeTypeCmb.addItem(_fromUtf8(""))
        self.exchangeTypeCmb.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_sender, _fromUtf8(""))
        self.tab_recv = QtGui.QWidget()
        self.tab_recv.setObjectName(_fromUtf8("tab_recv"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_recv)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 961, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(188, 30, 31, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(276, 30, 54, 12))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(440, 30, 31, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.cs_serverEdt = QtGui.QLineEdit(self.groupBox_2)
        self.cs_serverEdt.setGeometry(QtCore.QRect(64, 27, 113, 20))
        self.cs_serverEdt.setMaxLength(50)
        self.cs_serverEdt.setObjectName(_fromUtf8("cs_serverEdt"))
        self.cs_portEdt = QtGui.QLineEdit(self.groupBox_2)
        self.cs_portEdt.setGeometry(QtCore.QRect(220, 27, 51, 20))
        self.cs_portEdt.setMaxLength(20)
        self.cs_portEdt.setObjectName(_fromUtf8("cs_portEdt"))
        self.cs_unameEdt = QtGui.QLineEdit(self.groupBox_2)
        self.cs_unameEdt.setGeometry(QtCore.QRect(320, 27, 111, 20))
        self.cs_unameEdt.setMaxLength(20)
        self.cs_unameEdt.setObjectName(_fromUtf8("cs_unameEdt"))
        self.cs_passEdt = QtGui.QLineEdit(self.groupBox_2)
        self.cs_passEdt.setGeometry(QtCore.QRect(474, 28, 121, 20))
        self.cs_passEdt.setInputMask(_fromUtf8(""))
        self.cs_passEdt.setMaxLength(20)
        self.cs_passEdt.setEchoMode(QtGui.QLineEdit.Password)
        self.cs_passEdt.setObjectName(_fromUtf8("cs_passEdt"))
        self.cs_connectBtn = QtGui.QPushButton(self.groupBox_2)
        self.cs_connectBtn.setGeometry(QtCore.QRect(824, 22, 121, 23))
        self.cs_connectBtn.setObjectName(_fromUtf8("cs_connectBtn"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(604, 30, 31, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.cs_VhostEdt = QtGui.QLineEdit(self.groupBox_2)
        self.cs_VhostEdt.setGeometry(QtCore.QRect(638, 28, 91, 20))
        self.cs_VhostEdt.setMaxLength(20)
        self.cs_VhostEdt.setObjectName(_fromUtf8("cs_VhostEdt"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_recv)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 80, 961, 501))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(10, 23, 101, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.sc_queue_edt = QtGui.QLineEdit(self.groupBox_3)
        self.sc_queue_edt.setGeometry(QtCore.QRect(110, 20, 611, 20))
        self.sc_queue_edt.setText(_fromUtf8(""))
        self.sc_queue_edt.setObjectName(_fromUtf8("sc_queue_edt"))
        self.cs_startListenBtn = QtGui.QPushButton(self.groupBox_3)
        self.cs_startListenBtn.setGeometry(QtCore.QRect(496, 350, 121, 23))
        self.cs_startListenBtn.setObjectName(_fromUtf8("cs_startListenBtn"))
        self.cs_stopListenBtn = QtGui.QPushButton(self.groupBox_3)
        self.cs_stopListenBtn.setGeometry(QtCore.QRect(620, 350, 121, 23))
        self.cs_stopListenBtn.setObjectName(_fromUtf8("cs_stopListenBtn"))
        self.sc_sendContentTxtEdt = QtGui.QTextEdit(self.groupBox_3)
        self.sc_sendContentTxtEdt.setGeometry(QtCore.QRect(10, 80, 471, 411))
        self.sc_sendContentTxtEdt.setObjectName(_fromUtf8("sc_sendContentTxtEdt"))
        self.testJsExecBtn = QtGui.QPushButton(self.groupBox_3)
        self.testJsExecBtn.setGeometry(QtCore.QRect(360, 52, 121, 23))
        self.testJsExecBtn.setObjectName(_fromUtf8("testJsExecBtn"))
        self.label_23 = QtGui.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(12, 55, 331, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(490, 70, 451, 271))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.cs_send_passEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_passEdt.setGeometry(QtCore.QRect(291, 55, 121, 20))
        self.cs_send_passEdt.setText(_fromUtf8("guest"))
        self.cs_send_passEdt.setMaxLength(100)
        self.cs_send_passEdt.setEchoMode(QtGui.QLineEdit.Password)
        self.cs_send_passEdt.setObjectName(_fromUtf8("cs_send_passEdt"))
        self.label_24 = QtGui.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(20, 149, 61, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.cs_send_QueueEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_QueueEdt.setGeometry(QtCore.QRect(100, 145, 321, 20))
        self.cs_send_QueueEdt.setText(_fromUtf8(""))
        self.cs_send_QueueEdt.setMaxLength(100)
        self.cs_send_QueueEdt.setObjectName(_fromUtf8("cs_send_QueueEdt"))
        self.cs_send_exchangeType_cmb = QtGui.QComboBox(self.groupBox_4)
        self.cs_send_exchangeType_cmb.setGeometry(QtCore.QRect(292, 82, 121, 22))
        self.cs_send_exchangeType_cmb.setObjectName(_fromUtf8("cs_send_exchangeType_cmb"))
        self.cs_send_exchangeType_cmb.addItem(_fromUtf8(""))
        self.cs_send_exchangeType_cmb.addItem(_fromUtf8(""))
        self.cs_send_exchangeType_cmb.addItem(_fromUtf8(""))
        self.cs_send_RtKeyEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_RtKeyEdt.setGeometry(QtCore.QRect(100, 175, 321, 20))
        self.cs_send_RtKeyEdt.setText(_fromUtf8(""))
        self.cs_send_RtKeyEdt.setMaxLength(100)
        self.cs_send_RtKeyEdt.setObjectName(_fromUtf8("cs_send_RtKeyEdt"))
        self.label_27 = QtGui.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(20, 31, 54, 12))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.cs_send_unameEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_unameEdt.setGeometry(QtCore.QRect(100, 54, 111, 20))
        self.cs_send_unameEdt.setMaxLength(50)
        self.cs_send_unameEdt.setObjectName(_fromUtf8("cs_send_unameEdt"))
        self.cs_send_serverEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_serverEdt.setGeometry(QtCore.QRect(100, 27, 113, 20))
        self.cs_send_serverEdt.setMaxLength(50)
        self.cs_send_serverEdt.setObjectName(_fromUtf8("cs_send_serverEdt"))
        self.label_29 = QtGui.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(20, 57, 54, 12))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_26 = QtGui.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(20, 177, 81, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.cs_send_VhostEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_VhostEdt.setGeometry(QtCore.QRect(101, 83, 91, 20))
        self.cs_send_VhostEdt.setMaxLength(50)
        self.cs_send_VhostEdt.setObjectName(_fromUtf8("cs_send_VhostEdt"))
        self.label_33 = QtGui.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(213, 86, 81, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_30 = QtGui.QLabel(self.groupBox_4)
        self.label_30.setGeometry(QtCore.QRect(260, 57, 31, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.cs_send_portEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_portEdt.setGeometry(QtCore.QRect(293, 28, 121, 20))
        self.cs_send_portEdt.setMaxLength(100)
        self.cs_send_portEdt.setObjectName(_fromUtf8("cs_send_portEdt"))
        self.cs_test_connectBtn = QtGui.QPushButton(self.groupBox_4)
        self.cs_test_connectBtn.setGeometry(QtCore.QRect(300, 210, 121, 23))
        self.cs_test_connectBtn.setObjectName(_fromUtf8("cs_test_connectBtn"))
        self.label_31 = QtGui.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(22, 86, 31, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.cs_send_exchageNameEdt = QtGui.QLineEdit(self.groupBox_4)
        self.cs_send_exchageNameEdt.setGeometry(QtCore.QRect(100, 119, 321, 20))
        self.cs_send_exchageNameEdt.setText(_fromUtf8(""))
        self.cs_send_exchageNameEdt.setMaxLength(100)
        self.cs_send_exchageNameEdt.setObjectName(_fromUtf8("cs_send_exchageNameEdt"))
        self.label_28 = QtGui.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(260, 30, 31, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.recvLogChk = QtGui.QCheckBox(self.groupBox_4)
        self.recvLogChk.setGeometry(QtCore.QRect(20, 220, 241, 16))
        self.recvLogChk.setObjectName(_fromUtf8("recvLogChk"))
        self.onrecvMsgChk = QtGui.QCheckBox(self.groupBox_4)
        self.onrecvMsgChk.setGeometry(QtCore.QRect(20, 240, 241, 16))
        self.onrecvMsgChk.setObjectName(_fromUtf8("onrecvMsgChk"))
        self.tabWidget.addTab(self.tab_recv, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 14pt \"微软雅黑\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(9, 9, 261, 31))
        self.label_22.setStyleSheet(_fromUtf8("font: 75 14pt \"微软雅黑\";\n"
                                              "color:rgb(73, 221, 108);"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(MainWindow, QtCore.SIGNAL(_fromUtf8("destroyed()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "RabbitMQ 服务器设置", None))
        self.label_2.setText(_translate("MainWindow", "服务器IP", None))
        self.label_3.setText(_translate("MainWindow", "端口", None))
        self.label_4.setText(_translate("MainWindow", "用户名", None))
        self.label_5.setText(_translate("MainWindow", "密码", None))
        self.serverEdt.setText(_translate("MainWindow", "172.0.0.1", None))
        self.portEdt.setText(_translate("MainWindow", "5672", None))
        self.unameEdt.setText(_translate("MainWindow", "guest", None))
        self.connectBtn.setText(_translate("MainWindow", "连  接", None))
        self.label_10.setText(_translate("MainWindow", "Vhost", None))
        self.VhostEdt.setText(_translate("MainWindow", "/", None))
        self.httpChk.setText(_translate("MainWindow", "https", None))
        self.label_6.setText(_translate("MainWindow", "发送内容，可指定替换标识,格式: $英文标识$,如$seqNum$", None))
        self.label_7.setText(_translate("MainWindow", "Exchange名称", None))
        self.label_8.setText(_translate("MainWindow", "Queue名称", None))
        self.label_9.setText(_translate("MainWindow", "Routing_key", None))
        self.replaceTag_group.setTitle(_translate("MainWindow", "替换标识规则", None))
        self.label_11.setText(_translate("MainWindow", "标识前缀", None))
        self.label_12.setText(_translate("MainWindow", "开始序号", None))
        self.label_13.setText(_translate("MainWindow", "结束序号", None))
        self.label_14.setText(_translate("MainWindow", "替换标识", None))
        self.label_15.setText(_translate("MainWindow", "发送次数", None))
        self.sendMsgBtn.setText(_translate("MainWindow", "发送消息", None))
        self.sendLogChk.setText(_translate("MainWindow", "发送内容写入日志", None))
        self.send_status_lbl.setText(_translate("MainWindow", "      ", None))

        self.label_32.setText(_translate("MainWindow", "Exchange类型", None))
        self.exchangeTypeCmb.setItemText(0, _translate("MainWindow", "topic", None))
        self.exchangeTypeCmb.setItemText(1, _translate("MainWindow", "direct", None))
        self.exchangeTypeCmb.setItemText(2, _translate("MainWindow", "fanout", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sender), _translate("MainWindow", "发送", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收消息 RabbitMQ 服务器设置", None))
        self.label_16.setText(_translate("MainWindow", "服务器IP", None))
        self.label_17.setText(_translate("MainWindow", "端口", None))
        self.label_18.setText(_translate("MainWindow", "用户名", None))
        self.label_19.setText(_translate("MainWindow", "密码", None))
        self.cs_serverEdt.setText(_translate("MainWindow", "172.0.0.1", None))
        self.cs_portEdt.setText(_translate("MainWindow", "5672", None))
        self.cs_unameEdt.setText(_translate("MainWindow", "guest", None))
        self.cs_passEdt.setText(_translate("MainWindow", "guest", None))
        self.cs_connectBtn.setText(_translate("MainWindow", "测试连接", None))
        self.label_20.setText(_translate("MainWindow", "Vhost", None))
        self.cs_VhostEdt.setText(_translate("MainWindow", "/", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "监听处理", None))
        self.label_21.setText(_translate("MainWindow", "监听Queue名称", None))
        self.cs_startListenBtn.setText(_translate("MainWindow", "开始监听", None))
        self.cs_stopListenBtn.setText(_translate("MainWindow", "停止监听", None))
        self.sc_sendContentTxtEdt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">//在处理的代码段中一定要定义一个function MsgCallback(msg)方法，返回要发送的信息，参数msg为接收到的MQ信息</p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">// 测试消息内容</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/*</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*  { item1:100,</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*    item2:&quot;500&quot;,</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*    item3:{</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*           item3_1:&quot;结果值&quot;,</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*           item3_2:500.2</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*            }  </p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*  }</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*/</p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">//String转换为Json</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14px; color:#362e2b; background-color:#ffffff;\">function strToJson(str){ </span><span style=\" font-family:\'Arial,Tahoma,Verdana,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\"> </span></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14px; color:#362e2b; background-color:#ffffff;\">  return (new Function(&quot;return &quot; + str))(); </span></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Tahoma,Verdana,sans-serif\'; font-size:14px; color:#333333; background-color:#ffffff;\"> </span><span style=\" font-family:\'Arial\'; font-size:14px; color:#362e2b; background-color:#ffffff;\">} </span></p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">//消费处理函数，一定要定义</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">function MsgCallback(msg){</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   var msgObj =<span style=\" font-family:\'Arial\'; font-size:14px; color:#362e2b; background-color:#ffffff;\">strToJson(msg);</span></p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   //TODO</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   //必须以字符串返回</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   return &quot;{result:ok}&quot;;</p>\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p>\n"
                                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.testJsExecBtn.setText(_translate("MainWindow", "测试执行", None))
        self.label_23.setText(_translate("MainWindow", "Javascript消费逻辑", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "处理后要发送的MQ服务器设置", None))
        self.label_24.setText(_translate("MainWindow", "Queue名称", None))
        self.cs_send_exchangeType_cmb.setItemText(0, _translate("MainWindow", "topic", None))
        self.cs_send_exchangeType_cmb.setItemText(1, _translate("MainWindow", "direct", None))
        self.cs_send_exchangeType_cmb.setItemText(2, _translate("MainWindow", "fanout", None))
        self.label_27.setText(_translate("MainWindow", "服务器IP", None))
        self.cs_send_unameEdt.setText(_translate("MainWindow", "guest", None))
        self.cs_send_serverEdt.setText(_translate("MainWindow", "172.0.0.1", None))
        self.label_29.setText(_translate("MainWindow", "用户名", None))
        self.label_26.setText(_translate("MainWindow", "Routing_key", None))
        self.cs_send_VhostEdt.setText(_translate("MainWindow", "/", None))
        self.label_33.setText(_translate("MainWindow", "Exchange类型", None))
        self.label_30.setText(_translate("MainWindow", "密码", None))
        self.cs_send_portEdt.setText(_translate("MainWindow", "5672", None))
        self.cs_test_connectBtn.setText(_translate("MainWindow", "测试连接", None))
        self.label_31.setText(_translate("MainWindow", "Vhost", None))
        self.label_25.setText(_translate("MainWindow", "Exchange名称", None))
        self.label_28.setText(_translate("MainWindow", "端口", None))
        self.recvLogChk.setText(_translate("MainWindow", "消费内容写入日志", None))
        self.onrecvMsgChk.setText(_translate("MainWindow", "只接收不发送响应消息", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recv), _translate("MainWindow", "消费", None))
        self.label.setText(_translate("MainWindow", "Rabbit MQ Mock Tool V1.0", None))
        self.label_22.setText(_translate("MainWindow", "Rabbit MQ Mock Tool V1.0", None))

     # 初始化处理

    # 初始化系统
    def __init__(self,appInst):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        # 当前界面常量
        self._currentMQUtilObj = None
        self._listenMsgThread  = None
        self._app = appInst
        self.setWindowTitle(u"RabbitMQ Mock V1.0 ")

        #发送状态status Bar
        sender_label = QtGui.QLabel(u" ")
        sender_label.setObjectName(_fromUtf8('sender_label'))
        sender_label.setStyleSheet(' QLabel {color: green}')
        self.statusBar().addWidget(sender_label)

        #消费状态status Bar
        consumer_label = QtGui.QLabel(u"系统准备就绪   |   Ver:1.0 ")
        consumer_label.setObjectName(_fromUtf8('consumer_label'))
        consumer_label.setStyleSheet(' QLabel {color: green}')
        self.statusBar().addWidget(consumer_label)

        self.repaint()

    # 重载关闭事件
    def closeEvent(self, event):
        msgBox = QMessageBox(QMessageBox.Warning,
                 u"确认退出",
                 u"您真的确认退出吗？",
                 QMessageBox.Yes |  QMessageBox.No , self)
        if (msgBox.exec_() == QMessageBox.Yes):
            sys.exit(0)
        else:
            event.ignore()

    # 连接MQ按钮
    def connectBtnClicked( obj ):

        # 读取MQ发送配置
        server = utils._char2utf8(win.serverEdt.text())
        port  =  utils._char2utf8(win.portEdt.text())
        vhost  = utils._char2utf8(win.VhostEdt.text())

        uname = utils._char2utf8(win.unameEdt.text())
        upass = utils._char2utf8(win.passEdt.text())

        # 数据输入检验
        if ( server.strip()=="" or
            port.strip()=="" or
            vhost.strip()=="" or
            uname.strip()=="" or
            upass.strip()=="" ):
                QtGui.QMessageBox.information( obj, u"输入出错", u"请输入完整的MQ服务器信息后再进行连接.." )
                return

        # 禁用连接按钮
        win.connectBtn.setDisabled(True)
        credentials = pika.PlainCredentials(uname, upass)

        # 线程连接，防止界面锁死
        MqUtilObj = MqUtil.MQUtils( mainWindowObj= win )
        connthread = threading.Thread(target=MqUtilObj.connMQServer,args=( server , port , vhost , credentials))
        connthread.setDaemon(True)
        connthread.start()
        connthread.join()

        if MqUtilObj.getConnResult() == True:
            QtGui.QMessageBox.information(win, u"连接提示", u"已经成功连接！")
            #禁止相关输入
            win.serverEdt.setReadOnly(True)
            win.portEdt.setReadOnly(True)
            win.unameEdt.setReadOnly(True)
            win.passEdt.setReadOnly(True)
            win.VhostEdt.setReadOnly(True)
        else:
            QtGui.QMessageBox.information(win, u"连接失败", u"连接失败，请检查设置是否正确或MQ服务器是否开启.")
            win.connectBtn.setDisabled(False)

    # 得到定义的替换Tags 定义
    def getReplaceTags(self, winObj):
        replaceTagMap = []

        # 替换处理
        for i in range(11,16):
            edt = winObj.findChild(QtGui.QLineEdit,_fromUtf8("tagEdt"+str(i)))
            tagName_ = unicode(edt.text())

            edt = winObj.findChild(QtGui.QLineEdit,_fromUtf8("tagPreEdt"+str(i)))
            tagPrefix_ = unicode(edt.text())

            edt = winObj.findChild(QtGui.QSpinBox,_fromUtf8("tagSpBox"+str(i)+"_1"))
            startNum_ = str(edt.value())

            edt = winObj.findChild(QtGui.QSpinBox,_fromUtf8("tagSpBox"+str(i)+"_2"))
            endNum_ = str(edt.value())

            if tagName_.strip() != "":
                replaceTagMap.append({
                                        'tag':tagName_,
                                        'tagPrefix':tagPrefix_,
                                        'startNum':startNum_,
                                        'endNum':endNum_
                                    })

        return replaceTagMap

    # 发送按钮处理
    def sendMessageBtnClicked( obj ):
        if win.serverEdt.isReadOnly() == False:
            QtGui.QMessageBox.information( obj, u"操作出错", u"请先进行连接操作，再进行发送消息操作.." )
            return

        # 发送数据检查
        server = utils._char2utf8(win.serverEdt.text())
        port  =  utils._char2utf8(win.portEdt.text())
        vhost  = utils._char2utf8(win.VhostEdt.text())
        uname = utils._char2utf8(win.unameEdt.text())
        upass = utils._char2utf8(win.passEdt.text())

        msgBody = utils._char2utf8(win.sendContentTxtEdt.toPlainText())
        exchangeType = utils._char2utf8( win.exchangeTypeCmb.currentText())
        exchangeName  =  utils._char2utf8(win.exchageNameEdt.text())
        QueueName  = utils._char2utf8(win.QueueEdt.text())
        RtKey =      utils._char2utf8(win.RtKeyEdt.text())
        sendCount = win.sendCountSpBox.text()

        # MQ发送设置数据检查
        if ( msgBody.strip()=="" or
            exchangeName.strip()=="" or
            QueueName.strip()=="" or
            RtKey.strip()=="" or
            exchangeType.strip()=="" ):
                QtGui.QMessageBox.information( obj, u"输入出错", u"请输入完整的发送设置信息后再进行发送.." )
                return

        # 发送逻辑
        win.sendMsgBtn.setDisabled(True);
        # 得到设置的Tag列表
        tagArray = win.getReplaceTags(win)
        print 'tagArray=='
        print tagArray

        # 调用线程发送MQ消息,防止界面假死
        MqUtilObj = MqUtil.MQUtils( mainWindowObj= win )
        credentials = pika.PlainCredentials(uname, upass)
        print u"开始发送"
        sendMsgThread = threading.Thread(target=MqUtilObj.sendMessage , args=( server ,
                                                                                 port ,
                                                                                 vhost ,
                                                                                 credentials ,
                                                                                 exchangeType,
                                                                                 exchangeName,
                                                                                 QueueName,
                                                                                 RtKey,
                                                                                 msgBody,
                                                                                 int(sendCount)
                                                                                 ) )
        sendMsgThread.setDaemon(True)
        sendMsgThread.start()

        # 等线程跑完再返回
        '''
        sendMsgThread.join()
        sendResult = MqUtilObj.getSendResult()
        if sendResult['send_result'] == 'ok':
            QtGui.QMessageBox.information( obj, u"发送处理", u"发送完成" )
        else:
            QtGui.QMessageBox.information( obj, u"发送出错", u"发送出错,出错提示为" + sendResult['error_msg'])
        '''

    # 消费端MQ服务器连接按钮处理
    def scConnectBtnClicked( obj):
        # 读取MQ发送配置
        server = utils._char2utf8(win.cs_serverEdt.text())
        port  =  utils._char2utf8(win.cs_portEdt.text())
        vhost  = utils._char2utf8(win.cs_VhostEdt.text())

        uname = utils._char2utf8(win.cs_unameEdt.text())
        upass = utils._char2utf8(win.cs_passEdt.text())

        # 数据输入检验
        if ( server.strip()=="" or
            port.strip()=="" or
            vhost.strip()=="" or
            uname.strip()=="" or
            upass.strip()=="" ):
                QtGui.QMessageBox.information( obj, u"输入出错", u"请输入完整的MQ服务器信息后再进行连接.." )
                return

        # 禁用连接按钮
        win.cs_connectBtn.setDisabled(True)
        credentials = pika.PlainCredentials(uname, upass)

        # 线程连接，防止界面锁死
        MqUtilObj = MqUtil.MQUtils( mainWindowObj= win )
        connThread = threading.Thread(target=MqUtilObj.connMQServer,args=( server , port , vhost , credentials))
        connThread.setDaemon(True)
        connThread.start()
        connThread.join()

        if MqUtilObj.getConnResult() == True:
            QtGui.QMessageBox.information(win, u"连接提示", u"已经成功连接！")
            #禁止相关输入
            win.cs_serverEdt.setReadOnly(True)
            win.cs_portEdt.setReadOnly(True)
            win.cs_unameEdt.setReadOnly(True)
            win.cs_passEdt.setReadOnly(True)
            win.cs_VhostEdt.setReadOnly(True)
        else:
            QtGui.QMessageBox.information(win, u"连接失败", u"连接失败，请检查设置是否正确或MQ服务器是否开启.")
            win.cs_connectBtn.setDisabled(False)

    # 脚本测试
    def testScriptBtnClicked(self):
        scriptBody = utils._char2utf8( win.sc_sendContentTxtEdt.toPlainText())
        demo_json_str = u"{ item1:100, item2:'500', item3:{  item3_1:'结果值', item3_2:500.2  }  }"

        try:
            ctx = execjs.compile( scriptBody )
            ret_value = ctx.call("MsgCallback",demo_json_str)
            QtGui.QMessageBox.information( win, u"脚本测试", u"测试通过.返回结果为: "+ ret_value )
        except Exception as err:
            print unicode(err)
            QtGui.QMessageBox.information( win, u"脚本测试", u"测试失败.返回结果为: "+ repr(err) )

    # 开始监听
    def scListenerBtnClicked( obj ):
        if win.cs_serverEdt.isReadOnly() == False:
            QtGui.QMessageBox.information( obj, u"操作出错", u"请先进行测试连接操作，再进行消息监听操作.." )
            return

        # 监听参数设置
        listenQueue = utils._char2utf8(win.sc_queue_edt.text())
        cs_send_server = utils._char2utf8(win.cs_send_serverEdt.text())
        cs_send_port =  utils._char2utf8(win.cs_send_portEdt.text())
        cs_send_uname = utils._char2utf8(win.cs_send_unameEdt.text())
        cs_send_pass  = utils._char2utf8(win.cs_send_passEdt.text())
        cs_send_Vhost = utils._char2utf8(win.cs_send_VhostEdt.text())
        cs_send_exchangeType = utils._char2utf8(win.cs_send_exchangeType_cmb.currentText())
        cs_send_exchageName  = utils._char2utf8(win.cs_send_exchageNameEdt.text())
        cs_send_Queue = utils._char2utf8(win.cs_send_QueueEdt.text())
        cs_send_RtKey = utils._char2utf8(win.cs_send_RtKeyEdt.text())
        scriptBody = utils._char2utf8(win.sc_sendContentTxtEdt.toPlainText())

        if ( listenQueue.strip()==""):
            QtGui.QMessageBox.information( obj, u"输入出错", u"请输入监听Queue名称.." )
            return

        # 数据输入检验
        if (win.onrecvMsgChk.isChecked() == False and (
            cs_send_server.strip()=="" or
            cs_send_port.strip()=="" or
            cs_send_uname.strip()=="" or
            cs_send_pass.strip()=="" or
            cs_send_Vhost.strip()=="" or
            cs_send_exchageName.strip()=="" or
            cs_send_Queue.strip()=="" or
            cs_send_RtKey.strip()=="" or
            scriptBody.strip()=="" )):
                QtGui.QMessageBox.information( obj, u"输入出错", u"请输入完整的脚本处理信息、转发的MQ服务器信息后再进行监听处理.." )
                return

        server = utils._char2utf8(win.cs_serverEdt.text())
        port  =  int(utils._char2utf8(win.cs_portEdt.text()))
        vhost  = utils._char2utf8(win.cs_VhostEdt.text())

        uname = utils._char2utf8(win.cs_unameEdt.text())
        upass = utils._char2utf8(win.cs_passEdt.text())

        #组装转发MQ服务器配置对象
        consume_send_MQ_info = {
                                    'server':cs_send_server,
                                    'port':cs_send_server,
                                    'uname':cs_send_uname,
                                    'upass':cs_send_pass,
                                    'vhost':cs_send_Vhost,
                                    'exchangeType':cs_send_exchangeType,
                                    'exchangeName':cs_send_exchageName,
                                    'queueName':cs_send_Queue,
                                    'rtkey':cs_send_RtKey,
                                    'is_recv_sendflag':win.onrecvMsgChk.isChecked()
                                }

        # 调用监听线程进行处理
        win._currentMQUtilObj = MqUtil.MQUtils( mainWindowObj= win )
        credentials = pika.PlainCredentials(uname, upass)
        win._listenMsgThread = threading.Thread(target = win._currentMQUtilObj.ListenMessage , args=( server ,
                                                                                                 port ,
                                                                                                 vhost ,
                                                                                                 credentials ,
                                                                                                 listenQueue,
                                                                                                 scriptBody,
                                                                                                 consume_send_MQ_info
                                                                                                 ) )
        win._listenMsgThread.setDaemon(True)
        win._listenMsgThread.start()

        win.cs_startListenBtn.setDisabled(True)
        win.cs_stopListenBtn.setDisabled(False)

    # 要转发的MQ服务器测试连接
    def scTestConnectBtnClicked( obj ):
         # 读取MQ发送配置
        server = utils._char2utf8(win.cs_send_serverEdt.text())
        port  =  utils._char2utf8(win.cs_send_portEdt.text())
        vhost  = utils._char2utf8(win.cs_send_VhostEdt.text())

        uname = utils._char2utf8(win.cs_send_unameEdt.text())
        upass = utils._char2utf8(win.cs_send_passEdt.text())

        # 数据输入检验
        if ( server.strip()=="" or
            port.strip()=="" or
            vhost.strip()=="" or
            uname.strip()=="" or
            upass.strip()=="" ):
                QtGui.QMessageBox.information( obj, u"输入出错", u"请输入完整的MQ服务器信息后再进行连接.." )
                return

        # 禁用连接按钮
        win.cs_test_connectBtn.setDisabled(True)
        credentials = pika.PlainCredentials(uname, upass)

        # 线程连接，防止界面锁死
        MqUtilObj = MqUtil.MQUtils( mainWindowObj= win )
        connThread = threading.Thread(target=MqUtilObj.connMQServer,args=( server , port , vhost , credentials))
        connThread.setDaemon(True)
        connThread.start()
        connThread.join()

        if MqUtilObj.getConnResult() == True:
            QtGui.QMessageBox.information(win, u"连接提示", u"已经成功连接！")
            #禁止相关输入
            win.cs_send_serverEdt.setReadOnly(True)
            win.cs_send_portEdt.setReadOnly(True)
            win.cs_send_unameEdt.setReadOnly(True)
            win.cs_send_passEdt.setReadOnly(True)
            win.cs_send_VhostEdt.setReadOnly(True)
        else:
            QtGui.QMessageBox.information(win, u"连接失败", u"连接失败，请检查设置是否正确或MQ服务器是否开启.")
            win.cs_test_connectBtn.setDisabled(False)

    # 服务器编辑器完成编辑
    def serverEdtFinished( obj ,str ):
        sender= obj.sender()
        sendObjName = sender.objectName()
        if sendObjName == "serverEdt":
            if win.cs_serverEdt.isReadOnly() == False:
                win.cs_serverEdt.setText( str )
            if win.cs_send_serverEdt.isReadOnly() == False:
                win.cs_send_serverEdt.setText(str)

        if sendObjName == "portEdt":
            if win.cs_portEdt.isReadOnly() == False:
                win.cs_portEdt.setText( str )
            if win.cs_send_portEdt.isReadOnly() == False:
                win.cs_send_portEdt.setText(str)

        if sendObjName == "unameEdt":
            if win.cs_unameEdt.isReadOnly() == False:
                win.cs_unameEdt.setText( str )
            if win.cs_send_unameEdt.isReadOnly() == False:
                win.cs_send_unameEdt.setText(str)

        if sendObjName == "passEdt":
            if win.cs_passEdt.isReadOnly() == False:
                win.cs_passEdt.setText( str )
            if win.cs_send_passEdt.isReadOnly() == False:
                win.cs_send_passEdt.setText(str)

        if sendObjName == "VhostEdt":
            if win.cs_VhostEdt.isReadOnly() == False:
                win.cs_VhostEdt.setText( str )
            if win.cs_send_VhostEdt.isReadOnly() == False:
                win.cs_send_VhostEdt.setText(str)

        if sendObjName == "QueueEdt":
            if win.sc_queue_edt.isReadOnly() == False:
                win.sc_queue_edt.setText(str)
            if win.cs_send_QueueEdt.isReadOnly() == False:
                win.cs_send_QueueEdt.setText( str )

        if sendObjName == "RtKeyEdt":
            if win.cs_send_RtKeyEdt.isReadOnly() == False:
                win.cs_send_RtKeyEdt.setText( str )


    # 停止监听按钮
    def stopListenBtnClicked(obj):
        #if win._currentMQUtilObj != None:
        #    win._currentMQUtilObj.stopListenMessage()

        if win._currentMQUtilObj !=None and win._listenMsgThread.isAlive() == True:
            win._currentMQUtilObj.stop()

        win.cs_stopListenBtn.setDisabled(True)
        win.cs_startListenBtn.setDisabled(False)

# 绑定事件
def bindEvent(win):
    win.connect(win.connectBtn, QtCore.SIGNAL("clicked()"), win.connectBtnClicked)
    win.connect(win.sendMsgBtn, QtCore.SIGNAL("clicked()"), win.sendMessageBtnClicked)
    # 测试连接事件连接
    win.connect(win.cs_connectBtn, QtCore.SIGNAL("clicked()"), win.scConnectBtnClicked)
    # 开始监听事件连接
    win.connect(win.cs_startListenBtn, QtCore.SIGNAL("clicked()"), win.scListenerBtnClicked)
    # 脚本测试
    win.connect(win.testJsExecBtn, QtCore.SIGNAL("clicked()"), win.testScriptBtnClicked)
    # 消费后要转发消息的服务器测试连接
    win.connect(win.cs_test_connectBtn, QtCore.SIGNAL("clicked()"), win.scTestConnectBtnClicked)
    # 停止监听
    win.connect(win.cs_stopListenBtn, QtCore.SIGNAL("clicked()"), win.stopListenBtnClicked)

    # 编辑自动同步 - 服务器
    win.connect(win.serverEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - 端口
    win.connect(win.portEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - 用户名
    win.connect(win.unameEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - 密码
    win.connect(win.passEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - Vhost
    win.connect(win.VhostEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - 队列
    win.connect(win.QueueEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)
    # 编辑自动同步 - rounterKey
    win.connect(win.RtKeyEdt, QtCore.SIGNAL("textChanged(QString)"), win.serverEdtFinished)

app = QtGui.QApplication(sys.argv)
win = Ui_MainWindow(app)
# 绑定事件
bindEvent(win)

win.show()
app.exec_()