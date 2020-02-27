#CTS application

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from search import Ui_search_dialog
from quantity import Ui_quantity
from cash import Ui_cash_input
from error import Ui_error
import datetime
from Login import Ui_Login
import sqlite3
import hashlib

#imports directory of the file
#scriptDir = os.path.dirname(os.path.realpath(__file__))


class Ui_main_window(object):


    amount = -1.00 #stores the cash amount of the data from user input
    qty = -1 #stores the quantity of the item
    total = 0.0 #stores the total price of the items
    total_tax = 0.0 #stores total tax
    price_of_item = -1 #stores price of the item when user enters the price
    string_store_information = "" #for displaying the store information
    row_of_tree_view = 0  # for the Qtree widget's row access
    item_type_for_tree_view = "" #type of item whether tax or non tax that is used in Qtree widget
    change_for_the_transaction = 0.0 #calculated change
    error_message_from_main = ""  #to store error messages
    cash_py_cancel_button_is_clicked = False #if cancel is clicked in the cash
    login_cancel_button_pressed = False #if login cancel is clicked
    store_value = 1 #store the store number
    payment_type = "" #payment type

    def create_database(self):
        file = open("database_counter.txt", "r")
        database_counter = int(file.read(1))
        if database_counter == 0:
            connection = sqlite3.connect("CTS.db")
            cursor = connection.cursor()

            sql_command = """
            CREATE TABLE CTS( Store_ID INT(1), Transaction_ID TEXT
            PRIMARY KEY, Date TEXT, Transaction_details TEXT);"""
            cursor.execute(sql_command)
            file.close()
            database_counter = 1
            file = open("database_counter.txt", "w")
            file.write(str(database_counter))
            file.close()
        file.close()


    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    # for opening error dialog box
    def error(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_error()
        self.ui.seterrormessage(self.error_message_from_main)
        self.ui.setupUi(self.window)
        self.window.exec_()

    #for opening cash input dialog box
    def validate_cash_input(self):

        #showing cash window
        self.window = QtWidgets.QDialog()
        self.ui = Ui_cash_input()
        self.ui.setupUi(self.window)
        # setting focus in the input box back again
        self.item_input.setFocus()

        #passing total of the items to the 'cash.py' class
        self.ui.settotal(self.total)

        self.window.exec_()
        # setting focus in the input box back again
        self.item_input.setFocus()

        #when cancel is clicked no changes to the data or user interface
        self.cash_py_cancel_button_is_clicked = self.ui.get_info_about_cancel_button()
        if self.cash_py_cancel_button_is_clicked == False:

            #setting amount entered to current amount
            self.amount = self.ui.getamount()

            self.change_for_the_transaction = self.amount - self.total #calculating change
            self.change_for_the_transaction = round(self.change_for_the_transaction, 2) #rounding the change

            self.displays_change.setText("$ " +str(self.change_for_the_transaction)) #displaying the change


            self.item_input.setText("") #clearing any data in the input box

            #disabling quantity, cash and card payments button
            self.quantity_button.setEnabled(False)
            self.cash_button.setEnabled(False)
            self.card_payments_button.setEnabled(False)
            self.void_transaction_button.setEnabled(False)

            self.payment_type = "Cash"
            self.store_transaction()
            self.item_display.clear()  # clearing the Qtreewidget items
            self.row_of_tree_view = 0



    #when the users clicks card payment option
    def card_payment_handler(self):
        self.calculate_Tax_and_Total()
        #setting the change equal to total on clicking card payment
        self.change_for_the_transaction = 0.0

        self.displays_change.setText("$ 0.0")#clearing display

        self.item_input.setText("") #clearing any data in the input box

        #disabling the quantity, card and cash button
        self.quantity_button.setEnabled(False)
        self.cash_button.setEnabled(False)
        self.card_payments_button.setEnabled(False)
        self.void_transaction_button.setEnabled(False)
        #setting row value of the tree back to zero

        #setting focus in the input box back again
        self.item_input.setFocus()
        self.payment_type = "Card Transaction"
        self.store_transaction()

        self.item_display.clear()  # clearing item in the tree
        self.row_of_tree_view = 0





    #for opening quantity dialog box
    def quantity(self, main_window):

        _translate = QtCore.QCoreApplication.translate #adding translate button to translate the QTree Widge
        item = self.item_display.currentItem() #item which is currently selected
        index = self.item_display.indexOfTopLevelItem(item) #index of the selected item
        #checking whether item is selected or not
        if index >= 0:

            #executing quantity window
            self.window = QtWidgets.QDialog()
            self.ui = Ui_quantity()
            self.ui.setupUi(self.window)
            self.window.exec_()

            #setting quantity to the user entered quantity
            self.qty = self.ui.getqty()

            #changing the quantity
            self.item_display.topLevelItem(index).setText(1, _translate("main_window", str(self.qty)))
            self.calculate_Tax_and_Total()
            # setting focus in the input box back again
            self.item_input.setFocus()

        else:

            #showing error if the item is not selected
            self.error_message_from_main = "No Item Selected!" #passing message to show
            self.error()
            # setting focus in the input box back again
            self.item_input.setFocus()

    #calculates Tax and Total price of the items
    def calculate_Tax_and_Total(self):
        tax_rate = 0.07
        iterator = 0
        self.total_tax = 0
        self.total = 0
        while (self.item_display.topLevelItem(iterator) != None):

            local_item_type = str(self.item_display.topLevelItem(iterator).text(0))
            local_quantity = float(self.item_display.topLevelItem(iterator).text(1))
            local_price = float(self.item_display.topLevelItem(iterator).text(2))
            if (local_item_type.startswith("T")):
                local_tax = tax_rate * local_quantity * local_price
                self.total_tax = tax_rate * local_quantity * local_price + self.total_tax
                self.total = local_price * local_quantity + local_tax + self.total
                self.total_tax = round(self.total_tax, 2)
                self.total = round(self.total, 2)
            else:
                self.total = local_price * local_quantity + self.total
                self.total = round(self.total, 2)
            iterator = iterator + 1

            # displaying the total tax charged
            self.displays_total_tax.setText("$ " + str(self.total_tax))

            # displaying the total amount of the items
            self.displays_total.setText("$ " +str(self.total))

    def store_transaction(self):
        iterator = 0
        self.calculate_Tax_and_Total()
        file = open("counter.txt", "r")
        count = int(file.read(10))
        file.close()

        generated_transaction_id = str(count).zfill(10)
        #generated_transaction_id = int(generated_transaction_id_initial)
        local_item_type = []
        local_quantity = []
        local_price = []

        connection = sqlite3.connect("CTS.db")
        cursor = connection.cursor()
        string = ""
        while (self.item_display.topLevelItem(iterator) != None):

            local_item_type.append(str(self.item_display.topLevelItem(iterator).text(0)))
            local_quantity.append(str(self.item_display.topLevelItem(iterator).text(1)))
            local_price.append(self.item_display.topLevelItem(iterator).text(2))            
            string = "Item : " + local_item_type[iterator] + ", Quantity : " + local_quantity[iterator] + ", Price : $ " + local_price[iterator] + "\n" + string

            iterator = iterator + 1
        file = open("previous_transaction.txt", "r")
        previous_transaction = file.read(10)
        file.close()
        hash_value = hashlib.sha3_256(previous_transaction.encode() + generated_transaction_id.encode())
        hash_value = hash_value.hexdigest()
        file = open("previous_transaction.txt", "w")
        file.write(str(hash_value))
        file.close()
        string = string + "\n" + "Hash Value: " + str(hash_value) + "\n"
        date = datetime.datetime.now().strftime("%m") + "/" + datetime.datetime.now().strftime("%d")+"/"+datetime.datetime.now().strftime("%Y")
        cursor.execute("INSERT INTO CTS(Store_ID, Transaction_ID, Date, Transaction_details) values (?,?,?,?)",
                       (self.store_value, generated_transaction_id, date, string))
        connection.commit()
        connection.close()
        file = open("counter.txt", "w")
        count = count + 1
        file.write(str(count))
        file.close()


    #for opening search dialog box
    def open_search(self):

        #setting up the window of the 'search.py' class

        self.window = QtWidgets.QDialog()
        self.ui = Ui_search_dialog()
        self.ui.setupUi(self.window)
        self.window.exec_()


        # setting focus in the input box back again
        self.item_input.setFocus()


    # the validate_input_price method checks whether the user enters valid input price when tax button is pressed
    def validate_input_price_for_tax(self, main_window):
            valid = True
            try:
                a = float(self.item_input.text())
            except:
                valid = False

            if (valid and a > 0.0):
                self.price_of_item = float(self.item_input.text()) #setting price of the item
                self.item_type_for_tree_view = "Taxable Item" #giving message that it is taxable item
                self.adding_item(main_window) #adding the item in the main window
                self.item_input.setText("")   #clearing the entryfield

                self.calculate_Tax_and_Total()
                self.quantity_button.setEnabled(True)
                self.cash_button.setEnabled(True)
                self.card_payments_button.setEnabled(True)
                self.void_transaction_button.setEnabled(True)
                # setting focus in the input box back again
                self.item_input.setFocus()
                self.displays_change.setText("----")

            else:
                self.error_message_from_main ="Invalid Amount!!!"
                self.item_input.setText("") #clearing the entry field
                self.error()
                # setting focus in the input box back again
                self.item_input.setFocus()


    #the function checks if the input price is valid when non-tax button is pressed
    def validate_input_price_for_nontax(self, main_window):
            valid = True
            try:
                a = float(self.item_input.text())
            except:
                valid = False

            if (valid and a > 0.0):
                self.price_of_item = float(self.item_input.text()) #setting the price of the item to the variable
                self.item_type_for_tree_view = "Non-Taxable Item" #passing message that it is a non taxable item
                self.adding_item(main_window)  # adding this item in the tree view widget
                self.item_input.setText("") #clearing the input box

                self.calculate_Tax_and_Total()
                self.quantity_button.setEnabled(True)
                self.cash_button.setEnabled(True)
                self.card_payments_button.setEnabled(True)
                self.void_transaction_button.setEnabled(True)
                # setting focus in the input box back again
                self.item_input.setFocus()
                self.displays_change.setText("----")
            else:
                self.error_message_from_main = "Invalid Amount!!!"
                self.item_input.setText("")
                self.error()
                # setting focus in the input box back again
                self.item_input.setFocus()


    #adds item in the tree view Qwidget of the user interface
    def adding_item(self, main_window):

        #for translating the items in the QtreeWidget
        _translate = QtCore.QCoreApplication.translate
        QtWidgets.QTreeWidgetItem(self.item_display)


        #these functions displays the item
        self.item_display.topLevelItem(self.row_of_tree_view).setText(0, _translate("main_window", self.item_type_for_tree_view))
        self.item_display.topLevelItem(self.row_of_tree_view).setText(1, _translate("main_window", "1"))
        self.item_display.topLevelItem(self.row_of_tree_view).setText(2, _translate("main_window", str(self.price_of_item)))

        #increasing row every time the items gets added
        self.row_of_tree_view = self.row_of_tree_view + 1


    #when digit buttons are clicked
    def clickedbutton0(self):
        self.item_input.setText(self.item_input.text()+"0")
        self.item_input.setFocus()
    def clickedbutton1(self):
        self.item_input.setText(self.item_input.text()+"1")
        self.item_input.setFocus()
    def clickedbutton2(self):
        self.item_input.setText(self.item_input.text()+"2")
        self.item_input.setFocus()
    def clickedbutton3(self):
        self.item_input.setText(self.item_input.text()+"3")
        self.item_input.setFocus()
    def clickedbutton4(self):
        self.item_input.setText(self.item_input.text()+"4")
        self.item_input.setFocus()
    def clickedbutton5(self):
        self.item_input.setText(self.item_input.text()+"5")
        self.item_input.setFocus()
    def clickedbutton6(self):
        self.item_input.setText(self.item_input.text()+"6")
        self.item_input.setFocus()
    def clickedbutton7(self):
        self.item_input.setText(self.item_input.text()+"7")
        self.item_input.setFocus()
    def clickedbutton8(self):
        self.item_input.setText(self.item_input.text()+"8")
        self.item_input.setFocus()
    def clickedbutton9(self):
        self.item_input.setText(self.item_input.text()+"9")
        self.item_input.setFocus()
    def clickedbuttondot(self):
        self.item_input.setText(self.item_input.text()+".")
        self.item_input.setFocus()



    #setting up main window
    def setupUi(self, main_window):


        #the main window of the program
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        main_window.setEnabled(True)
        main_window.resize(813, 600)
        main_window.setMinimumSize(QtCore.QSize(813, 600))
        main_window.setMaximumSize(QtCore.QSize(10000, 16777215))
        main_window.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        main_window.setAcceptDrops(False)
        icon = QtGui.QIcon()
        image_path = self.resource_path("cash-register.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setAutoFillBackground(False)

        #some frame
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")

        #another frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 795, 561))
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(-2)
        self.frame.setObjectName("frame")

        
        #input price button
        self.item_input = QtWidgets.QLineEdit(self.frame)
        self.item_input.setGeometry(QtCore.QRect(410, 150, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_input.setFont(font)
        self.item_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.item_input.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_input.setAutoFillBackground(False)
        self.item_input.setText("")
        self.item_input.setMaxLength(8)
        self.item_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.item_input.setCursorPosition(0)
        self.item_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.item_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.item_input.setFocus()
        self.item_input.setClearButtonEnabled(True)
        self.item_input.setObjectName("item_input")



        #tax button
        self.tax_button = QtWidgets.QPushButton(self.frame)
        self.tax_button.setEnabled(True)
        self.tax_button.setGeometry(QtCore.QRect(410, 250, 81, 71))
        self.tax_button.setFont(font)
        self.tax_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tax_button.setObjectName("tax")
        self.tax_button.setStyleSheet("background-color:#d6d6c2;")
        self.tax_button.clicked.connect(lambda: self.validate_input_price_for_tax(main_window))



        #non tax button
        self.non_tax_button = QtWidgets.QPushButton(self.frame)
        self.non_tax_button.setGeometry(QtCore.QRect(500, 250, 81, 71))
        self.non_tax_button.setFont(font)
        self.non_tax_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.non_tax_button.setObjectName("non_tax")
        self.non_tax_button.setStyleSheet("background-color:#d6d6c2;")
        self.non_tax_button.clicked.connect(lambda: self.validate_input_price_for_nontax(main_window))


        #quantity button
        self.quantity_button = QtWidgets.QPushButton(self.frame)
        self.quantity_button.setGeometry(QtCore.QRect(410, 330, 81, 71))
        self.quantity_button.setFont(font)
        self.quantity_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quantity_button.setObjectName("quantity_button")
        self.quantity_button.setStyleSheet("background-color:#d6d6c2;")
        self.quantity_button.setEnabled(False)
        # event for quantity function
        self.quantity_button.clicked.connect(lambda: self.quantity(main_window))


        #search button
        self.search = QtWidgets.QPushButton(self.frame)
        self.search.setGeometry(QtCore.QRect(500, 330, 81, 71))
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setObjectName("search")
        self.search.setStyleSheet("background-color:#d6d6c2;")
        #event for search function
        self.search.clicked.connect(self.open_search)


        #cash button
        self.cash_button = QtWidgets.QPushButton(self.frame)
        self.cash_button.setGeometry(QtCore.QRect(410, 410, 81, 71))
        self.cash_button.setFont(font)
        self.cash_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cash_button.setObjectName("cash_button")
        self.cash_button.setStyleSheet("background-color:#d6d6c2;")
        self.cash_button.setEnabled(False)
        #event for cash button
        self.cash_button.clicked.connect(self.validate_cash_input)
        

        #card button
        self.card_payments_button = QtWidgets.QPushButton(self.frame)
        self.card_payments_button.setGeometry(QtCore.QRect(500, 410, 81, 71))
        self.card_payments_button.setFont(font)
        self.card_payments_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_payments_button.setEnabled(False)
        self.card_payments_button.setObjectName("card_payments")
        self.card_payments_button.setStyleSheet("background-color:#d6d6c2;")
        self.card_payments_button.clicked.connect(self.card_payment_handler)

        #void Transaction button
        self.void_transaction_button = QtWidgets.QPushButton(self.frame)
        self.void_transaction_button.setEnabled(True)
        self.void_transaction_button.setGeometry(QtCore.QRect(410, 490, 171, 51))
        self.void_transaction_button.setFont(font)
        self.void_transaction_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.void_transaction_button.setObjectName("void_transaction_button")
        self.void_transaction_button.setStyleSheet("background-color:#d6d6c2;")
        self.void_transaction_button.clicked.connect(self.void_all_transaction)
        self.void_transaction_button.setEnabled(False)

        #digits from 0 to 9 in an ascending order
        self.digitbutton0 = QtWidgets.QPushButton(self.frame)
        self.digitbutton0.setGeometry(QtCore.QRect(630, 430, 51, 51))
        self.digitbutton0.setFont(font)
        self.digitbutton0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton0.setObjectName("digitbutton0")
        self.digitbutton0.setStyleSheet("background-color:#ffffff;")

        self.digitbutton1 = QtWidgets.QPushButton(self.frame)
        self.digitbutton1.setGeometry(QtCore.QRect(600, 370, 51, 51))
        self.digitbutton1.setFont(font)
        self.digitbutton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton1.setObjectName("digitbutton1")
        self.digitbutton1.setStyleSheet("background-color:#ffffff;")


        self.digitbutton2 = QtWidgets.QPushButton(self.frame)
        self.digitbutton2.setGeometry(QtCore.QRect(660, 370, 51, 51))
        self.digitbutton2.setFont(font)
        self.digitbutton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton2.setObjectName("digitbutton2")
        self.digitbutton2.setStyleSheet("background-color:#ffffff;")
        
        self.digitbutton3 = QtWidgets.QPushButton(self.frame)
        self.digitbutton3.setGeometry(QtCore.QRect(720, 370, 51, 51))
        self.digitbutton3.setFont(font)
        self.digitbutton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton3.setObjectName("digtibutton3")
        self.digitbutton3.setStyleSheet("background-color:#ffffff;")

        self.digitbutton4 = QtWidgets.QPushButton(self.frame)
        self.digitbutton4.setGeometry(QtCore.QRect(600, 310, 51, 51))
        self.digitbutton4.setFont(font)
        self.digitbutton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton4.setObjectName("digitbutton4")
        self.digitbutton4.setStyleSheet("background-color:#ffffff;")

        self.digitbutton5 = QtWidgets.QPushButton(self.frame)
        self.digitbutton5.setGeometry(QtCore.QRect(660, 310, 51, 51))
        self.digitbutton5.setFont(font)
        self.digitbutton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton5.setObjectName("digitbutton5")
        self.digitbutton5.setStyleSheet("background-color:#ffffff;")

        self.digitbutton6 = QtWidgets.QPushButton(self.frame)
        self.digitbutton6.setGeometry(QtCore.QRect(720, 310, 51, 51))
        self.digitbutton6.setFont(font)
        self.digitbutton6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton6.setObjectName("digitbutton6")
        self.digitbutton6.setStyleSheet("background-color:#ffffff;")

        self.digitbutton7 = QtWidgets.QPushButton(self.frame)
        self.digitbutton7.setGeometry(QtCore.QRect(600, 250, 51, 51))
        self.digitbutton7.setFont(font)
        self.digitbutton7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton7.setObjectName("digitbutton7")
        self.digitbutton7.setStyleSheet("background-color:#ffffff;")

        self.digitbutton8 = QtWidgets.QPushButton(self.frame)
        self.digitbutton8.setGeometry(QtCore.QRect(660, 250, 51, 51))
        self.digitbutton8.setFont(font)
        self.digitbutton8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton8.setObjectName("digitbutton8")
        self.digitbutton8.setStyleSheet("background-color:#ffffff;")

        self.digitbutton9 = QtWidgets.QPushButton(self.frame)
        self.digitbutton9.setGeometry(QtCore.QRect(720, 250, 51, 51))
        self.digitbutton9.setFont(font)
        self.digitbutton9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbutton9.setObjectName("digitbutton9")
        self.digitbutton9.setStyleSheet("background-color:#ffffff;")

        self.digitbuttondot = QtWidgets.QPushButton(self.frame)
        self.digitbuttondot.setGeometry(QtCore.QRect(700, 430, 51, 51))
        self.digitbuttondot.setFont(font)
        self.digitbuttondot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.digitbuttondot.setObjectName("digitbuttondot")
        self.digitbuttondot.setStyleSheet("background-color:#ffffff;")

        self.digitbutton0.clicked.connect(self.clickedbutton0)
        self.digitbutton1.clicked.connect(self.clickedbutton1)
        self.digitbutton2.clicked.connect(self.clickedbutton2)
        self.digitbutton3.clicked.connect(self.clickedbutton3)
        self.digitbutton4.clicked.connect(self.clickedbutton4)
        self.digitbutton5.clicked.connect(self.clickedbutton5)
        self.digitbutton6.clicked.connect(self.clickedbutton6)
        self.digitbutton7.clicked.connect(self.clickedbutton7)
        self.digitbutton8.clicked.connect(self.clickedbutton8)
        self.digitbutton9.clicked.connect(self.clickedbutton9)
        self.digitbuttondot.clicked.connect(self.clickedbuttondot)


        #will show about store information
        self.label_store_information = QtWidgets.QTextBrowser(self.frame)
        self.label_store_information.setEnabled(True)
        self.label_store_information.setGeometry(QtCore.QRect(330, 20, 210, 91))
        self.label_store_information.setObjectName("label_store_information")
        self.label_store_information.setAlignment(QtCore.Qt.AlignCenter)
        self.label_store_information.setFont(font)



        #graphics will show the user every information of the items
        self.item_display = QtWidgets.QTreeWidget(self.frame)
        self.item_display.setGeometry(QtCore.QRect(20, 150, 361, 311))
        self.item_display.setFont(font)
        self.item_display.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_display.setFrameShape(QtWidgets.QFrame.Box)
        self.item_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.item_display.setObjectName("item_display")


        #displays word'tax' in the user interface
        self.label_tax = QtWidgets.QLabel(self.frame)
        self.label_tax.setGeometry(QtCore.QRect(20, 460, 41, 31))
        self.label_tax.setFont(font)
        self.label_tax.setObjectName("label_tax")
        self.label_tax.setText("Tax")

        #displays total tax in the item
        self.displays_total_tax = QtWidgets.QLabel(self.frame)
        self.displays_total_tax.setGeometry(QtCore.QRect(70, 460, 101, 31))
        self.displays_total_tax.setFont(font)
        self.displays_total_tax.setText("0.0")
        self.displays_total_tax.setObjectName("displays_total_tax")
        self.displays_total_tax.setAlignment(QtCore.Qt.AlignCenter)
        self.displays_total_tax.setFrameShape(QtWidgets.QFrame.Box)
        self.displays_total_tax.setFrameShadow(QtWidgets.QFrame.Sunken)

        #displays word 'total' in the user interface
        self.label_total = QtWidgets.QLabel(self.frame)
        self.label_total.setGeometry(QtCore.QRect(190, 460, 51, 31))
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.label_total.setText("Total :")

        #displays the total amount of the item
        self.displays_total = QtWidgets.QLabel(self.frame)
        self.displays_total.setGeometry(QtCore.QRect(260, 460, 121, 31))
        self.displays_total.setFont(font)
        self.displays_total.setText("0.0")
        self.displays_total.setObjectName("displays_total")
        self.displays_total.setAlignment(QtCore.Qt.AlignCenter)
        self.displays_total.setFrameShape(QtWidgets.QFrame.Box)
        self.displays_total.setFrameShadow(QtWidgets.QFrame.Sunken)

        # displays word 'change' in the user interface
        self.label_change = QtWidgets.QLabel(self.frame)
        self.label_change.setGeometry(QtCore.QRect(170, 500, 71, 31))
        self.label_change.setFont(font)
        self.label_change.setObjectName("label_change")
        self.label_change.setText("Change :")

        #displays the amount to change
        self.displays_change = QtWidgets.QLabel(self.frame)
        self.displays_change.setGeometry(QtCore.QRect(260, 500, 121, 31))
        self.displays_change.setFont(font)
        self.displays_change.setText("-----")
        self.displays_change.setObjectName("displays_change")
        self.displays_change.setAlignment(QtCore.Qt.AlignCenter)
        self.displays_change.setFrameShape(QtWidgets.QFrame.Box)
        self.displays_change.setFrameShadow(QtWidgets.QFrame.Sunken)

        #icon of the store
        self.store_label = QtWidgets.QLabel(self.frame)
        self.store_label.setGeometry(QtCore.QRect(60, 20, 101, 101))
        self.store_label.setText("")
        image_path = self.resource_path("buy.png")
        self.store_label.setPixmap(QtGui.QPixmap(image_path))
        self.store_label.setScaledContents(True)
        self.store_label.setObjectName("store_label")

        #some menu
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        #calling Login window
        self.Login_window()

        self.show_store_message()

        self.create_database()

    #other pretty function for retranslating main window and buttons
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Customer Transaction System"))


        self.item_input.setPlaceholderText(_translate("main_window", "Enter your price here..."))

        self.tax_button.setText(_translate("main_window", "Tax"))

        self.quantity_button.setText(_translate("main_window", "Quantity"))

        self.cash_button.setText(_translate("main_window", "Cash"))

        self.card_payments_button.setText(_translate("main_window", "Card \n"
"Payments"))

        self.void_transaction_button.setText(_translate("main_window", "Void Transaction"))

        self.digitbutton0.setText(_translate("main_window", "0"))
        self.digitbutton1.setText(_translate("main_window", "1"))
        self.digitbutton2.setText(_translate("main_window", "2"))
        self.digitbutton3.setText(_translate("main_window", "3"))
        self.digitbutton4.setText(_translate("main_window", "4"))
        self.digitbutton5.setText(_translate("main_window", "5"))
        self.digitbutton6.setText(_translate("main_window", "6"))
        self.digitbutton7.setText(_translate("main_window", "7"))
        self.digitbutton8.setText(_translate("main_window", "8"))
        self.digitbutton9.setText(_translate("main_window", "9"))
        self.digitbuttondot.setText(_translate("main_window", "."))


        self.item_display.headerItem().setText(0, _translate("main_window", "Items"))
        self.item_display.headerItem().setText(1, _translate("main_window", "Quantity"))
        self.item_display.headerItem().setText(2, _translate("main_window", "Unit Price"))

        self.non_tax_button.setText(_translate("main_window", "Non-Tax"))

        self.search.setText(_translate("main_window", "Search "))




    #function to show the message of the store
    def show_store_message(self):

        file = open("storeinformation.txt", "r")
        self.string_store_information = file.read()
        self.string_store_information = self.string_store_information + "\n" + str(datetime.datetime.now().strftime("%A,  %b-%d-%Y"))
        self.label_store_information.setText(self.string_store_information)

    #function to void all the transacton
    def void_all_transaction(self):
        self.item_display.clear()
        self.item_input.setText("")

        self.displays_total_tax.setText("")
        self.displays_total.setText("")
        self.cash_button.setEnabled(False)
        self.card_payments_button.setEnabled(False)
        self.void_transaction_button.setEnabled(False)
        # setting focus in the input box back again
        self.item_input.setFocus()
        self.row_of_tree_view = 0


    #function shows login window
    def Login_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.exec_()
        self.store_value = self.ui.get_store_value()
        self.login_cancel_button_pressed = self.ui.get_is_cancel_pressed()


if __name__ == "__main__":
    #import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    cancel_value = ui.login_cancel_button_pressed
    if cancel_value == True:
        main_window.show()
        sys.exit(app.exec_())
