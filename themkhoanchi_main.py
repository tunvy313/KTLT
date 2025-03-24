from PyQt6.QtWidgets import QApplication, QMainWindow
from themkhoanchi_extend import themkhoanchi_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
f = themkhoanchi_ext()
f.setupUi(w)
w.show()


sys.exit(app.exec())

