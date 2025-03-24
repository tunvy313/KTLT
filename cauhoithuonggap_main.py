from PyQt6.QtWidgets import QApplication, QMainWindow
from cauhoithuonggap_extend import cauhoithuonggap_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
f = cauhoithuonggap_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
