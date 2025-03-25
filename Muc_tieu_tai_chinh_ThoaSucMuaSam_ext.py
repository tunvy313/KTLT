from PyQt6.QtWidgets import QMessageBox, QLineEdit, QMainWindow
import datetime
import json
import os
from PyQt6.QtCore import QDate
from Muc_tieu_tai_chinh_ThoaSucMuaSam import Ui_ThoaSucMuaSam
from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext

class Ui_ThoaSucMuaSam_Ext(QMainWindow, Ui_ThoaSucMuaSam):
    def setupUi(self, thoa_suc_mua_sam_mw):
        super().setupUi(thoa_suc_mua_sam_mw)
        self.thoa_suc_mua_sam_mw = thoa_suc_mua_sam_mw

        self.txtTenQuy.setPlaceholderText("Tên quỹ của bạn")
        self.txtSoTienMucTieu.setPlaceholderText("Số tiền mục tiêu")
        self.txtSoTienCanGop.setReadOnly(True)
        self.txtSoTienCanGop.setPlaceholderText("0 VNĐ")
        self.txtNgayBatDau.setCalendarPopup(True)
        self.txtNgayBatDau.setDate(QDate.currentDate())
        self.txtNgayKetThuc.setCalendarPopup(True)
        self.txtNgayKetThuc.setDate(QDate.currentDate())

    #ấn quay lại
        self.btnQuayLai.clicked.connect(self.quay_lai_tu_thoa_suc_mua_sam)


    #bấm xác nhận
        self.btnXacNhan.clicked.connect(self.xac_nhan)

    # ấn xem lại các loại quỹ
        self.btnXemLai.clicked.connect(self.xem_lai_cac_quy)

    def xem_lai_cac_quy(self):
        from xem_lai_quy_ext import xem_lai_quy_ext
        self.xem_lai_quy_mw = QMainWindow()
        self.ui_xem_lai_quy = xem_lai_quy_ext()
        self.ui_xem_lai_quy.setupUi(self.xem_lai_quy_mw)
        self.xem_lai_quy_mw.show()
        self.thoa_suc_mua_sam_mw.close()

    def quay_lai_tu_thoa_suc_mua_sam(self):
        from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
        self.Muc_tieu_tai_chinh_Mainwindow = QMainWindow()
        self.ui_muc_tieu_tai_chinh = Ui_MainWindow_Ext()
        self.ui_muc_tieu_tai_chinh.setupUi(self.Muc_tieu_tai_chinh_Mainwindow)
        self.Muc_tieu_tai_chinh_Mainwindow.show()
        self.thoa_suc_mua_sam_mw.close()

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
        ten_quy = self.txtTenQuy.text()
        so_tien_muc_tieu = self.txtSoTienMucTieu.text()
        ngay_bat_dau = self.txtNgayBatDau.text()
        ngay_ket_thuc = self.txtNgayKetThuc.text()
        so_tien_can_gop = self.txtSoTienCanGop.text()
        muc_tieu_tai_chinh = {
            "Loại quỹ": "Sinh hoạt hằng ngày",
            "Tên quỹ": ten_quy,
            "Số tiền mục tiêu": so_tien_muc_tieu,
            "Ngày bắt đầu": ngay_bat_dau,
            "Ngày kết thúc": ngay_ket_thuc,
            "Số tiền cần góp mỗi ngày": so_tien_can_gop
        }
        self.append_to_json_file("data/muc_tieu_tai_chinh.json", muc_tieu_tai_chinh)

    def xac_nhan(self):
        if self.kiem_tra_tien() and self.kiem_tra_ngay() and self.kiem_tra_ten():
            self.tinhtien()
            reply = QMessageBox.question(self.thoa_suc_mua_sam_mw, "Xác nhận", "Bạn có xác nhận lập quỹ không?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                    QMessageBox.information(self.thoa_suc_mua_sam_mw, "Thông báo", "Lập quỹ thành công")
                    self.quay_lai_tu_thoa_suc_mua_sam()
                    self.luu_thong_tin_muc_tieu_tai_chinh()

    def luu_thay_doi(self):
        # Lấy dữ liệu từ giao diện chỉnh sửa:
        ten_quy = self.ui_an_uong_vui_ve.txtTenQuy.text()
        so_tien_muc_tieu = self.ui_an_uong_vui_ve.txtSoTienCanGop.text()
        ngay_bat_dau = self.ui_an_uong_vui_ve.txtNgayBatDau.date().toString("dd/MM/yyyy")
        ngay_ket_thuc = self.ui_an_uong_vui_ve.txtNgayKetThuc.date().toString("dd/MM/yyyy")

        # Đọc dữ liệu từ tệp JSON:
        with open("data/muc_tieu_tai_chinh.json", "r", encoding="utf-8") as file:
            try:
                muc_tieu_an_uong_vui_ve = json.load(file)
            except:
                muc_tieu_an_uong_vui_ve = []

        # Tìm mục tiêu cần chỉnh sửa:
        hang_chinh_sua = self.tblXemLai.selectedItems()
        hang_duoc_chon = hang_chinh_sua[0].row()
        ten_quy_cu = self.tblXemLai.item(hang_duoc_chon, 1).text()

        for muc_tieu in muc_tieu_an_uong_vui_ve:
            if muc_tieu["Tên quỹ"] == ten_quy_cu:
                # Cập nhật dữ liệu:
                muc_tieu["Tên quỹ"] = ten_quy
                muc_tieu["Số tiền cần góp mỗi ngày"] = so_tien_muc_tieu
                muc_tieu["Ngày bắt đầu"] = ngay_bat_dau
                muc_tieu["Ngày kết thúc"] = ngay_ket_thuc
                break

        # Ghi dữ liệu vào tệp JSON:
        with open("data/muc_tieu_tai_chinh.json", "w", encoding="utf-8") as file:
            json.dump(muc_tieu_an_uong_vui_ve, file, ensure_ascii=False, indent=4)

        # Cập nhật tblXemLai:
        self.hien_thi_cac_quy()  # Hoặc cập nhật trực tiếp hàng được chỉnh sửa.

        # Đóng cửa sổ chỉnh sửa:
        self.an_uong_vui_ve_mw.close()

    def kiem_tra_ngay(self):
        if self.txtNgayBatDau.text()> self.txtNgayKetThuc.text():
            QMessageBox.information(self.thoa_suc_mua_sam_mw, "Thông báo", "Ngày kết thúc phải sau ngày bắt đầu")
            return False
        return True

    def kiem_tra_ten(self):
        if self.txtTenQuy.text() == "":
            QMessageBox.warning(self.thoa_suc_mua_sam_mw, "Cảnh báo", "Hãy điền tên quỹ")
            return False
        return True

    def kiem_tra_tien(self):
        if self.txtSoTienMucTieu.text() == "" or not self.txtSoTienMucTieu.text().isdigit():
            QMessageBox.warning(self.an_uong_vui_ve_mw, "Cảnh báo", "Số tiền phải là 1 số")
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
                tien=float(tien_str)/(khoang_thoi_gian.days)
                self.txtSoTienCanGop.setText(str(tien) + " "+"VNĐ")
            elif self.txtNgayKetThuc.text() == self.txtNgayBatDau.text():
                self.txtSoTienCanGop.setText(self.txtSoTienMucTieu.text() +" "+"VNĐ")
            else:
                QMessageBox.information(self.thoa_suc_mua_sam_mw, "Thông báo", "Ngày không hợp lệ")
