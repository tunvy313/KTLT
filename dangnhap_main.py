from PyQt6.QtWidgets import QApplication, QMainWindow
from dangnhap_extend import dangnhap_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
f = dangnhap_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
