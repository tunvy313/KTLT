from PyQt6.QtWidgets import QMainWindow
from cdxoataikhoan_form import Ui_cdxoataikhoan_form
from caidat_extend import caidat_ext

class cdxoataikhoan_ext(Ui_cdxoataikhoan_form):

    def setupUi(self, cdxoataikhoan_form):
        super().setupUi(cdxoataikhoan_form)
        self.cdxoataikhoan = cdxoataikhoan_form

        # Connect events
        self.btn_xoa.clicked.connect(self.process_xoatk)
        self.btn_huybo.clicked.connect(self.process_quaylai)
        self.btn_return.clicked.connect(self.process_quaylai)

    def process_xoatk(self):
        # Chuyển sang màn hình xác nhận xóa tài khoản
        from cdxoataikhoan2_extend import cdxoataikhoan2_ext
        self.cdxoataikhoan2_form = QMainWindow()
        self.ui_cdxoataikhoan2 = cdxoataikhoan2_ext()
        self.ui_cdxoataikhoan2.setupUi(self.cdxoataikhoan2_form)

        self.cdxoataikhoan.close()
        self.cdxoataikhoan2_form.show()

    def process_quaylai(self):
        # Quay lại màn hình cài đặt
        self.caidat_form = QMainWindow()
        self.ui_caidat = caidat_ext()
        self.ui_caidat.setupUi(self.caidat_form)

        self.cdxoataikhoan.close()  # Đóng cửa sổ hiện tại
        self.caidat_form.show()  # Hiển thị màn hình cài đặt