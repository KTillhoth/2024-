# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Grade three\DataBase\lab2\ui\adminmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addstu = QtWidgets.QPushButton(self.centralwidget)
        self.addstu.setGeometry(QtCore.QRect(80, 40, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addstu.setFont(font)
        self.addstu.setObjectName("addstu")
        self.addteach = QtWidgets.QPushButton(self.centralwidget)
        self.addteach.setGeometry(QtCore.QRect(80, 150, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addteach.setFont(font)
        self.addteach.setObjectName("addteach")
        self.reward = QtWidgets.QPushButton(self.centralwidget)
        self.reward.setGeometry(QtCore.QRect(80, 260, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reward.setFont(font)
        self.reward.setObjectName("reward")
        self.major = QtWidgets.QPushButton(self.centralwidget)
        self.major.setGeometry(QtCore.QRect(290, 40, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.major.setFont(font)
        self.major.setObjectName("major")
        self.changemajor = QtWidgets.QPushButton(self.centralwidget)
        self.changemajor.setGeometry(QtCore.QRect(290, 150, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.changemajor.setFont(font)
        self.changemajor.setObjectName("changemajor")
        self.course = QtWidgets.QPushButton(self.centralwidget)
        self.course.setGeometry(QtCore.QRect(290, 250, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.course.setFont(font)
        self.course.setObjectName("course")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addstu.setText(_translate("MainWindow", "添加学生"))
        self.addteach.setText(_translate("MainWindow", "添加老师"))
        self.reward.setText(_translate("MainWindow", "奖惩"))
        self.major.setText(_translate("MainWindow", "专业与学院"))
        self.changemajor.setText(_translate("MainWindow", "转专业审核"))
        self.course.setText(_translate("MainWindow", "课程审核"))
