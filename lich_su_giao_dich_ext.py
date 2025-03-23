import json

from PyQt6.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem

from lich_su_giao_dich_mainwindow import Ui_MainWindow
class Ui_MainWindow_ext (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.tblLichSuGiaoDich.setHorizontalHeaderLabels(["Tên giao dịch","Số tiền","Ngày thực hiện","Ghi chú"])
        self.tblLichSuGiaoDich.setColumnWidth(0, 200)
        self.tblLichSuGiaoDich.setColumnWidth(1, 200)
        self.tblLichSuGiaoDich.setColumnWidth(2, 200)
        self.tblLichSuGiaoDich.setColumnWidth(3, 200)
        self.txtNgayBatDau.setCalendarPopup(True)
        self.txtNgayKetThuc.setCalendarPopup(True)
        self.txtTongChiTieu.setReadOnly(True)
        self.txtTongChiTieu.setPlaceholderText("0 VND")

        #ấn tìm kiếm
        self.btnTimKiem.clicked.connect (self.kiem_tra_thong_tin)

        #ấn cộng tiền
        self.btnTongchiTieu.clicked.connect (self.tong_chi_tieu)

    def tong_chi_tieu(self):
        tong_tien = 0
        for row in range (self.tblLichSuGiaoDich.rowCount()):
            tien=self.tblLichSuGiaoDich.item(row,1).text()
            tong_tien= tong_tien + int(tien)
        self.txtTongChiTieu.setText(f"{str(tong_tien)} VND")

    def kiem_tra_thong_tin (self):
        if not self.kiem_tra_loai_giao_dich():
            return
        if not self.kiem_tra_ngay():
            return
        self.cap_nhat_du_lieu()

    def kiem_tra_loai_giao_dich (self):
        if self.txtLoaiGiaoDich.currentText() == "Loại giao dịch":
            self.btnTimKiem.setEnabled(False)
            QMessageBox.information(self.MainWindow, "Thông báo", "Bạn chưa chọn loại giao dịch")
            return False
        return True

    def kiem_tra_ngay(self):
        if self.txtNgayBatDau.text()> self.txtNgayKetThuc.text():
            # self.btnTimKiem.setEnabled(False)
            QMessageBox.information(self.MainWindow, "Thông báo", "Ngày kết thúc phải sau ngày bắt đầu")
            return False
        return True

    def cap_nhat_du_lieu (self):
        with open ("data/muctieutc.json", "r", encoding="utf-8") as file:
            try:
                lich_su_giao_dich = json.load(file)
            except:
                lich_su_giao_dich = []
        for giao_dich in lich_su_giao_dich:
            giao_dich_ton_tai=[]
            if self.txtNgayBatDau.text() <= giao_dich["ngày"] <= self.txtNgayKetThuc.text():
                giao_dich_ton_tai.append(giao_dich)
                self.tblLichSuGiaoDich.setRowCount(len(giao_dich_ton_tai))
                for row, giao_dich in enumerate (giao_dich_ton_tai):
                    self.tblLichSuGiaoDich.setItem(row, 0, QTableWidgetItem(giao_dich["khoản thu"]))
                    self.tblLichSuGiaoDich.setItem(row, 1, QTableWidgetItem(giao_dich["số tiền"]))
                    self.tblLichSuGiaoDich.setItem(row, 2, QTableWidgetItem(giao_dich["ngày"]))
                    self.tblLichSuGiaoDich.setItem(row, 3, QTableWidgetItem(giao_dich["ghi chú"]))
            else:
                QMessageBox.information(self.MainWindow,"Thông báo","Không có giao dịch nào trong khoảng thời gian này")





