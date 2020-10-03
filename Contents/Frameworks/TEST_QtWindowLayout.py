#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, \
    QHBoxLayout, QSplitter
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "RtoX"
        self.top = 150
        self.left = 100
        self.width = 1000
        self.height = 750

        hbox = QHBoxLayout()
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.setStyleSheet('background-color:#DCDCDC')
        lineedit = QLineEdit()
        lineedit.setStyleSheet('background-color:#DCDCDC')
        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200, 200])

        spliiter2 = QSplitter(Qt.Vertical)
        spliiter2.addWidget(splitter1)
        spliiter2.addWidget(bottom)
        spliiter2.setStyleSheet('background-color:yellow')

        hbox.addWidget(spliiter2)

        self.setLayout(hbox)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
