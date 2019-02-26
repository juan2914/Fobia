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
from validate_email import validate_email
IDUSER = 0
NPAC =""
IDPAC = 0


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

def CreateConexion():
    conexion = pymysql.connect(host="localhost", 
                           user="root", 
                           passwd="root", 
                           database="tt_fobia")
    cursor = conexion.cursor()
    return cursor, conexion

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
        query = "SELECT tipo, idUser FROM user WHERE USUARIO = '"+usuario +"' AND PASSWORD = '"+password+"';"
        print(query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchone()
        if(registro):
            self.hide()
            if registro[0]== 2 :
                menu_form = Menu(self)
                menu_form.show()
            else:
                psicologo_form = Psicologo(self)
                psicologo_form.show()

        else:
            cajaTexto("Usuario y/o contraseña incorrectos", 1)
        global IDUSER
        IDUSER = registro[1]
        print("----", IDUSER)
        
        
            

class Menu(QMainWindow):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        uic.loadUi('menu.ui', self)
        self.button_logout.clicked.connect(self.regresar)
        self.button_tratamiento.clicked.connect(self.tratamiento)

    def regresar(self):
        Menu.repaint()
        self.parent().show()
        self.close()

    def tratamiento(self):
        self.hide()
        tratamiento_form = Tratamiento(self)
        tratamiento_form.show()

class Tratamiento(QMainWindow):
    def __init__(self, parent=None):
        super (Tratamiento, self).__init__(parent)
        uic.loadUi('inicio.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_nvo_psicologo.clicked.connect(self.nuevoPsicologo)
        idUser = str(IDUSER)
        query = "SELECT * FROM paciente WHERE idUser = '"+idUser +"'"
        print(query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lista_psicologos.addItem(i[1]+" "+i[2]+" "+i[3])
        self.lista_psicologos.itemClicked.connect(self.itemSeleccionado)

    def itemSeleccionado(self, item):
        self.hide()
        global NPAC
        NPAC = item.text()
        #print(NPAC)
        detalles_Paciente = DetallePaciente(self)
        detalles_Paciente.show()
        #print(item.text())

        """uic.loadUi('frecuencia.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_terminar.clicked.connect(self.terminar_monitoreo)
        self.button_guardar.clicked.connect(self.guardar)"""

    def regresar(self):
        Tratamiento.repaint()
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

    def nuevoPsicologo(self):
        self.hide()
        nuevo_form = AltaPaciente(self)
        nuevo_form.show()

class DetallePaciente(QMainWindow):
    """docstring for DetallePaciente"""
    def __init__(self, parent = None):
        super(DetallePaciente, self).__init__(parent)
        uic.loadUi('detalles.ui', self)
        self.ApMaterno.hide()
        self.cargarDatos()
        self.button_volver.clicked.connect(self.regresar)
        self.button_editar.clicked.connect(self.editarPaciente)
        self.button_nuevoescenario.clicked.connect(self.nuevaTerapia)

    def regresar(self):
        self.parent().repaint()
        self.parent().show()
        self.close()
    def cargarDatos(self):
        n,p,m = NPAC.split(' ')
        query = "SELECT * FROM PACIENTE WHERE Nombre= '"+n+"' AND ApPaterno = '"+p+"' AND ApMaterno = '"+m+"'"
        print("QUery-_-",query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        global IDPAC
        for i in registro:
            self.Nombre.setText(i[1])
            self.ApPaterno.setText(i[2]+ " " + i[3])
            self.Edad.setText(str(i[5]))
            self.Domicilio.setText(i[4])
            self.Telefono.setText(str(i[6]))
            self.Correo.setText(i[7])
            IDPAC = i[0]

    def editarPaciente(self):
        editForm = EditForm(self)
        editForm.show()


    def nuevaTerapia(self):
        print("Estamos trabajando en ello!!")
        

class EditForm(QMainWindow):
    """docstring for EditForm"""
    def __init__(self, parent):
        super(EditForm, self).__init__(parent)
        uic.loadUi('editar.ui', self)
        n,p,m = NPAC.split(' ')
        query = "SELECT * FROM PACIENTE WHERE Nombre= '"+n+"' AND ApPaterno = '"+p+"' AND ApMaterno = '"+m+"'"
        print("QUery-_-",query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lineNombre.setText(str(i[1]))
            self.linePaterno.setText(str(i[2]))
            self.lineMaterno.setText(str(i[3]))
            self.lineDomicilio.setText(str(i[4]))
            self.lineEdad.setText(str(i[5]))
            self.lineTelefono.setText(str(i[6]))
            self.lineCorreo.setText(str(i[7]))
            self.textComentario.setText(str(i[9]))
        """self.lineNombre.repaint()
                                self.linePaterno.repaint()
                                self.lineMaterno.repaint()
                                self.lineDomicilio.repaint()
                                self.lineEdad.repaint()
                                self.lineTelefono.repaint()
                                self.lineCorreo.repaint()
                                self.textComentario.repaint()"""
        self.buttonCancel.clicked.connect(self.cancelar)
        self.buttonActualizar.clicked.connect(self.actualizar)

    def actualizar(self):
        Nombre = self.lineNombre.text()
        Paterno = self.linePaterno.text()
        Materno = self.lineMaterno.text()
        Domicilio = self.lineDomicilio.text()
        Edad = self.lineEdad.text()
        Telefono = self.lineTelefono.text()
        Correo = self.lineCorreo.text()
        Comentario = self.textComentario.toPlainText()
        if Edad.isdigit():
            if validate_email(Correo):
                if Telefono.isdigit():
                    query = "UPDATE paciente SET Nombre = '"+Nombre+"', ApPaterno = '"+Paterno+"', ApMaterno = '"+Materno+"', Domicilio = '"+Domicilio+"', Edad = '"+Edad+"', Telefono = '"+Telefono+"', Correo = '"+Correo+"', Comentario = '"+Comentario+"' WHERE IdPaciente = '"+str(IDPAC)+"' "
                    print (query)
                    cursor, conexion = CreateConexion()
                    cursor.execute(query)
                    msgBoxCancel = QtGui.QMessageBox( self )
                    msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                    msgBoxCancel.setText( "Paciente actualizado con exito" )
                    msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                    msgBoxCancel.exec_()
                    conexion.commit()
                    self.parent().repaint()
                    self.parent().show()
                    self.close()
                else:
                    msgBoxCancel = QtGui.QMessageBox( self )
                    msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                    msgBoxCancel.setText( "¡Telefono invalido, ingrese telefono valido!" )
                    msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                    msgBoxCancel.exec_()
            else:
                msgBoxCancel = QtGui.QMessageBox( self )
                msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                msgBoxCancel.setText( "¡Correo invalido, ingrese correo valido!" )
                msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                msgBoxCancel.exec_()
        else:
            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "¡Ingrese una edad valida!" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()


    def cancelar(self):
        self.close()
        

class AltaPaciente(QMainWindow):
    def __init__(self, parent=None):
        super(AltaPaciente, self).__init__(parent)
        uic.loadUi('alta_paciente.ui', self)
        self.line_especialidad.hide()
        self.label_6.hide()
        self.line_password_2.hide()
        self.label_9.hide()
        self.button_eliminar.hide()
        self.button_volver.clicked.connect(self.regresar)
        self.button_guardar.clicked.connect(self.guardar)

    def regresar(self):
        self.parent().repaint()
        self.parent().show()
        self.close()

    def guardar(self):
        nombre = self.line_nombre.text()
        app = self.line_app.text()
        apm = self.line_apm.text()
        domicilio = self.line_domicilio.text()
        edad = self.line_edad.text()
        telefono = self.line_telefono.text()
        correo = self.line_correo_2.text()
        sexo = str(self.combo_sexo.currentText())
        print(sexo)
        comentario = self.text_comentario.toPlainText()
        if sexo != "Seleccione una opción":
            if edad.isdigit():
                if validate_email(correo):
                    if telefono.isdigit():
                        query = "INSERT INTO paciente(IdPaciente, Nombre, ApPaterno, ApMaterno, Domicilio, Edad, Telefono, Correo, Sexo, Comentario, IdUser) VALUES (0,'"+nombre+"','"+app+"', '"+apm+"', '"+domicilio+"', '"+edad+"', '"+telefono+"', '"+correo+"','"+sexo+"', '"+comentario+"' , "+str(IDUSER)+");"
                        print (query)
                        cursor, conexion = CreateConexion()
                        cursor.execute(query)
                        msgBoxCancel = QtGui.QMessageBox( self )
                        msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                        msgBoxCancel.setText( "Paciente registrado con exito" )
                        msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                        msgBoxCancel.exec_()
                        conexion.commit()
                        conexion.close()
                        self.parent().repaint()
                        self.parent().show()
                        self.close()
                    else:
                        msgBoxCancel = QtGui.QMessageBox( self )
                        msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                        msgBoxCancel.setText( "¡Telefono invalido, ingrese telefono valido!" )
                        msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                        msgBoxCancel.exec_()
                else:
                    msgBoxCancel = QtGui.QMessageBox( self )
                    msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                    msgBoxCancel.setText( "¡Correo invalido, ingrese correo valido!" )
                    msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                    msgBoxCancel.exec_()
            else:
                msgBoxCancel = QtGui.QMessageBox( self )
                msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                msgBoxCancel.setText( "¡Ingrese una edad valida!" )
                msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                msgBoxCancel.exec_()
        else:
            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "¡Seleccione sexo!" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()
        

class Psicologo(QMainWindow):

    def __init__(self, parent=None):
        super(Psicologo, self).__init__(parent)
        uic.loadUi('inicio.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_nvo_psicologo.clicked.connect(self.nuevoPsicologo)
        query = "SELECT * FROM user"
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lista_psicologos.addItem(i[1]+" "+i[2]+" "+i[3])


    def regresar(self):
        self.parent().repaint()
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
        self.combo_sexo.hide()
        self.label_12.hide()
        self.text_comentario.hide()
        self.label_14.hide()
        self.line_correo_2.hide()
        self.label_13.hide()
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
        if password == pass2:
            if edad.isdigit():
                if validate_email(correo):
                    if telefono.isdigit():
                        query = "INSERT INTO user(idUser, Nombre, ApPaterno, ApMaterno, Domicilio, Edad, Telefono, Especialidad, Correo, Usuario, Password, Tipo) VALUES (0,'"+nombre+"','"+app+"', '"+apm+"', '"+domicilio+"', '"+edad+"', '"+telefono+"', '"+especialidad+"', '"+correo+"', '"+usuario+"', '"+password+"', 2);"
                        print (query)
                        cursor, conexion = CreateConexion()
                        cursor.execute(query)
                        msgBoxCancel = QtGui.QMessageBox( self )
                        msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                        msgBoxCancel.setText( "Usuario registrado con exito" )
                        msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                        msgBoxCancel.exec_()
                        conexion.commit()
                        conexion.close()
                        self.parent().show()
                        self.QMainWindow.update()
                        self.close()
                    else:
                        msgBoxCancel = QtGui.QMessageBox( self )
                        msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                        msgBoxCancel.setText( "¡Telefono invalido, ingrese telefono valido!" )
                        msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                        msgBoxCancel.exec_()
                else:
                    msgBoxCancel = QtGui.QMessageBox( self )
                    msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                    msgBoxCancel.setText( "¡Correo invalido, ingrese correo valido!" )
                    msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                    msgBoxCancel.exec_()
            else:
                msgBoxCancel = QtGui.QMessageBox( self )
                msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
                msgBoxCancel.setText( "¡Ingrese una edad valida!" )
                msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
                msgBoxCancel.exec_()
        else:
            msgBoxCancel = QtGui.QMessageBox( self )
            msgBoxCancel.setIcon( QtGui.QMessageBox.Information )
            msgBoxCancel.setText( "¡La contraseña no coincide, intentelo de nuevo!" )
            msgBoxCancel.addButton( QtGui.QMessageBox.Ok )
            msgBoxCancel.exec_()

        

    def regresar(self):
        self.parent().repaint()
        self.parent().show()
        self.close()

app = QApplication(sys.argv)
main = Login()
main.show()
sys.exit(app.exec_())

"""CREATE TABLE `tt_fobia`.`user` (
  `IdUser` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `ApPaterno` VARCHAR(45) NULL,
  `ApMaterno` VARCHAR(45) NULL,
  `Domicilio` VARCHAR(45) NULL,
  `Edad` INT NULL,
  `Telefono` INT NULL,
  `Especialidad` VARCHAR(100) NULL,
  `Correo` VARCHAR(50) NULL,
  `Usuario` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Tipo` INT NOT NULL,
  PRIMARY KEY (`IdUser`));

CREATE TABLE `tt_fobia`.`paciente` (
  `IdPaciente` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `ApPaterno` VARCHAR(45) NOT NULL,
  `ApMaterno` VARCHAR(45) NOT NULL,
  `Domicilio` VARCHAR(45) NULL,
  `Edad` INT NOT NULL,
  `Telefono` VARCHAR(45) NULL,
  `Sexo` INT NOT NULL,
  `Comentario` TEXT NULL,
  PRIMARY KEY (`IdPaciente`));



  """