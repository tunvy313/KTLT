from PyQt6.QtWidgets import QApplication, QMainWindow
from cdxoataikhoan2_extend import cdxoataikhoan2_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = cdxoataikhoan2_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())