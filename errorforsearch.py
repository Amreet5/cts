# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

#imports directory of the file
scriptDir = os.path.dirname(os.path.realpath(__file__))

class Ui_error(object):

    #method for setting up window
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(270, 153)
        error.setMinimumSize(QtCore.QSize(270, 153))
        error.setMaximumSize(QtCore.QSize(270, 153))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(scriptDir + os.path.sep + 'error.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error.setWindowIcon(icon)

        #ok button for the window
        self.ok = QtWidgets.QDialogButtonBox(error)
        self.ok.setGeometry(QtCore.QRect(120, 100, 81, 32))
        self.ok.setOrientation(QtCore.Qt.Horizontal)
        self.ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.ok.setObjectName("ok")

        #an label that displays "error"
        self.error_label = QtWidgets.QLabel(error)
        self.error_label.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.error_label.setFont(font)
        self.error_label.setObjectName("error_label")

        #label that displays word "invalid amount"
        self.invalid_amount = QtWidgets.QLabel(error)
        self.invalid_amount.setGeometry(QtCore.QRect(100, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.invalid_amount.setFont(font)
        self.invalid_amount.setObjectName("invalid_amount")


        #holds picture for the window
        self.picture = QtWidgets.QLabel(error)
        self.picture.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.picture.setPixmap(QtGui.QPixmap(scriptDir + os.path.sep + 'Error-icon.png'))
        self.picture.setScaledContents(True)

        #calling retranslateUi function
        self.retranslateUi(error)

        #when 'ok' button is pressed connects to 'error' function
        self.ok.accepted.connect(error.accept)

        #closes the window when 'cancel' button is pressed
        self.ok.rejected.connect(error.reject)

        QtCore.QMetaObject.connectSlotsByName(error)

    #retranslates the window
    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "Error"))
        self.error_label.setText(_translate("error", "ERROR !!!!"))
        self.invalid_amount.setText(_translate("error", "Invalid ID!!!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QDialog()
    ui = Ui_error()
    ui.setupUi(error)
    error.show()
    sys.exit(app.exec_())
