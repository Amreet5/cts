

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from error import Ui_error
import sys
#imports directory of the file
scriptDir = os.path.dirname(os.path.realpath(__file__))


class Ui_quantity(object):
    qty = 1

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def getqty(self):
        return self.qty

    #for opening error dialog box
    def error(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error()
        self.ui.seterrormessage("Invalid Quantity!!!")
        self.ui.setupUi(self.window)
        self.window.exec_()

    def verify(self, quantity):
        valid = True
        try:
            a = int(self.input_quantity.text())
        except:
            valid = False
        if valid and a > 0:
            quantity.close()
            self.qty = int(self.input_quantity.text())
        else:
            self.error()
            self.input_quantity.setFocus()

    def setupUi(self, quantity):
        quantity.setObjectName("quantity")
        quantity.resize(189, 97)
        quantity.setMinimumSize(QtCore.QSize(189, 97))
        quantity.setMaximumSize(QtCore.QSize(189, 97))
        icon = QtGui.QIcon()
        image_path = self.resource_path("quantity.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        quantity.setWindowIcon(icon)

        self.ok = QtWidgets.QDialogButtonBox(quantity)
        self.ok.setGeometry(QtCore.QRect(0, 60, 171, 32))
        self.ok.setOrientation(QtCore.Qt.Horizontal)
        self.ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok.setObjectName("ok")
        self.ok.accepted.connect(lambda: self.verify(quantity))

        self.quantity_label = QtWidgets.QLabel(quantity)
        self.quantity_label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)

        self.quantity_label.setFont(font)
        self.quantity_label.setObjectName("quantity_label")

        self.input_quantity = QtWidgets.QLineEdit(quantity)
        self.input_quantity.setGeometry(QtCore.QRect(90, 20, 51, 20))
        self.input_quantity.setMinimumSize(QtCore.QSize(0, 0))
        self.input_quantity.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_quantity.setMaxLength(3)
        self.input_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.input_quantity.setObjectName("input_quantity")
        self.input_quantity.setFocus()

        self.retranslateUi(quantity)
        #self.ok.accepted.connect(quantity.accept)
        self.ok.rejected.connect(quantity.reject)
        QtCore.QMetaObject.connectSlotsByName(quantity)

    def retranslateUi(self, quantity):
        _translate = QtCore.QCoreApplication.translate
        quantity.setWindowTitle(_translate("quantity", "Quantity"))
        self.quantity_label.setText(_translate("quantity", "Quantity :"))
        self.input_quantity.setPlaceholderText(_translate("quantity", "0"))


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    quantity = QtWidgets.QDialog()
    ui = Ui_quantity()
    ui.setupUi(quantity)
    quantity.show()
    sys.exit(app.exec_())
