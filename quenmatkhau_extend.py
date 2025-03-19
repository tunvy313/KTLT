from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from quenmatkhau_form import Ui_quenmatkhau_form
from dangnhap_extend import dangnhap_ext
import json
import random

class quenmatkhau_ext(QMainWindow, Ui_quenmatkhau_form):
    def setupUi(self, quenmatkhau_form):
        super().setupUi(quenmatkhau_form)
        self.quenmatkhau_window = quenmatkhau_form

        # Biến lưu mã OTP hiện tại
        self.current_otp = None
        self.otp_sent = False  # Biến kiểm tra OTP có được gửi chưa

        # Kết nối sự kiện của các nút
        self.btnnhanmaotp.clicked.connect(self.nhan_ma_otp)
        self.btntieptuc.clicked.connect(self.mo_doi_mat_khau)
        self.btn_return.clicked.connect(self.back_to_dangnhap_form)
        self.btndangky.clicked.connect(self.back_to_dangky)


    # def doc_du_lieu(self):
    #     """Đọc dữ liệu từ file JSON và trả về danh sách người dùng"""
    #     try:
    #         with open("thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
    #             data = json.load(file)
    #             # Nếu JSON lưu dưới dạng dictionary, chuyển sang list
    #             if isinstance(data, dict):
    #                 data = list(data.values())
    #
    #             if not isinstance(data, list):
    #                 QMessageBox.critical(self, "Lỗi", "Dữ liệu không hợp lệ!")
    #                 return []
    #             return data
    #     except Exception as e:
    #         QMessageBox.critical(self, "Lỗi", f"Không thể đọc dữ liệu: {str(e)}")
    #         return []
    def doc_du_lieu(self):
        """Đọc dữ liệu từ file JSON và trả về danh sách người dùng"""
        try:
            with open("thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                # Làm phẳng danh sách lồng nhau
                users = []
                for sublist in data:
                    if isinstance(sublist, list):
                        users.extend(sublist)  # Nối tất cả người dùng vào danh sách chính
                    else:
                        users.append(sublist)

                return users
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể đọc dữ liệu: {str(e)}")
            return []

    def kiem_tra_email_hop_le(self, email):
        """Kiểm tra email có tồn tại trong dữ liệu không"""
        # return any(user["Email"] == email for user in self.doc_du_lieu())
        """Kiểm tra email có tồn tại trong dữ liệu không"""
        users = self.doc_du_lieu()
        return any(user.get("Email") == email for user in users)

    def nhan_ma_otp(self):
        """Gửi OTP nếu email hợp lệ"""
        email_nhap = self.txtemail.text().strip()

        if not email_nhap:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập email!")
            return

        if not self.kiem_tra_email_hop_le(email_nhap):
            QMessageBox.warning(self, "Lỗi", "Email không hợp lệ!")
            return

        self.current_otp = str(random.randint(100000, 999999))
        self.otp_sent = True

        if self.otp_sent:
            QMessageBox.information(self, "OTP", f"Mã OTP của bạn là: {self.current_otp}")
            return

    def mo_doi_mat_khau(self):
        otp_nhap = self.txtnhapmaotp.text().strip()
        email_nhap = self.txtemail.text().strip()

        if not email_nhap:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập email!")
            return
        # Kiểm tra nếu OTP chưa nhập
        if not otp_nhap:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập mã OTP!")
            return
        # Kiểm tra nếu OTP sai
        if otp_nhap != self.current_otp:
            QMessageBox.warning(self, "Lỗi", "Mã OTP không chính xác!")
            return

        from doimatkhau_form import Ui_doimatkhau_form
        self.doimatkhau_window = QtWidgets.QMainWindow()
        self.ui_doimatkhau = Ui_doimatkhau_form()
        self.ui_doimatkhau.setupUi(self.doimatkhau_window)
        self.doimatkhau_window.show()
        self.quenmatkhau_window.close()

    def back_to_dangnhap_form(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.dangnhap_form = QMainWindow()
        self.ui_dangnhap_form = dangnhap_ext()
        self.ui_dangnhap_form.setupUi(self.dangnhap_form)
        self.quenmatkhau_window.close()
        self.dangnhap_form.show()

    def back_to_dangky(self):
        """Trở về cửa sổ đăng ký"""
        from Sign_Up_MainWindow import Ui_MainWindow  # Import giao diện
        # Tạo một cửa sổ mới
        self.Sign_Up_MainWindow = QMainWindow()
        self.ui_sign_up = Ui_MainWindow()  # Khởi tạo giao diện
        self.ui_sign_up.setupUi(self.Sign_Up_MainWindow)  # Gán giao diện vào cửa sổ mới
        self.Sign_Up_MainWindow.show()  # Hiển thị cửa sổ đăng ký
        self.quenmatkhau_window.close()