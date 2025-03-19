import sys

from Sign_Up_MainWindown_Ext import Ui_MainWindow_Ext
from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication.instance()
if app is None:
    app=QApplication(sys.argv)
w=QMainWindow()
f=Ui_MainWindow_Ext()
f.setupUi(w)

w.show()

sys.exit(app.exec())
