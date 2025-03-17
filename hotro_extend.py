from PyQt6.QtWidgets import QMainWindow, QMessageBox
from hotro_form import Ui_hotro_form

class hotro_ext(QMainWindow, Ui_hotro_form):
    def setupUi(self, hotro_form):
        super().setupUi(hotro_form)
        self.hotro_window = hotro_form

        # Kết nối sự kiện
        self.btnchat.clicked.connect(self.open_chat_form)
        self.btncauhoithuonggap.clicked.connect(self.open_cauhoithuonggap_form)
        self.btnlienhetongdai.clicked.connect(self.open_gdhtlienhetongdai)

    def open_chat_form(self):
        """Import ở đây để tránh vòng lặp"""
        from chat_extend import chat_ext  # Import trễ

        self.chat_form = QMainWindow()
        self.ui_chat_form = chat_ext()
        self.ui_chat_form.setupUi(self.chat_form)

        self.hotro_window.close()
        self.chat_form.show()

    def open_cauhoithuonggap_form(self):
        """Import ở đây để tránh vòng lặp"""
        from cauhoithuonggap_extend import cauhoithuonggap_ext

        self.cauhoithuonggap_form = QMainWindow()
        self.ui_cauhoithuonggap_form = cauhoithuonggap_ext()
        self.ui_cauhoithuonggap_form.setupUi(self.cauhoithuonggap_form)

        self.hotro_window.close()
        self.cauhoithuonggap_form.show()

    def open_gdhtlienhetongdai(self):
        QMessageBox.information(self.hotro_window,"Hỗ trợ", "Để được hỗ trợ vui lòng liên hệ: 1900 368686")