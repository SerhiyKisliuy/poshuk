from my_modules.poshuk import Ui_MainWindow
from my_modules.select_file import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_D(Ui_Dialog):  # Діалогове вікно для вибору файлів (Успадкування та перевизначення).
    def setupUi(self, dialog):
        super().setupUi(dialog)


class Ui_MW(Ui_MainWindow):
    visibleDialogWindow = False

    def setupUi(self, mainWindow: object) -> object:
        print("ClassUi_MW_setapUi")
        super().setupUi(mainWindow)
        self.pushButton.clicked.connect(self.start_Ui_Dialog)

    def start_Ui_Dialog(self):  #Создає діалогове вікно і виводить його.
        if not self.visibleDialogWindow:  #Умова для запобігання відкриття декількох діалогових вікон
            self.visibleDialogWindow = True
            dialog = QtWidgets.QDialog()
            uid = Ui_D()
            uid.setupUi(dialog)
            dialog.show()
            dialog.exec()

        else:
            print("Error Діалогове вікно вже існує")


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
