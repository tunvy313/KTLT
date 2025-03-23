import sys

from lich_su_giao_dich_ext import Ui_MainWindow_ext
from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication.instance()
if app is None:
    app=QApplication(sys.argv)
w=QMainWindow()
f=Ui_MainWindow_ext()
f.setupUi(w)

w.show()

sys.exit(app.exec())