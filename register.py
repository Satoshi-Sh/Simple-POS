from PyQt5 import QtCore, QtGui, QtWidgets
from note import Ui_NoteWindow
import re
from write_record import write_record 
import datetime
import sys

class Ui_MainWindow(object):
    # open the note window
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NoteWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(550, 30, 461, 581))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.output.setFont(font)
        self.output.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output.setObjectName("output")
        self.output.setStyleSheet("color: white; background-color: black;")
        self.button1 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button1.text()))
        self.button1.setGeometry(QtCore.QRect(50, 30, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button2.text()))
        self.button2.setGeometry(QtCore.QRect(220, 30, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it(self.button3.text()))
        self.button3.setGeometry(QtCore.QRect(390, 30, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button4.text()))
        self.button4.setGeometry(QtCore.QRect(50, 150, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button5.text()))
        self.button5.setGeometry(QtCore.QRect(220, 150, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button6.text()))
        self.button6.setGeometry(QtCore.QRect(390, 150, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button7.text()))
        self.button7.setGeometry(QtCore.QRect(50, 280, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button8.text()))
        self.button8.setGeometry(QtCore.QRect(220, 280, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.button9 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it(self.button9.text()))
        self.button9.setGeometry(QtCore.QRect(390, 280, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(70, 470, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.received = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.calc())
        self.received.setGeometry(QtCore.QRect(370, 460, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.received.setFont(font)
        self.received.setObjectName("received")
        self.delete = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.delete_on())
        self.delete.setGeometry(QtCore.QRect(40, 550, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete.setFont(font)
        self.delete.setObjectName("delete")
        self.complete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.completes())
        self.complete.setGeometry(QtCore.QRect(210, 550, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.complete.setFont(font)
        self.complete.setObjectName("complete")
        self.next = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.turn_page(True))
        self.next.setGeometry(QtCore.QRect(340, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.next.setFont(font)
        self.next.setObjectName("next")
        self.back = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.turn_page(False))
        self.back.setGeometry(QtCore.QRect(150, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.back.setFont(font)
        self.back.setObjectName("back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionnote = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pencil--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnote.setIcon(icon)
        self.actionnote.setObjectName("actionnote")
        self.actionnote.triggered.connect(self.openWindow)
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/minus-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon1)
        self.actionClose.setObjectName("actionClose")
        self.toolBar.addAction(self.actionnote)
        self.toolBar.addAction(self.actionClose)
        self.actionClose.triggered.connect(self.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def __init__(self,restaurant,menu=[]):
        self.restaurant = restaurant
        self.menu = menu
        self.order = {}
        self.subtotal = 0
        self.del_on = False
        self.cash = True
        self.current_page = 0
        self.message = ""
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cashier"))
        self.button1.setText(_translate("MainWindow", self.menu[0][0]))
        self.button2.setText(_translate("MainWindow", self.menu[0][1]))
        self.button3.setText(_translate("MainWindow", self.menu[0][2]))
        self.button4.setText(_translate("MainWindow", self.menu[0][3]))
        self.button5.setText(_translate("MainWindow", self.menu[0][4]))
        self.button6.setText(_translate("MainWindow", self.menu[0][5]))
        self.button7.setText(_translate("MainWindow", self.menu[0][6]))
        self.button8.setText(_translate("MainWindow", self.menu[0][7]))
        self.button9.setText(_translate("MainWindow", self.menu[0][8]))
        self.received.setText(_translate("MainWindow", "Received"))
        self.delete.setText(_translate("MainWindow", "Del"))
        self.complete.setText(_translate("MainWindow", "Complete"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.back.setText(_translate("MainWindow", "Back"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionnote.setText(_translate("MainWindow", "note"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
    # to remove an item
    def delete_on(self):
        if self.del_on == False:
          self.del_on = True
          self.delete.setStyleSheet("color: black; background-color: red;")
        else:
          self.del_on = False
          self.delete.setStyleSheet("color: black; background-color: light gray;")
    # add items to the order
    def press_it(self,pressed):
            if pressed == "":
                pass
            else:
                pressed = pressed.replace("\n","")
                # ex tacos: $2.50
                matches = re.search("([\w\- ]+): \$([0-9.]+)",pressed)
                name  = matches.group(0)
                price = matches.group(2)
                
                # Add order
                if self.del_on == False:
                    if name not in self.order:
                        self.order[name] = 1
                    else: 
                        self.order[name] +=1
                    self.subtotal +=  float(price)
                # Delete order
                else:
                    if name not in self.order:
                        pass
                    elif self.order[name] == 1:
                        del self.order[name]
                        self.subtotal -= float(price)
                    else:
                        self.order[name] -=1
                        self.subtotal -=  float(price)
                # Prepare output and subtotal
                text=""
                for i in self.order:
                    text += f"{i} x {self.order[i]}" + "\n" 
                
                #after tax
                total = round(1.1 * self.subtotal,2)
                                
                self.output.setText(text)
                if self.subtotal !=0:
                    self.output.setText(self.output.text() + "\n Subtotal: ${:.2f}\n".format(self.subtotal) + " Total:${:.2f}".format(total))
    
    # calculate change 
    def calc(self):
        #after tax
        total = round(1.1 * self.subtotal,2)
        receive = self.doubleSpinBox.value()
        gap = round(receive - total,2) 

        if receive ==0:
              self.output.setText(self.output.text() + "\n\n" + "Paid by Credit/Card")
              self.cash = False
        elif gap > 0:      
              self.output.setText(self.output.text() + "\n\n" + "Change: ${:.2f}".format(gap))
        elif gap < 0:
              gap *= -1
              self.output.setText(self.output.text() + "\n\n" + "Due: ${:.2f}".format(gap))
        else:
              self.output.setText(self.output.text() + "\n\n" + "Exactamente!")
    # for exit button
    def close(self):
        sys.exit()
    
    # to turn the page
    def turn_page(self,back_next):
        pages = len(self.menu)
        # turn page to next 
        if back_next == True and self.current_page < pages -1:
            self.current_page +=1
        if back_next == False and self.current_page > 0 :
            self.current_page -=1
        self.button1.setText(self.menu[self.current_page][0])
        self.button2.setText(self.menu[self.current_page][1])
        self.button3.setText(self.menu[self.current_page][2])
        self.button4.setText(self.menu[self.current_page][3])
        self.button5.setText(self.menu[self.current_page][4])
        self.button6.setText(self.menu[self.current_page][5])
        self.button7.setText(self.menu[self.current_page][6])
        self.button8.setText(self.menu[self.current_page][7])
        self.button9.setText(self.menu[self.current_page][8])

            

    
    # complete the order and record the sales
    def completes(self):
        # send date to the file
        total = round(self.subtotal * 1.1,2)
        now = datetime.datetime.now()
        time = now.strftime("%m-%d-%Y %H:%M:%S")
        try:
            self.message = self.ui.message
        except:
            pass
        write_record(self.restaurant,{"items": self.order,"total":total, "time":time, "cash": self.cash,"comment":self.message})
         
        # delete for the next order
        self.order = {}
        self.subtotal = 0
        self.del_on = False
        self.output.setText("")
        self.cash = True
        self.message = ""
        try:
            self.ui.message = ""
        except:
            pass 
        self.doubleSpinBox.setValue(0)
        self.current_page = 0
        self.turn_page(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
