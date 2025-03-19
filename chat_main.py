from PyQt6.QtWidgets import QApplication, QMainWindow
from chat_extend import chat_ext #Gọi lớp kế thừa
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
f = chat_ext()
f.setupUi(w)

w.show()
sys.exit(app.exec())
