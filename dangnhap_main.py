from PyQt6.QtWidgets import QApplication, QMainWindow
from dangnhap_extend import dangnhap_ext #Gọi lớp kế thừa
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
# f = Ui_MainWindow
f = dangnhap_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
