#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
__name__ = "__main__"

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("/Users/gradyke/Documents/DEV_RtoX/Contents/Library"
                   "/preferences.ui", self)

        self.button = self.findChild(QtWidgets.QPushButton, 'cancelButton')
        self.button.clicked.connect(self.cancelButtonPressed)

        self.show()

    def cancelButtonPressed(self):
        print("cancelButtonPressed")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
