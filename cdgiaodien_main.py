from PyQt6.QtWidgets import QApplication, QMainWindow
from cdgiaodien_extend import cdgiaodien_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = cdgiaodien_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())