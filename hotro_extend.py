from PyQt6.QtWidgets import QMainWindow, QMessageBox
from hotro_form import Ui_hotro_form
from manhinhchinh_extend import manhinhchinh_ext

class hotro_ext(Ui_hotro_form):
    def setupUi(self, hotro_form):
        super().setupUi(hotro_form)
        self.hotro = hotro_form

        # Kết nối sự kiện
        self.btnchat.clicked.connect(self.open_chat_form)
        self.btncauhoithuonggap.clicked.connect(self.open_cauhoithuonggap_form)
        self.btnlienhetongdai.clicked.connect(self.open_lienhetongdai_form)
        self.btn_return.clicked.connect(self.process_quaylai)

    def open_chat_form(self):
        from chat_extend import chat_ext
        self.chat_form = QMainWindow()
        self.ui_chat_form = chat_ext()
        self.ui_chat_form.setupUi(self.chat_form)

        self.hotro.close()
        self.chat_form.show()

    def open_cauhoithuonggap_form(self):
        from cauhoithuonggap_extend import cauhoithuonggap_ext
        self.cauhoithuonggap_form = QMainWindow()
        self.ui_cauhoithuonggap_form = cauhoithuonggap_ext()
        self.ui_cauhoithuonggap_form.setupUi(self.cauhoithuonggap_form)

        self.hotro.close()
        self.cauhoithuonggap_form.show()

    def open_lienhetongdai_form(self):
        QMessageBox.information(self.hotro,"Liên hệ tổng đài", "Để được hỗ trợ vui lòng liên hệ: 1900 368686")

    def process_quaylai(self):
        # Quay lại màn hình chính
        self.manhinhchinh_form = QMainWindow()
        self.ui_manhinhchinh = manhinhchinh_ext()
        self.ui_manhinhchinh.setupUi(self.manhinhchinh_form)
        self.hotro.close()  # Đóng cửa sổ hiện tại
        self.manhinhchinh_form.show()  # Hiển thị màn hình chính
