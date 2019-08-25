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
        Form.resize(265, 120)
        self.Download_Button = QtWidgets.QPushButton(Form)
        self.Download_Button.setGeometry(QtCore.QRect(10, 60, 101, 51))
        self.Download_Button.setCheckable(False)
        self.Download_Button.setObjectName("Download_Button")
        self.ID_Label = QtWidgets.QLabel(Form)
        self.ID_Label.setGeometry(QtCore.QRect(120, 70, 141, 16))
        self.ID_Label.setObjectName("ID_Label")
        self.Name_Label = QtWidgets.QLabel(Form)
        self.Name_Label.setGeometry(QtCore.QRect(120, 90, 131, 16))
        self.Name_Label.setObjectName("Name_Label")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 241, 21))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        self.Download_Button.clicked.connect(self.On_Download_Button_Clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MusicDownloader"))
        self.Download_Button.setText(_translate("Form", "下载"))
        self.ID_Label.setText(_translate("Form", "歌曲ID:"))
        self.Name_Label.setText(_translate("Form", "歌曲名："))
        self.label.setText(_translate("Form", "输入下载歌曲ID或搜索歌曲"))

    def On_Download_Button_Clicked(self):
        pass