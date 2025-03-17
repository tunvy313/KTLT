from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import QTimer
from chat_form import Ui_chat_form  # Import giao diện đã tạo từ Qt Designer
from hotro_extend import hotro_ext  # Import giao diện hỗ trợ

class chat_ext(QMainWindow, Ui_chat_form):
    def setupUi(self, chat_form):
        super().setupUi(chat_form)
        self.chat_window = chat_form

        # Đặt placeholder mặc định
        self.txtnhaptinnhan.setPlaceholderText("Nhập tin nhắn")

        # Khi mở giao diện, hệ thống tự động gửi tin nhắn chào mừng
        self.tbthoptinnhan.append("FinD: Xin chào, tôi có thể giúp gì cho bạn!")
        # Kết nối nút gửi tin nhắn với hàm xử lý gửi tin
        self.tbnguitinnhan.clicked.connect(self.send_message)

        # Kết nối sự kiện nút "btn_return" để quay lại giao diện hỗ trợ
        self.btn_return.clicked.connect(self.back_to_hotro_form)

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

    def back_to_hotro_form(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.hotro_form = QMainWindow()
        self.ui_hotro_form = hotro_ext()
        self.ui_hotro_form.setupUi(self.hotro_form)

        self.chat_window.close()  # Đóng màn hình câu hỏi thường gặp
        self.hotro_form.show()  # Hiển thị màn hình giao diện hỗ trợ
