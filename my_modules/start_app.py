from my_modules.poshuk import Ui_MainWindow
from my_modules.select_file import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_D(Ui_Dialog):  # Діалогове вікно для вибору файлів (Успадкування та перевизначення).
    def setupUi(self, dialog):
        super().setupUi(dialog)


class Ui_MW(Ui_MainWindow):
    visibleDialogWindow = False

    def setupUi(self, mainWindow: object) -> object:
        print("ClassUi_MW_setapUi")
        super().setupUi(mainWindow)
        self.pushButton.clicked.connect(self.getDirectory)

    def getDirectory(self):  # <-----
        dirlist = QFileDialog.getExistingDirectory()
        print(dirlist)

    def getFileName(self):
        filename = QFileDialog.getOpenFileName()[0]

        print(filename)



def start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MW()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MW()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
