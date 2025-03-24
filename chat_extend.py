from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QTimer
from chat_form import Ui_chat_form  # Giao diện chat
from hotro_extend import hotro_ext  # Giao diện hỗ trợ

from fuzzywuzzy import fuzz  # Thư viện fuzzy matching


class chat_ext(QMainWindow, Ui_chat_form):
    def setupUi(self, chat_form):
        super().setupUi(chat_form)
        self.chat_window = chat_form

        # Thiết lập UI
        self.txtnhaptinnhan.setPlaceholderText("Nhập tin nhắn của bạn")
        self.tbthoptinnhan.append("FinD: Xin chào, tôi có th giúp gì cho bạn?")

        # Kết nối các nút
        self.tbnguitinnhan.clicked.connect(self.send_message)
        self.btn_return.clicked.connect(self.back_to_hotro_form)

        self.txtnhaptinnhan.returnPressed.connect(self.send_message)

        # Danh sách từ khóa và câu trả lời
        self.auto_reply_data = {
            "chào": "Chào bạn, tôi có thể giúp gì cho bạn.",
            "chi tiêu": "Bạn có thể thêm khoản chi trong mục 'Chi', nhập số tiền, danh mục và ghi chú.",
            "ngôn ngữ": "Bạn có thể thay đổi ngôn ngữ trong phần 'Cài đặt'.",
            "mật khẩu": "Bạn có thể thay đổi mật khẩu trong phần 'Cài đặt'.",
            "ngân sách": "Đặt ngân sách hàng tháng giúp bạn kiểm soát chi tiêu hiệu quả.",
            "thu nhập": "Thêm khoản thu nhập bằng cách vào mục 'Thu', nhập nguồn thu, số tiền và ngày.",
            "khoản thu": "Hãy vào mục 'Thu' để nhập thông tin thu nhập của bạn.",
            "khoản chi": "Trong mục 'Chi', bạn có thể thêm chi tiết khoản chi, danh mục và phương thức thanh toán.",
            "phương thức thanh toán": "Ứng dụng hỗ trợ thanh toán qua tiền mặt, ngân hàng.",
            "ngân hàng": "Hệ thống hỗ trợ liên kết tài khoản ngân hàng khi thêm khoản chi.",
            "lưu dữ liệu": "Thông tin bạn nhập sẽ được lưu tự động vào cơ sở dữ liệu.",
            "thống kê": "Bạn có thể xem biểu đồ thống kê thu/chi trong mục 'Báo cáo'.",
            "báo cáo": "Mục 'Báo cáo' cung cấp thống kê chi tiết về tài chính cá nhân của bạn.",
            "xem lịch sử": "Bạn có thể xem lại các khoản thu/chi tại mục 'Lịch sử giao dịch'.",
            "mục tiêu tài chính": "Bạn có thể đặt mục tiêu tiết kiệm hoặc chi tiêu tại mục 'Mục tiêu'.",
            "tiết kiệm": "Thiết lập mục tiêu tiết kiệm để theo dõi tiến độ và kiểm soát chi tiêu.",
            "phân tích": "Ứng dụng sẽ phân tích dữ liệu thu/chi để đề xuất tối ưu tài chính.",
            "đề xuất": "Dựa vào hành vi tài chính, ứng dụng sẽ đưa ra các đề xuất hữu ích.",
            "số dư": "Số dư được cập nhật tự động sau mỗi lần nhập khoản thu/chi.",
            "đăng nhập": "Bạn có thể đăng nhập bằng email hoặc số điện thoại đã đăng ký.",
            "đăng ký": "Nếu chưa có tài khoản, bạn có thể đăng ký bằng thông tin cá nhân cơ bản."
        }
    def send_message(self):
        # Lấy tin nhắn người dùng
        user_message = self.txtnhaptinnhan.text().strip()
        if user_message:
            self.tbthoptinnhan.append(f"Bạn: {user_message}")
            reply = self.get_auto_reply(user_message)
            self.tbthoptinnhan.append(f"FinD: {reply}")
            self.txtnhaptinnhan.clear()
            self.txtnhaptinnhan.setPlaceholderText("Nhập tin nhắn của bạn")

    def get_auto_reply(self, message):
        # So khớp mờ với các từ khóa
        message_lower = message.lower()
        best_score = 0
        best_reply = None

        for keyword, reply in self.auto_reply_data.items():
            score = fuzz.partial_ratio(message_lower, keyword)
            if score > best_score:
                best_score = score
                best_reply = reply

        if best_score >= 70:
            return best_reply
        else:
            return "Bạn vui lòng đợi trong ít phút."

    def back_to_hotro_form(self):
        self.hotro_form = QMainWindow()
        self.ui_hotro_form = hotro_ext()
        self.ui_hotro_form.setupUi(self.hotro_form)

        self.chat_window.close()
        self.hotro_form.show()
