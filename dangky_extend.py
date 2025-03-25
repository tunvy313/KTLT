import json
import os
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QMainWindow
from PyQt6.QtCore import QDate
from dangky_form import Ui_dangky_form

class dangky_ext(Ui_dangky_form):
    def setupUi(self, dangky_form):
        super().setupUi(dangky_form)
        self.dangky = dangky_form

        self.txtNgaySinh.setDate(QDate.currentDate())

        self.txtTen.setPlaceholderText("Nguyễn Văn A")
        self.txtEmail.setPlaceholderText("abc@gmail.com")
        self.txtNgaySinh.setCalendarPopup(True)

        # chỉnh ngày sinh mờ khi đăng nhập
        self.txtTenDangNhap.setPlaceholderText("abc123@")
        self.txtMatKhau.setPlaceholderText("*********")
        self.txtNhapLaiMatKhau.setPlaceholderText("*********")
        self.btnAnMatKhau.setEnabled(False)
        self.btnAnMatKhau_2.setEnabled(False)

        self.btnDangKy.clicked.connect(self.dang_ky)
        self.btnquaylai.clicked.connect(self.open_dangnhap_form)
        self.btnHienMatKhau_3.clicked.connect(self.hien_mat_khau)
        self.btnAnMatKhau.clicked.connect(self.an_mat_khau)
        self.btnHienMatKhau_4.clicked.connect(self.hien_mat_khau_2)
        self.btnAnMatKhau_2.clicked.connect(self.an_mat_khau_2)

    def hien_mat_khau(self):
        self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        self.btnHienMatKhau_3.setVisible(False)
        self.btnHienMatKhau_3.setEnabled(False)
        self.btnAnMatKhau.setVisible(True)
        self.btnAnMatKhau.setEnabled(True)

    def an_mat_khau(self):
        self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnAnMatKhau.setVisible(False)
        self.btnAnMatKhau.setEnabled(False)
        self.btnHienMatKhau_3.setVisible(True)
        self.btnHienMatKhau_3.setEnabled(True)

    def hien_mat_khau_2(self):
        self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        self.btnHienMatKhau_4.setVisible(False)
        self.btnHienMatKhau_4.setEnabled(False)
        self.btnAnMatKhau_2.setVisible(True)
        self.btnAnMatKhau_2.setEnabled(True)

    def an_mat_khau_2(self):
        self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnAnMatKhau_2.setVisible(False)
        self.btnAnMatKhau_2.setEnabled(False)
        self.btnHienMatKhau_4.setVisible(True)
        self.btnHienMatKhau_4.setEnabled(True)

    @staticmethod
    def append_to_json_file(f_path, new_data):
        with open(f_path, "r+", encoding="utf8") as file:
            file.seek(0, os.SEEK_END)
            cursor_position = file.tell()
            if cursor_position > 2:
                file.seek(cursor_position - 1)
                file.write(", \n" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")
            else:
                file.write("[" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")

    def luu_thong_tin_dang_ky(self):
        ten = self.txtTen
        ngay_sinh = self.txtNgaySinh
        email = self.txtEmail
        ten_dang_nhap = self.txtTenDangNhap
        mat_khau = self.txtMatKhau
        thong_tin_dang_ky={
            "Họ và tên": ten.text().strip(),
            "Ngày tháng năm sinh": ngay_sinh.text(),
            "Email": email.text().strip(),
            "Tên đăng nhập": ten_dang_nhap.text().strip(),
            "Mật khẩu": mat_khau.text().strip()
        }
        self.append_to_json_file("data/thong_tin_dang_ky.json",thong_tin_dang_ky)

    def dang_ky(self):
        thong_tin_hop_le = self.kiem_tra_ten() and self.kiem_tra_email() and self.kiem_tra_ten_dang_nhap() and self.kiem_tra_mat_khau() and self.kiem_tra_nhap_lai_mat_khau() and self.kiem_tra_ngay_sinh()

        if thong_tin_hop_le:
            QMessageBox.information(self.dangky, "Thông báo", "Đăng kí thành công!")
            self.luu_thong_tin_dang_ky()
            self.luu_thong_tin_dang_nhap(self.txtTenDangNhap.text().strip(), self.txtMatKhau.text().strip())
            self.open_manhinhchinh_form()
        else:
            QMessageBox.warning(self.dangky, "Cảnh báo", "Vui lòng nhập đủ thông tin!")

    def kiem_tra_ten(self):
        if self.txtTen.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo", "Hãy điền tên!")
            return False
        return True

    def kiem_tra_ngay_sinh(self):
        if self.txtNgaySinh.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo","Hãy điền ngày sinh!")
            return False
        return True

    def kiem_tra_email(self):
        if self.txtEmail.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo", "Hãy điền email!")
            return False
        elif self.txtEmail.text().count("@")>1 or self.txtEmail.text().count("@")==0 or self.txtEmail.text().count(".")==0:
            QMessageBox.warning(self.dangky, "Cảnh báo", "Email không hợp lệ!")
            return False
        return True
        #kiểm tra email có tồn tại hong nữa

    def kiem_tra_ten_dang_nhap(self):
        if self.txtTenDangNhap.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo", "Hãy điền tên đăng nhập!")
            return False
        elif len(self.txtTenDangNhap.text()) > 10:
            QMessageBox.warning(self.dangky, "Cảnh báo", "Tên đăng nhập phải ít hơn 10 kí tự!")
            return False
        return True

    def kiem_tra_mat_khau(self):
        if self.txtMatKhau.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo", "Hãy điền mật khẩu!")
            return False
        return True

    def kiem_tra_nhap_lai_mat_khau(self):
        if self.txtNhapLaiMatKhau.text() == "":
            QMessageBox.warning(self.dangky, "Cảnh báo", "Hãy điền lại mật khẩu!")
            return False
        if self.txtNhapLaiMatKhau.text() != self.txtMatKhau.text():
            QMessageBox.warning(self.dangky, "Cảnh báo", "Mật khẩu không trùng khớp. Hãy nhập lại!")
            return False
        return True

    def luu_thong_tin_dang_nhap(self, ten, mat_khau):
        user_data = {"Tên đăng nhập": ten, "Mật khẩu": mat_khau}
        try:
            with open("data/thong_tin_dang_nhap.json", "w", encoding="utf-8") as file:
                json.dump(user_data, file, ensure_ascii=False, indent=4)
        except Exception:
            QMessageBox.critical(self.dangky, "Lỗi", "Đã xảy ra lỗi khi lưu thông tin.")

    def open_dangnhap_form(self):
        from dangnhap_extend import dangnhap_ext
        self.dangnhap_form = QMainWindow()
        self.ui_dangnhap = dangnhap_ext()
        self.ui_dangnhap.setupUi(self.dangnhap_form)
        self.dangky.close()
        self.dangnhap_form.show()

    def open_manhinhchinh_form(self):
        from manhinhchinh_extend import manhinhchinh_ext
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.dangky.close()
        self.manhinhchinh_form.show()