import json
import os

from PyQt6.QtWidgets import QMessageBox, QMainWindow
from cddangxuat_form import Ui_cddangxuat_form
from dangnhap_extend import dangnhap_ext
from caidat_extend import caidat_ext

class cddangxuat_ext(Ui_cddangxuat_form):
    LOGIN_PATH = "data/thong_tin_dang_nhap.json"
    def setupUi(self, cddangxuat_form):
        super().setupUi(cddangxuat_form)
        self.cddangxuat = cddangxuat_form

        # Connect events
        self.btn_dangxuat.clicked.connect(self.process_dangxuat)
        self.btn_huybo.clicked.connect(self.process_quaylai)
        self.btn_return.clicked.connect(self.process_quaylai)

    def process_dangxuat(self):
        QMessageBox.information(self.cddangxuat, "Thông báo", "Đăng xuất thành công!")
        if os.path.exists(self.LOGIN_PATH):
            try:
                with open(self.LOGIN_PATH, "w", encoding="utf-8") as file:
                    json.dump({}, file)  # Xóa nội dung file bằng cách ghi vào một dictionary rỗng
            except Exception as e:
                QMessageBox.warning(self.cddangxuat, "Lỗi", f"Không thể xóa dữ liệu đăng nhập: {str(e)}")
                return
        # Chuyển sang màn hình đăng nhập
        self.dangnhap_form = QMainWindow()
        self.ui_dangnhap = dangnhap_ext()
        self.ui_dangnhap.setupUi(self.dangnhap_form)

        self.cddangxuat.close()  # Đóng cửa sổ hiện tại
        self.dangnhap_form.show()  # Hiển thị màn hình đăng nhập

    def process_quaylai(self):
        # Quay lại màn hình cài đặt
        self.caidat_form = QMainWindow()
        self.ui_caidat = caidat_ext()
        self.ui_caidat.setupUi(self.caidat_form)

        self.cddangxuat.close()  # Đóng cửa sổ hiện tại
        self.caidat_form.show()  # Hiển thị màn hình cài đặt