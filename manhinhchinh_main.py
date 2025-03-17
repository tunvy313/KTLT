from PyQt6.QtWidgets import QApplication, QMainWindow
from manhinhchinh_extend import manhinhchinh_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = manhinhchinh_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
