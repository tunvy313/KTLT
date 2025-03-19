from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit
from doimatkhau_form import Ui_doimatkhau_form
from quenmatkhau_extend import quenmatkhau_ext
import os
import json

class doimatkhau_ext(QMainWindow, Ui_doimatkhau_form):
    def setupUi(self, doimatkhau_form):
        super().setupUi(doimatkhau_form)
        self.doimatkhau_window = doimatkhau_form
        # Kết nối sự kiện nút "Đổi mật khẩu"
        self.btndoimatkhau.clicked.connect(self.doi_mat_khau)
        self.btnanmatkhaucu.clicked.connect(self.anhienmatkhaucu)
        self.btnanmatkhaumoi.clicked.connect(self.anhienmatkhaumoi)
        self.btnhienmatkhaucu.clicked.connect(self.anhienmatkhaucu)
        self.btnhienmatkhaumoi.clicked.connect(self.anhienmatkhaumoi)
        self.btn_return.clicked.connect(self.back_to_quenmatkhau_form)
        self.btndangky.clicked.connect(self.back_to_dangky)

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
        ten_dang_nhap = "linhchi"  # Giả định đang đăng nhập với tài khoản này
        mat_khau_moi = self.txtmatkhaumoi.text().strip()
        nhap_lai_mat_khau = self.txtnhaplaimatkhaumoi.text().strip()

        # Kiểm tra mật khẩu mới có trùng nhau không
        if not mat_khau_moi or not nhap_lai_mat_khau:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu không được để trống!")
            return

        if mat_khau_moi != nhap_lai_mat_khau:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu mới không khớp!")
            return

        try:
            if not os.path.exists("thong_tin_dang_ky.json"):
                QMessageBox.warning(self, "Lỗi", "Không tìm thấy file dữ liệu!")
                return

            # Đọc dữ liệu từ file JSON
            with open("thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            # Tìm người dùng và cập nhật mật khẩu
            user_found = False
            for user in data:
                if user["Tên đăng nhập"] == ten_dang_nhap:
                    user["Mật khẩu"] = mat_khau_moi
                    user_found = True
                    break

            if not user_found:
                QMessageBox.warning(self, "Lỗi", "Không tìm thấy tài khoản!")
                return

            # Ghi dữ liệu đã cập nhật vào file JSON
            with open("thong_tin_dang_ky.json.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            QMessageBox.information(self, "Thành công", "Mật khẩu đã được đổi thành công!")
            self.txtmatkhaumoi.clear()
            self.txtnhaplaimatkhaumoi.clear()

        except json.JSONDecodeError:
            QMessageBox.critical(self, "Lỗi", "File dữ liệu bị lỗi, vui lòng kiểm tra lại!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Có lỗi xảy ra: {str(e)}")

    def back_to_quenmatkhau_form(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.quenmatkhau_form = QMainWindow()
        self.ui_quenmatkhau_form = quenmatkhau_ext()
        self.ui_quenmatkhau_form.setupUi(self.quenmatkhau_form)

        self.doimatkhau_window.close()  # Đóng màn hình câu hỏi thường gặp
        self.quenmatkhau_form.show()  # Hiển thị màn hình giao diện hỗ trợ

    def back_to_dangky(self):
        """Trở về cửa sổ đăng ký"""
        from Sign_Up_MainWindow import Ui_MainWindow  # Import giao diện
        # Tạo một cửa sổ mới
        self.Sign_Up_MainWindow = QMainWindow()
        self.ui_sign_up = Ui_MainWindow()  # Khởi tạo giao diện
        self.ui_sign_up.setupUi(self.Sign_Up_MainWindow)  # Gán giao diện vào cửa sổ mới
        self.Sign_Up_MainWindow.show()  # Hiển thị cửa sổ đăng ký
        self.doimatkhau_window.close()
