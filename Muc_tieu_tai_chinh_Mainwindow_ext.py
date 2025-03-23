from PyQt6.QtWidgets import QMessageBox, QLineEdit, QWidget, QMainWindow, QApplication
import sys
from Muc_tieu_tai_chinh_MainWindow import Ui_MainWindow

class Ui_MainWindow_Ext(QMainWindow, Ui_MainWindow):
    def setupUi(self, muc_tieu_tai_chinh_mw):
        super().setupUi(muc_tieu_tai_chinh_mw)
        self.muc_tieu_tai_chinh_mw = muc_tieu_tai_chinh_mw

    #mở thoả sức mua sắm
        self.btnTSMS.clicked.connect(self.mo_thoa_suc_mua_sam)

    # mở ăn uống vui vẻ
        self.btnAUVV.clicked.connect(self.mo_an_uong_vui_ve)

    # mở sinh hoạt hằng ngày
        self.btnSHHN.clicked.connect(self.mo_sinh_hoat_hang_ngay)

    # mở du lịch bốn phương
        self.btnDLBP.clicked.connect(self.mo_du_lich_bon_phuong)

    # mở phát triển bản thân
        self.btnPTBT.clicked.connect(self.mo_phat_trien_ban_than)

    # mở dự phòng rủi ro
        self.btnDPRR.clicked.connect(self.mo_du_phong_rui_ro)

    def mo_thoa_suc_mua_sam(self):
        from Muc_tieu_tai_chinh_ThoaSucMuaSam_ext import Ui_ThoaSucMuaSam_Ext
        self.Muc_tieu_tai_chinh_ThoaSucMuaSam = QMainWindow()
        self.ui_ThoaSucMuaSam_ext = Ui_ThoaSucMuaSam_Ext()
        self.ui_ThoaSucMuaSam_ext.setupUi(self.Muc_tieu_tai_chinh_ThoaSucMuaSam)
        self.Muc_tieu_tai_chinh_ThoaSucMuaSam.show()
        self.muc_tieu_tai_chinh_mw.close()

    def mo_an_uong_vui_ve(self):
        from Muc_tieu_tai_chinh_AnUongVuiVe_ext import Ui_AnUongVuiVe_Ext
        self.Muc_tieu_tai_chinh_AnUongVuiVe = QMainWindow()
        self.ui_AnUongVuiVe_ext = Ui_AnUongVuiVe_Ext()
        self.ui_AnUongVuiVe_ext.setupUi(self.Muc_tieu_tai_chinh_AnUongVuiVe)
        self.Muc_tieu_tai_chinh_AnUongVuiVe.show()
        self.muc_tieu_tai_chinh_mw.close()

    def mo_sinh_hoat_hang_ngay(self):
        from Muc_tieu_tai_chinh_SinhHoatHangNgay_ext import Ui_SinhHoatHangNgay_Ext
        self.Muc_tieu_tai_chinh_SinhHoatHangNgay = QMainWindow()
        self.ui_SinhHoatHangNgay_ext = Ui_SinhHoatHangNgay_Ext()
        self.ui_SinhHoatHangNgay_ext.setupUi(self.Muc_tieu_tai_chinh_SinhHoatHangNgay)
        self.Muc_tieu_tai_chinh_SinhHoatHangNgay.show()
        self.muc_tieu_tai_chinh_mw.close()

    def mo_du_lich_bon_phuong(self):
        from Muc_tieu_tai_chinh_DuLichBonPhuong_ext import Ui_DuLichBonPhuong_Ext
        self.Muc_tieu_tai_chinh_DuLichBonPhuong = QMainWindow()
        self.ui_DuLichBonPhuong_ext = Ui_DuLichBonPhuong_Ext()
        self.ui_DuLichBonPhuong_ext.setupUi(self.Muc_tieu_tai_chinh_DuLichBonPhuong)
        self.Muc_tieu_tai_chinh_DuLichBonPhuong.show()
        self.muc_tieu_tai_chinh_mw.close()

    def mo_phat_trien_ban_than(self):
        from Muc_tieu_tai_chinh_PhatTrienBanThan_ext import Ui_PhatTrienBanThan_Ext
        self.Muc_tieu_tai_chinh_PhatTrienBanThan = QMainWindow()
        self.ui_PhatTrienBanThan_ext = Ui_PhatTrienBanThan_Ext()
        self.ui_PhatTrienBanThan_ext.setupUi(self.Muc_tieu_tai_chinh_PhatTrienBanThan)
        self.Muc_tieu_tai_chinh_PhatTrienBanThan.show()
        self.muc_tieu_tai_chinh_mw.close()

    def mo_du_phong_rui_ro(self):
        from Muc_tieu_tai_chinh_DuPhongRuiRo_ext import Ui_DuPhongRuiRo_Ext
        self.Muc_tieu_tai_chinh_DuPhongRuiRo = QMainWindow()
        self.ui_DuPhongRuiRo_ext = Ui_DuPhongRuiRo_Ext()
        self.ui_DuPhongRuiRo_ext.setupUi(self.Muc_tieu_tai_chinh_DuPhongRuiRo)
        self.Muc_tieu_tai_chinh_DuPhongRuiRo.show()
        self.muc_tieu_tai_chinh_mw.close()

