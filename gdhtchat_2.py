from PyQt6.QtWidgets import QApplication, QMainWindow
from gdhtchat_Extend import gdhtchat_ext #Gọi lớp kế thừa
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
f = gdhtchat_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
