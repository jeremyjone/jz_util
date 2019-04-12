# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Thread timer is used to change the transparent style parameters to achieve a 
short gradient effect of the endless window.

利用线程定时器改变透明样式参数，实现一个短时渐变的无边窗口效果。
"""
__author__ = "jeremyjone"
__datetime__ = "2019/3/13 10:27"
__all__ = ["__version__", "JWidget"]
__version__ = "1.0.0"
import os, sys
import threading
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class JWidget(QtGui.QWidget):
    UPDATE_SHOW = QtCore.Signal(str)
    def __init__(self, parent=None):
        super(JWidget, self).__init__(parent)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.Tool |
                            QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.X11BypassWindowManagerHint |
                            QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(False)
        self.initUI()

        self._update_interval = 0.1
        self._alpha = 0
        self.showSlow()

    def initUI(self):
        self.label = QtGui.QLabel("test")
        self.label.setFixedSize(200, 200)
        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)
        self.UPDATE_SHOW.connect(self.myShow)

    def showSlow(self):
        self._timer = threading.Timer(self._update_interval, self.showSlow)
        self._timer.start()

        style = """
            QWidget {
                background: rgb(155, 100, 50, %d);
            }
        """ % self._alpha

        self._alpha += 1

        if self._alpha > 255:
            print("finish")
            self._timer.cancel()

        self.UPDATE_SHOW.emit(style)

    def myShow(self, alpha):
        self.setStyleSheet(alpha)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    t = JWidget()
    t.show()
    sys.exit(app.exec_())
