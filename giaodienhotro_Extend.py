from PyQt6.QtWidgets import QMainWindow, QMessageBox
from giaodienhotro import Ui_Giaodienhotro

class giaodienhotro_ext(QMainWindow, Ui_Giaodienhotro):
    def setupUi(self, giaodienhotro):
        super().setupUi(giaodienhotro)
        self.hotro_window = giaodienhotro

        # Kết nối sự kiện
        self.btnchat.clicked.connect(self.open_gdhtchat)
        self.btncauhoithuonggap.clicked.connect(self.open_gdhtcauhoithuonggap)
        self.btnlienhetongdai.clicked.connect(self.open_gdhtlienhetongdai)

    def open_gdhtchat(self):
        """Import ở đây để tránh vòng lặp"""
        from gdhtchat_Extend import gdhtchat_ext  # Import trễ

        self.gdhtchat_form = QMainWindow()
        self.ui_gdhtchat = gdhtchat_ext()
        self.ui_gdhtchat.setupUi(self.gdhtchat_form)

        self.hotro_window.close()
        self.gdhtchat_form.show()

    def open_gdhtcauhoithuonggap(self):
        """Import ở đây để tránh vòng lặp"""
        from gdhtcauhoithuonggap_Extend import gdhtcauhoithuonggap_ext

        self.gdhtcauhoithuonggap_form = QMainWindow()
        self.ui_gdhtcauhoithuonggap = gdhtcauhoithuonggap_ext()
        self.ui_gdhtcauhoithuonggap.setupUi(self.gdhtcauhoithuonggap_form)

        self.hotro_window.close()
        self.gdhtcauhoithuonggap_form.show()

    def open_gdhtlienhetongdai(self):
        QMessageBox.information(self.hotro_window,"Hỗ trợ", "Để được hỗ trợ vui lòng liên hệ: 1900 368686")