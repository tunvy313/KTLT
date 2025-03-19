from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QLineEdit
from dangnhap_form import Ui_dangnhap_form
import json

class dangnhap_ext(QMainWindow, Ui_dangnhap_form):
    def setupUi(self, dangnhap_form):
        super().setupUi(dangnhap_form)
        self.dangnhap_window = dangnhap_form

        # Đặt placeholder mặc định
        self.txttendangnhap.setPlaceholderText("Tên đăng nhập")
        self.txtmatkhau.setPlaceholderText("Mật khẩu")

        # Mặc định ẩn mật khẩu
        self.txtmatkhau.setEchoMode(QLineEdit.EchoMode.Password)

        # Kết nối nút đăng nhập với hàm kiểm tra đăng nhập
        self.btndangnhap.clicked.connect(self.dang_nhap)

        # Kết nối nút ẩn mật khẩu
        self.btnan.clicked.connect(self.anhienmatkhau)

        # Kết nối nút hiện mật khẩu
        self.btnhien.clicked.connect(self.anhienmatkhau)

        # Kết nối nút "Quên mật khẩu" với phương thức mở giao diện quên mật khẩu
        self.btnquenmatkhau.clicked.connect(self.mo_quen_mat_khau)

        # Kết nối nút "Đăng ký" mở giao diện đăng ký
        self.btndangky.clicked.connect(self.mo_dang_ky)

    def anhienmatkhau(self):
        """Chuyển đổi trạng thái hiển thị mật khẩu"""
        if self.txtmatkhau.echoMode() == QLineEdit.EchoMode.Password:
            self.txtmatkhau.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btnan.hide()  # Ẩn nút hiện mật khẩu
            self.btnhien.show()  # Hiển thị nút ẩn mật khẩu
        else:
            self.txtmatkhau.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btnhien.hide()  # Ẩn nút ẩn mật khẩu
            self.btnan.show()  # Hiển thị nút hiện mật khẩu

    def dang_nhap(self):
        """Hàm kiểm tra đăng nhập từ file JSON"""
        username = self.txttendangnhap.text().strip()
        password = self.txtmatkhau.text().strip()

        # Kiểm tra nếu tên đăng nhập hoặc mật khẩu bị bỏ trống
        if not username and not password:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập thông tin!")
            return  # Dừng thực thi hàm nếu thông tin chưa đầy đủ

        try:
            with open("thong_tin_dang_ky.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                # Kiểm tra nếu data không phải danh sách, báo lỗi ngay
                if not isinstance(data, list):
                    QMessageBox.critical(self, "Lỗi", "Dữ liệu không hợp lệ!")
                    return

                # Chuẩn hóa dữ liệu: Mở rộng danh sách nếu có danh sách lồng nhau
                users = []
                for item in data:
                    if isinstance(item, list):  # Nếu item là danh sách
                        users.extend(item)
                    elif isinstance(item, dict):  # Nếu item là dictionary
                        users.append(item)

                # Tìm kiếm thông tin người dùng
                user = next(
                    (u for u in users if isinstance(u, dict) and
                     u.get("Tên đăng nhập") == username and u.get("Mật khẩu") == password),
                    None
                )
            if user:
                    QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                    self.open_manhinhchinh_form()
            else:
                    QMessageBox.warning(self, "Lỗi đăng nhập", "Tên đăng nhập hoặc mật khẩu không đúng.")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def open_manhinhchinh_form(self):
            """Mở giao diện màn hình chính"""
            from manhinhchinh_extend import manhinhchinh_ext
            self.manhinhchinh_form = QMainWindow()
            self.ui_manhinhchinh_form = manhinhchinh_ext()
            self.ui_manhinhchinh_form.setupUi(self.manhinhchinh_form)
            self.dangnhap_window.close()  # Đóng màn hình đăng nhập
            self.manhinhchinh_form.show()  # Hiển thị màn hình chính

    def mo_quen_mat_khau(self):
        from quenmatkhau_form import Ui_quenmatkhau_form
        """Chuyển sang giao diện Quên mật khẩu"""
        self.quenmatkhau_window = QtWidgets.QMainWindow()
        self.ui_quenmatkhau = Ui_quenmatkhau_form()
        self.ui_quenmatkhau.setupUi(self.quenmatkhau_window)
        self.quenmatkhau_window.show()
        self.dangnhap_window.close()  # Đóng cửa sổ đăng nhập nếu cần

    def mo_dang_ky(self):
        """Mở cửa sổ đăng ký"""
        from Sign_Up_MainWindow import Ui_MainWindow  # Import giao diện
        # Tạo một cửa sổ mới
        self.Sign_Up_MainWindow = QMainWindow()
        self.ui_sign_up = Ui_MainWindow()  # Khởi tạo giao diện
        self.ui_sign_up.setupUi(self.Sign_Up_MainWindow)  # Gán giao diện vào cửa sổ mới
        self.Sign_Up_MainWindow.show()  # Hiển thị cửa sổ đăng ký
        self.dangnhap_window.close()



