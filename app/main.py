import os
import platform
import sys
import widgets.mainwindow as mainwindow
from PySide6 import QtWidgets, QtCore
import main_rc  # noqa: F401


def main_gui():
    if platform.system() == "Linux":
        # this will enable automaic load of fcitx plugin
        os.environ["QT_PLUGIN_PATH"] = (
            os.environ.get("QT_PLUGIN_PATH", "") + ";" + "/usr/lib/qt6/plugins/"
        )
    app = QtWidgets.QApplication(sys.argv)

    translator = QtCore.QTranslator()
    translator.load(":/translation_zh_CN.qm")
    app.installTranslator(translator)

    _window = mainwindow.MainWindow()
    _window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main_gui()
