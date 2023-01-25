from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings
from settings import Settings
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Ui_MW(Ui_MainWindow):

    def __init__(self):
        super().__init__()


    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.information(self, 'Выход', 'Вы точно хотите выйти?',
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                  QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def setupUi(self, MainWindow: object) -> object:
        print("ClassUi_MW_setapUi")
        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.getFileNames)
        
        self.sett = Settings()
        self.settings = self.sett.getSettings()
        self.radioButton.setChecked(self.settings['radioButtonCheck'])
        self.radioButton_2.setChecked(self.settings['radioButton_2Check'])



    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, "Вибір файлів для пошуку", "/users", "Excel files (*.xlsx) ;;All files(*.*) ")[0]

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
    start()