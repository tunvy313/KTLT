from PyQt6.QtCore import Qt

from manhinhchinh_form import Ui_manhinhchinh_form
from PyQt6.QtWidgets import QMessageBox, QMainWindow


class manhinhchinh_ext(Ui_manhinhchinh_form):
    def setupUi(self, manhinhchinh_form):
        super().setupUi(manhinhchinh_form)
        self.manhinhchinh = manhinhchinh_form

        # Connect events
        self.btn_themgiaodich.clicked.connect(self.open_themkhoanthu_form)

    def open_themkhoanthu_form(self):
        # Mở màn hình thêm khoản thu
        from themkhoanthu_extend import khoanthu_ext
        self.themkhoanthu_form = khoanthu_ext()
        self.themkhoanthu_form.show()
        self.manhinhchinh.close()  # Đóng màn hình cài đặt
        self.themkhoanthu_form.show()  # Hiển thị màn hình đăng xuất

