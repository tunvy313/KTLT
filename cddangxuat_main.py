from PyQt6.QtWidgets import QApplication, QMainWindow
from cddangxuat_extend import cddangxuat_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = cddangxuat_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())