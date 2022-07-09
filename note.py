# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoteWindow(object):
    def setupUi(self, NoteWindow):
        NoteWindow.setObjectName("NoteWindow")
        NoteWindow.resize(712, 359)
        font = QtGui.QFont()
        font.setPointSize(13)
        NoteWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(NoteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 40, 611, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.save = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.save_note(NoteWindow))
        self.save.setGeometry(QtCore.QRect(280, 220, 161, 41))
        self.save.setObjectName("save")
        NoteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 29))
        self.menubar.setObjectName("menubar")
        NoteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NoteWindow)
        self.statusbar.setObjectName("statusbar")
        NoteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NoteWindow)
        QtCore.QMetaObject.connectSlotsByName(NoteWindow)

    def retranslateUi(self, NoteWindow):
        _translate = QtCore.QCoreApplication.translate
        NoteWindow.setWindowTitle(_translate("NoteWindow", "Note"))
        self.save.setText(_translate("NoteWindow", "Save"))
    
    def save_note(self,NoteWindow):
        self.message = self.textEdit.toPlainText()
        NoteWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoteWindow = QtWidgets.QMainWindow()
    ui = Ui_NoteWindow()
    ui.setupUi(NoteWindow)
    NoteWindow.show()
    sys.exit(app.exec_())

