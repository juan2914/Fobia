# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
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
        MainWindow.resize(800, 570)
        MainWindow.setMaximumSize(QtCore.QSize(800, 570))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 801, 551))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(50, 40, 201, 61))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 20pt \"Trebuchet MS\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listView = QtGui.QListView(self.widget)
        self.listView.setGeometry(QtCore.QRect(60, 80, 691, 421))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.button_volver = QtGui.QPushButton(self.widget)
        self.button_volver.setGeometry(QtCore.QRect(30, 40, 31, 61))
        self.button_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_volver.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 10px;"))
        self.button_volver.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_volver.setIcon(icon)
        self.button_volver.setObjectName(_fromUtf8("button_volver"))
        self.button_nvo_psicologo = QtGui.QPushButton(self.widget)
        self.button_nvo_psicologo.setGeometry(QtCore.QRect(720, 460, 61, 61))
        self.button_nvo_psicologo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_nvo_psicologo.setStyleSheet(_fromUtf8("background-color: rgb(57, 57, 209);\n"
"border-radius: 30px;"))
        self.button_nvo_psicologo.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/nuevo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_nvo_psicologo.setIcon(icon1)
        self.button_nvo_psicologo.setCheckable(False)
        self.button_nvo_psicologo.setObjectName(_fromUtf8("button_nvo_psicologo"))
        self.lista_psicologos = QtGui.QListWidget(self.widget)
        self.lista_psicologos.setGeometry(QtCore.QRect(60, 100, 691, 401))
        self.lista_psicologos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lista_psicologos.setMovement(QtGui.QListView.Static)
        self.lista_psicologos.setFlow(QtGui.QListView.TopToBottom)
        self.lista_psicologos.setLayoutMode(QtGui.QListView.Batched)
        self.lista_psicologos.setViewMode(QtGui.QListView.ListMode)
        self.lista_psicologos.setSelectionRectVisible(True)
        self.lista_psicologos.setObjectName(_fromUtf8("lista_psicologos"))
        item = QtGui.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsEnabled)
        self.lista_psicologos.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(22)
        item.setFont(font)
        item.setIcon(icon2)
        self.lista_psicologos.addItem(item)
        self.listView.raise_()
        self.widget_2.raise_()
        self.button_volver.raise_()
        self.lista_psicologos.raise_()
        self.button_nvo_psicologo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lista_psicologos.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Psicólogos", None))
        __sortingEnabled = self.lista_psicologos.isSortingEnabled()
        self.lista_psicologos.setSortingEnabled(False)
        item = self.lista_psicologos.item(0)
        item.setText(_translate("MainWindow", "Psicólogo", None))
        item.setWhatsThis(_translate("MainWindow", "Seleccionar Paciente", "Seleccionar Paciente"))
        item = self.lista_psicologos.item(1)
        item.setText(_translate("MainWindow", "Psicólogo2", None))
        self.lista_psicologos.setSortingEnabled(__sortingEnabled)

