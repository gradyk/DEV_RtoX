from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# Note: dialog.ui should be changed to the name of the .ui I have created.
Form, Window = uic.loadUiType("dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()