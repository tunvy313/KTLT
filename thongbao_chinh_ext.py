from thongbao_chinh import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

class thongbao_chinh_ext(QtWidgets.QMainWindow, Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.manhinhchinh = MainWindow
        self.le_hanmuc_per.setText("100%")
        self.le_hanmuc_per.setReadOnly(True)
    # Kết nối sự kiện thay đổi văn bản
        self.le_chitieu_so.textChanged.connect(self.calculate_percentage)

    def calculate_percentage(self):
        try:
            # Lấy dữ liệu từ giao diện
            chi_tieu_text = self.le_chitieu_so.text().strip()
            han_muc_text = self.lbl_hanmuc_so.text().strip()

            # Kiểm tra đầu vào hợp lệ
            if not chi_tieu_text or not han_muc_text:
                return

            chi_tieu = float(chi_tieu_text)
            han_muc = float(han_muc_text)

            if han_muc == 0:
                self.le_chitieu_per.setText("0%")
                self.le_chitieu_per.setStyleSheet("background-color: lightgray; color: black;")
                return

            # Tính phần trăm
            percent = (chi_tieu / han_muc) * 100
            percent_text = f"{percent:.0f}%"
            self.le_chitieu_per.setText(percent_text)

            # Điều chỉnh kích thước dựa trên tỷ lệ %
            hanmuc_width = self.le_hanmuc_per.width()
            width = min(max(int(hanmuc_width*percent/100), 0), 150)
            self.le_chitieu_per.setFixedWidth(width)

            # So sánh tỷ lệ và đổi màu hợp lý
            if percent > 100:
                self.le_chitieu_per.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                self.le_hanmuc_per.setStyleSheet("background-color: lightgreen; color: black;")
            else:
                self.le_chitieu_per.setStyleSheet("background-color: lightgreen; color: black;")
                self.le_hanmuc_per.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        except ValueError:
            self.le_chitieu_per.setText("Lỗi")
            self.le_chitieu_per.setStyleSheet("background-color: gray; color: white;")
