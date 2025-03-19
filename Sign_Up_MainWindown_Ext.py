import json
import os
from operator import truediv
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QMainWindow
from Sign_Up_MainWindow import Ui_MainWindow

class Ui_MainWindow_Ext(QMainWindow, Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.txtTen.setPlaceholderText("Nguyễn Văn A")
        self.txtemail.setPlaceholderText("abc@gmail.com")
        self.txtNgaySinh.setCalendarPopup(True)
        # chỉnh ngày sinh mờ khi đăng nhập
        self.txttendangnhap.setPlaceholderText("abc123@")
        self.txtMatKhau.setPlaceholderText("*********")
        self.txtNhapLaiMatKhau.setPlaceholderText("*********")
        self.btnDangKy.clicked.connect(self.dang_ky)
        self.btnHienMatKhau.clicked.connect(self.hienmatkhau)
        self.btnHienMatKhau_2.clicked.connect(self.hienlaimatkhau)
        self.btnquaylai.clicked.connect(self.dangnhap_form)

    def hienmatkhau(self):
        """Hiện/Ẩn mật khẩu cũ"""
        if self.txtMatKhau.echoMode() == QLineEdit.EchoMode.Password:
            self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Normal) # Hiển mật khẩu
        else:
            self.txtMatKhau.setEchoMode(QLineEdit.EchoMode.Password) # Ẩn lại mật khẩu

    def hienlaimatkhau(self):
        """Hiện/Ẩn mật khẩu mới"""
        if self.txtNhapLaiMatKhau.echoMode() == QLineEdit.EchoMode.Password:
            self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.txtNhapLaiMatKhau.setEchoMode(QLineEdit.EchoMode.Password)

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
        email=self.txtemail
        ten_dang_nhap=self.txttendangnhap
        mat_khau=self.txtMatKhau
        thong_tin_dang_ky=[{
            "Họ và tên": ten.text(),
            "Ngày tháng năm sinh": ngay_sinh.text(),
            "Email": email.text(),
            "Tên đăng nhập": ten_dang_nhap.text(),
            "Mật khẩu": mat_khau.text()
        }]
        self.append_to_json_file("data/thong_tin_dang_ky.json",thong_tin_dang_ky)

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
        if self.txtemail.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền mail")
            return False
        elif self.txtemail.text().count("@")>1 or self.txtemail.text().count("@")==0 or self.txtemail.text().count(".")==0:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Email không hợp lệ")
            return False
        return True
        #kiểm tra email có tồn tại hong nữa
    def kiem_tra_ten_dang_nhap(self):
        if self.txttendangnhap.text() == " ":
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Hãy điền tên đăng nhập")
            return False
        elif len(self.txttendangnhap.text()) > 10:
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

    def dangnhap_form(self):
        """Hàm quay lại giao diện đăng nhập khi nhấn nút"""
        from dangnhap_extend import dangnhap_ext  # Đảm bảo import class mở rộng nếu cần
        # Tạo cửa sổ mới cho đăng nhập
        self.dangnhap_window = QMainWindow()
        self.ui_dangnhap_form = dangnhap_ext()  # Nếu `dangnhap_ext` đã kế thừa `QMainWindow`, không cần gọi `setupUi`
        self.ui_dangnhap_form.setupUi(self.dangnhap_window)  # Nếu cần setup UI (chỉ khi không kế thừa QMainWindow)
        self.dangnhap_window.show()
        self.MainWindow.close()

