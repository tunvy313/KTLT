import sys

from dangky_extend import dangky_ext
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication.instance()
if app is None:
    app=QApplication(sys.argv)
w = QMainWindow()
f = dangky_ext()
f.setupUi(w)

w.show()

sys.exit(app.exec())
