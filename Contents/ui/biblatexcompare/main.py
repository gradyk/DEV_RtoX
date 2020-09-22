# This Python file uses the following encoding: utf-8

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import sys
import os

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QLabel, QFrame, QSizePolicy, \
    QMainWindow, QAction, QApplication, QVBoxLayout
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class biblatexcompare(QMainWindow, QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(biblatexcompare, self).__init__(*args, **kwargs)
        self.setWindowTitle("Biblatex to TPRES Map")
        self.setFixedSize(1600, 900)

        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        infoLabel = QLabel("Choose a menu option or right-click to "
                           "invoke a context menu")
        infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        infoLabel.setAlignment(QtCore.Qt.AlignCenter)

        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel |
                                          QtWidgets.QDialogButtonBox.Ok)

        # Connecting our 'Ok' and 'Cancel' buttons to the
        # corresponding return codes
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        # Defining our widgets and main layout
        layout = QVBoxLayout()
        layout.setMargin(5)
        layout.addWidget(topFiller)
        layout.addWidget(infoLabel)
        layout.addWidget(bottomFiller)
        layout.addWidget(self.buttonBox)

        # Act = biblatexcompare.createActions(self=self)
        # biblatexcompare.createMenus(self=self, Act=Act)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # message = "A context menu is available by right-clicking"
        # QMainWindow.statusBar(self=self, ).showMessage(
        #     message, 2000)

    def createActions(self):
        Act = QAction("&New", self)
        Act.setShortcuts(QtGui.QKeySequence.New)
        Act.setStatusTip("Create a new file")
        # Act.triggered.connect(newFile)
        return Act

    def createMenus(self, Act):
        fileMenu = self.menuBar().addMenu('&File')
        fileMenu.addAction(Act)
        # fileMenu.addAction("&Open")
        # fileMenu.addAction("&Save")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    mainwindow = biblatexcompare()
    mainwindow.show()
    sys.exit(app.exec_())
