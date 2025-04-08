from PyQt6.QtWidgets import QMainWindow

from Thong_ke_bao_cao_MainWindow import Ui_thong_ke_bao_cao
class Thong_ke_bao_cao_ext(QMainWindow,Ui_thong_ke_bao_cao):
    def setupUi(self, thong_ke_bao_cao_mw):
        super().setupUi(thong_ke_bao_cao_mw)
        self.thong_ke_bao_cao_mw = thong_ke_bao_cao_mw
        self.btnQuayLai.clicked.connect(self.process_quaylai)

    #mở lịch sử giao dịch
        self.btnLSGD.clicked.connect(self.mo_lich_su_giao_dich)
    #mở mục tiêu tài chính
        self.btnMTTC.clicked.connect(self.mo_muc_tieu_tai_chinh)
    #mở báo cáo tài chính
        self.btnBCTC.clicked.connect(self.mo_bct_chinh)

    def mo_lich_su_giao_dich(self):
        from lich_su_giao_dich_ext import Ui_MainWindow_ext
        self.lich_su_giao_dich = QMainWindow()
        self.ui_lich_su_giao_dich_ext = Ui_MainWindow_ext()
        self.ui_lich_su_giao_dich_ext.setupUi(self.lich_su_giao_dich)
        self.lich_su_giao_dich.show()
        self.thong_ke_bao_cao_mw.close()

    def mo_muc_tieu_tai_chinh(self):
        from Muc_tieu_tai_chinh_Mainwindow_ext import Ui_MainWindow_Ext
        self.muc_tieu_tai_chinh = QMainWindow()
        self.ui_muc_tieu_tai_chinh_ext = Ui_MainWindow_Ext()
        self.ui_muc_tieu_tai_chinh_ext.setupUi(self.muc_tieu_tai_chinh)
        self.muc_tieu_tai_chinh.show()
        self.thong_ke_bao_cao_mw.close()

    def mo_bct_chinh(self):
        from phantich_ext import phantich_ext
        self.phantich = QMainWindow()
        self.phantich_ext = phantich_ext()
        self.phantich_ext.setupUi(self.phantich)
        self.phantich.show()
        self.thong_ke_bao_cao_mw.close()

    def process_quaylai(self):
        # Quay lại màn hình chính
        from manhinhchinh_extend import manhinhchinh_ext
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.thong_ke_bao_cao_mw.close()  # Đóng cửa sổ hiện tại
        self.manhinhchinh_form.show()  # Hiển thị màn hình chính
