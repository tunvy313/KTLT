import json
import os

from PyQt6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from cdxoataikhoan2_form import Ui_cdxoataikhoan2_form
from cdxoataikhoan_extend import cdxoataikhoan_ext
from dangky_extend import dangky_ext

class cdxoataikhoan2_ext(Ui_cdxoataikhoan2_form):
    PATH = "data/thong_tin_dang_ky.json"
    LOGIN_PATH = "data/thong_tin_dang_nhap.json"

    def setupUi(self, cdxoataikhoan2_form):
        super().setupUi(cdxoataikhoan2_form)
        self.cdxoataikhoan2 = cdxoataikhoan2_form


        self.txt_matkhau.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_hienmk.hide()

        # Connect events
        self.btn_xacnhan.clicked.connect(self.process_xacnhanxoatk)
        self.btn_huybo.clicked.connect(self.process_quaylai)
        self.btn_return.clicked.connect(self.process_quaylai)

        self.btn_anmk.clicked.connect(self.anhienmatkhau)
        self.btn_hienmk.clicked.connect(self.anhienmatkhau)

    def anhienmatkhau(self):
        """Ẩn/hiện mật khẩu khi bấm nút"""
        if self.txt_matkhau.echoMode() == QLineEdit.EchoMode.Password:
            self.txt_matkhau.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btn_anmk.hide()  # Ẩn nút "ẩn mật khẩu"
            self.btn_hienmk.show()  # Hiện nút "hiện mật khẩu"
        else:
            self.txt_matkhau.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btn_hienmk.hide()  # Ẩn nút "hiện mật khẩu"
            self.btn_anmk.show()  # Hiện nút "ẩn mật khẩu"

    def thong_tin_dang_nhap(self):
        """Lấy tên đăng nhập của người dùng hiện tại"""
        if os.path.exists(self.LOGIN_PATH):
            with open(self.LOGIN_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("Tên đăng nhập", None)
        return None

    def process_xacnhanxoatk(self):
        matkhau = self.txt_matkhau.text().strip()
        ten_dang_nhap = self.thong_tin_dang_nhap()

        if not ten_dang_nhap:
            QMessageBox.warning(self.cdxoataikhoan2, "Lỗi", "Không tìm thấy thông tin đăng nhập!")
            return

        if not matkhau:
            QMessageBox.warning(self.cdxoataikhoan2, "Cảnh báo", "Mật khẩu không được để trống!")
            return

        if not os.path.exists(self.PATH):
            QMessageBox.warning(self.cdxoataikhoan2, "Lỗi", "Không tìm thấy dữ liệu người dùng!")
            return

        try:
            with open(self.PATH, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Kiểm tra tài khoản có tồn tại không
            user_exists = any(user["Tên đăng nhập"] == ten_dang_nhap and user["Mật khẩu"] == matkhau for user in data)
            if not user_exists:
                QMessageBox.warning(self.cdxoataikhoan2, "Lỗi", "Mật khẩu không đúng, vui lòng thử lại!")
                return

            # Xóa tài khoản khỏi danh sách
            data = [user for user in data if user["Tên đăng nhập"] != ten_dang_nhap]

            # Cập nhật lại file JSON
            with open(self.PATH, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            # Xóa thông tin đăng nhập
            if os.path.exists(self.LOGIN_PATH):
                os.remove(self.LOGIN_PATH)

            QMessageBox.information(self.cdxoataikhoan2, "Thông báo", "Xóa tài khoản thành công!")
            self.txt_matkhau.clear()
            self.quay_lai_manhinhdangky()

        except json.JSONDecodeError:
            QMessageBox.critical(self.cdxoataikhoan2, "Lỗi", "Lỗi dữ liệu người dùng!")

    def process_quaylai(self):
        # Quay lại màn hình xóa tài khoản
        self.cdxoataikhoan_form = QMainWindow()
        self.ui_cdxoataikhoan = cdxoataikhoan_ext()
        self.ui_cdxoataikhoan.setupUi(self.cdxoataikhoan_form)

        self.cdxoataikhoan2.close()  # Đóng cửa sổ hiện tại
        self.cdxoataikhoan_form.show()  # Hiển thị màn hình xóa tài khoản

    def quay_lai_manhinhdangky(self):
        # Quay lại màn hình cài đặt
        self.dangky_form = QMainWindow()
        self.ui_dangky = dangky_ext()
        self.ui_dangky.setupUi(self.dangky_form)

        self.cdxoataikhoan2.close()  # Đóng cửa sổ hiện tại
        self.dangky_form.show()  # Hiển thị màn hình cài đặt