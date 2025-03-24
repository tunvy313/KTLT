from PyQt6.QtWidgets import QApplication, QMainWindow
from vilienket_extend import vilienket_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()

f = vilienket_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())