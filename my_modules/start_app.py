from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings
from settings import Settings
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Ui_MW(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


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

        for i in filenames:
            self.item = QtWidgets.QListWidgetItem()
            self.item.setText(i)
            self.listWidget.addItem(self.item)
            print(self.item)
        print(filenames)

    def closeEvent(self, event):
        self.settings["radioButtonCheck"] = self.radioButton.isChecked()
        self.settings["radioButton_2Check"] = self.radioButton_2.isChecked()

        self.save = Settings()
        self.save.setSettings(self.settings)

def start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MW()
    #ui.setupUi(mainWindow)
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()