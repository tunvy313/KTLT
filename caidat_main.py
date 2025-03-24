from PyQt6.QtWidgets import QApplication, QMainWindow
from caidat_extend import caidat_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = caidat_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())