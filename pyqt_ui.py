# -*- coding: utf-8 -*-
import sys
import string
from my_dbmethods import MyDBCon
from my_codeeditor import MyCodeEditor
from my_highlighter import MyHighlighter1C
from my_dialog import MyUi_Dialog, MyUi_FindDialog
from my_search_intext import My_Search_InText

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql    
class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.appSettings = MyDBCon()       
        self.setupUi()


    def setSQLModel(self):
        if 'db' in dir(self):
            #delete connection and selection model
            self.listView.setModel(None)
            del self.sqlModel
            self.db.close()
            del self.db
            QtSql.QSqlDatabase.removeDatabase('mainConn')
        #set new data base
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE",'mainConn')
        self.db.setDatabaseName(self.appSettings.baseFile())
        self.db.open()
        #set main data model 
        self.sqlModel = QtSql.QSqlTableModel(db = self.db)
        self.sqlModel.setTable("shabl")
        self.sqlModel.select()
        self.currentRowId = 0
        #set new model
        self.listView.setModel(self.sqlModel)
        self.listView.setModelColumn(1)
        self.listView.selectionModel().selectionChanged.connect(self.listCurrentChanged)

    def setupUi(self):
        #resize form
        self.setObjectName("Form")
        self.resize(1080, 682)
        self.setMinimumSize(847, 395)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        #create layouts and form elements
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        #self.textEdit = QtWidgets.QPlainTextEdit (self.centralwidget)
        self.textEdit = MyCodeEditor (self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.verticalLayout_2.addWidget(self.lineEditSearch)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #lock to edit
        self.horizontalLayout_3.addWidget(self.listView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)

        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setObjectName("delButton")
        self.horizontalLayout_2.addWidget(self.delButton)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.setCentralWidget(self.centralwidget)

        #create main menu
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 18))
        exit_menu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu('&Help')

        find_ = QtWidgets.QAction('&Search text', self)
        find_.setShortcut(self.tr("Ctrl+F"))
        find_.setStatusTip(self.tr("Find menu"))
        find_.triggered.connect(self.find_menu)

        exit_menu.addAction(find_)

        settings_ = QtWidgets.QAction('&Settings', self)
        settings_.setStatusTip(self.tr("Programm settings"))
        settings_.triggered.connect(self.showSettingsForm)

        exit_menu.addAction(settings_)

        exit_ = QtWidgets.QAction('&Exit', self)
        exit_.setShortcut(self.tr("Ctrl+Q"))
        exit_.setStatusTip(self.tr("Exit the application"))
        exit_.triggered.connect(self.close)

        exit_menu.addAction(exit_)

        about_ = QtWidgets.QAction('&About', self)
        about_.setStatusTip(self.tr("Info about the application"))
        about_.triggered.connect(self.showProgrammInfo)
        help_menu.addAction(about_)

        #highlighte syntax
        self.highlighter = MyHighlighter1C(self.textEdit.document())
        
        #font edit
        font10 = QtGui.QFont('Courier New',10)
        font8 = QtGui.QFont('Courier New',8)
        self.textEdit.setFont(font10)
        self.lineEdit.setFont(font8)
        self.lineEditSearch.setFont(font8)
        self.listView.setFont(font8)

        #set color for text edit
        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.blue)
        self.textEdit.setCurrentCharFormat(keywordFormat)

        #fill listview from sql table
        self.setSQLModel()

        #button clicks events
        self.addButton.clicked.connect(self.addBtnclicked)
        self.saveButton.clicked.connect(self.saveBtnclicked)
        self.delButton.clicked.connect(self.delBtnclicked)

        #lineeditSearch events
        self.lineEdit.setText('theme')
        self.lineEditSearch.setText('search here')
        self.lineEditSearch.editingFinished.connect(self.lineEditSearch_editingFinished)
        self.lineEditSearch.returnPressed.connect(self.lineEditSearch_editingFinished)
        self.lineEditSearch.textChanged.connect(self.lineEditSearch_textChanged)
        
        self.Search_InText = My_Search_InText()
        self.ModalDialog_find = MyUi_FindDialog(self,QtCore.Qt.Window,self.Search_InText)
        self.ModalDialog_find.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        #minimize to tray
        self.icon = QtWidgets.QSystemTrayIcon()
        self.icon.isSystemTrayAvailable()
        self.icon.setIcon(QtGui.QIcon('icon.png'))
        self.icon.show()
        self.icon.setVisible(True)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.icon.activated.connect(self.activate)

        #tab sequence
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEditSearch, self.lineEdit)
        self.setTabOrder(self.listView, self.lineEdit)
        self.setTabOrder(self.lineEdit, self.textEdit)
        self.setTabOrder(self.textEdit, self.delButton)
        self.setTabOrder(self.delButton, self.saveButton)
        self.setTabOrder(self.saveButton, self.addButton)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F3:
            self.find_next_action()
        else:
            super().keyPressEvent(e)

    def find_menu(self):
        self.textCursor = self.textEdit.textCursor()
        self.Search_InText.setSeacrhParams(self.textEdit.toPlainText(),self.textCursor.position())
        self.ModalDialog_find.setWindowParams()
        self.ModalDialog_find.exec_()
        self.textCursor.setPosition(self.Search_InText.searchIndex(),QtGui.QTextCursor.MoveAnchor)
        self.textEdit.setTextCursor(self.textCursor)
        self.textEdit.setFocus()

    def find_next_action(self):
        if self.textEdit.toPlainText() != '':
            self.textCursor = self.textEdit.textCursor()
            self.Search_InText.setSeacrhParams(self.textEdit.toPlainText(),self.textCursor.position())
            self.Search_InText.searchNext()
            self.textCursor.setPosition(self.Search_InText.searchIndex(),QtGui.QTextCursor.MoveAnchor)
            self.textEdit.setTextCursor(self.textCursor)
            self.textEdit.setFocus()

    def lineEditSearch_editingFinished(self):
        if self.lineEditSearch.text() == '' or self.lineEditSearch.text() == 'search here':
            self.lineEditSearch.setText('search here')
            self.sqlModel.setTable("shabl")
            self.sqlModel.select()
            self.listView.setModelColumn(1)
        elif self.lineEditSearch.text() != 'search here':
            searchText = "keyword LIKE '%" + self.lineEditSearch.text() + "%'"
            self.sqlModel.setFilter(searchText)

    def lineEditSearch_textChanged(self,text):
        if text != '' or text != 'search here':
            searchText = "keyword LIKE '%" + self.lineEditSearch.text() + "%'"
            self.sqlModel.setFilter(searchText)
        else:
            self.sqlModel.setTable("shabl")
            self.sqlModel.select()
            self.listView.setModelColumn(1)


    #show modal dialog with settings
    def showSettingsForm(self):
        self.currbase = self.appSettings.baseFile()
        self.ModalDialog_center = MyUi_Dialog(self,QtCore.Qt.Window,self.appSettings)
        self.ModalDialog_center.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ModalDialog_center.exec_()
        if self.currbase != self.appSettings.baseFile():
            self.setSQLModel()
            self.lineEdit.setText('')
            self.textEdit.setPlainText('')


    #show info about programm
    def showProgrammInfo(self):
        information_ = QtWidgets.QMessageBox.information(self,'About programm','Simple code copy\paste for 1C lang\nv.1.0.3\nzakhar.it@gmail.com',QtWidgets.QMessageBox.Ok,QtWidgets.QMessageBox.Ok)

    # if minimize window, minimize it to tray
    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                self.icon.show()
                self.hide()
                event.ignore()
                return

    #activate from tray
    def activate(self, reason):
        if reason == 2:
            self.show()

    #activate from tray
    def __icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.show()

    #translate UI
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Copy/Paste 1C code"))
        self.addButton.setText(_translate("Form", "Add record"))
        self.saveButton.setText(_translate("Form", "Save changes"))
        self.delButton.setText(_translate("Form", "Delete record"))
    
    def saveBtnclicked(self):
        self.sqlModel.setData(self.sqlModel.index(self.currentRowId, 1), self.lineEdit.text())
        self.sqlModel.setData(self.sqlModel.index(self.currentRowId, 2), self.textEdit.toPlainText())
        self.sqlModel.submitAll()

    def delBtnclicked(self):
        row = self.listView.selectionModel().currentIndex().row()

        self.sqlModel.removeRows(row,1)

        self.sqlModel.submitAll()
        self.sqlModel.sort(0,QtCore.Qt.AscendingOrder)
        if row > 0:
            self.setListViewSelection(row-1)
        else:
            self.setListViewSelection(row+1)

    def addBtnclicked(self):
        newRow = int(self.sqlModel.rowCount())
        self.sqlModel.insertRows(newRow, 1)
        self.sqlModel.setData(self.sqlModel.index(newRow, 1), "New item")
        self.sqlModel.submitAll()
        self.setListViewSelection(newRow)

    #select new row in listView 
    def setListViewSelection(self,newrow):
        self.textEdit.setPlainText(str(self.sqlModel.record(newrow).field(2).value()))
        index = self.listView.model().index(newrow, 1)
        self.listView.selectionModel().setCurrentIndex(index,QtCore.QItemSelectionModel.ClearAndSelect)
        self.listView.scrollTo(index)
        self.listView.setFocus()

    #when listview change element, fill lineEdit and textEdit
    def listCurrentChanged(self,current,previous):
        row = current.indexes()[0].row()
        self.currentRowId = row
        self.lineEdit.setText(str(self.sqlModel.record(row).field(1).value()))
        self.textEdit.setPlainText(str(self.sqlModel.record(row).field(2).value()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
