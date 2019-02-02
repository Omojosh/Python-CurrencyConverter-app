# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/vlcsnap-2018-12-06-00h43m50s316.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(140, 189, 104, 31))
        self.textEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.convertFrm = QtWidgets.QComboBox(self.centralwidget)
        self.convertFrm.setGeometry(QtCore.QRect(270, 130, 151, 41))
        self.convertFrm.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.convertFrm.setObjectName("convertFrm")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertFrm.addItem("")
        self.convertTo = QtWidgets.QComboBox(self.centralwidget)
        self.convertTo.setGeometry(QtCore.QRect(270, 240, 151, 41))
        self.convertTo.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.convertTo.setObjectName("convertTo")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.convertTo.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 129, 101, 41))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 101, 41))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 311, 51))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 17pt \"Cantarell\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.amount = QtWidgets.QSpinBox(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(270, 190, 151, 29))
        self.amount.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.amount.setMinimum(1)
        self.amount.setMaximum(1000000000)
        self.amount.setObjectName("amount")
        self.convertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertBtn.setGeometry(QtCore.QRect(280, 300, 131, 31))
        self.convertBtn.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 oblique 13pt \"Cantarell\";\n"
"background-color: rgb(255, 255, 255);")
        self.convertBtn.setObjectName("convertBtn")
        self.Result = QtWidgets.QTextEdit(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(140, 350, 311, 70))
        self.Result.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.Result.setObjectName("Result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.convertBtn.clicked.connect(self.makeItHappen)

    def makeItHappen(self):
            amount = self.amount.value()
            currencyFrm = self.convertFrm.currentText()
            currencyTo = self.convertTo.currentText()
            url = 'https://v3.exchangerate-api.com/pair/299ed50dcd6809771a65613e/' + currencyFrm + '/' + currencyTo
            response = requests.get(url)
            data = response.json()
            result = data["rate"]
            answer = result * amount
            self.Result.setText(str(round(answer)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CurrencyConverter"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:13pt; font-weight:72; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400; font-style:normal;\">   Amount</span></p></body></html>"))
        self.convertFrm.setItemText(0, _translate("MainWindow", "USD"))
        self.convertFrm.setItemText(1, _translate("MainWindow", "NGN"))
        self.convertFrm.setItemText(2, _translate("MainWindow", "INR"))
        self.convertFrm.setItemText(3, _translate("MainWindow", "CAD"))
        self.convertFrm.setItemText(4, _translate("MainWindow", "EUR"))
        self.convertFrm.setItemText(5, _translate("MainWindow", "AOA"))
        self.convertFrm.setItemText(6, _translate("MainWindow", "BOB"))
        self.convertFrm.setItemText(7, _translate("MainWindow", "ARS"))
        self.convertFrm.setItemText(8, _translate("MainWindow", "AMD"))
        self.convertFrm.setItemText(9, _translate("MainWindow", "AUD"))
        self.convertFrm.setItemText(10, _translate("MainWindow", "CVE"))
        self.convertTo.setItemText(0, _translate("MainWindow", "USD"))
        self.convertTo.setItemText(1, _translate("MainWindow", "NGN"))
        self.convertTo.setItemText(2, _translate("MainWindow", "INR"))
        self.convertTo.setItemText(3, _translate("MainWindow", "CAD"))
        self.convertTo.setItemText(4, _translate("MainWindow", "EUR"))
        self.convertTo.setItemText(5, _translate("MainWindow", "AOA"))
        self.convertTo.setItemText(6, _translate("MainWindow", "BOB"))
        self.convertTo.setItemText(7, _translate("MainWindow", "ARS"))
        self.convertTo.setItemText(8, _translate("MainWindow", "AMD"))
        self.convertTo.setItemText(9, _translate("MainWindow", "AUD"))
        self.convertTo.setItemText(10, _translate("MainWindow", "CVE"))
        self.label.setText(_translate("MainWindow", "CurrencyFrom"))
        self.label_2.setText(_translate("MainWindow", "CurrencyTo"))
        self.label_3.setText(_translate("MainWindow", "          Currency  Converter "))
        self.convertBtn.setText(_translate("MainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

