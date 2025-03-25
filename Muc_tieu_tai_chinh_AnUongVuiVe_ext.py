from PyQt6.QtWidgets import QMessageBox, QLineEdit, QMainWindow
import datetime
import os
import json
from PyQt6.QtCore import QDate
from Muc_tieu_tai_chinh_AnUongVuiVe import Ui_AnUongVuiVe
class Ui_AnUongVuiVe_Ext(QMainWindow, Ui_AnUongVuiVe):
    def setupUi(self, an_uong_vui_ve_mw):
        super().setupUi(an_uong_vui_ve_mw)
        self.an_uong_vui_ve_mw=an_uong_vui_ve_mw

        self.txtTenQuy.setPlaceholderText("Tên quỹ của bạn")
        self.txtSoTienMucTieu.setPlaceholderText("Số tiền mục tiêu")
        self.txtSoTienCanGop.setReadOnly(True)
        self.txtSoTienCanGop.setPlaceholderText("0 VNĐ")
        self.txtNgayBatDau.setCalendarPopup(True)
        self.txtNgayBatDau.setDate(QDate.currentDate())
        self.txtNgayKetThuc.setCalendarPopup(True)
        self.txtNgayKetThuc.setDate(QDate.currentDate())

    #ấn quay lại
        self.btnQuayLai.clicked.connect(self.quay_lai_tu_an_uong_vui_ve)

    #bấm xác nhận
        self.btnXacNhan.clicked.connect(self.xac_nhan)

    #ấn xem lại các loại quỹ
        self.btnXemLai.clicked.connect(self.xem_lai_cac_quy)

    def xem_lai_cac_quy(self):
        from xem_lai_quy_ext import xem_lai_quy_ext
        self.xem_lai_quy_mw = QMainWindow()
        self.ui_xem_lai_quy = xem_lai_quy_ext()
        self.ui_xem_lai_quy.setupUi(self.xem_lai_quy_mw)
        self.xem_lai_quy_mw.show()
        self.an_uong_vui_ve_mw.close()

    def quay_lai_tu_an_uong_vui_ve(self):
        from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
        self.an_uong_vui_ve_mw.close()
        self.muc_tieu_tai_chinh_mw=QMainWindow()
        self.ui_muc_tieu_tai_chinh=Ui_MainWindow_Ext()
        self.ui_muc_tieu_tai_chinh.setupUi(self.muc_tieu_tai_chinh_mw)
        self.muc_tieu_tai_chinh_mw.show()

    def xac_nhan(self):
        if self.kiem_tra_tien() and self.kiem_tra_ngay() and self.kiem_tra_ten():
            self.tinhtien()
            reply = QMessageBox.question(self.an_uong_vui_ve_mw, "Xác nhận", "Bạn có xác nhận lập quỹ không?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                    QMessageBox.information(self.an_uong_vui_ve_mw, "Thông báo", "Lập quỹ thành công")
                    self.quay_lai_tu_an_uong_vui_ve()
                    self.luu_thong_tin_muc_tieu_tai_chinh()

    @staticmethod
    def append_to_json_file(f_path, new_data):
        with open(f_path, "r+", encoding="utf8") as file:
            file.seek(0, os.SEEK_END)
            cursor_position = file.tell()

            if cursor_position > 2:
                file.seek(cursor_position - 1)
                file.write(", \n" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")
            else:
                file.write("[" + json.dumps(new_data, ensure_ascii=False, indent=4) + "]")

    def luu_thong_tin_muc_tieu_tai_chinh(self):
        if self.kiem_tra_tien() and self.kiem_tra_ngay() and self.kiem_tra_ten():
            ten_quy=self.txtTenQuy.text()
            so_tien_muc_tieu=self.txtSoTienMucTieu.text()
            ngay_bat_dau=self.txtNgayBatDau.text()
            ngay_ket_thuc=self.txtNgayKetThuc.text()
            so_tien_can_gop=self.txtSoTienCanGop.text()
            muc_tieu_tai_chinh={
                "Loại quỹ": "Ăn uống vui vẻ",
                "Tên quỹ": ten_quy,
                "Số tiền mục tiêu": so_tien_muc_tieu,
                "Ngày bắt đầu": ngay_bat_dau,
                "Ngày kết thúc": ngay_ket_thuc,
                "Số tiền cần góp mỗi ngày": so_tien_can_gop
            }
            self.append_to_json_file("data/muc_tieu_tai_chinh.json", muc_tieu_tai_chinh)

    def kiem_tra_ngay(self):
        if self.txtNgayBatDau.text()> self.txtNgayKetThuc.text():
            QMessageBox.information(self.an_uong_vui_ve_mw, "Thông báo", "Ngày kết thúc phải sau ngày bắt đầu")
            return False
        return True

    def kiem_tra_ten(self):
        if self.txtTenQuy.text() == "":
            QMessageBox.warning(self.an_uong_vui_ve_mw, "Cảnh báo", "Hãy điền tên quỹ")
            return False
        return True

    def kiem_tra_tien(self):
        if self.txtSoTienMucTieu.text() == "" or not self.txtSoTienMucTieu.text().isdigit():
            QMessageBox.warning(self.an_uong_vui_ve_mw, "Cảnh báo", "Hãy điền số tiền mục tiêu")
            return False
        return True

    def tinhtien(self):
        if self.kiem_tra_tien() and self.kiem_tra_ngay():
            if self.txtNgayKetThuc.text() > self.txtNgayBatDau.text():
                ngay_ket_thuc_str=self.txtNgayKetThuc.text()
                ngay_bat_dau_str=self.txtNgayBatDau.text()
                ngay_ket_thuc = datetime.datetime.strptime(ngay_ket_thuc_str,"%d/%m/%Y").date()
                ngay_bat_dau = datetime.datetime.strptime(ngay_bat_dau_str, "%d/%m/%Y").date()
                khoang_thoi_gian=ngay_ket_thuc - ngay_bat_dau
                tien_str=self.txtSoTienMucTieu.text()
                tien=float(tien_str)/(khoang_thoi_gian.days+1)
                self.txtSoTienCanGop.setText(str(tien) + " "+"VNĐ")
            elif self.txtNgayKetThuc.text() == self.txtNgayBatDau.text():
                self.txtSoTienCanGop.setText(self.txtSoTienMucTieu.text() +" "+"VNĐ")
            else:
                QMessageBox.information(self.an_uong_vui_ve_mw, "Thông báo", "Ngày không hợp lệ")
