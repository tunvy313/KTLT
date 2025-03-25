from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QColor
from PyQt6 import QtGui
import sys
from thongbao_chinh import Ui_MainWindow  # Import giao diện từ file .py đã tạo bằng pyuic6

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
            chi_tieu = float(self.le_chitieu_so.text())
            han_muc = float(self.lbl_hanmuc_so.text())

            if han_muc == 0:
                return

            # Tính toán tỷ lệ %
            percent = (chi_tieu / han_muc) * 100
            self.le_chitieu_per.setText(f"{percent:.0f}%")

            # Điều chỉnh kích thước dựa trên tỷ lệ %
            width = min(max(int(percent), 50), 200)
            self.le_chitieu_per.setFixedWidth(width)

            # So sánh độ dài và đổi màu
            if len(self.le_chitieu_per.text()) > len(self.le_hanmuc_per.text()):
                self.le_chitieu_per.setStyleSheet("background-color: red; color: black;")
                self.le_hanmuc_per.setStyleSheet("background-color: lightgreen; color: black;")
            else:
                self.le_chitieu_per.setStyleSheet("background-color: lightgreen; color: black;")
                self.le_hanmuc_per.setStyleSheet("background-color: red; color: black;")

        except ValueError:
            self.le_chitieu_per.setText("0%")
            self.le_chitieu_per.setStyleSheet("background-color: lightgreen; color: black;")
