# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Grade three\DataBase\lab2\ui\teacherdisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teacherinfo(object):
    def setupUi(self, teacherinfo):
        teacherinfo.setObjectName("teacherinfo")
        teacherinfo.resize(648, 474)
        self.centralwidget = QtWidgets.QWidget(teacherinfo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 171, 16))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(321, 20, 81, 20))
        self.name.setText("")
        self.name.setObjectName("name")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(290, 330, 93, 28))
        self.quit.setObjectName("quit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 72, 15))
        self.label_2.setObjectName("label_2")
        self.teacher_id = QtWidgets.QLabel(self.centralwidget)
        self.teacher_id.setGeometry(QtCore.QRect(560, 20, 72, 15))
        self.teacher_id.setText("")
        self.teacher_id.setObjectName("teacher_id")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 140, 72, 15))
        self.label_3.setObjectName("label_3")
        self.gender = QtWidgets.QLabel(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(340, 140, 72, 15))
        self.gender.setText("")
        self.gender.setObjectName("gender")
        self.place = QtWidgets.QLabel(self.centralwidget)
        self.place.setGeometry(QtCore.QRect(550, 140, 72, 15))
        self.place.setText("")
        self.place.setObjectName("place")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 140, 72, 15))
        self.label_4.setObjectName("label_4")
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(320, 80, 111, 16))
        self.id.setText("")
        self.id.setObjectName("id")
        self.nation = QtWidgets.QLabel(self.centralwidget)
        self.nation.setGeometry(QtCore.QRect(550, 80, 72, 15))
        self.nation.setText("")
        self.nation.setObjectName("nation")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 80, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 80, 72, 15))
        self.label_6.setObjectName("label_6")
        self.depart = QtWidgets.QLabel(self.centralwidget)
        self.depart.setGeometry(QtCore.QRect(320, 200, 72, 15))
        self.depart.setText("")
        self.depart.setObjectName("depart")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 200, 72, 15))
        self.label_9.setObjectName("label_9")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 191, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        teacherinfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(teacherinfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 26))
        self.menubar.setObjectName("menubar")
        teacherinfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(teacherinfo)
        self.statusbar.setObjectName("statusbar")
        teacherinfo.setStatusBar(self.statusbar)

        self.retranslateUi(teacherinfo)
        QtCore.QMetaObject.connectSlotsByName(teacherinfo)

    def retranslateUi(self, teacherinfo):
        _translate = QtCore.QCoreApplication.translate
        teacherinfo.setWindowTitle(_translate("teacherinfo", "MainWindow"))
        self.label.setText(_translate("teacherinfo", "姓名："))
        self.quit.setText(_translate("teacherinfo", "返回"))
        self.label_2.setText(_translate("teacherinfo", "编号："))
        self.label_3.setText(_translate("teacherinfo", "性别："))
        self.label_4.setText(_translate("teacherinfo", "籍贯："))
        self.label_5.setText(_translate("teacherinfo", "民族"))
        self.label_6.setText(_translate("teacherinfo", "身份证号："))
        self.label_9.setText(_translate("teacherinfo", "学院："))
