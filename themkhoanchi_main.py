from PyQt6.QtWidgets import QApplication, QMainWindow
# from Product_UI_Ext import UI_Ext
# from Product_UI_Ext_2 import UI_Ext_2
from themkhoanchi_extend import themkhoanchi_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w= QMainWindow()
f = themkhoanchi_ext()
f.setupUi(w)
w.show()

sys.exit(app.exec())

