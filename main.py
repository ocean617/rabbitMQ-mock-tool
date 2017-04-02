# coding=utf-8

# rabbitMQ Mock工具
import sys

import utils
import pika

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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(995, 678)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 991, 591))
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
        self.label_4.setGeometry(QtCore.QRect(310, 30, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(470, 30, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(64, 27, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 27, 81, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 27, 111, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 28, 131, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.connectBtn = QtGui.QPushButton(self.groupBox)
        self.connectBtn.setGeometry(QtCore.QRect(824, 22, 121, 23))
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.sendBox = QtGui.QGroupBox(self.tab_sender)
        self.sendBox.setGeometry(QtCore.QRect(10, 80, 961, 481))
        self.sendBox.setObjectName(_fromUtf8("sendBox"))
        self.label_6 = QtGui.QLabel(self.sendBox)
        self.label_6.setGeometry(QtCore.QRect(10, 22, 501, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.scrollArea = QtGui.QScrollArea(self.sendBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 531, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 429))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 531, 431))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_sender, _fromUtf8(""))
        self.tab_recv = QtGui.QWidget()
        self.tab_recv.setObjectName(_fromUtf8("tab_recv"))
        self.tabWidget.addTab(self.tab_recv, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 14pt \"微软雅黑\";"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "RabbitMQ 服务器设置", None))
        self.label_2.setText(_translate("MainWindow", "服务器IP", None))
        self.label_3.setText(_translate("MainWindow", "端口", None))
        self.label_4.setText(_translate("MainWindow", "用户名", None))
        self.label_5.setText(_translate("MainWindow", "密码", None))
        self.connectBtn.setText(_translate("MainWindow", "连  接", None))
        self.sendBox.setTitle(_translate("MainWindow", "发送设置", None))
        self.label_6.setText(_translate("MainWindow", "发送内容，可指定替换标识,格式: $英文标识$", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sender), _translate("MainWindow", "发送", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recv), _translate("MainWindow", "消费", None))
        self.label.setText(_translate("MainWindow", "Rabbit MQ Mock Tool", None))

    # 初始化处理
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        abnormal_label = QtGui.QLabel(u"系统准备就绪   |   Ver:1.0 ")
        abnormal_label.setStyleSheet(' QLabel {color: green}')
        self.statusBar().addWidget(abnormal_label)
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
    def connectBtnClicked(obj):
        win.connectBtn.setDisabled(True)

        uname = utils._char2utf8(win.lineEdit_3.text())
        upass = utils._char2utf8(win.lineEdit_4.text())

        # credentials = pika.PlainCredentials('guest', 'guest')
        credentials = pika.PlainCredentials(uname, upass)

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.39', 5672, '/', credentials))
            QtGui.QMessageBox.information(obj, u"连接提示", u"已经成功连接！")
        except Exception ,e:
            QtGui.QMessageBox.information(obj, u"连接失败", u"连接失败，请检查设置是否正确或MQ服务器是否开启." + e.message)
            win.connectBtn.setDisabled(False)


# 绑定事件
def bindEvent(win):
    win.connect(win.connectBtn, QtCore.SIGNAL("clicked()"), win.connectBtnClicked)

app = QtGui.QApplication(sys.argv)
win = Ui_MainWindow()
# 绑定事件
bindEvent(win)
win.show()
app.exec_()
