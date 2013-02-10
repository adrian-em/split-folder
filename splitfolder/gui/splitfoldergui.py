try:
    import sip
    import sys
    sip.setapi("QString", 2)
    from PyQt4 import QtCore, QtGui
    from gui import Ui_SplitFolderWindow  # import ui
    from .splitfolder import main
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class SplitFolderApp(QtGui.QMainWindow):

    def __init__(self, parent=None):
        '''
            Construct UI.
        '''
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SplitFolderWindow()
        self.ui.setupUi(self)
        self.center()
        self.ui.folderSelect.clicked.connect(lambda: self.folderSelection())

    def folderSelection(self):
        return QtGui.QFileDialog.getExistingDirectory(self, "Select folder")

    def runScript(self):
        pass

    def center(self):

        '''
            Center the UI
        '''
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = SplitFolderApp()
    myapp.show()
    sys.exit(app.exec_())
