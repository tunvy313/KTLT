from PyQt6.QtWidgets import QMainWindow
from cdgiaodien_form import Ui_cdgiaodien_form
from caidat_extend import caidat_ext

class cdgiaodien_ext(Ui_cdgiaodien_form):
    def setupUi(self, cdgiaodien_form):
        super().setupUi(cdgiaodien_form)
        self.cdgiaodien = cdgiaodien_form

        # Connect events
        self.btn_return.clicked.connect(self.process_quaylai)
          # Ngôn ngữ
        self.rdb_tiengviet.toggled.connect(self.process_ngonngu)
        self.rdb_english.toggled.connect(self.process_ngonngu)
          # Đơn vị tiền tệ
        self.rdb_vnd.toggled.connect(self.process_donvitien)
        self.rdb_usd.toggled.connect(self.process_donvitien)
          # Chế độ sáng/tối
        self.rdb_sang.toggled.connect(self.process_chedosang)
        self.rdb_toi.toggled.connect(self.process_chedosang)
          # Hiện/ẩn tổng số dư
        self.rdb_co.toggled.connect(self.process_hienthisodu)
        self.rdb_khong.toggled.connect(self.process_hienthisodu)


    def process_ngonngu(self):
        if self.rdb_tiengviet.isChecked():
            self.cdgiaodien.setWindowTitle("Tùy chỉnh giao diện")
            self.label.setText('<html><head/><body><p align=\"center\">Tùy chỉnh giao diện</p></body></html>')
            self.grb_ngonngu.setTitle("Ngôn ngữ")
            self.rdb_tiengviet.setText("Tiếng Việt")
            self.rdb_english.setText("English")
            self.grb_donvitien.setTitle("Đơn vị tiền")
            self.rdb_vnd.setText("Việt Nam Đồng (VNĐ)")
            self.rdb_usd.setText("United States dollar (USD)")
            self.grb_chedosang.setTitle("Chế độ sáng / tối")
            self.rdb_sang.setText("Sáng")
            self.rdb_toi.setText("Tối")
            self.grb_hienthisodu.setTitle("Hiển thị số dư")
            self.rdb_co.setText("Có")
            self.rdb_khong.setText("Không")
        elif self.rdb_english.isChecked():
            self.cdgiaodien.setWindowTitle("Display Settings")
            self.label.setText('<html><head/><body><p align=\"center\">Display Settings</p></body></html>')
            self.grb_ngonngu.setTitle("Language")
            self.rdb_tiengviet.setText("Vietnamese")
            self.rdb_english.setText("English")
            self.grb_donvitien.setTitle("Monetary unit")
            self.rdb_vnd.setText("Viet Nam Dong (VND)")
            self.rdb_usd.setText("United States dollar (USD)")
            self.grb_chedosang.setTitle("Theme mode")
            self.rdb_sang.setText("Bright")
            self.rdb_toi.setText("Dark")
            self.grb_hienthisodu.setTitle("Always show balance")
            self.rdb_co.setText("Yes")
            self.rdb_khong.setText("No")

    def process_donvitien(self):
        pass

    def process_chedosang(self):
        if self.rdb_sang.isChecked():
            # Chuyển sang chế độ sáng
            self.cdgiaodien.setStyleSheet("background-color: rgb(224, 243, 253);")
            self.grb_ngonngu.setStyleSheet("background-color: rgb(188, 234, 255);")
            self.grb_donvitien.setStyleSheet("background-color: rgb(188, 234, 255);")
            self.grb_chedosang.setStyleSheet("background-color: rgb(188, 234, 255);")
            self.grb_hienthisodu.setStyleSheet("background-color: rgb(188, 234, 255);")
        elif self.rdb_toi.isChecked():
            # Chuyển sang chế độ tối
            self.cdgiaodien.setStyleSheet("background-color: rgb(39, 64, 139);")
            self.grb_ngonngu.setStyleSheet("background-color: rgb(25, 25, 112); color: rgb(255, 255, 255);")
            self.grb_donvitien.setStyleSheet("background-color: rgb(25, 25, 112); color: rgb(255, 255, 255);")
            self.grb_chedosang.setStyleSheet("background-color: rgb(25, 25, 112); color: rgb(255, 255, 255);")
            self.grb_hienthisodu.setStyleSheet("background-color: rgb(25, 25, 112); color: rgb(255, 255, 255);")

    def process_hienthisodu(self):
        pass

    def process_quaylai(self):
        # Quay lại màn hình cài đặt
        self.caidat_form = QMainWindow()
        self.ui_caidat = caidat_ext()
        self.ui_caidat.setupUi(self.caidat_form)

        self.cdgiaodien.close()  # Đóng cửa sổ hiện tại
        self.caidat_form.show()  # Hiển thị màn hình cài đặt