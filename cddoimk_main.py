from PyQt6.QtWidgets import QApplication, QMainWindow
from cddoimk_extend import cddoimk_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = cddoimk_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())