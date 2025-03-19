import json
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow, QTableWidget
from themkhoanthu_form import Ui_themkhoanthu_form
from manhinhchinh_extend import manhinhchinh_ext

class themkhoanthu_ext(Ui_themkhoanthu_form):
    PATH = "data/khoanthu.json"

    def setupUi(self, themkhoanthu_form):
        super().setupUi(themkhoanthu_form)
        self.themkhoanthu = themkhoanthu_form
        self.tbl_table.setHorizontalHeaderLabels(
            ["ID", "Số tiền", "Ngày", "Khoản thu", "Ghi chú", "Mục tiêu tài chính"])
        self.tbl_table.setColumnWidth(3, 160)
        self.tbl_table.setColumnWidth(5, 160)
        self.tbl_table.setColumnHidden(0, True)  # ẩn cột ID
        self.tbl_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        # Tải dữ liệu lên
        self.load_sample_data()

        # Click vào bảng
        self.tbl_table.cellClicked.connect(self.load_data_from_table)

        # Tạo combo box
        self.cbb_muctieutc.addItems(["--Chọn mục tiêu--", "Thỏa sức mua sắm", "Ăn uống vui vẻ", "Sinh hoạt hằng ngày", "Du lịch bốn phương", "Phát triển bản thân", "Dự phòng rủi ro"])

        # Chọn ngày bắt đầu từ ngày hôm nay
        self.dateEdit.setDate(QDate.currentDate())

        # Connect events
        self.btn_luu.clicked.connect(self.process_themgiaodich)
        self.btn_capnhat.clicked.connect(self.process_capnhat)
        self.btn_xoa.clicked.connect(self.process_xoa)
        self.btn_huy.clicked.connect(self.process_huybo)
        self.btn_return.clicked.connect(self.process_quaylai)  # Bấm mũi tên để quay lại màn hình chính

    def load_sample_data(self):
        with open(themkhoanthu_ext.PATH, "r", encoding="utf-8") as file:
            try:
                sample_transaction = json.load(file)
            except json.JSONDecodeError:
                sample_transaction = []
        self.tbl_table.setRowCount(len(sample_transaction))
        for row, item in enumerate(sample_transaction):
            self.tbl_table.setItem(row, 1, QTableWidgetItem(str(item["số tiền"])))
            self.tbl_table.setItem(row, 2, QTableWidgetItem(item["ngày"]))
            self.tbl_table.setItem(row, 3, QTableWidgetItem(item["khoản thu"]))
            self.tbl_table.setItem(row, 4, QTableWidgetItem(item["ghi chú"]))
            self.tbl_table.setItem(row, 5, QTableWidgetItem(item["mục tiêu"]))

    def load_data_from_table(self, row, _):
        self.txt_sotien.setText(self.tbl_table.item(row, 1).text())
        self.txt_ghichu.setText(self.tbl_table.item(row, 4).text())

    def process_themgiaodich(self):
        sotien = self.txt_sotien.text().strip()
        ngay = self.dateEdit.text()
        khoanthu = self.trw_khoanthu.currentItem().text(0) if self.trw_khoanthu.currentItem() else ""
        ghichu = self.txt_ghichu.text().strip()
        muctieu = self.cbb_muctieutc.currentText() if self.cbb_muctieutc.currentText() != "--Chọn mục tiêu--" else ""

        if not sotien.replace('.', '', 1).isdigit():
            QMessageBox.warning(self.themkhoanthu, "Lỗi", "Số tiền đã nhập không hợp lệ!")
            return

        if sotien and khoanthu:
            row_count = self.tbl_table.rowCount()
            self.tbl_table.insertRow(row_count)
            self.tbl_table.setItem(row_count, 1, QTableWidgetItem(sotien))
            self.tbl_table.setItem(row_count, 2, QTableWidgetItem(ngay))
            self.tbl_table.setItem(row_count, 3, QTableWidgetItem(khoanthu))
            self.tbl_table.setItem(row_count, 4, QTableWidgetItem(ghichu))
            self.tbl_table.setItem(row_count, 5, QTableWidgetItem(muctieu))

            # Lưu nối tiếp dữ liệu mới vào tệp json
            self.them_vao_file_json(themkhoanthu_ext.PATH,{"số tiền": float(sotien), "ngày": ngay, "khoản thu": khoanthu, "ghi chú": ghichu, "mục tiêu": muctieu})
            # Load dữ liệu từ tệp json lên bảng tbl_table
            self.tbl_table.setRowCount(0)
            self.load_sample_data()
            self.process_huybo()
        else:
            QMessageBox.warning(self.themkhoanthu, "Lỗi", "Hãy nhập đầy đủ thông tin giao dịch.")

    @staticmethod
    def them_vao_file_json(f_path, new_data):
        try:
            # Đọc dữ liệu từ file
            with open(f_path, "r", encoding="utf-8") as file:
                try:
                    existing_transaction = json.load(file)
                    if not isinstance(existing_transaction, list):
                        existing_transaction = []  # Nếu JSON không phải danh sách, đặt thành []
                except json.JSONDecodeError:
                    existing_transaction = []  # Nếu JSON lỗi, đặt thành []
            # Thêm dữ liệu mới vào danh sách
            existing_transaction.append(new_data)
            # Ghi đè lại file JSON
            with open(f_path, "w", encoding="utf-8") as file:
                json.dump(existing_transaction, file, indent=4, ensure_ascii=False)
        except Exception:
            pass

    def process_luugiaodich(self):
        bangthu = []
        for row in range(self.tbl_table.rowCount()):
            sotien = self.tbl_table.item(row, 1).text()
            ngay = self.tbl_table.item(row, 2).text()
            khoanthu = self.tbl_table.item(row, 3).text()
            ghichu = self.tbl_table.item(row, 4).text()
            muctieu = self.tbl_table.item(row, 5).text()
            bangthu.append({"số tiền": float(sotien) if sotien else "", "ngày": ngay if ngay else "", "khoản thu": khoanthu if khoanthu else "", "ghi chú": ghichu if ghichu else "", "mục tiêu": muctieu if muctieu else ""})

        with open(themkhoanthu_ext.PATH, "w", encoding="utf-8") as file:
            json.dump(bangthu, file, indent=4, ensure_ascii=False)

    def process_capnhat(self):
        selected_row = self.tbl_table.currentRow()
        if selected_row >= 0:
            sotien = self.txt_sotien.text().strip() or self.tbl_table.item(selected_row, 1).text()
            ngay = self.dateEdit.text() or self.tbl_table.item(selected_row, 2).text()
            khoanthu = self.trw_khoanthu.currentItem().text(
                0) if self.trw_khoanthu.currentItem() else self.tbl_table.item(selected_row, 3).text()
            ghichu = self.txt_ghichu.text().strip() or self.tbl_table.item(selected_row, 4).text()
            muctieu = self.cbb_muctieutc.currentText()
            muctieu = muctieu if muctieu != "--Chọn mục tiêu--" else self.tbl_table.item(selected_row, 5).text()

            if not sotien or not sotien.replace('.', '', 1).isdigit():
                QMessageBox.warning(self.themkhoanthu, "Lỗi", "Số tiền đã nhập không hợp lệ hoặc đang trống!")
                return

            self.tbl_table.setItem(selected_row, 1, QTableWidgetItem(sotien))
            self.tbl_table.setItem(selected_row, 2, QTableWidgetItem(ngay))
            self.tbl_table.setItem(selected_row, 3, QTableWidgetItem(khoanthu))
            self.tbl_table.setItem(selected_row, 4, QTableWidgetItem(ghichu))
            self.tbl_table.setItem(selected_row, 5, QTableWidgetItem(muctieu))

            self.process_luugiaodich()
            self.process_huybo()
        else:
            QMessageBox.information(self.themkhoanthu, "Thông báo", "Chọn giao dịch bạn muốn cập nhật.")

    def process_xoa(self):
        selected_row = self.tbl_table.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(self.themkhoanthu, "Xác nhận", "Bạn chắc chắn muốn xóa giao dịch này?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.tbl_table.removeRow(selected_row)
                self.tbl_table.setCurrentCell(-1, -1)  # Ensure no row is auto-selected
                self.process_luugiaodich()
                self.process_huybo()
        else:
            QMessageBox.information(self.themkhoanthu, "Thông báo", "Chọn giao dịch bạn muốn xóa.")

    def process_huybo(self):
        self.txt_sotien.clear()
        self.txt_ghichu.clear()
        self.trw_khoanthu.clearSelection()
        self.cbb_muctieutc.setCurrentIndex(0)
        self.txt_sotien.setFocus()

    def process_quaylai(self):
        self.process_huybo()
        # Quay lại màn hình chính
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.themkhoanthu.close()  # Đóng cửa sổ hiện tại
        self.manhinhchinh_form.show()  # Hiển thị màn hình chính
