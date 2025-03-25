from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from thongbao_chinh_ext import thongbao_chinh_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
# f = UI_Ext()
# f = UI_Ext__2()
f = thongbao_chinh_ext()
# f = UI_Ext_2()
f.setupUi(w)
w.show()

sys.exit(app.exec())