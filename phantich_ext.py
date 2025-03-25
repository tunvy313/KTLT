from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from phantich import Ui_MainWindow  # Import file UI được sinh ra từ pyuic6

class phantich_ext(QMainWindow, Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.manhinhchinh = MainWindow

        # Thêm layout vào fr_bieudotron để chứa biểu đồ
        self.chart_layout = QVBoxLayout(self.fr_bieudotron)

        # Hiển thị biểu đồ ban đầu (Tổng chi)
        self.current_chart = None
        self.show_expense_chart()

        # Kết nối nút bấm để chuyển đổi biểu đồ
        self.btn_tongchi_2.clicked.connect(self.show_expense_chart)
        self.btn_tongthu.clicked.connect(self.show_income_chart)
        self.btn_tietkiem.clicked.connect(self.show_savings_chart)
        self.btn_sodu.clicked.connect(self.show_balance_chart)

        # Biến tất cả nút thành nút toggle (có thể giữ trạng thái khi nhấn)
        self.btn_tongchi_2.setCheckable(True)
        self.btn_tongthu.setCheckable(True)
        self.btn_tietkiem.setCheckable(True)
        self.btn_sodu.setCheckable(True)

        # Kết nối sự kiện click với hàm đổi màu
        self.btn_tongchi_2.clicked.connect(lambda: self.highlight_button(self.btn_tongchi_2))
        self.btn_tongthu.clicked.connect(lambda: self.highlight_button(self.btn_tongthu))
        self.btn_tietkiem.clicked.connect(lambda: self.highlight_button(self.btn_tietkiem))
        self.btn_sodu.clicked.connect(lambda: self.highlight_button(self.btn_sodu))

        # Đặt màu mặc định
        self.highlight_button(self.btn_tongchi_2)  # Mặc định chọn Tổng chi

    def highlight_button(self, button):
        """Làm nổi bật nút được nhấn và reset các nút khác"""
        buttons = [self.btn_tongchi_2, self.btn_tongthu, self.btn_tietkiem, self.btn_sodu]
        for btn in buttons:
            if btn == button:
                btn.setChecked(True)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(131, 175, 208);
                        font-weight: bold;
                    }
                    QPushButton:checked {
                        background-color: rgb(131, 175, 208);
                    }
                """)
            else:
                btn.setChecked(False)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: rgb(159, 223, 255);
                        font-weight: normal;
                    }
                    QPushButton:checked {
                        background-color: rgb(159, 223, 255);
                    }
                """)

    def show_expense_chart(self):
        """Hiển thị biểu đồ khoản chi"""
        labels = ["Nhà", "Ăn uống", "Mua sắm"]
        sizes = [50, 25, 25]
        colors = ["#8B0000", "#B22222", "#E57373"]
        explode = (0.1, 0, 0)
        self.update_chart(labels, sizes, colors, explode)

    def show_income_chart(self):
        """Hiển thị biểu đồ khoản thu"""
        labels = ["Chính", "Đầu tư", "Khác"]
        sizes = [40, 35, 25]
        colors = ["#0F5C4D", "#1D7A5D", "#5AA897"]
        explode = (0.1, 0, 0)
        self.update_chart(labels, sizes, colors, explode)

    def show_savings_chart(self):
        """Hiển thị biểu đồ khoản thu"""
        labels = ["Giáo dục", "Du lịch", "Khác"]
        sizes = [64, 15, 11]
        colors = ["#0B2545", "#144E78", "#57A0D3"]
        explode = (0.1, 0, 0)
        self.update_chart(labels, sizes, colors, explode)

    def show_balance_chart(self):
        """Hiển thị biểu đồ khoản thu"""
        labels = ["Tổng thu", "Tổng chi", "Tiết kiệm"]
        sizes = [40, 35, 25]
        colors = ["#FFD700", "#FFEB73", "#FFF7B2"]
        explode = (0.1, 0, 0)
        self.update_chart(labels, sizes, colors, explode)

    def update_chart(self, labels, sizes, colors, explode):
        """Cập nhật biểu đồ trong fr_bieudotron"""
        # Xóa biểu đồ cũ nếu có
        if self.current_chart:
            self.chart_layout.removeWidget(self.current_chart)
            self.current_chart.deleteLater()

        # Vẽ biểu đồ mới
        fig, ax = plt.subplots(figsize=(4, 2))
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, autopct='%1.0f%%', colors=colors,
            explode=explode, startangle=140, textprops={'fontsize': 8, 'color': "black"}
        )

        for text in texts + autotexts:
            text.set_fontweight("bold")

        fig.patch.set_facecolor("#E0F3FD")
        ax.set_facecolor("#E0F3FD")

        # Nhúng vào giao diện
        self.current_chart = FigureCanvas(fig)
        self.chart_layout.addWidget(self.current_chart)

