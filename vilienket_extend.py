import json
import os
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from vilienket_form import Ui_vilienket_form
from caidat_extend import caidat_ext

class vilienket_ext(Ui_vilienket_form):
    PATH = "data/thong_tin_lien_ket.json"
    def setupUi(self, vilienket_form):
        super().setupUi(vilienket_form)
        self.vilienket = vilienket_form

        self.tbl_lienketnh.setHorizontalHeaderLabels(
            ["ID", "Tên ngân hàng", "Số thẻ/tài khoản", "Trạng thái"])
        self.tbl_lienketnh.setColumnWidth(1, 130)
        self.tbl_lienketnh.setColumnWidth(2, 130)
        self.tbl_lienketnh.setColumnWidth(3, 130)
        self.tbl_lienketnh.setColumnHidden(0, True)
        self.tbl_lienketnh.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        # Tải dữ liệu lên
        self.load_linked_accounts()

        # Click vào bảng
        self.tbl_lienketnh.cellClicked.connect(self.load_linked_accounts)

        # Connect events
        self.btn_lktkmoi.clicked.connect(self.open_lienkettkmoi_form)
        self.btn_huylk.clicked.connect(self.process_huylienket)
        self.btn_khoatk.clicked.connect(self.process_khoamokhoa)
        self.btn_return.clicked.connect(self.process_quaylai)


    def open_lienkettkmoi_form(self):
        # Mở màn hình liên kết tài khoản mới
        from lienkettkmoi_extend import lienkettkmoi_ext
        self.lienkettkmoi_form = QMainWindow()
        self.ui_lienkettkmoi = lienkettkmoi_ext()
        self.ui_lienkettkmoi.setupUi(self.lienkettkmoi_form)
        self.vilienket.close()
        self.lienkettkmoi_form.show()

    def load_linked_accounts(self):
        """Đọc dữ liệu từ file JSON và hiển thị lên bảng, tự động thêm trạng thái nếu thiếu"""
        if os.path.exists(self.PATH):
            with open(self.PATH, "r", encoding="utf-8") as file:
                try:
                    accounts = json.load(file)
                    if not isinstance(accounts, list):
                        accounts = []  # Đảm bảo dữ liệu là danh sách
                except json.JSONDecodeError:
                    accounts = []
        else:
            accounts = []

        # Thêm trạng thái mặc định nếu thiếu
        updated = False
        for acc in accounts:
            if "Trạng thái" not in acc:
                acc["Trạng thái"] = "Đang mở khóa"
                updated = True

        # Nếu có cập nhật, ghi lại file JSON
        if updated:
            with open(self.PATH, "w", encoding="utf-8") as file:
                json.dump(accounts, file, indent=4, ensure_ascii=False)

        # Hiển thị dữ liệu lên bảng
        self.tbl_lienketnh.setRowCount(len(accounts))
        for row, acc in enumerate(accounts):
            self.tbl_lienketnh.setItem(row, 1, QTableWidgetItem(acc["Tên ngân hàng"]))
            self.tbl_lienketnh.setItem(row, 2, QTableWidgetItem(acc["Số thẻ/tài khoản"]))
            self.tbl_lienketnh.setItem(row, 3, QTableWidgetItem(acc.get("Trạng thái", "Đang mở khóa")))  # Sửa lỗi KeyError


    def save_linked_accounts(self, accounts):
        """Lưu dữ liệu danh sách tài khoản vào file JSON"""
        with open(self.PATH, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)

    def process_huylienket(self):
        selected_row = self.tbl_lienketnh.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(self.vilienket, "Xác nhận", "Bạn chắc chắn muốn hủy liên kết tài khoản này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    with open(self.PATH, "r", encoding="utf-8") as file:
                        accounts = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    accounts = []

                # Xóa tài khoản tương ứng khỏi danh sách
                del accounts[selected_row]

                # Lưu danh sách mới
                self.save_linked_accounts(accounts)

                # Load lại bảng
                self.load_linked_accounts()

                QMessageBox.information(self.vilienket, "Thành công", "Đã hủy liên kết tài khoản thành công!")
        else:
            QMessageBox.information(self.vilienket, "Thông báo", "Chọn tài khoản bạn muốn hủy liên kết.")

    def process_khoamokhoa(self):
        selected_row = self.tbl_lienketnh.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.vilienket, "Lỗi", "Vui lòng chọn tài khoản cần khóa/mở khóa.")
            return

        try:
            with open(self.PATH, "r", encoding="utf-8") as file:
                accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = []

        # Đổi trạng thái
        current_status = accounts[selected_row]["Trạng thái"]
        new_status = "Đang khóa" if current_status == "Đang mở khóa" else "Đang mở khóa"
        accounts[selected_row]["Trạng thái"] = new_status

        # Lưu lại danh sách cập nhật
        self.save_linked_accounts(accounts)

        # Cập nhật ngay trên bảng (tránh load lại toàn bộ)
        self.tbl_lienketnh.setItem(selected_row, 3, QTableWidgetItem(new_status))

        QMessageBox.information(self.vilienket, "Thành công", f"Tài khoản đã chuyển sang trạng thái: {new_status}")

    def process_quaylai(self):
        # Quay lại màn hình cài đặt
        self.caidat_form = QMainWindow()
        self.ui_caidat = caidat_ext()
        self.ui_caidat.setupUi(self.caidat_form)

        self.vilienket.close()  # Đóng cửa sổ hiện tại
        self.caidat_form.show()  # Hiển thị màn hình cài đặt