from PyQt6.QtWidgets import QApplication, QMainWindow
from lienkettkmoi_extend import lienkettkmoi_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = lienkettkmoi_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())