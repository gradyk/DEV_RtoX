#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
