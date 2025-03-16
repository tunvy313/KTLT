from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6.QtCore import QTimer
from gdhtcauhoithuonggap import Ui_gdhtcauhoithuonggap  # Import giao diện đã tạo từ Qt Designer
from giaodienhotro_Extend import giaodienhotro_ext  # Import giao diện hỗ trợ

class gdhtcauhoithuonggap_ext(Ui_gdhtcauhoithuonggap):
    def setupUi(self, gdhtcauhoithuonggap):
        super().setupUi(gdhtcauhoithuonggap)
        self.gdhtcauhoithuonggap_window = gdhtcauhoithuonggap

        # Kết nối sự kiện cho các nút câu hỏi
        self.btncauhoi1.clicked.connect(self.show_answer_1)
        self.btncauhoi2.clicked.connect(self.show_answer_2)
        self.btncauhoi3.clicked.connect(self.show_answer_3)
        self.btncauhoi4.clicked.connect(self.show_answer_4)
        self.btncauhoi5.clicked.connect(self.show_answer_5)
        self.btncauhoi7.clicked.connect(self.show_answer_7)
        self.btncauhoi8.clicked.connect(self.show_answer_8)
        self.btncauhoi9.clicked.connect(self.show_answer_9)

        # Kết nối sự kiện nút "btnmuiten" để quay lại giao diện hỗ trợ
        self.btnmuiten.clicked.connect(self.back_to_giaodienhotro)

    def show_answer_1(self):
        self.show_message_box("Câu trả lời", "Vào Cài đặt -> Chọn Đơn vị tiền tệ -> Chọn loại tiền mong muốn.")

    def show_answer_2(self):
        self.show_message_box("Câu trả lời", "Có, bạn sẽ nhận thông báo khi tổng chi tiêu vượt quá ngân sách đã đặt.")

    def show_answer_3(self):
        self.show_message_box("Câu trả lời", "Bạn có thể gửi email, gọi hotline hoặc sử dụng tính năng chat trực tuyến trong ứng dụng.")

    def show_answer_4(self):
        self.show_message_box("Câu trả lời",
                              "Có, ứng dụng sẽ phân tích dữ liệu tài chính và đưa ra gợi ý cắt giảm chi tiêu nếu cần.")

    def show_answer_5(self):
        self.show_message_box("Câu trả lời",
                              "Trên màn hình đăng nhập, chọn 'Quên mật khẩu', nhập email/số điện thoại đã đăng ký và làm theo hướng dẫn để đặt lại mật khẩu.")

    def show_answer_7(self):
        self.show_message_box("Câu trả lời", "Vào 'Cài đặt', chọn 'Thông báo' và bật/tắt tùy theo nhu cầu.")

    def show_answer_8(self):
        self.show_message_box("Câu trả lời", "Bạn có thể vào 'Cài đặt', chọn 'Xóa tài khoản' và xác nhận để xóa toàn bộ dữ liệu.")

    def show_answer_9(self):
        self.show_message_box("Câu trả lời", "Bạn có thể vào 'Cài đặt ngân sách', chọn thời gian theo dõi là ngày hoặc tuần.")

    def show_message_box(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def back_to_giaodienhotro(self):
        """Hàm quay lại giao diện hỗ trợ khi nhấn nút mũi tên"""
        self.giaodienhotro_form = QMainWindow()
        self.ui_giaodienhotro = giaodienhotro_ext()
        self.ui_giaodienhotro.setupUi(self.giaodienhotro_form)

        self.gdhtcauhoithuonggap_window.close()  # Đóng màn hình câu hỏi thường gặp
        self.giaodienhotro_form.show()  # Hiển thị màn hình giao diện hỗ trợ


