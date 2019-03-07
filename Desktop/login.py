import sys
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *


app = QApplication(sys.argv)
web = QWebEngineView()
web.settings().setAttribute(QWebSettings.PluginsEnabled, True)
web.load(QUrl("C:\\Users\\Boomerang\\Downloads\\portada.pdf"))
web.show()
app.exec_()