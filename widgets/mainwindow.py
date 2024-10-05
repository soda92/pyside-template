from ui.mainwindow import Ui_Form
from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        from widgets.debug_window import DebugWindowReloader
        self.debug_window = DebugWindowReloader(self)
        self.debug_window.show()

    def test(self):
        print("some test")

