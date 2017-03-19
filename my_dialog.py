# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from my_search_intext import My_Search_InText
import os

class MyUi_Dialog(QtWidgets.QDialog):
    def __init__(self,parent,flags,settings):
        super().__init__(parent,flags)
        self.settings = settings
        self.filename = (self.settings.baseFile(),)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(355, 76)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(0, 40, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_basepath = QtWidgets.QLineEdit(self)
        self.lineEdit_basepath.setGeometry(QtCore.QRect(100, 10, 221, 20))
        self.lineEdit_basepath.setObjectName("lineEdit_basepath")
        self.select_base_Btn = QtWidgets.QPushButton(self)
        self.select_base_Btn.setGeometry(QtCore.QRect(320, 10, 21, 20))
        self.select_base_Btn.setObjectName("select_base_Btn")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        # self.create_Btn = QtWidgets.QPushButton(self)
        # self.create_Btn.setGeometry(QtCore.QRect(10, 60, 91, 31))
        # self.create_Btn.setObjectName("create_Btn")
        self.create_Btn = self.buttonBox.addButton('Create new base',QtWidgets.QDialogButtonBox.ApplyRole)

        self.lineEdit_basepath.setText(self.filename[0])
        self.retranslateUi()
        #button clicks events
        self.create_Btn.clicked.connect(self.createBtnclicked)
        self.select_base_Btn.clicked.connect(self.select_baseBtnclicked)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(self)

    def accept(self):
        if self.settings.baseFile() != self.filename[0]:
            self.settings.set_baseFile(self.filename[0])
        self.close()

    def createBtnclicked(self):
        newBasePath = os.path.abspath(os.curdir) + '/myBase.db'
        path = newBasePath.replace('\\','/')
        self.lineEdit_basepath.setText(path)
        self.filename = None
        self.filename = (path,)

    def select_baseBtnclicked(self):
        self.filename = None
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        if self.filename[0] != '':
            self.lineEdit_basepath.setText(self.filename[0])

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Settings"))
        self.select_base_Btn.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "Current base:"))
        # self.create_Btn.setText(_translate("Dialog", "Create new base"))

class MyUi_FindDialog(QtWidgets.QDialog):
    def __init__(self,parent,flags,My_Search):
        super().__init__(parent,flags)
        self.My_Search = My_Search
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(355, 76)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(0, 40, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        font8 = QtGui.QFont('Courier New',8)
        self.buttonBox.addButton('Find (Enter)',QtWidgets.QDialogButtonBox.AcceptRole)
        self.findnext_Btn = self.buttonBox.addButton('Find next (F3)',QtWidgets.QDialogButtonBox.ApplyRole)
        self.buttonBox.addButton('Cancel',QtWidgets.QDialogButtonBox.RejectRole)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_search = QtWidgets.QLineEdit(self)
        self.lineEdit_search.setGeometry(QtCore.QRect(100, 10, 221, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setFont(font8)
        self.lineEdit_search.setClearButtonEnabled(True)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")

        self.lineEdit_search.setText('search here')
        self.retranslateUi()
        #button clicks events
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.findnext_Btn.clicked.connect(self.acceptNext)

        # shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F3), self)
        # # shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F3), self, QtCore.SLOT(self.acceptNext))
        # self.setShortcutEnabled(shortcut.id(),True)
        # findNext_ = QtWidgets.QAction('&FindNext', self)
        # findNext_.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F3))
        # findNext_.triggered.connect(self.acceptNext)

        find_ = QtWidgets.QAction('&Find', self)
        find_.setShortcut(self.tr("Enter"))
        find_.triggered.connect(self.accept)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEdit_search, self.findnext_Btn)
        self.setTabOrder(self.findnext_Btn, self.buttonBox)
    # def exec(self):
    #     return 1

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F3:
            self.acceptNext()
        else:
            super().keyPressEvent(e)

    def accept(self):
        self.My_Search.setSearchText(self.lineEdit_search.text())
        self.My_Search.search()
        self.close()

    def acceptNext(self):
        self.My_Search.setSearchText(self.lineEdit_search.text())
        self.My_Search.searchNext()
        self.close()

    def reject(self):
        super().reject()

    def setWindowParams(self):
        self.lineEdit_search.setSelection(0,len(self.lineEdit_search.text()))
        self.lineEdit_search.setFocus()

    def searchIndex(self):
        return self.search_index

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Find"))
        self.label.setText(_translate("Dialog", "Text search:"))
