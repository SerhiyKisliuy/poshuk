from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings
from settings import Settings

class Ui_MW(Ui_MainWindow, QMainWindow):
    def setupUi(self, mainWindow: object) -> object:
        print("ClassUi_MW_setapUi")
        super().setupUi(mainWindow)
        self.pushButton.clicked.connect(self.getFileNames)
        self.sett = Settings()
        self.settings = self.sett.getSettings()
        self.radioButton.setChecked(self.settings['radioButtonCheck'])
        self.radioButton_2.setChecked(self.settings['radioButton_2Check'])



    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, "Вибір файлів для пошуку", "/users", "Excel files (*.xlsx) ;;All files(*.*) ")[0]

        print(filenames)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




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