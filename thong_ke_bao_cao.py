import sys

from Thong_ke_bao_cao_ext import Thong_ke_bao_cao_ext

from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication.instance()
if app is None:
    app=QApplication(sys.argv)
w= QMainWindow()
f= Thong_ke_bao_cao_ext()
f.setupUi(w)

w.show()

sys.exit(app.exec())






# import sys
#
# from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
#
# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# app=QApplication.instance()
# if app is None:
#     app=QApplication(sys.argv)
# w=QMainWindow()
# f=Ui_MainWindow_Ext()
# f.setupUi(w)
#
# w.show()
#
# sys.exit(app.exec())