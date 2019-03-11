# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
command information
"""
__author__ = "jeremyjone"
__datetime__ = "${DATE} ${TIME}"
__all__ = ["__version__", "JWidget"]
__version__ = "1.0.0"


import os, sys
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class JWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(JWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    t = JWidget()
    t.show()
    sys.exit(app.exec_())

