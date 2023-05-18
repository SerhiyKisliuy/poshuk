import PyQt5.QtGui
import pyclip
from my_modules.poshuk import Ui_MainWindow
import my_modules.searsh_in_xls
from my_modules.tablemodel import TableModel
from my_modules.search_xlsx import SearchInXLSX
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from my_modules.settings import Settings
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
        self.pushButton_2.clicked.connect(self.poshuk)  #Починає пошук при натисканні кнопки
        self.lineEdit.returnPressed.connect(self.poshuk)  #Починає пошук при натисканні клавіши Ентер
        self.listWidget.installEventFilter(self)
        # self.listWidget.setSelectionMode(QListWidget.MultiSelection)
        # self.tableView(self)
        #self.tableView.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
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
        # print("list_item")
        # print(self.list_item)  #Список файлів
        # print("lineEdit")
        # print(self.lineEdit.text())  #Пошуковий запрос
        tableData = []
        self.list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]  # +++

        if self.radioButton.isChecked():
            searchXLSX = SearchInXLSX()
            curreItem = self.listWidget.currentItem().text()

            #print(curreItem)
            searchXLSX.setFileNames(str(curreItem))
            searchXLSX.setRequestSearch(self.lineEdit.text())
            searchXLSX.setOnFile(True)
            tableData = searchXLSX.getTableDate()
            # tableresults = my_modules.searsh_in_xls.search(self.list_item[0], self.lineEdit.text())
        if self.radioButton_2.isChecked():
            searchXLSX = SearchInXLSX()
            searchXLSX.setFileNames(self.list_item)
            searchXLSX.setRequestSearch(self.lineEdit.text())
            searchXLSX.setOnFile(False)
            tableData = searchXLSX.getTableDate()
        # print("poshuk")
        # print(tableData[1])
        dateTable = self.dataLengs(tableData)
        self.model = TableModel(dateTable[0])  # Створюємо обєкт - модел таблиці.
        self.model.setHader(dateTable[1])  # Передаємо в модель шапку
        self.model.setItems(dateTable[0])  # Передаємо в модель таблицю
        self.tableView.setModel(self.model)  # Передаємо модель таблиці у вієв.
        self.tableView.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)  #Розтягує стовбці згідно змісту

    def dataLengs(self, data):
        resultData = []
        maxLengsRow = 0
        for i in data:
            row = i
            le = len(row)
            if le > maxLengsRow:
                maxLengsRow = le
                print("maxLengsRow")
                print(maxLengsRow)
        for i in data:
            row = i
            while (len(row)) < (maxLengsRow):
                row.append("-")
            resultData.append(row)
        print("dataLengs")
        print(resultData)

        header = []
        for i in range(maxLengsRow - 2):
            header.append(str(i + 1))
        header = ["Лист"] + header
        header = ["Файл"] + header
        print(header)
        return resultData, header

    def eventFilter(self, obj, event):
        if obj is self.listWidget and event.type() == QtCore.QEvent.ContextMenu:
            self.item = self.listWidget.currentItem()
            if self.item:
                menu = Qt.QMenu()
                action = menu.addAction("Видалити")
                action1 = menu.addAction("Копіювати шлях")

                positionCursor = PyQt5.QtGui.QCursor.pos()  # Отримуємо позицію курсора
                result = menu.exec_(positionCursor)

                if action == result:
                    self.listWidget.takeItem(self.listWidget.row(self.item))
                if action1 == result:
                    pyclip.copy(self.listWidget.currentItem().text())

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
            #self.filenames[-1]
            self.pathFile = self.filenames[-1]  # Отримуємо останній та повний путь файлу
            # Розділяємо путь до файлу на путь до папки та ім'я файлу.
            self.pathDir, self.nameFile = os.path.split(self.pathFile)
            self.settings['path_dir'] = self.pathDir  # Записуємо у змінну налаштунків

            self.listWidget.setCurrentItem(self.item)  # Робимо елемент вибраним

        except Exception:
            self.item = self.listWidget.item(0)
            self.listWidget.setCurrentItem(self.item)  # Робимо елемент вибраним

    def testTypeFile(self, path_file):

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
