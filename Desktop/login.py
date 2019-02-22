# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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
        MainWindow.resize(800, 611)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 570))
        self.widget.setMaximumSize(QtCore.QSize(800, 570))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(53, 28, 195);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(160, 130, 511, 261))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.line_usuario = QtGui.QLineEdit(self.widget_2)
        self.line_usuario.setGeometry(QtCore.QRect(150, 90, 191, 31))
        self.line_usuario.setStyleSheet(_fromUtf8("border-bottom: rgb(124, 124, 124);"))
        self.line_usuario.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_usuario.setText(_fromUtf8(""))
        self.line_usuario.setMaxLength(20)
        self.line_usuario.setPlaceholderText(_fromUtf8(""))
        self.line_usuario.setObjectName(_fromUtf8("line_usuario"))
        self.line_pass = QtGui.QLineEdit(self.widget_2)
        self.line_pass.setGeometry(QtCore.QRect(150, 150, 191, 31))
        self.line_pass.setInputMask(_fromUtf8(""))
        self.line_pass.setText(_fromUtf8(""))
        self.line_pass.setMaxLength(50)
        self.line_pass.setObjectName(_fromUtf8("line_pass"))
        self.line_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(210, 130, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.button_pass = QtGui.QPushButton(self.widget_2)
        self.button_pass.setGeometry(QtCore.QRect(190, 200, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_pass.setFont(font)
        self.button_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_pass.setMouseTracking(True)
        self.button_pass.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border: solid;\n"
""))
        self.button_pass.setAutoDefault(True)
        self.button_pass.setDefault(True)
        self.button_pass.setFlat(True)
        self.button_pass.setObjectName(_fromUtf8("button_pass"))
        self.button_login = QtGui.QPushButton(self.widget)
        self.button_login.setGeometry(QtCore.QRect(350, 380, 121, 31))
        self.button_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_login.setStyleSheet(_fromUtf8("background-color: rgb(227, 1, 5);\n"
"font: 10pt \"Trebuchet MS\";\n"
"color: rgb(255, 255, 255);"))
        self.button_login.setObjectName(_fromUtf8("button_login"))
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
        self.line_pass.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Ingrese contraseña</p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Contraseña", None))
        self.label_2.setText(_translate("MainWindow", "Usuario", None))
        self.button_pass.setText(_translate("MainWindow", "Olvide la contraseña", None))
        self.button_login.setText(_translate("MainWindow", "Entrar", None))

