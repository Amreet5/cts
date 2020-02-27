
from PyQt5 import QtCore, QtGui, QtWidgets
from error import Ui_error
import os
import sys


class Ui_cash_input(object):
    amount = -1.0
    total = 0.0
    cancel_button_is_clicked = False

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_info_about_cancel_button(self):
        return self.cancel_button_is_clicked

    #setting total
    def settotal(self, total):
        self.total = total

    #get method for getting the amount
    def getamount(self):
        return self.amount


    # for opening error dialog box
    def error(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error()
        self.ui.seterrormessage("Invalid Amount!!! ")
        self.ui.setupUi(self.window)
        self.window.exec_()


    #error handling
    def verify(self, cash_input):
        valid = True
        try:
            a = float(self.input_cash_amount.text())

        except:
            valid = False
        if (valid == True and a > 0) and (self.total <= a):
            cash_input.close()
            self.amount = float(self.input_cash_amount.text())
        else:
            self.error()
            self.input_cash_amount.setFocus()

    def setupUi(self, cash_input):

        cash_input.setObjectName("cash_input")
        cash_input.resize(216, 119)
        cash_input.setMinimumSize(QtCore.QSize(216, 119))
        cash_input.setMaximumSize(QtCore.QSize(216, 119))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        cash_input.setFont(font)
        icon = QtGui.QIcon()
        image_path = self.resource_path("cash.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cash_input.setWindowIcon(icon)

        self.ok = QtWidgets.QDialogButtonBox(cash_input)
        self.ok.setGeometry(QtCore.QRect(40, 70, 161, 32))
        self.ok.setOrientation(QtCore.Qt.Horizontal)
        self.ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok.setObjectName("ok")
        self.ok.accepted.connect(lambda: self.verify(cash_input))


        self.cash_label = QtWidgets.QLabel(cash_input)
        self.cash_label.setGeometry(QtCore.QRect(10, 20, 101, 21))
        self.cash_label.setObjectName("cash_label")

        self.input_cash_amount = QtWidgets.QLineEdit(cash_input)
        self.input_cash_amount.setGeometry(QtCore.QRect(110, 20, 91, 21))
        self.input_cash_amount.setMaxLength(8)
        self.input_cash_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_cash_amount.setClearButtonEnabled(True)
        self.input_cash_amount.setObjectName("input_cash_amount")
        self.input_cash_amount.setFocus()

        self.retranslateUi(cash_input)
        self.ok.rejected.connect(lambda: self.cancel_button_clicked(cash_input))
        QtCore.QMetaObject.connectSlotsByName(cash_input)

    def cancel_button_clicked(self, cash_input):
        self.cancel_button_is_clicked = True
        cash_input.close()


    def retranslateUi(self, cash_input):
        _translate = QtCore.QCoreApplication.translate
        cash_input.setWindowTitle(_translate("cash_input", "Cash Input"))
        self.cash_label.setText(_translate("cash_input", "Cash Amount :"))
        self.input_cash_amount.setPlaceholderText(_translate("cash_input", "0"))


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    cash_input = QtWidgets.QDialog()
    ui = Ui_cash_input()
    ui.setupUi(cash_input)
    cash_input.show()
    sys.exit(app.exec_())
