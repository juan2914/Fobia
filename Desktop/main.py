# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys
import pymysql


# Importar el código del modulo compilado UI
from login import Ui_MainWindow 
from inicio  import Ui_MainWindow 
from PyQt4 import *

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, uic

conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="root", 
                           database="tt_fobia")
cursor = conexion.cursor()

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

def cajaTexto(Mensaje, botones):
    msgBox = QtGui.QMessageBox()
    msgBox.setIcon( QtGui.QMessageBox.Information )
    msgBox.setText( Mensaje )
    if botones>1:
        msgBox.addButton(QtGui.QMessageBox.Yes).setText("Si")
        msgBox.addButton(QtGui.QMessageBox.No)
    else:
        msgBox.addButton(QtGui.QMessageBox.Ok)
    msgBox.exec_()

# Crear una clase para nuestra ventana principal
class Login(QMainWindow):

    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('login.ui', self)
        self.line_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.button_login.clicked.connect(self.iniciarSesion)
        self.line_pass.returnPressed.connect(self.button_login.click) #Login al presionar enter en la linea de contraseña

    def iniciarSesion(self):
        usuario = self.line_usuario.text()
        password = self.line_pass.text()
        query = "SELECT tipo FROM user WHERE USUARIO = '"+usuario +"' AND PASSWORD = '"+password+"';"
        cursor.execute(query)
        registro = cursor.fetchone()
        if(registro):
            self.hide()
            if registro[0]== 1 :
                menu_form = Menu(self)
                menu_form.show()
            else:
                psicologo_form = Psicologo(self)
                psicologo_form.show()

        else:
            cajaTexto("Usuario y/o contraseña incorrectos", 1)
            
        
            

class Menu(QMainWindow):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        uic.loadUi('menu.ui', self)
        self.button_logout.clicked.connect(self.regresar)
        self.button_tratamiento.clicked.connect(self.tratamiento)

    def regresar(self):
        self.parent().show()
        self.close()

    def tratamiento(self):
        self.hide()
        tratamiento_form = Tratamiento(self)
        tratamiento_form.show()

class Tratamiento(QMainWindow):
    def __init__(self, parent=None):
        super (Tratamiento, self).__init__(parent)
        uic.loadUi('frecuencia.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_terminar.clicked.connect(self.terminar_monitoreo)
        self.button_guardar.clicked.connect(self.guardar)

    def regresar(self):
        self.parent().show()
        self.close()

    def terminar_monitoreo(self):
        msgBox = QtGui.QMessageBox( self )
        msgBox.setIcon( QtGui.QMessageBox.Information )
        msgBox.setText( "¿Esta seguro que desea detener el monitoreo?" )
        msgBox.addButton( QtGui.QMessageBox.Yes ).setText('Si')
        msgBox.addButton( QtGui.QMessageBox.No ) 
        ret = msgBox.exec_()
        if ret == QtGui.QMessageBox.Yes:
            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "Monitoreo Terminado" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()
    def guardar(self):
        msgBoxCancel = QtGui.QMessageBox( self )
        msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
        msgBoxCancel.setText( "Monitoreo guardado" )
        msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
        msgBoxCancel.exec_()

        

class AltaPsico(QMainWindow):
    def __init__(self, parent=None):
        super(AltaPsico, self).__init__(parent)
        uic.loadUi('alta_paciente.ui', self)
        self.button_volver.clicked.connect(self.regresar)

    def regresar(self):
        self.parent().show()
        self.close()

class Psicologo(QMainWindow):

    def __init__(self, parent=None):
        super(Psicologo, self).__init__(parent)
        uic.loadUi('inicio.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_nvo_psicologo.clicked.connect(self.nuevoPsicologo)
        query = "SELECT * FROM user WHERE tipo = 2"
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lista_psicologos.addItem(i[1]+" "+i[2]+" "+i[3])


    def regresar(self):
        self.parent().show()
        self.close()

    def nuevoPsicologo(self):
        self.hide()
        nuevo_form = AltaPsico(self)
        nuevo_form.show()

class AltaPsico(QMainWindow):
    def __init__(self, parent=None):
        super(AltaPsico, self).__init__(parent)
        uic.loadUi('alta_paciente.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_guardar.clicked.connect(self.guardar)
        self.button_eliminar.hide()

    def guardar(self):
        nombre = self.line_nombre.text()
        app = self.line_app.text()
        apm = self.line_apm.text()
        domicilio = self.line_domicilio.text()
        edad = self.line_edad.text()
        telefono = self.line_telefono.text()
        especialidad = self.line_especialidad.text()
        correo = self.line_correo.text()
        usuario = self.line_usuario.text()
        password = self.line_password.text()
        pass2 = self.line_password_2.text()
        if(self.line_password.text() == (self.line_password_2.text())):
            query = "INSERT INTO user(idUser, Nombre, ApPaterno, ApMaterno, Domicilio, Edad, Telefono, Especialidad, Correo, Usuario, Password, Tipo) VALUES (0,'"+nombre+"','"+app+"', '"+apm+"', '"+domicilio+"', '"+edad+"', '"+telefono+"', '"+especialidad+"', '"+correo+"', '"+usuario+"', '"+password+"', 2);"
            print (query)
            cursor.execute(query)

            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "Usuario registrado con exito" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()
            self.parent().show()
            self.close()
        else:
            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "¡La contraseña no coincide, intentelo de nuevo!" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()

        

    def regresar(self):
        self.parent().show()
        self.close()

app = QApplication(sys.argv)
main = Login()
main.show()
sys.exit(app.exec_())

