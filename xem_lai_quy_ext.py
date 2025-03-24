from xem_lai_quy import Ui_xem_lai_quy
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QDateEdit
import json
import datetime
from PyQt6.QtCore import QDate
class xem_lai_quy_ext(QMainWindow, Ui_xem_lai_quy):
    def setupUi(self, xem_lai_quy_mw):
        super().setupUi(xem_lai_quy_mw)
        self.xem_lai_quy_mw=xem_lai_quy_mw

        self.tblXemLai.setHorizontalHeaderLabels(["Loại quỹ", "Tên quỹ", "Số tiền cần góp (VNĐ)", "Số ngày còn lại","Ngày Bắt Đầu", "Ngày Kết Thúc", "Số tiền cần góp mỗi ngày (VNĐ)", "Số tiền mục tiêu"])
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

        #ấn xoá
        self.btnXoa.clicked.connect(self.xoa_quy)

    def quay_lai_an_uong_vui_ve(self):
        from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
        self.Muc_tieu_tai_chinh_Mainwindow = QMainWindow()
        self.ui_Muc_tieu_tai_chinh = Ui_MainWindow_Ext()
        self.ui_Muc_tieu_tai_chinh.setupUi(self.Muc_tieu_tai_chinh_Mainwindow)
        self.Muc_tieu_tai_chinh_Mainwindow.show()
        self.xem_lai_quy_mw.close()

        def xoa_quy(self):
        reply = QMessageBox.question(self.xem_lai_quy_mw, "Xác nhận", "Bạn có xác nhận xoá quỹ không?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self.xem_lai_quy_mw, "Thông báo", "Đã xoá quỹ thành công")
            hang_xoa = self.tblXemLai.selectedItems()
            if not hang_xoa:
                QMessageBox.warning(self.xem_lai_quy_mw, "Thông báo", "Vui lòng chọn một quỹ để xóa.")
                return

            hang_duoc_chon = hang_xoa[0].row()
            ten_quy = self.tblXemLai.item(hang_duoc_chon, 1).text()

            # Đọc dữ liệu từ tệp JSON:
            with open("data/muc_tieu_tai_chinh.json", "r", encoding="utf-8") as file:
                try:
                    muc_tieu_tai_chinh = json.load(file)
                except:
                    muc_tieu_tai_chinh = []

            for i, muc_tieu in enumerate(muc_tieu_tai_chinh):
                if muc_tieu["Tên quỹ"] == ten_quy:
                    del muc_tieu_tai_chinh[i]
                    break

            # Ghi dữ liệu vào tệp JSON:
            with open("data/muc_tieu_tai_chinh.json", "w", encoding="utf-8") as file:
                json.dump(muc_tieu_tai_chinh, file, ensure_ascii=False, indent=4)

            # Xóa hàng khỏi bảng:
            self.tblXemLai.removeRow(hang_duoc_chon)



    def hien_thi_cac_quy(self):
        with open("data/muc_tieu_tai_chinh.json", "r", encoding="utf-8") as file:
            try:
                muc_tieu_tai_chinh = json.load(file)
            except:
                muc_tieu_tai_chinh = []
        if len(muc_tieu_tai_chinh)>0:
            self.tblXemLai.setRowCount(len(muc_tieu_tai_chinh))
            for row, muc_tieu in enumerate (muc_tieu_tai_chinh):
                so_tien_can_gop_moi_ngay=0
                ngay_hom_nay_qdate = QDate.currentDate()
                ngay_hom_nay_str = ngay_hom_nay_qdate.toString("dd/MM/yyyy")
                ngay_hom_nay = datetime.datetime.strptime(ngay_hom_nay_str, "%d/%m/%Y").date()
                ngay_ket_thuc_str = muc_tieu["Ngày kết thúc"]
                ngay_ket_thuc = datetime.datetime.strptime(ngay_ket_thuc_str, "%d/%m/%Y").date()
                so_tien_can_gop_moi_ngay_str = muc_tieu["Số tiền cần góp mỗi ngày"].replace(" VNĐ" ,"")
                if so_tien_can_gop_moi_ngay_str:
                    try:
                        so_tien_can_gop_moi_ngay = float(so_tien_can_gop_moi_ngay_str)
                    except ValueError:
                        print(f"Lỗi: Không thể chuyển đổi '{so_tien_can_gop_moi_ngay_str}' thành số thực.")

                if ngay_hom_nay_str <= ngay_ket_thuc_str:
                    so_ngay_con_lai= (ngay_ket_thuc - ngay_hom_nay).days +1
                    so_tien_can_gop=so_tien_can_gop_moi_ngay*so_ngay_con_lai
                else:
                    so_ngay_con_lai= 0
                    so_tien_can_gop= 0
                self.tblXemLai.setItem(row, 0, QTableWidgetItem(muc_tieu["Loại quỹ"]))
                self.tblXemLai.setItem(row, 1, QTableWidgetItem(muc_tieu["Tên quỹ"]))
                self.tblXemLai.setItem(row, 2, QTableWidgetItem(str(so_tien_can_gop)))
                self.tblXemLai.setItem(row, 3, QTableWidgetItem(str(so_ngay_con_lai)))
                self.tblXemLai.setItem(row, 4, QTableWidgetItem(muc_tieu["Ngày bắt đầu"]))
                self.tblXemLai.setItem(row, 5, QTableWidgetItem(muc_tieu["Ngày kết thúc"]))
                self.tblXemLai.setItem(row, 6, QTableWidgetItem(muc_tieu["Số tiền cần góp mỗi ngày"]))
                self.tblXemLai.setItem(row, 7, QTableWidgetItem(muc_tieu["Số tiền mục tiêu"]))

        else:
            QMessageBox.information(self.xem_lai_quy_mw, "Thông báo","Chưa có quỹ nào được tạo")

