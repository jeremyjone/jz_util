# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
command information
"""
__author__ = "jeremyjone"
__datetime__ = "${DATE} ${TIME}"
__all__ = ["__version__", "JMainWindow"]
__version__ = "1.0.0"


import os, sys
import webbrowser
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class JMainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(JMainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        readme = QtGui.QAction()
        readme.setIcon(QtGui.QIcon("=== icon file ==="))
        readme.triggered.connect(self.readme)

        about = QtGui.QAction()
        about.setIcon(QtGui.QIcon("=== icon file ==="))
        about.triggered.connect(self.about)

    @staticmethod
    def readme():
        webbrowser.open("=== readme file ===")

    def about(self):
        with open("=== about file ===", "rU") as f:
            contents = f.read()

        msg_box = QtGui.QMessageBox()
        msg_box.setIconPixmap(QtGui.QPixmap("=== icon file ==="))
        msg_box.about(self, "About Title",
                      u"%s" % contents.decode("utf8").replace("\n", "<br>"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    t = JMainWindow()
    t.show()
    sys.exit(app.exec_())


