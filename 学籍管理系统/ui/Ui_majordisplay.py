# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Grade three\DataBase\lab2\ui\majordisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAJORDISPLAY(object):
    def setupUi(self, MAJORDISPLAY):
        MAJORDISPLAY.setObjectName("MAJORDISPLAY")
        MAJORDISPLAY.resize(1045, 600)
        self.centralwidget = QtWidgets.QWidget(MAJORDISPLAY)
        self.centralwidget.setObjectName("centralwidget")
        self.departtable = QtWidgets.QTableWidget(self.centralwidget)
        self.departtable.setGeometry(QtCore.QRect(20, 30, 431, 261))
        self.departtable.setObjectName("departtable")
        self.departtable.setColumnCount(3)
        self.departtable.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.departtable.setHorizontalHeaderItem(2, item)
        self.majortable = QtWidgets.QTableWidget(self.centralwidget)
        self.majortable.setGeometry(QtCore.QRect(460, 30, 541, 281))
        self.majortable.setObjectName("majortable")
        self.majortable.setColumnCount(4)
        self.majortable.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.majortable.setHorizontalHeaderItem(3, item)
        self.adddepart = QtWidgets.QPushButton(self.centralwidget)
        self.adddepart.setGeometry(QtCore.QRect(160, 370, 111, 61))
        self.adddepart.setObjectName("adddepart")
        self.addmajor = QtWidgets.QPushButton(self.centralwidget)
        self.addmajor.setGeometry(QtCore.QRect(670, 357, 121, 61))
        self.addmajor.setObjectName("addmajor")
        MAJORDISPLAY.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MAJORDISPLAY)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        MAJORDISPLAY.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MAJORDISPLAY)
        self.statusbar.setObjectName("statusbar")
        MAJORDISPLAY.setStatusBar(self.statusbar)

        self.retranslateUi(MAJORDISPLAY)
        QtCore.QMetaObject.connectSlotsByName(MAJORDISPLAY)

    def retranslateUi(self, MAJORDISPLAY):
        _translate = QtCore.QCoreApplication.translate
        MAJORDISPLAY.setWindowTitle(_translate("MAJORDISPLAY", "MainWindow"))
        item = self.departtable.horizontalHeaderItem(0)
        item.setText(_translate("MAJORDISPLAY", "学院号"))
        item = self.departtable.horizontalHeaderItem(1)
        item.setText(_translate("MAJORDISPLAY", "学院名"))
        item = self.departtable.horizontalHeaderItem(2)
        item.setText(_translate("MAJORDISPLAY", "学院人数"))
        item = self.majortable.horizontalHeaderItem(0)
        item.setText(_translate("MAJORDISPLAY", "专业号"))
        item = self.majortable.horizontalHeaderItem(1)
        item.setText(_translate("MAJORDISPLAY", "专业名"))
        item = self.majortable.horizontalHeaderItem(2)
        item.setText(_translate("MAJORDISPLAY", "专业人数"))
        item = self.majortable.horizontalHeaderItem(3)
        item.setText(_translate("MAJORDISPLAY", "所属学院"))
        self.adddepart.setText(_translate("MAJORDISPLAY", "添加"))
        self.addmajor.setText(_translate("MAJORDISPLAY", "添加"))
