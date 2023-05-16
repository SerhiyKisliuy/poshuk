import typing

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import QModelIndex


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, head, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []
        self.hader = []

    def setItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()

    def setHader(self, hader):
        self.beginResetModel()
        self.hader = hader
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        # return super().rowCount(*args, **kwargs)  #Вертає кількість строк
        return len(self.items)

    def columnCount(self, *args, **kwargs) -> int:
        # return super().columnCount(*args, **kwargs)  #Вертає кількість стовбців
        return len(self.hader)

    def data(self, index: QModelIndex, role: QtCore.Qt.DisplayRole):
        # return 'a'
        if not index.isValid():
            return
        if role == QtCore.Qt.DisplayRole:
            row = self.items[index.row()]
            return row[index.column()]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.hader[section]
            if orientation == QtCore.Qt.Orientation.Vertical:
                return section
