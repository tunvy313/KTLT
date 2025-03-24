from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit
from doimatkhau_form import Ui_doimatkhau_form
from dangky_extend import dangky_ext
from dangnhap_extend import dangnhap_ext
import os
import json

class doimatkhau_ext(Ui_doimatkhau_form):
    def setupUi(self, doimatkhau_form):
        super().setupUi(doimatkhau_form)
        self.doimatkhau = doimatkhau_form
        self.email_nguoi_dung = None
        # Kết nối sự kiện nút "Đổi mật khẩu"
        self.btndoimatkhau.clicked.connect(self.doi_mat_khau)
        self.btnanmatkhaucu.clicked.connect(self.anhienmatkhaucu)
        self.btnanmatkhaumoi.clicked.connect(self.anhienmatkhaumoi)
        self.btnhienmatkhaucu.clicked.connect(self.anhienmatkhaucu)
        self.btnhienmatkhaumoi.clicked.connect(self.anhienmatkhaumoi)

        self.btn_return.clicked.connect(self.back_to_quenmatkhau_form)
        self.btndangky.clicked.connect(self.back_to_dangky)

    def set_email(self, email):
        """Nhận email từ giao diện quên mật khẩu"""
        self.email_nguoi_dung = email

    def anhienmatkhaucu(self):
        """Chuyển đổi trạng thái hiển thị mật khẩu"""
        if self.txtmatkhaumoi.echoMode() == QLineEdit.EchoMode.Password:
            self.txtmatkhaumoi.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btnanmatkhaucu.hide()  # Ẩn nút hiện mật khẩu
            self.btnhienmatkhaucu.show()  # Hiển thị nút ẩn mật khẩu
        else:
            self.txtmatkhaumoi.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btnhienmatkhaucu.hide()  # Ẩn nút ẩn mật khẩu
            self.btnanmatkhaucu.show()  # Hiển thị nút hiện mật khẩu

    def anhienmatkhaumoi(self):
        """Chuyển đổi trạng thái hiển thị mật khẩu"""
        if self.txtnhaplaimatkhaumoi.echoMode() == QLineEdit.EchoMode.Password:
            self.txtnhaplaimatkhaumoi.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btnanmatkhaumoi.hide()  # Ẩn nút hiện mật khẩu
            self.btnhienmatkhaumoi.show()  # Hiển thị nút ẩn mật khẩu
        else:
            self.txtnhaplaimatkhaumoi.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btnhienmatkhaumoi.hide()  # Ẩn nút ẩn mật khẩu
            self.btnanmatkhaumoi.show()  # Hiển thị nút hiện mật khẩu

    def doi_mat_khau(self):
        """Xử lý đổi mật khẩu"""
        mat_khau_moi = self.txtmatkhaumoi.text().strip()
        nhap_lai_mat_khau = self.txtnhaplaimatkhaumoi.text().strip()

        # Kiểm tra mật khẩu mới có trùng nhau không
        if not mat_khau_moi or not nhap_lai_mat_khau:
            QMessageBox.warning(self.doimatkhau, "Cảnh báo", "Mật khẩu không được để trống!")
            return

        if mat_khau_moi != nhap_lai_mat_khau:
            QMessageBox.warning(self.doimatkhau, "Lỗi", "Mật khẩu không trùng khớp!")
            return

        try:
            if not os.path.exists("data/thong_tin_dang_ky.json"):
                QMessageBox.warning(self.doimatkhau, "Lỗi", "Không tìm thấy dữ liệu đăng ký!")
                return

            with open("data/thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            # Tìm email trong danh sách và cập nhật mật khẩu
            user_found = False
            for user in data:
                if user["Email"] == self.email_nguoi_dung:
                    user["Mật khẩu"] = mat_khau_moi
                    user_found = True
                    break
            if not user_found:
                QMessageBox.warning(self.doimatkhau, "Lỗi", "Không tìm thấy tài khoản!")
                return

            with open("data/thong_tin_dang_ky.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            QMessageBox.information(self.doimatkhau, "Thông báo", "Đổi mật khẩu thành công!")
            self.txtmatkhaumoi.clear()
            self.txtnhaplaimatkhaumoi.clear()
            self.open_dangnhap_form()
        except json.JSONDecodeError:
            QMessageBox.critical(self.doimatkhau, "Lỗi", "Lỗi dữ liệu người dùng!")

    def back_to_quenmatkhau_form(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        from quenmatkhau_extend import quenmatkhau_ext
        self.quenmatkhau_form = QMainWindow()
        self.ui_quenmatkhau = quenmatkhau_ext()
        self.ui_quenmatkhau.setupUi(self.quenmatkhau_form)
        self.doimatkhau.close()  # Đóng cửa sổ đăng nhập nếu cần
        self.quenmatkhau_form.show()

    def back_to_dangky(self):
        """Trở về cửa sổ đăng ký"""
        self.dangky_form = QMainWindow()
        self.ui_dangky = dangky_ext()  # Khởi tạo giao diện
        self.ui_dangky.setupUi(self.dangky_form)  # Gán giao diện vào cửa sổ mới

        self.doimatkhau.close()
        self.dangky_form.show()  # Hiển thị cửa sổ đăng ký

    def open_dangnhap_form(self):
        self.dangnhap_form = QMainWindow()
        self.ui_dangnhap = dangnhap_ext()
        self.ui_dangnhap.setupUi(self.dangnhap_form)
        self.doimatkhau.close()
        self.dangnhap_form.show()
