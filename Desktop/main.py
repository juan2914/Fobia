# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys
import pymysql
from email.mime.text import MIMEText
from smtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Importar el código del modulo compilado UI
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from validate_email import validate_email
import os, platform, logging
IDUSER = 0
NPAC =""
NUSER = ""
IDPAC = 0
IDSESSION = 0

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

if platform.platform().startswith('Windows'):
    fichero_log = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'log.log')
else:
    fichero_log = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.log')

print('Archivo Log en ', fichero_log)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = 'w',)
logging.debug('Comienza el programa')


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
        self.button_pass.clicked.connect(self.recuperarPass)

    def recuperarPass(self):
        logging.info("Modulo enviar correo")
        rem ="Administrador Cuentas"
        asunto = "Recuperacion de contraseña"
        mensaje = "Esta es su contraseña:  "
        mail, ok = QInputDialog.getText(self, 'Recuperar contraseña', 'Ingresa tu correo:')
        if ok:
            cursor, conexion = CreateConexion()
            query = "SELECT Password FROM USER WHERE Correo = '"+mail+"' "
            cursor.execute(query)
            registro = cursor.fetchone()
            if registro:
                msg = MIMEMultipart()
                msg['From'] = rem
                msg['To'] = mail
                msg['Subject'] = asunto
                body = mensaje+ registro[0]
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('tt.2018a097@gmail.com', 'ttfobiaadministrador')
                text = str(msg)
                try:
                    server.sendmail(rem, mail, text)
                    server.quit()
                    cajaTexto("Contraseña enviada al correo",1)
                    logging.info("Correo enviado exitosamente")
                except Exception as e:
                    logging.warning("Error al enviar correo "+str(e) + " " + rem)
                    print(Exception, e)        
                    cajaTexto("Ocurrio un error al enviar correo",1)
            else:
                logging.info("Correo no registrado " + "'"+mail+"'")
                cajaTexto("Correo no registrado!!!", 1)
            self.recuperarPass()


    def iniciarSesion(self):
        usuario = self.line_usuario.text()
        password = self.line_pass.text()
        query = "SELECT tipo, idUser FROM user WHERE USUARIO = '"+usuario +"' AND PASSWORD = '"+password+"';"
        print(query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchone()
        global IDUSER, IDSESSION
        if(registro):
            IDUSER = registro[1]
            IDSESSION = registro[1]
            self.hide()
            if registro[0]== 2 :
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
        uic.loadUi('inicio.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_nvo_psicologo.clicked.connect(self.nuevoPsicologo)
        self.label.setText("Pacientes")
        self.load_from_db()
        self.lista_psicologos.itemClicked.connect(self.itemSeleccionado)

    def load_from_db(self):
        idUser = str(IDUSER)
        self.lista_psicologos.clear()
        query = "SELECT * FROM paciente WHERE idUser = '"+idUser +"'"
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lista_psicologos.addItem("{} {} {}".format(i[1], i[2], i[3]))

    def itemSeleccionado(self, item):
        self.hide()
        global NPAC
        NPAC = item.text()
        detalles_Paciente = DetallePaciente(self)
        detalles_Paciente.show()

    def regresar(self):
        self.parent().show()
        self.close()

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
        self.button_volver.clicked.connect(self.regresar)
        self.button_editar.clicked.connect(self.editarPaciente)
        self.button_nuevoescenario.clicked.connect(self.nuevaTerapia)
        #self.lista_escenarios.itemClicked.connect(self.escenario_seleccionado)
        self.cargarDatos()


    def regresar(self):
        self.parent().show()
        self.parent().load_from_db()
        self.close()

    def cargarDatos(self):
        self.Nombre.clear()
        self.ApPaterno.clear()
        self.Edad.clear()
        self.Domicilio.clear()
        self.Telefono.clear()
        self.Correo.clear()
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
        self.hide()
        #print = item.text()
        lectura_frecuencia = LecturaFrecuencia(self)
        lectura_frecuencia.show()

class LecturaFrecuencia(QMainWindow):
    """docstring for LecturaFrecuencia"""
    def __init__(self, parent):
        super(LecturaFrecuencia, self).__init__(parent)
        uic.loadUi('frecuencia.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_terminar.clicked.connect(self.terminar_monitoreo)
        self.button_guardar.clicked.connect(self.guardar)
    
    def cajaTexto(self, texto, botones):
        msgBox = QtGui.QMessageBox( self )
        msgBox.setIcon( QtGui.QMessageBox.Information )
        msgBox.setText( texto )
        if botones>1:
            msgBox.addButton(QtGui.QMessageBox.Yes).setText("Si")
            msgBox.addButton(QtGui.QMessageBox.No)
        else:
            msgBox.addButton(QtGui.QMessageBox.Ok)
        return msgBox.exec_()
    
    def terminar_monitoreo(self):
        mess = self.cajaTexto("¿Esta seguro que desea detener el monitoreo?", 2)
        if mess == QtGui.QMessageBox.Yes:
            self.cajaTexto("Monitoreo Terminado",1)
        else:
            print("Otro")
    def guardar(self):
        self.cajaTexto("Monitoreo guardado",1)

    def regresar(self):
        self.parent().show()
        self.close()

class EditForm(QMainWindow):
    """docstring for EditForm"""
    def __init__(self, parent):
        super(EditForm, self).__init__(parent)
        uic.loadUi('editar.ui', self)
        self.load_db()

    def cajaTexto(self, texto, botones):
        msgBox = QtGui.QMessageBox( self )
        msgBox.setIcon( QtGui.QMessageBox.Information )
        msgBox.setText( texto )
        if botones>1:
            msgBox.addButton(QtGui.QMessageBox.Yes).setText("Si")
            msgBox.addButton(QtGui.QMessageBox.No)
        else:
            msgBox.addButton(QtGui.QMessageBox.Ok)
        return msgBox.exec_()

    def load_db(self):
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
        self.buttonCancel.clicked.connect(self.cancelar)
        self.buttonActualizar.clicked.connect(self.actualizar)

    def actualizar(self):
        global NPAC
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
                    self.cajaTexto("Paciente actualizado con exito",1)
                    conexion.commit()
                    conexion.close()
                    NPAC = Nombre+" "+Paterno+" "+Materno
                    self.parent().show()
                    self.parent().cargarDatos()
                    self.close()
                else:
                    self.cajaTexto("¡Telefono invalido, ingrese telefono valido!",1)
            else:
                self.cajaTexto("¡Correo invalido, ingrese correo valido!",1)
        else:
            self.cajaTexto("¡Ingrese una edad valida!",1)

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

    def cajaTexto(self, texto, botones):
        msgBox = QtGui.QMessageBox( self )
        msgBox.setIcon( QtGui.QMessageBox.Information )
        msgBox.setText( texto )
        if botones>1:
            msgBox.addButton(QtGui.QMessageBox.Yes).setText("Si")
            msgBox.addButton(QtGui.QMessageBox.No)
        else:
            msgBox.addButton(QtGui.QMessageBox.Ok)
        return msgBox.exec_()

    def regresar(self):
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
                        self.cajaTexto("Paciente registrado con exito",1)
                        conexion.commit()
                        conexion.close()
                        self.parent().show()
                        self.parent().load_from_db()
                        self.close()
                    else:
                        self.cajaTexto("¡Telefono invalido, ingrese telefono valido!",1)
                else:
                    self.cajaTexto("¡Correo invalido, ingrese correo valido!" ,1)
            else:
                self.cajaTexto("¡Ingrese una edad valida!" ,1)
        else:
            self.cajaTexto("¡Seleccione sexo!" ,1)
        

class Psicologo(QMainWindow):

    def __init__(self, parent=None):
        super(Psicologo, self).__init__(parent)
        uic.loadUi('inicio.ui', self)
        self.button_volver.clicked.connect(self.regresar)
        self.button_nvo_psicologo.clicked.connect(self.nuevoPsicologo)
        self.lista_psicologos.itemClicked.connect(self.itemSeleccionado)
        self.load_from_db()

    def load_from_db(self):
        self.lista_psicologos.clear()
        #print(IDSESSION, IDUSER)
        query = "SELECT * FROM user WHERE NOT idUser = '"+str(IDSESSION)+"'"
        print(query)
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        for i in registro:
            self.lista_psicologos.addItem("{} {} {}".format(i[1], i[2], i[3]))

    def itemSeleccionado(self, item):
        self.hide()
        global NUSER
        NUSER = item.text()
        editarPerfil = AltaPsico(self)
        editarPerfil.show()
        editarPerfil.button_eliminar.show()
        editarPerfil.button_actualizar.show()
        editarPerfil.cargarDatos()


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
        self.combo_sexo.hide()
        self.label_12.hide()
        self.text_comentario.hide()
        self.label_14.hide()
        self.line_correo_2.hide()
        self.label_13.hide()
        self.button_actualizar.hide()
        self.button_volver.clicked.connect(self.regresar)
        self.button_guardar.clicked.connect(self.guardar)
        self.line_password.setEchoMode(QtGui.QLineEdit.Password)
        self.line_password_2.setEchoMode(QtGui.QLineEdit.Password)
        self.button_eliminar.hide()
        self.button_actualizar.clicked.connect(self.actualizar)
        self.button_eliminar.clicked.connect(self.eliminar)

    def cajaTexto(self, texto, botones):
        msgBox = QtGui.QMessageBox( self )
        msgBox.setIcon( QtGui.QMessageBox.Information )
        msgBox.setText( texto )
        if botones>1:
            msgBox.addButton(QtGui.QMessageBox.Yes).setText("Si")
            msgBox.addButton(QtGui.QMessageBox.No)
        else:
            msgBox.addButton(QtGui.QMessageBox.Ok)
        return msgBox.exec_()

    def cargarDatos(self):
        n,p,m = NUSER.split(' ')
        query = "SELECT * FROM USER WHERE Nombre= '"+n+"' AND ApPaterno = '"+p+"' AND ApMaterno = '"+m+"'"
        cursor, conexion = CreateConexion()
        cursor.execute(query)
        registro = cursor.fetchall()
        global IDUSER
        for i in registro:
            IDUSER = i[0]
            self.line_nombre.setText(str(i[1]))
            self.line_app.setText(str(i[2]))
            self.line_apm.setText(str(i[3]))
            self.line_domicilio.setText(str(i[4]))
            self.line_edad.setText(str(i[5]))
            self.line_telefono.setText(str(i[6]))
            self.line_especialidad.setText(str(i[7]))
            self.line_correo.setText(str(i[8]))
            self.line_usuario.setText(str(i[9]))
            self.line_password.setText(str(i[10]))
            self.line_password_2.setText(str(i[10]))

    def eliminar(self):
        if(IDSESSION == IDUSER):
            self.cajaTexto("No puedes eliminar tu propio perfil",1)
        try:
            query = "DELETE FROM USER WHERE IdUser = '"+str(IDUSER)+"'"
            cursor, conexion = CreateConexion()
            cursor.execute(query)
            self.cajaTexto("Usuario eliminado con exito",1)
            conexion.commit()
            conexion.close()
            self.parent().load_from_db()
            self.parent().show()
            self.close()
        except Exception as e:
            self.cajaTexto("No se pueden eliminar perfiles con pacientes",1)

    def actualizar(self):
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
                        query = "UPDATE USER SET Nombre = '"+nombre+"', ApPaterno = '"+app+"', ApMaterno = '"+apm+"', Domicilio = '"+domicilio+"', Edad = '"+edad+"', Telefono = '"+telefono+"', Especialidad = '"+especialidad+"', Correo = '"+ correo+"', Usuario = '"+usuario+"', Password = '"+password+"' WHERE IdUser = '"+str(IDUSER)+"' "
                        print (query)
                        cursor, conexion = CreateConexion()
                        cursor.execute(query)
                        self.cajaTexto("¡Usuario actualizado con exito!",1)
                        conexion.commit()
                        conexion.close()
                        self.parent().load_from_db()
                        self.parent().show()
                        self.close()
                    else:
                        self.cajaTexto("¡Telefono invalido, ingrese telefono valido!",1)
                else:
                    self.cajaTexto("¡Correo invalido, ingrese correo valido!" ,1)
            else:
                self.cajaTexto("¡Ingrese una edad valida!" ,1)
        else:
            self.cajaTexto("¡Las contraseñas no coinciden, intente de nuevo!" ,1)

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
                        self.cajaTexto("¡Usuario registrado con exito!",1)
                        conexion.commit()
                        conexion.close()
                        self.parent().load_from_db()
                        self.parent().show()
                        self.close()
                    else:
                        self.cajaTexto("¡Telefono invalido, ingrese telefono valido!",1)
                else:
                    self.cajaTexto("¡Correo invalido, ingrese correo valido!" ,1)
            else:
                self.cajaTexto("¡Ingrese una edad valida!" ,1)
        else:
            self.cajaTexto("¡Las contraseñas no coinciden, intente de nuevo!" ,1)

    def regresar(self):
        self.parent().close()
        self.parent().show()
        self.close()
app = QApplication(sys.argv)
main = Login()
main.show()
sys.exit(app.exec_())