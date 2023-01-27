from PyQt5 import Qt

class MenuLabel(Qt.QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def contextMenuEvent(self, event):
        menu = Qt.QMenu(self)
        action = menu.addAction("Action")
        result = menu.exec_(self.mapToGlobal(event.pos()))
        if action == result:
            print("Action")


if __name__ == "__main__":
    app = Qt.QApplication([])
    label = MenuLabel("Label with menu")
    label.show()
    app.exec_()