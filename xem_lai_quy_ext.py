from xem_lai_quy import Ui_xem_lai_quy
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QDateEdit
import json
import datetime
from PyQt6.QtCore import QDate
class xem_lai_quy_ext(QMainWindow, Ui_xem_lai_quy):
    def setupUi(self, xem_lai_quy_mw):
        super().setupUi(xem_lai_quy_mw)
        self.xem_lai_quy_mw=xem_lai_quy_mw

        self.tblXemLai.setHorizontalHeaderLabels(["Loại quỹ", "Tên quỹ", "Số tiền cần góp", "Số ngày còn lại","Ngày Bắt Đầu", "Ngày Kết Thúc", "Số tiền cần góp mỗi ngày", "Số tiền mục tiêu"])
        self.tblXemLai.setColumnWidth(0, 150)
        self.tblXemLai.setColumnWidth(1, 150)
        self.tblXemLai.setColumnWidth(2, 150)
        self.tblXemLai.setColumnWidth(3, 150)
        self.tblXemLai.setColumnWidth(4, 150)
        self.tblXemLai.setColumnWidth(5, 150)
        self.tblXemLai.setColumnWidth(6, 150)
        self.tblXemLai.setColumnWidth(7, 150)

        #xem quỹ
        self.hien_thi_cac_quy()

        #ấn quay lại
        self.btnQuayLai.clicked.connect(self.quay_lai_an_uong_vui_ve)

        #ấn chỉnh sửa
        self.btnChinhSua.clicked.connect(self.chinh_sua_an_uong_vui_ve)

    def quay_lai_an_uong_vui_ve(self):
        from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
        self.Muc_tieu_tai_chinh_Mainwindow = QMainWindow()
        self.ui_Muc_tieu_tai_chinh = Ui_MainWindow_Ext()
        self.ui_Muc_tieu_tai_chinh.setupUi(self.Muc_tieu_tai_chinh_Mainwindow)
        self.Muc_tieu_tai_chinh_Mainwindow.show()
        self.xem_lai_quy_mw.close()

    def chinh_sua_an_uong_vui_ve(self, row,_):
        from Muc_tieu_tai_chinh_AnUongVuiVe_ext import Ui_AnUongVuiVe_Ext
        self.An_uong_vui_ve_Mainwindow = QMainWindow()
        self.ui_An_uong_vui_ve = Ui_AnUongVuiVe_Ext()
        self.ui_An_uong_vui_ve.setupUi(self.An_uong_vui_ve_Mainwindow)
        self.An_uong_vui_ve_Mainwindow.show()
        print(self.tblXemLai.item(row, 1).text())
        # self.txtTenQuy.setText(self.tblXemLai.item(row, 1).text())
        # self.txtNgayBatDau.setText(self.tblXemLai.item(row, 4).text())
        # self.txtNgayKetThuc.setText(self.tblXemLai.item(row, 5).text())
        # self.txtSoTienMucTieu.setText(self.tblXemLai.item(row,7).text())
        # self.txtSoTienCanGop.setText(self.tblXemLai.item(row,6).text())
        self.xem_lai_quy_mw.close()

    def hien_thi_cac_quy(self):
        with open("data/muc_tieu_tai_chinh.json", "r", encoding="utf-8") as file:
            try:
                muc_tieu_an_uong_vui_ve = json.load(file)
            except:
                muc_tieu_an_uong_vui_ve = []
        if len(muc_tieu_an_uong_vui_ve)>0:
            for muc_tieu in muc_tieu_an_uong_vui_ve:
                self.tblXemLai.setRowCount(len(muc_tieu_an_uong_vui_ve))
                ngay_hom_nay_qdate = QDate.currentDate()
                ngay_hom_nay_str = ngay_hom_nay_qdate.toString("dd/MM/yyyy")
                ngay_hom_nay = datetime.datetime.strptime(ngay_hom_nay_str, "%d/%m/%Y").date()
                ngay_ket_thuc_str = muc_tieu["Ngày kết thúc"]
                ngay_ket_thuc = datetime.datetime.strptime(ngay_ket_thuc_str, "%d/%m/%Y").date()

            if ngay_hom_nay_str <= ngay_ket_thuc_str:
                so_tien_can_gop_moi_ngay_str = muc_tieu["Số tiền cần góp mỗi ngày"].replace(" VNĐ","")
                so_ngay_con_lai= (ngay_ket_thuc - ngay_hom_nay).days +1
                so_tien_can_gop=float(so_tien_can_gop_moi_ngay_str)*so_ngay_con_lai
            else:
                    so_ngay_con_lai= 0
                    so_tien_can_gop=0

            for row, muc_tieu in enumerate(muc_tieu_an_uong_vui_ve):
                self.tblXemLai.setItem(row, 0, QTableWidgetItem("Ăn uống vui vẻ"))
                self.tblXemLai.setItem(row, 1, QTableWidgetItem(muc_tieu["Tên quỹ"]))
                self.tblXemLai.setItem(row, 2, QTableWidgetItem(str(so_tien_can_gop)))
                self.tblXemLai.setItem(row, 3, QTableWidgetItem(str(so_ngay_con_lai)))
        else:
            QMessageBox.information(self.xem_lai_quy_mw, "Thông báo",
                                        "Chưa có quỹ nào được tạo")

