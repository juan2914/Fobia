# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detalles.ui'
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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 800, 591))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(40, 30, 201, 61))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 20pt \"Trebuchet MS\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.button_volver = QtGui.QPushButton(self.widget)
        self.button_volver.setGeometry(QtCore.QRect(20, 30, 31, 61))
        self.button_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_volver.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.button_volver.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_volver.setIcon(icon)
        self.button_volver.setObjectName(_fromUtf8("button_volver"))
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 60, 421, 191))
        self.widget_3.setStyleSheet(_fromUtf8("border: 1px solid gray;\n"
"font: 10pt \"Trebuchet MS\";\n"
""))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.Nombre = QtGui.QLabel(self.widget_3)
        self.Nombre.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.Nombre.setStyleSheet(_fromUtf8("border: 1px solid white;\n"
"font: 75 15pt \"Trebuchet MS\";"))
        self.Nombre.setObjectName(_fromUtf8("Nombre"))
        self.ApPaterno = QtGui.QLabel(self.widget_3)
        self.ApPaterno.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.ApPaterno.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.ApPaterno.setObjectName(_fromUtf8("ApPaterno"))
        self.ApMaterno = QtGui.QLabel(self.widget_3)
        self.ApMaterno.setGeometry(QtCore.QRect(120, 100, 111, 16))
        self.ApMaterno.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.ApMaterno.setObjectName(_fromUtf8("ApMaterno"))
        self.Edad = QtGui.QLabel(self.widget_3)
        self.Edad.setGeometry(QtCore.QRect(20, 120, 51, 16))
        self.Edad.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.Edad.setObjectName(_fromUtf8("Edad"))
        self.Domicilio = QtGui.QLabel(self.widget_3)
        self.Domicilio.setGeometry(QtCore.QRect(20, 140, 61, 16))
        self.Domicilio.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.Domicilio.setObjectName(_fromUtf8("Domicilio"))
        self.Telefono = QtGui.QLabel(self.widget_3)
        self.Telefono.setGeometry(QtCore.QRect(20, 160, 47, 13))
        self.Telefono.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.Telefono.setObjectName(_fromUtf8("Telefono"))
        self.button_editar = QtGui.QPushButton(self.widget_3)
        self.button_editar.setGeometry(QtCore.QRect(370, 140, 50, 50))
        self.button_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_editar.setStyleSheet(_fromUtf8("background-color: rgb(40, 36, 176);\n"
"border: 1px solid white;\n"
"border-radius:25px;"))
        self.button_editar.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_editar.setIcon(icon1)
        self.button_editar.setIconSize(QtCore.QSize(20, 20))
        self.button_editar.setObjectName(_fromUtf8("button_editar"))
        self.button_foto = QtGui.QPushButton(self.widget)
        self.button_foto.setGeometry(QtCore.QRect(560, 70, 151, 151))
        self.button_foto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_foto.setStyleSheet(_fromUtf8("border: 1px solid gray;"))
        self.button_foto.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_foto.setIcon(icon2)
        self.button_foto.setIconSize(QtCore.QSize(120, 120))
        self.button_foto.setObjectName(_fromUtf8("button_foto"))
        self.lista_escenarios = QtGui.QListWidget(self.widget)
        self.lista_escenarios.setGeometry(QtCore.QRect(20, 280, 691, 251))
        self.lista_escenarios.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lista_escenarios.setObjectName(_fromUtf8("lista_escenarios"))
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/view.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.lista_escenarios.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        item.setIcon(icon3)
        self.lista_escenarios.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        item.setIcon(icon3)
        self.lista_escenarios.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        item.setIcon(icon3)
        self.lista_escenarios.addItem(item)
        self.button_nuevoescenario = QtGui.QPushButton(self.widget)
        self.button_nuevoescenario.setGeometry(QtCore.QRect(680, 490, 50, 50))
        self.button_nuevoescenario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_nuevoescenario.setStyleSheet(_fromUtf8("background-color: rgb(40, 36, 176);\n"
"border: 1px solid white;\n"
"border-radius:25px;"))
        self.button_nuevoescenario.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/nuevo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_nuevoescenario.setIcon(icon4)
        self.button_nuevoescenario.setIconSize(QtCore.QSize(20, 20))
        self.button_nuevoescenario.setObjectName(_fromUtf8("button_nuevoescenario"))
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(575, 200, 121, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.widget_3.raise_()
        self.widget_2.raise_()
        self.button_volver.raise_()
        self.button_foto.raise_()
        self.lista_escenarios.raise_()
        self.button_nuevoescenario.raise_()
        self.label_8.raise_()
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
        self.label.setText(_translate("MainWindow", "Detalles", None))
        self.Nombre.setText(_translate("MainWindow", "NOMBRE", None))
        self.ApPaterno.setText(_translate("MainWindow", "Apellido Paterno", None))
        self.ApMaterno.setText(_translate("MainWindow", "Apelldo Materno", None))
        self.Edad.setText(_translate("MainWindow", "Edad", None))
        self.Domicilio.setText(_translate("MainWindow", "Domicilio", None))
        self.Telefono.setText(_translate("MainWindow", "Teléfono", None))
        __sortingEnabled = self.lista_escenarios.isSortingEnabled()
        self.lista_escenarios.setSortingEnabled(False)
        item = self.lista_escenarios.item(0)
        item.setText(_translate("MainWindow", "Escenario 1", None))
        item = self.lista_escenarios.item(1)
        item.setText(_translate("MainWindow", "Escenario 2", None))
        item = self.lista_escenarios.item(2)
        item.setText(_translate("MainWindow", "Escenario 3", None))
        item = self.lista_escenarios.item(3)
        item.setText(_translate("MainWindow", "Escenario 4", None))
        self.lista_escenarios.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Seleccionar foto de perfil", None))

