from PyQt6.QtWidgets import QApplication, QMainWindow

# from Product_UI_Ext_2 import UI_Ext_2
# from Product_UI_Ext import UI_Ext
# from Product_UI_Ext__2 import UI_Ext__2
from phantich_ext import phantich_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QMainWindow()
# f = UI_Ext()
# f = UI_Ext__2()
f = phantich_ext()
# f = UI_Ext_2()
f.setupUi(w)
w.show()

sys.exit(app.exec())