from PyQt6.QtWidgets import QApplication, QMainWindow
from themkhoanthu_extend import themkhoanthu_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = themkhoanthu_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())