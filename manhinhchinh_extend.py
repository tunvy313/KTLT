from manhinhchinh_form import Ui_manhinhchinh_form
from PyQt6.QtWidgets import QMainWindow


class manhinhchinh_ext(Ui_manhinhchinh_form):
    def setupUi(self, manhinhchinh_form):
        super().setupUi(manhinhchinh_form)
        self.manhinhchinh = manhinhchinh_form

        # Connect events
        self.btn_themthunhap.clicked.connect(self.open_themkhoanthu_form)
        self.btn_themchitieu.clicked.connect(self.open_themkhoanchi_form)
        self.btn_xemlichsu.clicked.connect(self.open_lichsugiaodich_form)
        self.btn_caidat.clicked.connect(self.open_caidat_form)
        self.btn_hotro.clicked.connect(self.open_hotro_form)

    def open_themkhoanthu_form(self):
        # Mở màn hình thêm khoản thu
        from themkhoanthu_extend import themkhoanthu_ext
        self.themkhoanthu_form = QMainWindow()
        self.ui_themkhoanthu = themkhoanthu_ext()
        self.ui_themkhoanthu.setupUi(self.themkhoanthu_form)

        self.manhinhchinh.close() # Đóng màn hình chính
        self.themkhoanthu_form.show() # Hiển thị màn hình thêm khoản thu

    def open_themkhoanchi_form(self):
        # Mở màn hình thêm khoản chi
        from themkhoanchi_extend import themkhoanchi_ext
        self.themkhoanchi_form = QMainWindow()
        self.ui_themkhoanchi = themkhoanchi_ext()
        self.ui_themkhoanchi.setupUi(self.themkhoanchi_form)

        self.manhinhchinh.close()  # Đóng màn hình chính
        self.themkhoanchi_form.show()  # Hiển thị màn hình thêm khoản thu
        
    def open_lichsugiaodich_form(self):
        pass
    
    def open_caidat_form(self):
        pass
    
    def open_hotro_form(self):
        pass
