# search dialog form

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from error import Ui_error
import sys
from receipts import Ui_reciept_display

class Ui_search_dialog(object):

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    transaction_id = "-1"  #stores the transaction_id
    string_date1 = "-1"       #stores the Date number one
    string_date2 = "-1"       #stores Date number two
    store_value = 1  #stores the value of which store is checked
    transaction_display = ""
    result_by_date = ""
    search_for_date = False


    def display_reciept_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_reciept_display()
        self.ui.setupUi(self.window)
        if (self.search_for_date == False):
            self.ui.Displays_reciept.setText(str(self.transaction_display))
            self.window.exec_()
        else:
            self.ui.Displays_reciept.setText(str(self.result_by_date))
            self.window.exec_()



    #returns date number one
    def getdate1(self):
        return self.string_date1


    #returns date number two
    def getdate2(self):
        return self.string_date2


    # for opening error dialog box
    def error(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error()
        self.ui.seterrormessage("Invalid ID Length!!!")
        self.ui.setupUi(self.window)
        self.window.exec_()


    #setting up main dialog window
    def setupUi(self, search_dialog):


        #main frame for the search dialog
        search_dialog.setObjectName("search_dialog")
        search_dialog.resize(422, 242)
        icon = QtGui.QIcon()
        image_path = self.resource_path("search.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        search_dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(search_dialog)
        self.gridLayout.setObjectName("gridLayout")


        # ok button
        self.Ok = QtWidgets.QDialogButtonBox(search_dialog)
        self.Ok.setOrientation(QtCore.Qt.Horizontal)
        self.Ok.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.Ok.setObjectName("Ok")
        self.gridLayout.addWidget(self.Ok, 2, 0, 1, 3)

        self.blank_frame = QtWidgets.QFrame(search_dialog)
        self.blank_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blank_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blank_frame.setObjectName("blank_frame")
        self.gridLayout.addWidget(self.blank_frame, 1, 2, 1, 1)


        self.radio_frame = QtWidgets.QFrame(search_dialog)
        self.radio_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.radio_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.radio_frame.setObjectName("radio_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.radio_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        # radio button for transaction id
        self.radio_transaction_id = QtWidgets.QRadioButton(self.radio_frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radio_transaction_id.setFont(font)
        self.radio_transaction_id.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radio_transaction_id.setChecked(True)
        self.radio_transaction_id.setObjectName("transaction_id")
        self.verticalLayout_3.addWidget(self.radio_transaction_id)

        # capturing event for transaction id button
        self.radio_transaction_id.toggled.connect(lambda: self.tbuttonClicked(self.radio_transaction_id))


        # radio button for date
        self.radio_date = QtWidgets.QRadioButton(self.radio_frame)
        self.radio_date.setFont(font)
        self.radio_date.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radio_date.setObjectName("radio_date")
        self.verticalLayout_3.addWidget(self.radio_date)
        self.gridLayout.addWidget(self.radio_frame, 0, 0, 1, 1)


        # capturing event for date button
        self.radio_date.toggled.connect(lambda: self.dbuttonClicked(self.radio_date))


        self.get_reciepts_frame = QtWidgets.QFrame(search_dialog)
        self.get_reciepts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.get_reciepts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.get_reciepts_frame.setObjectName("get_reciepts_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.get_reciepts_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # label for "get reciepts"
        self.getreceipts = QtWidgets.QLabel(self.get_reciepts_frame)
        self.getreceipts.setFont(font)
        self.getreceipts.setObjectName("getreceipts")
        self.verticalLayout_2.addWidget(self.getreceipts)



        # label for "from"
        self.label_from = QtWidgets.QLabel(self.get_reciepts_frame)
        self.label_from.setFont(font)
        self.label_from.setObjectName("label_from")
        self.verticalLayout_2.addWidget(self.label_from)
        self.gridLayout.addWidget(self.get_reciepts_frame, 1, 0, 1, 1)



        self.check_box_frame = QtWidgets.QFrame(search_dialog)
        self.check_box_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.check_box_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.check_box_frame.setObjectName("check_box_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.check_box_frame)
        self.verticalLayout.setObjectName("verticalLayout")



        # check button for store 1
        self.store1 = QtWidgets.QCheckBox(self.check_box_frame)
        self.store1.setChecked(True)
        self.store1.setObjectName("store1")
        self.verticalLayout.addWidget(self.store1)

        # check button for store 2
        self.store2 = QtWidgets.QCheckBox(self.check_box_frame)
        self.store2.setObjectName("store2")
        self.verticalLayout.addWidget(self.store2)


        # check button for store 3
        self.store3 = QtWidgets.QCheckBox(self.check_box_frame)
        self.store3.setObjectName("store3")
        self.verticalLayout.addWidget(self.store3)

        self.gridLayout.addWidget(self.check_box_frame, 1, 1, 1, 1)





        #another frame
        self.input_and_date_frame = QtWidgets.QFrame(search_dialog)
        self.input_and_date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_and_date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_and_date_frame.setObjectName("input_and_date_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.input_and_date_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        self.input_frame = QtWidgets.QFrame(self.input_and_date_frame)
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.input_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # input box for transaction ID
        self.input_transaction_id = QtWidgets.QLineEdit(self.input_frame)
        self.input_transaction_id.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.input_transaction_id.setClearButtonEnabled(True)
        self.input_transaction_id.setMaxLength(10)
        self.input_transaction_id.setObjectName("input_transaction_id")
        self.horizontalLayout.addWidget(self.input_transaction_id)
        self.verticalLayout_4.addWidget(self.input_frame)

        self.date_frame = QtWidgets.QFrame(self.input_and_date_frame)
        self.date_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_frame.setObjectName("date_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.date_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")


        # date 1 input button
        self.dateEdit1 = QtWidgets.QDateEdit(self.date_frame)
        self.dateEdit1.setEnabled(False)
        self.dateEdit1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit1.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 11), QtCore.QTime(0, 0, 0)))
        self.dateEdit1.setMinimumDate(QtCore.QDate(2019, 11, 11))
        self.dateEdit1.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit1.setCalendarPopup(True)
        self.dateEdit1.setObjectName("dateEdit1")
        self.horizontalLayout_2.addWidget(self.dateEdit1)


        # label for "to"
        self.to = QtWidgets.QLabel(self.date_frame)
        self.to.setFont(font)
        self.to.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.to.setObjectName("to")
        self.horizontalLayout_2.addWidget(self.to)



        # another date input button
        self.dateEdit2 = QtWidgets.QDateEdit(self.date_frame)
        self.dateEdit2.setEnabled(False)
        self.dateEdit2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit2.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 11, 11), QtCore.QTime(0, 0, 0)))
        self.dateEdit2.setMinimumDate(QtCore.QDate(2019, 11, 11))
        self.dateEdit2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit2.setCalendarPopup(True)
        self.dateEdit2.setDate(QtCore.QDate(2019, 11, 11))
        self.dateEdit2.setObjectName("dateEdit_2")
        self.horizontalLayout_2.addWidget(self.dateEdit2)

        self.verticalLayout_4.addWidget(self.date_frame)
        self.gridLayout.addWidget(self.input_and_date_frame, 0, 1, 1, 2)





        #all the check box option for store number call the store_value
        self.store1.toggled.connect(self.store_value)
        self.store2.toggled.connect(self.store_value)
        self.store3.toggled.connect(self.store_value)




        # calling retranslateUi function
        self.retranslateUi(search_dialog)


        #on pressing ok button calls search_dialog function
        self.Ok.accepted.connect(lambda: self.selected(search_dialog))

        #on pressing cancel button cancels the dialgo
        self.Ok.rejected.connect(search_dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(search_dialog)



    #checks which stores are checked and assigns unique number to the store_value variable
    def store_value(self):
        if self.store2.isChecked():
            self.store_value = 2
        elif self.store3.isChecked():
            self.store_value = 3
        elif self.store1.isChecked() and self.store2.isChecked():
            self.store_value = 4
        elif self.store1.isChecked() and self.store3.isChecked():
            self.store_value = 5
        elif self.store2.isChecked() and self.store3.isChecked():
            self.store_value = 6
        elif self.store1.isChecked() and self.store2.isChecked() and self.store3.isChecked():
            self.store_value = 7
        else:
            self.store_value = 1

    def search_by_date(self, x, y):
        import sqlite3
        connection = sqlite3.connect("CTS.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * from CTS where Date BETWEEN ? AND ?', (x, y))
        result = cursor.fetchall()
        return result



    #enables input button either for transaction id or for date
    #depending upon which button is pressed
    def selected(self, search_dialog):
        if (self.radio_transaction_id.isChecked()):
            self.id_verify(search_dialog)

        if (self.radio_date.isChecked()):
            self.search_for_date = True
            self.string_date1 = (self.dateEdit1.text())
            self.string_date2 = (self.dateEdit2.text())

            self.result_by_date = self.search_by_date(self.string_date1, self.string_date2)
            #display get reciepts window
            self.display_reciept_window()


    def search_by_transaction(self, transaction):
        import sqlite3
        connection = sqlite3.connect("CTS.db")
        cursor = connection.cursor()
        cursor.execute("SELECT Transaction_ID from CTS where Transaction_ID = ?", (transaction,))
        result = cursor.fetchall()
        string = ""
        for i in result:
            string = "Transaction ID: " + i[0]
        cursor.execute("select Store_ID from CTS where Transaction_id = ?", (transaction,))
        result = cursor.fetchall()
        for i in result:
            string = "Store Id: " + str(i[0]) + "\n" + string + "\n"
        cursor.execute("select Date from CTS where Transaction_id = ?", (transaction,))
        result = cursor.fetchall()
        for i in result:
            string = "Date: " + str(i[0]) + "\n" + string + "\n"
        cursor.execute("select Transaction_details from CTS where transaction_id = ?", (transaction,))
        result = cursor.fetchall()
        for i in result:
            details = str(i[0]).split(";")
            for j in details:
                string = string + "\n" + j
        return string



    #the id_verify method checks whether the user enters valid transaction ID
    def id_verify(self, search_dialog):
        valid = True
        try:
            a = int(self.input_transaction_id.text())
            b = str(self.input_transaction_id.text())
        except:
            valid = False

        if (valid and a > 0 and len(b) == 10):
            self.transaction_id = str(self.input_transaction_id.text())
            self.transaction_display = self.search_by_transaction(self.transaction_id)
            self.display_reciept_window()
        else:
            self.error()



    # disables date input button when user clicks transaction id radio button
    def tbuttonClicked(self, button):
        self.input_transaction_id.setEnabled(True)
        self.dateEdit1.setEnabled(False)
        self.dateEdit2.setEnabled(False)



    # disables input box for transaction id when user clicks date radio button
    def dbuttonClicked(self, button):
        self.input_transaction_id.setEnabled(False)
        self.dateEdit1.setEnabled(True)
        self.dateEdit2.setEnabled(True)



    #the method retranslate the main window
    def retranslateUi(self, search_dialog):
        _translate = QtCore.QCoreApplication.translate
        search_dialog.setWindowTitle(_translate("search_dialog", "Search"))
        self.input_transaction_id.setPlaceholderText(_translate("search_dialog", "Enter transaction ID number here..."))
        self.to.setText(_translate("search_dialog", "to"))
        self.store1.setText(_translate("search_dialog", "Store 1"))
        self.store2.setText(_translate("search_dialog", "Store 2"))
        self.store3.setText(_translate("search_dialog", "Store 3"))
        self.radio_transaction_id.setText(_translate("search_dialog", "Transaction ID :"))
        self.radio_date.setText(_translate("search_dialog", "     Date From :"))
        self.getreceipts.setText(_translate("search_dialog", "Get Receipts"))
        self.label_from.setText(_translate("search_dialog", "From :"))



if __name__ == "__main__":
    #import sys

    app = QtWidgets.QApplication(sys.argv)
    search_dialog = QtWidgets.QDialog()
    ui = Ui_search_dialog()
    ui.setupUi(search_dialog)
    search_dialog.show()
    sys.exit(app.exec_())
