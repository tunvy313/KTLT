import os
import requests
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QCompleter, QMessageBox
from lienkettkmoi_form import Ui_lienkettkmoi_form
from vilienket_extend import vilienket_ext

class lienkettkmoi_ext(Ui_lienkettkmoi_form):
    API_URL = "https://67df85a27635238f9aa9c5c4.mockapi.io/accounts"
    PATH = "data/thong_tin_lien_ket.json"

    def setupUi(self, lienkettkmoi_form):
        super().setupUi(lienkettkmoi_form)
        self.lienkettkmoi = lienkettkmoi_form

        # Lấy danh sách ngân hàng từ API
        self.danh_sach_ngan_hang = self.lay_danh_sach_ngan_hang()
        self.completer = QCompleter(self.danh_sach_ngan_hang)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.txt_timnh.setCompleter(self.completer)

        # Kết nối sự kiện Enter
        self.txt_timnh.returnPressed.connect(self.kiem_tra_ngan_hang)

        # Khóa phần nhập số tài khoản và tên chủ tài khoản ban đầu
        self.khoa_nhap_thong_tin(False)

        # Connect events
        self.btn_lienket.clicked.connect(self.process_lienket)
        self.btn_huy.clicked.connect(self.process_huybo)
        self.btn_return.clicked.connect(self.process_quaylai)

    def lay_danh_sach_ngan_hang(self):
        """Lấy danh sách ngân hàng từ API"""
        try:
            response = requests.get(self.API_URL)
            if response.status_code == 200:
                data = response.json()
                return list(set(item["bank_name"] for item in data))  # Lọc danh sách ngân hàng duy nhất
            else:
                QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Không thể lấy danh sách ngân hàng từ API!")
                return []
        except requests.exceptions.RequestException:
            QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Lỗi kết nối!")
            return []

    def kiem_tra_ngan_hang(self):
        """Kiểm tra ngân hàng có trong danh sách API không"""
        ten_ngan_hang_nhap = self.txt_timnh.text().strip().lower()

        # Chuẩn hóa danh sách ngân hàng về chữ thường để so sánh
        mapping_ngan_hang = {nh.lower(): nh for nh in self.danh_sach_ngan_hang}  # Chuyển thành dict

        if ten_ngan_hang_nhap in mapping_ngan_hang:
            self.ten_ngan_hang_chuan = mapping_ngan_hang[ten_ngan_hang_nhap]
            self.khoa_nhap_thong_tin(True)
            self.txt_stk.setFocus()
        else:
            QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Ngân hàng không tồn tại hoặc chưa tích hợp với ứng dụng.")
            self.txt_timnh.clear()
            self.txt_timnh.setFocus()
            self.khoa_nhap_thong_tin(False)

    def khoa_nhap_thong_tin(self, trang_thai: bool):
        """Bật/tắt phần nhập thông tin tài khoản"""
        self.txt_stk.setEnabled(trang_thai)
        self.txt_ten.setEnabled(trang_thai)

    def process_lienket(self):
        so_tai_khoan = self.txt_stk.text().strip()
        chu_tai_khoan = self.txt_ten.text().strip()

        if not hasattr(self, 'ten_ngan_hang_chuan'):
            QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Ngân hàng chưa được xác thực!")
            return

        ten_ngan_hang = self.ten_ngan_hang_chuan  # Sử dụng tên chuẩn từ API

        if not so_tai_khoan or not chu_tai_khoan:
            QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            response = requests.get(self.API_URL)
            if response.status_code == 200:
                danh_sach_tai_khoan = response.json()
                tai_khoan_hop_le = next(
                    (acc for acc in danh_sach_tai_khoan if acc["bank_name"] == ten_ngan_hang
                     and acc["account_number"] == so_tai_khoan
                     and acc["owner"] == chu_tai_khoan), None
                )

                if tai_khoan_hop_le:
                    QMessageBox.information(self.lienkettkmoi, "Thành công", "Liên kết tài khoản ngân hàng thành công!")
                    self.luu_tai_khoan_lien_ket(ten_ngan_hang, so_tai_khoan, chu_tai_khoan)
                    self.process_quaylai()
                else:
                    QMessageBox.warning(self.lienkettkmoi, "Lỗi", "Tài khoản không hợp lệ. Vui lòng kiểm tra lại.")
            else:
                QMessageBox.critical(self.lienkettkmoi, "Lỗi", "Không thể kiểm tra tài khoản từ API.")
        except requests.exceptions.RequestException:
            QMessageBox.critical(self.lienkettkmoi, "Lỗi", "Lỗi kết nối!")

    def luu_tai_khoan_lien_ket(self, ten_ngan_hang, so_tai_khoan, chu_tai_khoan):
        """Lưu thông tin liên kết tài khoản vào file JSON"""
        du_lieu = {
            "Tên ngân hàng": ten_ngan_hang,
            "Số thẻ/tài khoản": so_tai_khoan,
            "Tên chủ thẻ/tài khoản": chu_tai_khoan,
            "Trạng thái": "Đang mở khóa"
        }

        if os.path.exists(self.PATH):
            with open(self.PATH, "r", encoding="utf-8") as file:
                try:
                    danh_sach = json.load(file)
                    if not isinstance(danh_sach, list):
                        danh_sach = []
                except json.JSONDecodeError:
                    danh_sach = []
        else:
            danh_sach = []

        danh_sach.append(du_lieu)

        with open(self.PATH, "w", encoding="utf-8") as file:
            json.dump(danh_sach, file, indent=4, ensure_ascii=False)

    def process_huybo(self):
        self.txt_timnh.clear()
        self.txt_stk.clear()
        self.txt_ten.clear()
        self.txt_timnh.setFocus()
        self.khoa_nhap_thong_tin(False)

    def process_quaylai(self):
        # Quay lại màn hình ví liên kết
        self.vilienket_form = QMainWindow()
        self.ui_vilienket = vilienket_ext()
        self.ui_vilienket.setupUi(self.vilienket_form)

        self.lienkettkmoi.close()  # Đóng cửa sổ hiện tại
        self.vilienket_form.show()  # Hiển thị màn hình ví liên kết
