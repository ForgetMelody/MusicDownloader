# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(265, 316)
        self.Download_Button = QtWidgets.QPushButton(Form)
        self.Download_Button.setGeometry(QtCore.QRect(10, 60, 111, 51))
        self.Download_Button.setCheckable(False)
        self.Download_Button.setObjectName("Download_Button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 161, 21))
        self.textEdit.setObjectName("textEdit")
        self.ChangeDownloadDir_Button = QtWidgets.QPushButton(Form)
        self.ChangeDownloadDir_Button.setGeometry(QtCore.QRect(140, 60, 111, 51))
        self.ChangeDownloadDir_Button.setCheckable(False)
        self.ChangeDownloadDir_Button.setObjectName("ChangeDownloadDir_Button")
        self.Console = QtWidgets.QTextBrowser(Form)
        self.Console.setGeometry(QtCore.QRect(5, 121, 251, 191))
        self.Console.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Console.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Console.setObjectName("Console")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(180, 30, 71, 21))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        self.Download_Button.clicked.connect(self.Download_Button_click)
        self.ChangeDownloadDir_Button.clicked.connect(self.ChangeDownloadDir_Button_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MusicDownloader"))
        self.Download_Button.setText(_translate("Form", "下载"))
        self.label.setText(_translate("Form", "输入下载歌曲ID或搜索歌曲"))
        self.ChangeDownloadDir_Button.setText(_translate("Form", "选择下载路径"))
        self.checkBox.setText(_translate("Form", "下载歌词"))

    def ChangeDownloadDir_button_click(self):
        pass

    def Download_Button_click(self):
        pass
