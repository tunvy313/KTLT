# Form implementation generated from reading ui file 'lich_su_giao_dich_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 687)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 31))
        self.label.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.label.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"font:bold")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btnTimKiem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTimKiem.setGeometry(QtCore.QRect(430, 82, 51, 24))
        self.btnTimKiem.setStyleSheet("border-radius: 10px;\n"
"background-color: #e9f8ff")
        self.btnTimKiem.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ic_magnifying-glass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTimKiem.setIcon(icon)
        self.btnTimKiem.setObjectName("btnTimKiem")
        self.tblLichSuGiaoDich = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tblLichSuGiaoDich.setGeometry(QtCore.QRect(10, 170, 461, 231))
        self.tblLichSuGiaoDich.setStyleSheet("background-color: #e9f8ff")
        self.tblLichSuGiaoDich.setColumnCount(4)
        self.tblLichSuGiaoDich.setObjectName("tblLichSuGiaoDich")
        self.tblLichSuGiaoDich.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 127, 17))
        self.label_5.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"border-radius: 10px")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 50, 126, 17))
        self.label_6.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 50, 127, 17))
        self.label_7.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btnTongchiTieu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTongchiTieu.setGeometry(QtCore.QRect(10, 126, 191, 32))
        self.btnTongchiTieu.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnTongchiTieu.setAutoFillBackground(False)
        self.btnTongchiTieu.setStyleSheet("border-radius: 10px;\n"
"background-color: #e9f8ff")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../calculator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTongchiTieu.setIcon(icon1)
        self.btnTongchiTieu.setIconSize(QtCore.QSize(16, 16))
        self.btnTongchiTieu.setObjectName("btnTongchiTieu")
        self.txtTongChiTieu = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTongChiTieu.setGeometry(QtCore.QRect(210, 126, 261, 31))
        self.txtTongChiTieu.setStyleSheet("border-radius: 10px;\n"
"background-color: #e9f8ff")
        self.txtTongChiTieu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtTongChiTieu.setObjectName("txtTongChiTieu")
        self.txtNgayKetThuc = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.txtNgayKetThuc.setGeometry(QtCore.QRect(290, 80, 129, 24))
        self.txtNgayKetThuc.setStyleSheet("border-radius: 10px;\n"
"background-color: #e9f8ff")
        self.txtNgayKetThuc.setObjectName("txtNgayKetThuc")
        self.txtNgayBatDau = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.txtNgayBatDau.setGeometry(QtCore.QRect(150, 80, 129, 24))
        self.txtNgayBatDau.setStyleSheet("border-radius: 10px;\n"
"background-color: #e9f8ff")
        self.txtNgayBatDau.setObjectName("txtNgayBatDau")
        self.txtLoaiGiaoDich = QtWidgets.QComboBox(parent=self.centralwidget)
        self.txtLoaiGiaoDich.setGeometry(QtCore.QRect(10, 80, 129, 24))
        self.txtLoaiGiaoDich.setStyleSheet("border-radius:10px;\n"
"background-color: #e9f8ff;")
        self.txtLoaiGiaoDich.setObjectName("txtLoaiGiaoDich")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        self.txtLoaiGiaoDich.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lich_su_giao_dich"))
        self.label.setText(_translate("MainWindow", "LỊCH SỬ GIAO DỊCH"))
        self.label_5.setText(_translate("MainWindow", "Loại giao dịch"))
        self.label_6.setText(_translate("MainWindow", "Ngày bắt đầu "))
        self.label_7.setText(_translate("MainWindow", "Ngày kết thúc"))
        self.btnTongchiTieu.setText(_translate("MainWindow", "Tính tổng chi tiêu "))
        self.txtLoaiGiaoDich.setItemText(0, _translate("MainWindow", "Loại giao dịch"))
        self.txtLoaiGiaoDich.setItemText(1, _translate("MainWindow", "Tất cả"))
        self.txtLoaiGiaoDich.setItemText(2, _translate("MainWindow", "Hoá đơn"))
        self.txtLoaiGiaoDich.setItemText(3, _translate("MainWindow", "Nhà cửa "))
        self.txtLoaiGiaoDich.setItemText(4, _translate("MainWindow", "Người thân"))
        self.txtLoaiGiaoDich.setItemText(5, _translate("MainWindow", "Chợ"))
        self.txtLoaiGiaoDich.setItemText(6, _translate("MainWindow", "Ăn uống"))
        self.txtLoaiGiaoDich.setItemText(7, _translate("MainWindow", "Di chuyển"))
        self.txtLoaiGiaoDich.setItemText(8, _translate("MainWindow", "Mua sắm"))
        self.txtLoaiGiaoDich.setItemText(9, _translate("MainWindow", "Giải trí"))
        self.txtLoaiGiaoDich.setItemText(10, _translate("MainWindow", "Làm đẹp"))
        self.txtLoaiGiaoDich.setItemText(11, _translate("MainWindow", "Sức khoẻ"))
        self.txtLoaiGiaoDich.setItemText(12, _translate("MainWindow", "Từ thiện"))
        self.txtLoaiGiaoDich.setItemText(13, _translate("MainWindow", "Đầu tư"))
        self.txtLoaiGiaoDich.setItemText(14, _translate("MainWindow", "Tiết kiệm"))
        self.txtLoaiGiaoDich.setItemText(15, _translate("MainWindow", "Học tập "))
        self.txtLoaiGiaoDich.setItemText(16, _translate("MainWindow", "Khác"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
