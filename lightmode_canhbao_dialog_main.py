from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from lightmode_canhbao_dialog_ext import lightmode_canhbao_dialog_ext
import sys

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

w = QDialog()
# f = UI_Ext()
# f = UI_Ext__2()
f = lightmode_canhbao_dialog_ext()
# f = UI_Ext_2()
f.setupUi(w)
w.show()

sys.exit(app.exec())
