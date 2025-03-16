from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import QTimer
from gdhtchat import Ui_gdhtchat  # Import giao diện đã tạo từ Qt Designer
from giaodienhotro_Extend import giaodienhotro_ext  # Import giao diện hỗ trợ

class gdhtchat_ext(QMainWindow, Ui_gdhtchat):
    def setupUi(self, gdhtchat):
        super().setupUi(gdhtchat)
        self.chat_window = gdhtchat

        # Đặt placeholder mặc định
        self.txtnhaptinnhan.setPlaceholderText("Nhập tin nhắn")

        # Khi mở giao diện, hệ thống tự động gửi tin nhắn chào mừng
        self.tbthoptinnhan.append("FinD: Xin chào, tôi có thể giúp gì cho bạn!")
        # Kết nối nút gửi tin nhắn với hàm xử lý gửi tin
        self.tbnguitinnhan.clicked.connect(self.send_message)

        # Kết nối sự kiện nút "btnmuiten" để quay lại giao diện hỗ trợ
        self.btnmuiten.clicked.connect(self.back_to_giaodienhotro)

    def send_message(self):
        # Lấy nội dung tin nhắn từ ô nhập liệu
        user_message = self.txtnhaptinnhan.text().strip()

        if user_message:
            # Hiển thị tin nhắn của người dùng trong khung chat
            self.tbthoptinnhan.append(f"Bạn: {user_message}")

            # Hiển thị phản hồi từ hệ thống
            self.tbthoptinnhan.append("FinD: Bạn vui lòng chờ ít phút!")

            # Xóa nội dung ô nhập tin nhắn
            self.txtnhaptinnhan.clear()
            self.txtnhaptinnhan.setPlaceholderText("Nhập tin nhắn")

    def back_to_giaodienhotro(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.giaodienhotro_form = QMainWindow()
        self.ui_giaodienhotro = giaodienhotro_ext()
        self.ui_giaodienhotro.setupUi(self.giaodienhotro_form)

        self.chat_window.close()  # Đóng màn hình câu hỏi thường gặp
        self.giaodienhotro_form.show()  # Hiển thị màn hình giao diện hỗ trợ
