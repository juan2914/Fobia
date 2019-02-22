# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alta_paciente.ui'
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
        MainWindow.resize(800, 568)
        MainWindow.setMaximumSize(QtCore.QSize(800, 570))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.widget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"font: 13pt \"Trebuchet MS\";\n"
""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 201, 61))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"color:rgb(255, 255, 255);\n"
"font: 18pt \"Trebuchet MS\";\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.button_volver = QtGui.QPushButton(self.widget)
        self.button_volver.setGeometry(QtCore.QRect(20, 50, 31, 61))
        self.button_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_volver.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.button_volver.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_volver.setIcon(icon)
        self.button_volver.setObjectName(_fromUtf8("button_volver"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 180, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(250, 180, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 300, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_nombre = QtGui.QLineEdit(self.widget)
        self.line_nombre.setGeometry(QtCore.QRect(40, 200, 201, 20))
        self.line_nombre.setStyleSheet(_fromUtf8(""))
        self.line_nombre.setMaxLength(30)
        self.line_nombre.setObjectName(_fromUtf8("line_nombre"))
        self.line_apellidos = QtGui.QLineEdit(self.widget)
        self.line_apellidos.setGeometry(QtCore.QRect(250, 200, 321, 20))
        self.line_apellidos.setMaxLength(50)
        self.line_apellidos.setObjectName(_fromUtf8("line_apellidos"))
        self.line_domicilio = QtGui.QLineEdit(self.widget)
        self.line_domicilio.setGeometry(QtCore.QRect(40, 260, 401, 20))
        self.line_domicilio.setMaxLength(100)
        self.line_domicilio.setObjectName(_fromUtf8("line_domicilio"))
        self.line_telefono = QtGui.QLineEdit(self.widget)
        self.line_telefono.setGeometry(QtCore.QRect(40, 320, 201, 20))
        self.line_telefono.setMaxLength(20)
        self.line_telefono.setObjectName(_fromUtf8("line_telefono"))
        self.button_foto = QtGui.QPushButton(self.widget)
        self.button_foto.setGeometry(QtCore.QRect(610, 30, 121, 121))
        self.button_foto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_foto.setStyleSheet(_fromUtf8("border-radius: 60px;\n"
"border:1px solid black;"))
        self.button_foto.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_foto.setIcon(icon1)
        self.button_foto.setIconSize(QtCore.QSize(80, 80))
        self.button_foto.setObjectName(_fromUtf8("button_foto"))
        self.button_guardar = QtGui.QPushButton(self.widget)
        self.button_guardar.setGeometry(QtCore.QRect(160, 410, 181, 41))
        self.button_guardar.setStyleSheet(_fromUtf8("background-color: rgb(131, 131, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_guardar.setIcon(icon2)
        self.button_guardar.setObjectName(_fromUtf8("button_guardar"))
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(30, 90, 711, 341))
        self.frame.setStyleSheet(_fromUtf8("border: 1px solid gray;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(430, 150, 51, 16))
        self.label_4.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_edad = QtGui.QLineEdit(self.frame)
        self.line_edad.setGeometry(QtCore.QRect(430, 170, 113, 20))
        self.line_edad.setMaxLength(10)
        self.line_edad.setObjectName(_fromUtf8("line_edad"))
        self.line_especialidad = QtGui.QLineEdit(self.frame)
        self.line_especialidad.setGeometry(QtCore.QRect(220, 230, 321, 21))
        self.line_especialidad.setMaxLength(500)
        self.line_especialidad.setObjectName(_fromUtf8("line_especialidad"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(220, 210, 111, 16))
        self.label_6.setStyleSheet(_fromUtf8("border: 1px solid white;"))
        self.label_6.setLineWidth(0)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.raise_()
        self.line_edad.raise_()
        self.line_especialidad.raise_()
        self.label_4.raise_()
        self.button_eliminar = QtGui.QPushButton(self.widget)
        self.button_eliminar.setGeometry(QtCore.QRect(420, 410, 181, 41))
        self.button_eliminar.setStyleSheet(_fromUtf8("background-color: rgb(232, 119, 121);\n"
"color:rgb(255,255,255) ;\n"
"border-radius: 3px;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_eliminar.setIcon(icon3)
        self.button_eliminar.setObjectName(_fromUtf8("button_eliminar"))
        self.frame.raise_()
        self.pushButton.raise_()
        self.button_volver.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.line_nombre.raise_()
        self.line_apellidos.raise_()
        self.line_domicilio.raise_()
        self.line_telefono.raise_()
        self.button_foto.raise_()
        self.button_guardar.raise_()
        self.button_eliminar.raise_()
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
        self.pushButton.setText(_translate("MainWindow", "Editar Perfil", None))
        self.label.setText(_translate("MainWindow", "Nombre (s)", None))
        self.label_2.setText(_translate("MainWindow", "Apellidos", None))
        self.label_3.setText(_translate("MainWindow", "Domicilio", None))
        self.label_5.setText(_translate("MainWindow", "Telefono", None))
        self.button_guardar.setText(_translate("MainWindow", "Guardar", None))
        self.label_4.setText(_translate("MainWindow", "Edad", None))
        self.label_6.setText(_translate("MainWindow", "Especialidad", None))
        self.button_eliminar.setText(_translate("MainWindow", "Eliminar", None))

