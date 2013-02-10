# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitfolder.ui'
#
# Created: Sun Feb 10 18:29:07 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SplitFolderWindow(object):
    def setupUi(self, SplitFolderWindow):
        SplitFolderWindow.setObjectName(_fromUtf8("SplitFolderWindow"))
        SplitFolderWindow.resize(438, 348)
        SplitFolderWindow.setStatusTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(SplitFolderWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.elementsNumber = QtGui.QLineEdit(self.centralwidget)
        self.elementsNumber.setGeometry(QtCore.QRect(110, 140, 61, 27))
        self.elementsNumber.setObjectName(_fromUtf8("elementsNumber"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 110, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.folderSelect = QtGui.QPushButton(self.centralwidget)
        self.folderSelect.setGeometry(QtCore.QRect(110, 30, 161, 31))
        self.folderSelect.setObjectName(_fromUtf8("folderSelect"))
        SplitFolderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SplitFolderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        SplitFolderWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SplitFolderWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SplitFolderWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(SplitFolderWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SplitFolderWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), SplitFolderWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SplitFolderWindow)

    def retranslateUi(self, SplitFolderWindow):
        SplitFolderWindow.setWindowTitle(QtGui.QApplication.translate("SplitFolderWindow", "Split Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.elementsNumber.setToolTip(QtGui.QApplication.translate("SplitFolderWindow", "Write the number of elements per folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SplitFolderWindow", "Elements per folder", None, QtGui.QApplication.UnicodeUTF8))
        self.folderSelect.setText(QtGui.QApplication.translate("SplitFolderWindow", "Select folder...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("SplitFolderWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("SplitFolderWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

