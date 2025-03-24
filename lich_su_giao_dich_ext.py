import json

from PyQt6.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem, QMainWindow
from PyQt6.QtCore import QDate
from lich_su_giao_dich_mainwindow import Ui_MainWindow
class Ui_MainWindow_ext (Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.tblLichSuGiaoDich.setHorizontalHeaderLabels(["Ghi chú","Số tiền","Ngày thực hiện","Loại giao dịch"])
        self.tblLichSuGiaoDich.setColumnWidth(0, 200)
        self.tblLichSuGiaoDich.setColumnWidth(1, 200)
        self.tblLichSuGiaoDich.setColumnWidth(2, 200)
        self.tblLichSuGiaoDich.setColumnWidth(3, 200)
        self.txtNgayBatDau.setCalendarPopup(True)
        self.txtNgayBatDau.setDate(QDate.currentDate())
        self.txtNgayKetThuc.setCalendarPopup(True)
        self.txtNgayKetThuc.setDate(QDate.currentDate())
        self.txtTongChiTieu.setReadOnly(True)
        self.txtTongChiTieu.setPlaceholderText("0 VND")

        #ấn tìm kiếm
        self.btnTimKiem.clicked.connect (self.kiem_tra_thong_tin)

        #ấn cộng tiền
        self.btnTongchiTieu.clicked.connect (self.tong_chi_tieu)

        #ấn quay lại
        self.btnQuayLai.clicked.connect(self.quay_lai)

    def quay_lai(self):
        from Thong_ke_bao_cao_ext import Thong_ke_bao_cao_ext
        self.MainWindow.close()
        self.thong_ke_bao_cao=QMainWindow()
        self.ui_thong_ke_bao_cao=Thong_ke_bao_cao_ext()
        self.ui_thong_ke_bao_cao.setupUi(self.thong_ke_bao_cao)
        self.thong_ke_bao_cao.show()

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
            QMessageBox.information(self.MainWindow, "Thông báo", "Bạn chưa chọn loại giao dịch")
            return False
        return True

    def kiem_tra_ngay(self):
        if self.txtNgayBatDau.text()> self.txtNgayKetThuc.text():
            QMessageBox.information(self.MainWindow, "Thông báo", "Ngày kết thúc phải sau ngày bắt đầu")
            return False
        return True

    def cap_nhat_du_lieu (self):
        with open ("data/khoanchi.json", "r", encoding="utf-8") as file:
            try:
                lich_su_giao_dich = json.load(file)
            except:
                lich_su_giao_dich = []
        giao_dich_ton_tai = []
        giao_dich_theo_ngay=[]
        for giao_dich in lich_su_giao_dich:
            ngay_bat_dau = self.txtNgayBatDau.date().toString("dd/MM/yyyy")
            ngay_ket_thuc = self.txtNgayKetThuc.date().toString("dd/MM/yyyy")

            if ngay_bat_dau <= giao_dich["ngày"] <= ngay_ket_thuc:
                giao_dich_theo_ngay.append(giao_dich)
                if self.txtLoaiGiaoDich.currentText() == "Tất cả":
                    giao_dich_ton_tai=giao_dich_theo_ngay
                else:
                    if giao_dich.get("khoản chi")==self.txtLoaiGiaoDich.currentText():
                        giao_dich_ton_tai.append(giao_dich)
        if len(giao_dich_ton_tai)==0:
            QMessageBox.information(self.MainWindow, "Thông báo", "Không tìm được ngày hoặc loại giao dịch phù hợp")
        else:
            self.tblLichSuGiaoDich.setRowCount(len(giao_dich_ton_tai))
            for row, giao_dich in enumerate (giao_dich_ton_tai):
                self.tblLichSuGiaoDich.setItem(row, 0, QTableWidgetItem(giao_dich["ghi chú"]))
                self.tblLichSuGiaoDich.setItem(row, 1, QTableWidgetItem(giao_dich["số tiền"]))
                self.tblLichSuGiaoDich.setItem(row, 2, QTableWidgetItem(giao_dich["ngày"]))
                self.tblLichSuGiaoDich.setItem(row, 3, QTableWidgetItem(giao_dich["khoản chi"]))





