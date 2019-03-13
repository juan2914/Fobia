import random
import sys

import pyqtgraph as pg
from PyQt4 import QtGui, QtCore


class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Start Plotting')
        layout.addWidget(self.button)
        self.plot = pg.PlotWidget()
        layout.addWidget(self.plot)
        self.setLayout(layout)
        self.button.clicked.connect(self.plotter)

    def plotter(self):
        self.data = [0]
        self.curve = self.plot.getPlotItem().plot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.timer.start(0)

    def updater(self):
        self.data.append(self.data[-1] + 0.2 * (0.5 - random.random()))
        self.curve.setData(self.data)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.centralwidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.login_widget_1 = LoginWidget(self)
        self.horizontalLayout.addWidget(self.login_widget_1)

        self.login_widget_2 = LoginWidget(self)
        self.horizontalLayout.addWidget(self.login_widget_2)

        self.setCentralWidget(self.centralwidget)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())