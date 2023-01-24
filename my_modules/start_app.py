from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *



class Ui_MW(Ui_MainWindow, QMainWindow):
    def setupUi(self, mainWindow: object) -> object:
        print("ClassUi_MW_setapUi")
        super().setupUi(mainWindow)
        self.pushButton.clicked.connect(self.getFileNames)

    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, "Вибір файлів для пошуку", "/users", "Excel files (*.xlsx)")[0]

        print(filenames)


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
