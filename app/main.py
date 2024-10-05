import os
import platform
import sys
import widgets.mainwindow as mainwindow
from PySide6 import QtWidgets


def main_gui():
    if platform.system() == "Linux":
        # this will enable automaic load of fcitx plugin
        os.environ["QT_PLUGIN_PATH"] = (
            os.environ.get("QT_PLUGIN_PATH", "") + ";" + "/usr/lib/qt6/plugins/"
        )
    app = QtWidgets.QApplication(sys.argv)

    _window = mainwindow.MainWindow(app)
    _window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main_gui()
