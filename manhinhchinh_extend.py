from manhinhchinh_form import Ui_manhinhchinh_form
from PyQt6.QtWidgets import QMainWindow
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ChartCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(5, 3), dpi=100)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

    def draw_chart(self, time_period="Month"):
        """Hàm vẽ biểu đồ Stacked Bar Chart"""
        self.ax.clear()  # Xóa dữ liệu cũ
        self.ax.set_facecolor("#E9F8FF")

        # Dữ liệu giả lập (tùy chỉnh theo yêu cầu)
        months = ["10/2024", "11/2024", "12/2024", "1/2025", "2/2025"]
        x = np.arange(len(months))
        income = [5, 10, 7, 5, 6]  # Thu nhập
        expense = [4, 12, 6, 4, 5]  # Chi tiêu
        savings = [3, 5, 4, 3, 2]  # Tiết kiệm

        # Vẽ biểu đồ stacked bar
        bar1 = self.ax.bar(x, income, color="#1D860D", label="Thu")
        bar2 = self.ax.bar(x, expense, bottom=income, color="#D62828", label="Chi")
        bar3 = self.ax.bar(x, savings, bottom=np.array(income) + np.array(expense), color="#2568D8", label="Tiết kiệm")

        # Cấu hình hiển thị trục x/y
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(months)
        self.ax.set_yticks(range(0, 35, 10))
        self.ax.set_yticklabels(["0", "10M", "20M", "30M"])
        self.ax.legend()
        self.ax.grid(axis="y", linestyle="--", alpha=0.7)

        self.draw()  # Cập nhật biểu đồ
        
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

        # Thêm biểu đồ vào `fr_bieudo`
        layout = QVBoxLayout(self.fr_bieudo)
        self.chart = ChartCanvas(self.fr_bieudo)
        layout.addWidget(self.chart)
        
        # Cập nhật biểu đồ khi chọn thời gian
        self.time_options.currentTextChanged.connect(self.update_chart)
        self.chart.draw_chart()  # Vẽ biểu đồ ban đầu

    def update_chart(self):
        """Hàm gọi lại khi chọn chế độ thời gian"""
        selected_time = self.time_options.currentText()
        self.chart.draw_chart(time_period=selected_time)
        
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
