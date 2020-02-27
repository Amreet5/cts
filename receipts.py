# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reciepts.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reciept_display(object):
    def setupUi(self, reciept_display):
        reciept_display.setObjectName("reciept_display")
        reciept_display.resize(760, 437)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(reciept_display)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_display = QtWidgets.QFrame(reciept_display)
        self.frame_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_display.setObjectName("frame_display")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_display)
        self.verticalLayout.setObjectName("verticalLayout")


        self.Displays_reciept = QtWidgets.QTextBrowser(self.frame_display)
        self.Displays_reciept.setObjectName("Displays_reciept")
        self.verticalLayout.addWidget(self.Displays_reciept)
        self.verticalLayout_2.addWidget(self.frame_display)


        self.Okbutton = QtWidgets.QDialogButtonBox(reciept_display)
        self.Okbutton.setOrientation(QtCore.Qt.Horizontal)
        self.Okbutton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Okbutton.setObjectName("Okbutton")
        self.verticalLayout_2.addWidget(self.Okbutton)

        self.retranslateUi(reciept_display)
        self.Okbutton.accepted.connect(reciept_display.accept)
        self.Okbutton.rejected.connect(reciept_display.reject)
        QtCore.QMetaObject.connectSlotsByName(reciept_display)

    def retranslateUi(self, reciept_display):
        _translate = QtCore.QCoreApplication.translate
        reciept_display.setWindowTitle(_translate("reciept_display", "Receipts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reciept_display = QtWidgets.QDialog()
    ui = Ui_reciept_display()
    ui.setupUi(reciept_display)
    reciept_display.show()
    sys.exit(app.exec_())
