# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from error import Ui_error
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
import os
import sys


class Ui_Login(object):

    _username = "5a6852dab0cc1b764ab95fdccfa5109086595788f24a897a58024f5fa42e8f40"
    _password = "2f55f230e67bfe8212d87059d52ff5d4675eadc381d0a163b096f58d4edb913f"
    login_cancel_pressed = False
    store_value = 1


    def get_store_value(self):
        return self.store_value

    def get_is_cancel_pressed(self):
        return self.login_cancel_pressed

    def login_cancel_is_pressed(self, Login):
        self.login_cancel_pressed = True
        Login.close()

    # for opening error dialog box
    def error(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error()
        self.ui.seterrormessage("Cannot Login!!!")
        self.ui.setupUi(self.window)
        self.window.exec_()

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def hash_username_password(self, Login):
        username = str(self.username_input.text())
        password = str(self.password_input.text())
        salt = "f95e54460a7a1697862bdfdcfd4ac82366e49fcf"
        username = hashlib.sha3_256(username.encode()+salt.encode())
        password = hashlib.sha3_256(password.encode()+salt.encode())
        if self._username == username.hexdigest() and self._password == password.hexdigest():
            Login.close()
        else:
            self.error()

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(363, 165)
        icon = QtGui.QIcon()
        image_path = self.resource_path("login.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)

        self.gridLayout = QtWidgets.QGridLayout(Login)
        self.gridLayout.setObjectName("gridLayout")
        self.Login_frame = QtWidgets.QFrame(Login)
        self.Login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Login_frame.setObjectName("Login_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Login_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_label = QtWidgets.QLabel(self.Login_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.verticalLayout.addWidget(self.username_label)
        self.username_input = QtWidgets.QLineEdit(self.Login_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.username_input.setFont(font)
        self.username_input.setClearButtonEnabled(True)
        self.username_input.setObjectName("username_input")
        self.verticalLayout.addWidget(self.username_input)
        self.password_label = QtWidgets.QLabel(self.Login_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.verticalLayout.addWidget(self.password_label)
        self.password_input = QtWidgets.QLineEdit(self.Login_frame)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setObjectName("password_input")
        self.verticalLayout.addWidget(self.password_input)
        self.Ok_button = QtWidgets.QDialogButtonBox(self.Login_frame)
        self.Ok_button.setOrientation(QtCore.Qt.Horizontal)
        self.Ok_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Ok_button.setObjectName("Ok_button")
        self.verticalLayout.addWidget(self.Ok_button)
        self.gridLayout.addWidget(self.Login_frame, 0, 0, 1, 1)

        self.frame_for_radio = QtWidgets.QFrame(self.Login_frame)
        self.frame_for_radio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_for_radio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_for_radio.setObjectName("frame_for_radio")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_for_radio)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_store1 = QtWidgets.QRadioButton(self.frame_for_radio)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.radio_store1.setFont(font)
        self.radio_store1.setChecked(True)
        self.radio_store1.setObjectName("radio_store1")
        self.horizontalLayout.addWidget(self.radio_store1)
        self.radio_store2 = QtWidgets.QRadioButton(self.frame_for_radio)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.radio_store2.setFont(font)
        self.radio_store2.setObjectName("radio_store2")
        self.horizontalLayout.addWidget(self.radio_store2)
        self.radio_store3 = QtWidgets.QRadioButton(self.frame_for_radio)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.radio_store3.setFont(font)
        self.radio_store3.setObjectName("radio_store3")
        self.horizontalLayout.addWidget(self.radio_store3)
        self.verticalLayout.addWidget(self.frame_for_radio)


        self.radio_store1.toggled.connect(self.store_value)
        self.radio_store2.toggled.connect(self.store_value)
        self.radio_store3.toggled.connect(self.store_value)

        self.retranslateUi(Login)
        self.Ok_button.accepted.connect(lambda: self.hash_username_password(Login))
        self.Ok_button.rejected.connect(lambda: self.login_cancel_is_pressed(Login))
        QtCore.QMetaObject.connectSlotsByName(Login)
        self.store_value()


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.username_label.setText(_translate("Login", "Username :"))
        self.password_label.setText(_translate("Login", "Password :"))
        self.radio_store1.setText(_translate("Login", "Store 1"))
        self.radio_store2.setText(_translate("Login", "Store 2"))
        self.radio_store3.setText(_translate("Login", "Store 3"))

    def store_value(self):
        if self.radio_store2.isChecked():
            self.store_value = 2
        elif self.radio_store3.isChecked():
            self.store_value = 3
        else:
            self.store_value = 1

if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
