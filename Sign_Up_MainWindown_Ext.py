import json
import os
from operator import truediv

from PyQt6.QtWidgets import QMessageBox, QLineEdit

from Sign_Up_MainWindow import Ui_MainWindow
class Ui_MainWindow_Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.txtTen.setPlaceholderText("Nguyễn Văn A")
        self.txtEmail.setPlaceholderText("abc@gmail.com")
        self.txtNgaySinh.setCalendarPopup(True)
        # chỉnh ngày sinh mờ khi đăng nhập
        self.txtTenDangNhap.setPlaceholderText("abc123@")
        self.txtMatKhau.setPlaceholderText("*********")
        self.txtNhapLaiMatKhau.setPlaceholderText("*********")
        self.btnDangKy.clicked.connect(self.dang_ky)
        self.btnAnMatKhau.setEnabled(False)
        self.btnAnMatKhau_4.setEnabled(False)
        self.btnHienMatKhau.clicked.connect(self.hien_mat_khau)
        self.btnAnMatKhau.clicked.connect(self.an_mat_khau)
        self.btnHienMatKhau_2.clicked.connect(self.hien_mat_khau_2)
        self.btnAnMatKhau_4.clicked.connect(self.an_mat_khau_2)

    def hien_mat_khau(self):
        self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        self.btnHienMatKhau.setVisible(False)
        self.btnHienMatKhau.setEnabled(False)
        self.btnAnMatKhau.setVisible(True)
        self.btnAnMatKhau.setEnabled(True)

    def an_mat_khau(self):
        self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnAnMatKhau.setVisible(False)
        self.btnAnMatKhau.setEnabled(False)
        self.btnHienMatKhau.setVisible(True)
        self.btnHienMatKhau.setEnabled(True)

    def hien_mat_khau_2(self):
        self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        self.btnHienMatKhau_2.setVisible(False)
        self.btnHienMatKhau_2.setEnabled(False)
        self.btnAnMatKhau_4.setVisible(True)
        self.btnAnMatKhau_4.setEnabled(True)


    def an_mat_khau_2(self):
        self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnAnMatKhau_4.setVisible(False)
        self.btnAnMatKhau_4.setEnabled(False)
        self.btnHienMatKhau_2.setVisible(True)
        self.btnHienMatKhau_2.setEnabled(True)

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
        ten=self.txtTen
        ngay_sinh=self.txtNgaySinh
        email=self.txtEmail
        ten_dang_nhap=self.txtTenDangNhap
        mat_khau=self.txtMatKhau
        thong_tin_dang_ký=[{
            "Họ và tên": ten.text(),
            "Ngày tháng năm sinh": ngay_sinh.text(),
            "Email": email.text(),
            "Tên đăng nhập": ten_dang_nhap.text(),
            "Mật khẩu": mat_khau.text()
        }]
        self.append_to_json_file("data/thong_tin_dang_ky.json",thong_tin_dang_ký)

    def dang_ky (self):
        thong_tin_hop_le = self.kiem_tra_ten() and self.kiem_tra_email() and self.kiem_tra_ten_dang_nhap() and self.kiem_tra_mat_khau() and self.kiem_tra_nhap_lai_mat_khau() and self.kiem_tra_ngay_sinh()

        if thong_tin_hop_le:
        # self.btnDangKy.setEnabled(thong_tin_hop_le)
            QMessageBox.information(self.MainWindow, "Thông báo", "Đăng kí thành công")
            self.luu_thong_tin_dang_ky()
        else:
            self.kiem_tra_ten()
            self.kiem_tra_email()
            self.kiem_tra_ten_dang_nhap()
            self.kiem_tra_mat_khau()
            self.kiem_tra_nhap_lai_mat_khau()
            self.kiem_tra_ngay_sinh()


    def kiem_tra_ten(self):
        if self.txtTen.text() == "":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền tên")
            return False
        return True
    def kiem_tra_ngay_sinh(self):
        if self.txtNgaySinh.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo","Hãy điền ngày sinh")
            return False
        return True
    def kiem_tra_email(self):
        if self.txtEmail.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền mail")
            return False
        elif self.txtEmail.text().count("@")>1 or self.txtEmail.text().count("@")==0 or self.txtEmail.text().count(".")==0:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Email không hợp lệ")
            return False
        return True
        #kiểm tra email có tồn tại hong nữa
    def kiem_tra_ten_dang_nhap(self):
        if self.txtTenDangNhap.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền tên đăng nhập")
            return False
        elif len(self.txtTenDangNhap.text()) > 10:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Tên đăng nhập phải ít hơn 10 kí tự")
            return False
        return True
    def kiem_tra_mat_khau(self):
        if self.txtMatKhau.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền tên mật khẩu")
            return False
        return True
    def kiem_tra_nhap_lai_mat_khau(self):
        if self.txtNhapLaiMatKhau.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền lại mật khẩu")
            return False
        if self.txtNhapLaiMatKhau.text() != self.txtMatKhau.text():
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Mật khẩu không trùng khớp. Hãy nhập lại")
            return False
        return True
