# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'POSTLAB_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 165)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.farenheit = QtWidgets.QLabel(self.centralwidget)
        self.farenheit.setGeometry(QtCore.QRect(60, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.farenheit.setFont(font)
        self.farenheit.setObjectName("farenheit")
        self.farenheit_2 = QtWidgets.QLabel(self.centralwidget)
        self.farenheit_2.setGeometry(QtCore.QRect(280, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.farenheit_2.setFont(font)
        self.farenheit_2.setObjectName("farenheit_2")
        self.input_far = QtWidgets.QTextEdit(self.centralwidget)
        self.input_far.setGeometry(QtCore.QRect(20, 50, 191, 31))
        self.input_far.setObjectName("input_far")
        self.input_cel = QtWidgets.QTextEdit(self.centralwidget)
        self.input_cel.setGeometry(QtCore.QRect(230, 50, 191, 31))
        self.input_cel.setObjectName("input_cel")
        self.FtC = QtWidgets.QPushButton(self.centralwidget)
        self.FtC.setGeometry(QtCore.QRect(60, 100, 93, 28))
        self.FtC.setObjectName("FtC")
        self.CtF = QtWidgets.QPushButton(self.centralwidget)
        self.CtF.setGeometry(QtCore.QRect(270, 100, 93, 28))
        self.CtF.setObjectName("CtF")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter"))
        self.farenheit.setText(_translate("MainWindow", "Farenheit:"))
        self.farenheit_2.setText(_translate("MainWindow", "Celcius:"))
        self.FtC.setText(_translate("MainWindow", ">>>>>>"))
        self.CtF.setText(_translate("MainWindow", "<<<<<<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
