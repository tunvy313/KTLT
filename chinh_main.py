from PyQt6 import QtWidgets, QtCore
from thongbao_chinh_ext import thongbao_chinh_ext
from lightmode_canhbao_dialog_ext import lightmode_canhbao_dialog_ext
import sys

class MainApp(QtCore.QObject):
    def __init__(self):
        super().__init__()  # Gọi constructor của QObject
        self.app = QtWidgets.QApplication(sys.argv)

        # Tạo cửa sổ cảnh báo
        self.dialog = QtWidgets.QDialog()
        self.ui_dialog = lightmode_canhbao_dialog_ext()
        self.ui_dialog.setupUi(self.dialog)

        # Tạo cửa sổ chính
        self.main_window = QtWidgets.QMainWindow()
        self.ui_main = thongbao_chinh_ext()
        self.ui_main.setupUi(self.main_window)

        # Đóng dialog khi nhấn vào bất cứ đâu trừ btn_exit
        self.dialog.installEventFilter(self)

        # Hiển thị dialog trước
        self.dialog.show()
        sys.exit(self.app.exec())

    def eventFilter(self, obj, event):
        if obj == self.ui_dialog and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if not self.ui_dialog.btn_exit.underMouse():  # Kiểm tra nếu không nhấn vào btn_exit
                self.dialog.close()
                self.main_window.show()
                return True  # Chặn sự kiện tiếp tục xử lý
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    MainApp()