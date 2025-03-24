import json
import os

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from cddoimk_form import Ui_cddoimk_form
from caidat_extend import caidat_ext

class cddoimk_ext(Ui_cddoimk_form):
    PATH = "data/thong_tin_dang_ky.json"
    LOGIN_PATH = "data/thong_tin_dang_nhap.json"
    def setupUi(self, cddoimk_form):
        super().setupUi(cddoimk_form)
        self.cddoimk = cddoimk_form

        self.txt_mkcu.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_mkmoi.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_nhaplaimk.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_hienmk.hide()
        self.btn_hienmk_2.hide()
        self.btn_hienmk_3.hide()

        # Connect events
        self.btn_luu.clicked.connect(self.process_doimk)
        self.btn_huybo.clicked.connect(self.process_quaylai)
        self.btn_return.clicked.connect(self.process_quaylai)

        self.btn_anmk.clicked.connect(self.anhienmatkhau)
        self.btn_hienmk.clicked.connect(self.anhienmatkhau)
        self.btn_anmk_2.clicked.connect(self.anhienmatkhau2)
        self.btn_hienmk_2.clicked.connect(self.anhienmatkhau2)
        self.btn_anmk_3.clicked.connect(self.anhienmatkhau3)
        self.btn_hienmk_3.clicked.connect(self.anhienmatkhau3)

    def anhienmatkhau(self):
        """Ẩn/hiện mật khẩu khi bấm nút"""
        if self.txt_mkcu.echoMode() == QLineEdit.EchoMode.Password:
            self.txt_mkcu.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btn_anmk.hide()  # Ẩn nút "ẩn mật khẩu"
            self.btn_hienmk.show()  # Hiện nút "hiện mật khẩu"
        else:
            self.txt_mkcu.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btn_hienmk.hide()  # Ẩn nút "hiện mật khẩu"
            self.btn_anmk.show()  # Hiện nút "ẩn mật khẩu"

    def anhienmatkhau2(self):
        """Ẩn/hiện mật khẩu khi bấm nút"""
        if self.txt_mkmoi.echoMode() == QLineEdit.EchoMode.Password:
            self.txt_mkmoi.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btn_anmk_2.hide()  # Ẩn nút "ẩn mật khẩu"
            self.btn_hienmk_2.show()  # Hiện nút "hiện mật khẩu"
        else:
            self.txt_mkmoi.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btn_hienmk_2.hide()  # Ẩn nút "hiện mật khẩu"
            self.btn_anmk_2.show()  # Hiện nút "ẩn mật khẩu"

    def anhienmatkhau3(self):
        """Ẩn/hiện mật khẩu khi bấm nút"""
        if self.txt_nhaplaimk.echoMode() == QLineEdit.EchoMode.Password:
            self.txt_nhaplaimk.setEchoMode(QLineEdit.EchoMode.Normal)  # Hiện mật khẩu
            self.btn_anmk_3.hide()  # Ẩn nút "ẩn mật khẩu"
            self.btn_hienmk_3.show()  # Hiện nút "hiện mật khẩu"
        else:
            self.txt_nhaplaimk.setEchoMode(QLineEdit.EchoMode.Password)  # Ẩn mật khẩu
            self.btn_hienmk_3.hide()  # Ẩn nút "hiện mật khẩu"
            self.btn_anmk_3.show()  # Hiện nút "ẩn mật khẩu"

    def thong_tin_dang_nhap(self):
        """Lấy tên đăng nhập của người dùng hiện tại"""
        if os.path.exists(self.LOGIN_PATH):
            with open(self.LOGIN_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("Tên đăng nhập", None)
        return None

    def process_doimk(self):
        """Xử lý đổi mật khẩu"""
        mkht = self.txt_mkcu.text().strip()
        mkm = self.txt_mkmoi.text().strip()
        mkm2 = self.txt_nhaplaimk.text().strip()
        ten_dang_nhap = self.thong_tin_dang_nhap()

        if not ten_dang_nhap:
            QMessageBox.warning(self.cddoimk, "Lỗi", "Không tìm thấy thông tin đăng nhập!")
            return

        if not mkht or not mkm or not mkm2:
            QMessageBox.warning(self.cddoimk, "Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
            return
        if mkm == mkht:
            QMessageBox.warning(self.cddoimk, "Cảnh báo", "Mật khẩu mới không được trùng với mật khẩu hiện tại!")
            return
        if mkm2 != mkm:
            QMessageBox.warning(self.cddoimk, "Lỗi", "Mật khẩu xác nhận không trùng khớp!")
            return

        if not os.path.exists(self.PATH):
            QMessageBox.warning(self.cddoimk, "Lỗi", "Không tìm thấy dữ liệu người dùng!")
            return

        try:
            with open(self.PATH, "r", encoding="utf-8") as file:
                data =  json.load(file)

            user_found = False
            for user in data:
                if user["Tên đăng nhập"] == ten_dang_nhap:
                    user_found = True
                    if user["Mật khẩu"] != mkht:
                        QMessageBox.warning(self.cddoimk, "Lỗi", "Mật khẩu cũ không đúng, vui lòng nhập lại!")
                        return
                    else:
                        user["Mật khẩu"] = mkm
                        break

            if not user_found:
                QMessageBox.warning(self.cddoimk, "Lỗi", "Không tìm thấy tài khoản!")
                return

            with open(self.PATH, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            # Cập nhật mật khẩu trong thong_tin_dang_nhap.json
            if os.path.exists(self.LOGIN_PATH):
                with open(self.LOGIN_PATH, "r", encoding="utf-8") as file:
                    login_data = json.load(file)

                login_data["Mật khẩu"] = mkm  # Cập nhật mật khẩu mới

                with open(self.LOGIN_PATH, "w", encoding="utf-8") as file:
                    json.dump(login_data, file, ensure_ascii=False, indent=2)

            QMessageBox.information(self.cddoimk, "Thông báo", "Đổi mật khẩu thành công!")
            self.txt_mkcu.clear()
            self.txt_mkmoi.clear()
            self.txt_nhaplaimk.clear()
            self.process_quaylai()

        except json.JSONDecodeError:
            QMessageBox.critical(self.cddoimk, "Lỗi", "Lỗi dữ liệu người dùng!")


    def process_quaylai(self):
        # Quay lại màn hình cài đặt
        self.caidat_form = QMainWindow()
        self.ui_caidat = caidat_ext()
        self.ui_caidat.setupUi(self.caidat_form)

        self.cddoimk.close()  # Đóng cửa sổ hiện tại
        self.caidat_form.show()  # Hiển thị màn hình cài đặt