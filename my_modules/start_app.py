import PyQt5.QtGui

from my_modules.poshuk import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from settings import Settings
from PyQt5 import Qt
import os


class Ui_MW(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.list_item = None
        self.setupUi(self)

    def setupUi(self, MainWindow: object) -> object:

        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.getFileNames)
        self.pushButton_3.clicked.connect(self.clearListWidget)
        self.pushButton_2.clicked.connect(self.poshuk)
        self.listWidget.installEventFilter(self)
        # self.listWidget.setSelectionMode(QListWidget.MultiSelection)

        self.sett = Settings()
        self.settings = self.sett.getSettings()  # Отримуємо налаштунки програми

        # Застосовуємо налаштунки програми
        self.radioButton.setChecked(self.settings['radioButtonCheck'])
        self.radioButton_2.setChecked(self.settings['radioButton_2Check'])
        self.list_item = self.settings["list_item"]
        self.listWidget.addItems(self.list_item)
        self.pathDir = self.settings["path_dir"]

        item = self.listWidget.item(0)  # Отримуємо перший єлемент списку
        self.listWidget.setCurrentItem(item)  # Робимо елемент вибраним

    def clearListWidget(self):
        self.listWidget.clear()

    def poshuk(self):
        pass

    def eventFilter(self, obj, event):
        if obj is self.listWidget and event.type() == QtCore.QEvent.ContextMenu:
            self.item = self.listWidget.currentItem()
            if self.item:
                menu = Qt.QMenu()
                action = menu.addAction("Видалити")

                positionCursor = PyQt5.QtGui.QCursor.pos()  # Отримуємо позицію курсора
                result = menu.exec_(positionCursor)

                if action == result:
                    self.listWidget.takeItem(self.listWidget.row(self.item))

        return super().eventFilter(obj, event)

    def getFileNames(self):
        self.pathDir = self.settings['path_dir']
        self.filenames = QFileDialog.getOpenFileNames(self, "Вибір файлів для пошуку", self.pathDir,
                                                      "Excel files (*.xlsx) ;;All files(*.*) ")[0]

        self.list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]

        for i in self.filenames:

            if i not in self.list_item:
                if self.testTypeFile(i):
                    self.item = QtWidgets.QListWidgetItem()
                    self.item.setText(i)
                    self.listWidget.addItem(self.item)

        try:
            self.filenames[-1]
            self.pathFile = self.filenames[-1]  # Отримуємо останній та повний путь файлу
            # Розділяємо путь до файлу на путь до папки та ім'я файлу.
            self.pathDir, self.nameFile = os.path.split(self.pathFile)
            self.settings['path_dir'] = self.pathDir  # Записуємо у змінну налаштунків

            self.listWidget.setCurrentItem(self.item)  # Робимо елемент вибраним

        except Exception:
            self.item = self.listWidget.item(0)
            self.listWidget.setCurrentItem(self.item)  # Робимо елемент вибраним


    def testTypeFile (self, path_file):

        path_dir, name_file = os.path.split(path_file)
        filename, type_file = os.path.splitext(name_file)
        if type_file == '.xlsx':
            return True
        else:
            return False

    def closeEvent(self, event):

        self.list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]  # +++

        self.settings["radioButtonCheck"] = self.radioButton.isChecked()
        self.settings["radioButton_2Check"] = self.radioButton_2.isChecked()
        self.settings["list_item"] = self.list_item
        self.settings["path_dir"] = self.pathDir

        self.save = Settings()
        self.save.setSettings(self.settings)


def start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MW()
    # ui.setupUi(mainWindow)
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
