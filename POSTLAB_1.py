"""
 *
 name:  Alcaraz, Flynn 
        Velasco, Louisse
        Garcia, Loven
 group no.: 4
 program description: A simple GUI that is made from PyQt designer.exe and is capable of converting the 
                        temperature from celcius to farenheit and vice versa.
 *
"""


from POSTLABgui_1 import *
from PyQt5.QtWidgets import QMessageBox
import sys

def convertToCelcius():
    try:
        num = float(ui.input_far.toPlainText())
        formula = float(5/9 * (num - 32))
        answer = ui.input_cel.setText(f"{formula}")
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Temperature Converter")
        msg.setText("Invalid Input. Please enter an integer value.")
        msg.exec_()


def convertToFarenheit():
    try:
        num = float(ui.input_cel.toPlainText())
        formula = float((num * (9/5)) + 32)
        answer = ui.input_far.setText(f"{formula}")
    except:
        msg = QMessageBox()
        msg.setWindowTitle("Temperature Converter")
        msg.setText("Invalid Input. Please enter an integer value.")
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.FtC.clicked.connect(convertToCelcius)
    ui.CtF.clicked.connect(convertToFarenheit)
    MainWindow.show()
    sys.exit(app.exec_())