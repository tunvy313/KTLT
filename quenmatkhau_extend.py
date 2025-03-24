import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from quenmatkhau_form import Ui_quenmatkhau_form
import json
import random
from dangky_extend import dangky_ext
from dangnhap_extend import dangnhap_ext
from doimatkhau_extend import doimatkhau_ext

class quenmatkhau_ext(Ui_quenmatkhau_form):
    def setupUi(self, quenmatkhau_form):
        super().setupUi(quenmatkhau_form)
        self.quenmatkhau = quenmatkhau_form

        # Biến lưu mã OTP hiện tại
        self.current_otp = None
        self.otp_sent = False  # Biến kiểm tra OTP có được gửi chưa
        self.email_xac_nhan = ""  # Lưu email hợp lệ

        # Kết nối sự kiện của các nút
        self.btnnhanmaotp.clicked.connect(self.nhan_ma_otp)
        self.btntieptuc.clicked.connect(self.kiem_tra_thong_tin)
        self.btn_return.clicked.connect(self.back_to_dangnhap_form)
        self.btndangky.clicked.connect(self.back_to_dangky)

    def doc_du_lieu(self):
        """Đọc dữ liệu từ file JSON và trả về danh sách người dùng"""
        try:
            with open("data/thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            QMessageBox.critical(self.quenmatkhau, "Lỗi", "Không thể đọc dữ liệu!")
            return []

    def kiem_tra_email_hop_le(self, email):
        """Kiểm tra email có tồn tại trong file dữ liệu không"""
        users = self.doc_du_lieu()
        return any(user.get("Email") == email for user in users)

    def nhan_ma_otp(self):
        """Gửi OTP nếu email hợp lệ"""
        email_nhap = self.txtemail.text().strip()
        if not email_nhap:
            QMessageBox.warning(self.quenmatkhau, "Cảnh báo", "Vui lòng nhập email!")
            return

        if not self.kiem_tra_email_hop_le(email_nhap):
            QMessageBox.warning(self.quenmatkhau, "Lỗi", "Email không tồn tại!")
            return

        self.current_otp = str(random.randint(100000, 999999))
        self.otp_sent = True
        self.email_xac_nhan = email_nhap

        QMessageBox.information(self.quenmatkhau, "OTP", f"Mã OTP của bạn là: {self.current_otp}")


    def kiem_tra_thong_tin(self):
        otp_nhap = self.txtnhapmaotp.text().strip()
        # email_nhap = self.txtemail.text().strip()
        if not self.email_xac_nhan:
            QMessageBox.warning(self.quenmatkhau, "Cảnh báo", "Vui lòng nhập email!")
            return

        if not otp_nhap:
            QMessageBox.warning(self.quenmatkhau, "Cảnh báo", "Vui lòng nhập mã OTP!")
            return
        # Kiểm tra nếu OTP sai
        if otp_nhap != self.current_otp:
            QMessageBox.warning(self.quenmatkhau, "Lỗi", "Mã OTP không chính xác!")
            return

        self.open_doi_mat_khau()

    def open_doi_mat_khau(self):
        self.doimatkhau_form = QMainWindow()
        self.ui_doimatkhau = doimatkhau_ext()
        self.ui_doimatkhau.setupUi(self.doimatkhau_form)
        self.ui_doimatkhau.set_email(self.email_xac_nhan)
        self.quenmatkhau.close()
        self.doimatkhau_form.show()

    def back_to_dangnhap_form(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.dangnhap_form = QMainWindow()
        self.ui_dangnhap = dangnhap_ext()
        self.ui_dangnhap.setupUi(self.dangnhap_form)
        self.quenmatkhau.close()
        self.dangnhap_form.show()

    def back_to_dangky(self):
        """Trở về cửa sổ đăng ký"""
        # Tạo một cửa sổ mới
        self.dangky_form = QMainWindow()
        self.ui_dangky = dangky_ext()
        self.ui_dangky.setupUi(self.dangky_form)
        self.quenmatkhau.close()  # Đóng cửa sổ hiện tại
        self.dangky_form.show()  # Hiển thị cửa sổ đăng ký
