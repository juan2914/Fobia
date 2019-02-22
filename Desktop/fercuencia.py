# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frecuencia.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 201, 61))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 20pt \"Trebuchet MS\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.button_volver = QtGui.QPushButton(self.centralwidget)
        self.button_volver.setGeometry(QtCore.QRect(10, 20, 31, 61))
        self.button_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_volver.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.button_volver.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_volver.setIcon(icon)
        self.button_volver.setObjectName(_fromUtf8("button_volver"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 50, 701, 431))
        self.widget.setStyleSheet(_fromUtf8("border: 1px solid gray;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.frecuencia = QtGui.QLabel(self.widget)
        self.frecuencia.setGeometry(QtCore.QRect(540, 140, 91, 101))
        self.frecuencia.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.frecuencia.setObjectName(_fromUtf8("frecuencia"))
        self.button_iniciar = QtGui.QPushButton(self.widget)
        self.button_iniciar.setGeometry(QtCore.QRect(520, 250, 75, 23))
        self.button_iniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_iniciar.setStyleSheet(_fromUtf8("background-color: rgb(97, 255, 97);\n"
"border-radius: 5px;"))
        self.button_iniciar.setObjectName(_fromUtf8("button_iniciar"))
        self.button_terminar = QtGui.QPushButton(self.widget)
        self.button_terminar.setGeometry(QtCore.QRect(595, 250, 75, 23))
        self.button_terminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_terminar.setStyleSheet(_fromUtf8("background-color: rgb(255, 184, 60);\n"
"border-radius: 5px;"))
        self.button_terminar.setObjectName(_fromUtf8("button_terminar"))
        self.button_guardar = QtGui.QPushButton(self.widget)
        self.button_guardar.setGeometry(QtCore.QRect(560, 290, 75, 23))
        self.button_guardar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_guardar.setStyleSheet(_fromUtf8("background-color: rgb(30, 14, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;"))
        self.button_guardar.setObjectName(_fromUtf8("button_guardar"))
        self.frecuencia_grafica = QtGui.QLabel(self.widget)
        self.frecuencia_grafica.setGeometry(QtCore.QRect(50, 100, 351, 241))
        self.frecuencia_grafica.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.frecuencia_grafica.setText(_fromUtf8(""))
        self.frecuencia_grafica.setPixmap(QtGui.QPixmap(_fromUtf8("Icon/pqrst.png")))
        self.frecuencia_grafica.setScaledContents(True)
        self.frecuencia_grafica.setObjectName(_fromUtf8("frecuencia_grafica"))
        self.widget.raise_()
        self.widget_2.raise_()
        self.button_volver.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Monitoreo", None))
        self.frecuencia.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">00</span></p></body></html>", None))
        self.button_iniciar.setText(_translate("MainWindow", "Iniciar", None))
        self.button_terminar.setText(_translate("MainWindow", "Detener", None))
        self.button_guardar.setText(_translate("MainWindow", "Guardar", None))

