from PyQt6.QtWidgets import QMainWindow
from caidat_form import Ui_caidat_form
from manhinhchinh_extend import manhinhchinh_ext

class caidat_ext(Ui_caidat_form):
    def setupUi(self, caidat_form):
        super().setupUi(caidat_form)
        self.caidat = caidat_form

        # Connect events
        self.btn_return.clicked.connect(self.process_quaylai)
        self.btn_ngonngu.clicked.connect(self.open_cdgiaodien_form)
        self.btn_donvitien.clicked.connect(self.open_cdgiaodien_form)
        self.btn_chedosang.clicked.connect(self.open_cdgiaodien_form)
        self.btn_hienthisodu.clicked.connect(self.open_cdgiaodien_form)
        self.btn_doimatkhau.clicked.connect(self.open_cddoimk_form)
        self.btn_dangxuat.clicked.connect(self.open_cddangxuat_form)
        self.btn_xoatk.clicked.connect(self.open_cdxoataikhoan_form)
        self.btn_lknganhang.clicked.connect(self.open_vilienket_form)


    def open_cddangxuat_form(self):
        # Mở màn hình đăng xuất
        from cddangxuat_extend import cddangxuat_ext
        self.cddangxuat_form = QMainWindow()
        self.ui_cddangxuat = cddangxuat_ext()
        self.ui_cddangxuat.setupUi(self.cddangxuat_form)

        self.caidat.close()  # Đóng màn hình cài đặt
        self.cddangxuat_form.show()  # Hiển thị màn hình đăng xuất

    def open_cdgiaodien_form(self):
        # Mở màn hình tùy chỉnh giao diện
        from cdgiaodien_extend import cdgiaodien_ext
        self.cdgiaodien_form = QMainWindow()
        self.ui_cdgiaodien = cdgiaodien_ext()
        self.ui_cdgiaodien.setupUi(self.cdgiaodien_form)

        self.caidat.close()
        self.cdgiaodien_form.show()

    def open_cddoimk_form(self):
        # Mở màn hình đổi mật khẩu
        from cddoimk_extend import cddoimk_ext
        self.cddoimk_form = QMainWindow()
        self.ui_cddoimk = cddoimk_ext()
        self.ui_cddoimk.setupUi(self.cddoimk_form)

        self.caidat.close()
        self.cddoimk_form.show()

    def open_cdxoataikhoan_form(self):
        # Mở màn hình xóa tài khoản
        from cdxoataikhoan_extend import cdxoataikhoan_ext
        self.cdxoataikhoan_form = QMainWindow()
        self.ui_cdxoataikhoan = cdxoataikhoan_ext()
        self.ui_cdxoataikhoan.setupUi(self.cdxoataikhoan_form)

        self.caidat.close()
        self.cdxoataikhoan_form.show()

    def open_vilienket_form(self):
        from vilienket_extend import vilienket_ext
        self.vilienket_form = QMainWindow()
        self.ui_vilienket = vilienket_ext()
        self.ui_vilienket.setupUi(self.vilienket_form)
        self.caidat.close()
        self.vilienket_form.show()



    def process_quaylai(self):
        # Quay lại màn hình chính
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.caidat.close()  # Đóng cửa sổ hiện tại
        self.manhinhchinh_form.show()  # Hiển thị màn hình chính
