import json
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QPushButton, QMainWindow
from PyQt6.QtCore import QDate
from datetime import datetime
from themkhoanchi_form import Ui_themkhoanchi_form
from manhinhchinh_extend import manhinhchinh_ext


class themkhoanchi_ext(Ui_themkhoanchi_form):
    PATH="data/bangchi.json"
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.tbl_table.setHorizontalHeaderLabels(["Số tiền","Ngày","Mục đích","Ghi chú"])  #Thiết lập tiêu đề các cột của bảng.
        self.tbl_table.setColumnWidth(3,160)

        # Click vào bảng
        self.tbl_table.cellClicked.connect(self.load_data_from_table)

        #Chon
        self.edit_ngay.setDate(QDate.currentDate())

        # Connect Events
        self.btn_reset.clicked.connect(self.reset_form)
        self.btn_save.clicked.connect(self.insert_data)
        self.btn_update.clicked.connect(self.update_data)
        self.btn_delete.clicked.connect(self.delete_data)
        self.btn_return.clicked.connect(self.process_quaylai)

    def load_sample_data(self):
        try:
            with open(themkhoanchi_ext.PATH, "r", encoding="utf-8") as file:
                sample_transaction = json.load(file)
        except json.JSONDecodeError:
            sample_transaction = [] # Reset if file is corrupted

        self.tbl_table.setRowCount(len(sample_transaction))
        for row, item in enumerate(sample_transaction):
            self.tbl_table.setItem(row, 0, QTableWidgetItem(item["số tiền"]))
            self.tbl_table.setItem(row, 1, QTableWidgetItem(item["ngày"]))
            self.tbl_table.setItem(row, 2, QTableWidgetItem(item["khoản chi"]))
            self.tbl_table.setItem(row, 3, QTableWidgetItem(item["ghi chú"]))
        print(self.tbl_table.rowCount())  # Kiểm tra số dòng

    def load_data_from_table(self,row,_):
        self.txt_tien.setText(self.tbl_table.item(row,0).text())
        self.txt_ghichu.setText(self.tbl_table.item(row,3).text())

    def reset_form(self):
        self.txt_tien.clear()
        self.txt_ghichu.clear()

        self.txt_tien.setFocus()

    def save_data(self):
        bangchi = []
        for row in range(self.tbl_table.rowCount()):
            tien = self.tbl_table.item(row, 0).text()
            ngay = self.tbl_table.item(row, 1).text()
            khoanchi = self.tbl_table.item(row, 2).text()
            ghichu = self.tbl_table.item(row, 3).text()
            bangchi.append({"số tiền": tien if tien else "", "ngày": ngay if ngay else "",
                            "khoản chi": khoanchi if khoanchi else "", "ghi chú": ghichu if ghichu else ""})


        with open(themkhoanchi_ext.PATH, "w", encoding="utf-8") as file:
            json.dump(bangchi, file, indent=4, ensure_ascii=False)

    @staticmethod
    def append_to_json_file(f_path, new_data):
        with open(f_path, "r+", encoding="utf-8") as file:
            file.seek(0, os.SEEK_END)
            cursor_position = file.tell()

            if cursor_position > 2:
                file.seek(cursor_position - 1)  # Move cursor before the closing bracket ']'
                file.write(",\n" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")
            else:
                file.write("[" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")

    def insert_data (self):

        tien=self.txt_tien.text().strip()
        ngay = self.edit_ngay.text()
        ghichu =self.txt_ghichu.text().strip()
        khoanchi = self.tree_list.currentItem().text(0) if self.tree_list.currentItem() else ""

        if not tien.replace('.', '', 1).isdigit():  # Cho phép số có dấu chấm (số thực)
            QMessageBox.warning(self.MainWindow, "Lỗi", "Số tiền phải là một số hợp lệ!")
            return

        if tien and ngay and khoanchi:
            row_count=self.tbl_table.rowCount()
            self.tbl_table.insertRow(row_count)
            self.tbl_table.setItem(row_count,0,QTableWidgetItem(tien))
            self.tbl_table.setItem(row_count, 1, QTableWidgetItem(ngay))
            self.tbl_table.setItem(row_count, 2, QTableWidgetItem(khoanchi))
            self.tbl_table.setItem(row_count,3,QTableWidgetItem(ghichu))

            # self.reset_form()
            # 1. Lưu nối tiếp dữ liệu mới --> tệp json
            self.append_to_json_file(themkhoanchi_ext.PATH,
                                     {"số tiền": tien, "ngày": ngay, "khoản chi": khoanchi, "ghi chú": ghichu})

            # 2. Load dữ liệu từ tệp json -> tbl_table
            self.load_sample_data()
            self.reset_form()
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Hãy nhập đầy đủ thông tin giao dịch.")


    def update_data(self):
        selected_row = self.tbl_table.currentRow()
        if selected_row >= 0:
                reply = QMessageBox.question(self.MainWindow, "Xác nhận", "Bạn chắc chắn muốn cập nhật giao dịch này",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    # self.tbl_table.setItem(selected_row,0,QTableWidgetItem(self.edit_ngay.text()))
                    self.tbl_table.setItem(selected_row, 0, QTableWidgetItem(self.txt_tien.text()))
                    self.tbl_table.setItem(selected_row, 1, QTableWidgetItem(self.edit_ngay.text()))
                    self.tbl_table.setItem(selected_row,3,QTableWidgetItem(self.txt_ghichu.text()))   #PlainText
                    self.tbl_table.setItem(selected_row,2,QTableWidgetItem(self.tree_list.currentItem().text(0)))
                    self.reset_form()
        else:
            QMessageBox.information(self.MainWindow, "Thông báo", "Chọn khoản chi bạn muốn cập nhật.")

    def delete_data(self):
        selected_row = self.tbl_table.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(self.MainWindow, "Thông báo", "Bạn có chắc chắn muốn xóa giao dịch",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.tbl_table.removeRow(selected_row)
                self.tbl_table.setCurrentCell(-1, -1)  # ensure no row is auto_selected
                self.save_data()
                self.reset_form()
        else:
            QMessageBox.information(self.MainWindow, "Thông báo", "Bạn cần chọn giao dịch muốn xóa")

    def process_quaylai(self):
        self.reset_form()
        # Quay lại màn hình chính
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.MainWindow.close()  # Đóng cửa sổ hiện tại
        self.manhinhchinh_form.show()  # Hiển thị màn hình chính






