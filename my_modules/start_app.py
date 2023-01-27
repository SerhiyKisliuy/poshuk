import PyQt5.QtGui

from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from settings import Settings
from PyQt5 import Qt
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Ui_MW(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def setupUi(self, MainWindow: object) -> object:

        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.getFileNames)
        self.pushButton_3.clicked.connect(self.clearListWidget)
        self.pushButton_2.clicked.connect(self.poshuk)
        self.listWidget.installEventFilter(self)
        #self.listWidget.setSelectionMode(QListWidget.MultiSelection)

        self.sett = Settings()
        self.settings = self.sett.getSettings()  # Отримуємо налаштунки програми

        # Застосовуємо налаштунки програми
        if self.settings['radioButtonCheck']:
            self.radioButton.setChecked(self.settings['radioButtonCheck'])
        if self.settings['radioButton_2Check']:
            self.radioButton_2.setChecked(self.settings['radioButton_2Check'])
        if self.settings["list_item"]:
            self.listWidget.addItems(self.settings["list_item"])

    def poshuk(self):
        pass
    def clearListWidget(self):
        self.listWidget.clear()

    def eventFilter(self, obj, event):
        if obj is self.listWidget and event.type() == QtCore.QEvent.ContextMenu:
            self.item = self.listWidget.currentItem()
            if self.item:
                #text = self.item.text()
                #print(f'clicked item text: {text}')
                menu = Qt.QMenu()
                action = menu.addAction("Видалити")

                positionCursor = PyQt5.QtGui.QCursor.pos()  #Отримуємо позицію курсора
                result = menu.exec_(positionCursor)

                if action == result:
                    self.listWidget.takeItem(self.listWidget.row(self.item))


        return super().eventFilter(obj, event)

    def contextMenuEvent(self, event):

        pass

    def getFileNames(self):
        filenames = QFileDialog.getOpenFileNames(self, "Вибір файлів для пошуку", "/users", "Excel files (*.xlsx) ;;All files(*.*) ")[0]

        for i in filenames:
            self.item = QtWidgets.QListWidgetItem()
            self.item.setText(i)
            self.listWidget.addItem(self.item)



    def closeEvent(self, event):

        self.list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]  # +++

        self.settings["radioButtonCheck"] = self.radioButton.isChecked()
        self.settings["radioButton_2Check"] = self.radioButton_2.isChecked()
        self.settings["list_item"] = self.list_item

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