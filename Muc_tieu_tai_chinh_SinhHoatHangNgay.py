# Form implementation generated from reading ui file 'Muc_tieu_tai_chinh_SinhHoatHangNgay.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SinhHoatHangNgay(object):
    def setupUi(self, SinhHoatHangNgay):
        SinhHoatHangNgay.setObjectName("SinhHoatHangNgay")
        SinhHoatHangNgay.resize(480, 351)
        self.centralwidget = QtWidgets.QWidget(parent=SinhHoatHangNgay)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNgayKetThuc = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.txtNgayKetThuc.setGeometry(QtCore.QRect(260, 160, 210, 35))
        self.txtNgayKetThuc.setStyleSheet("background-color:#e9f8ff;\n"
"border-radius:10px")
        self.txtNgayKetThuc.setObjectName("txtNgayKetThuc")
        self.txtSoTienCanGop = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtSoTienCanGop.setGeometry(QtCore.QRect(250, 205, 210, 35))
        self.txtSoTienCanGop.setStyleSheet("border-radius:10px;\n"
"background-color:#e9f8ff\n"
"")
        self.txtSoTienCanGop.setObjectName("txtSoTienCanGop")
        self.btnTinhTien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTinhTien.setGeometry(QtCore.QRect(10, 205, 231, 35))
        self.btnTinhTien.setStyleSheet("background-color:#e9f8ff;\n"
"border-radius:10px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ic_calculator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTinhTien.setIcon(icon)
        self.btnTinhTien.setObjectName("btnTinhTien")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 461, 51))
        self.label_2.setStyleSheet("border-radius: 10px")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../ic_nen1.png"))
        self.label_2.setObjectName("label_2")
        self.txtSoTienMucTieu = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtSoTienMucTieu.setGeometry(QtCore.QRect(260, 100, 210, 35))
        self.txtSoTienMucTieu.setStyleSheet("border-radius:10px;\n"
"background-color:#e9f8ff\n"
"")
        self.txtSoTienMucTieu.setObjectName("txtSoTienMucTieu")
        self.btnXacNhan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnXacNhan.setGeometry(QtCore.QRect(70, 250, 151, 32))
        self.btnXacNhan.setStyleSheet("background-color: rgb(255, 194, 209);\n"
"border-radius:10px")
        self.btnXacNhan.setObjectName("btnXacNhan")
        self.txtNgayBatDau = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.txtNgayBatDau.setGeometry(QtCore.QRect(10, 160, 210, 35))
        self.txtNgayBatDau.setStyleSheet("background-color:#e9f8ff;\n"
"border-radius:10px")
        self.txtNgayBatDau.setObjectName("txtNgayBatDau")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 141, 16))
        self.label_3.setObjectName("label_3")
        self.txtTenQuy = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTenQuy.setGeometry(QtCore.QRect(10, 100, 210, 35))
        self.txtTenQuy.setStyleSheet("border-radius:10px;\n"
"background-color: #e9f8ff")
        self.txtTenQuy.setObjectName("txtTenQuy")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(265, 140, 111, 16))
        self.label_4.setObjectName("label_4")
        self.btnQuayLai = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnQuayLai.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.btnQuayLai.setStyleSheet("background-color: rgba(245, 40, 145, 0);")
        self.btnQuayLai.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ic_arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnQuayLai.setIcon(icon1)
        self.btnQuayLai.setObjectName("btnQuayLai")
        self.btnXemLai = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnXemLai.setGeometry(QtCore.QRect(230, 250, 151, 32))
        self.btnXemLai.setStyleSheet("background-color: rgb(255, 194, 209);\n"
"border-radius:10px")
        self.btnXemLai.setObjectName("btnXemLai")
        SinhHoatHangNgay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SinhHoatHangNgay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 24))
        self.menubar.setObjectName("menubar")
        SinhHoatHangNgay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SinhHoatHangNgay)
        self.statusbar.setObjectName("statusbar")
        SinhHoatHangNgay.setStatusBar(self.statusbar)

        self.retranslateUi(SinhHoatHangNgay)
        QtCore.QMetaObject.connectSlotsByName(SinhHoatHangNgay)

    def retranslateUi(self, SinhHoatHangNgay):
        _translate = QtCore.QCoreApplication.translate
        SinhHoatHangNgay.setWindowTitle(_translate("SinhHoatHangNgay", "Muc_tieu_tai_chinh_SinhHoatHangNgay"))
        self.btnTinhTien.setText(_translate("SinhHoatHangNgay", "Số tiền bạn cần góp mỗi ngày là:"))
        self.label.setText(_translate("SinhHoatHangNgay", "SINH HOẠT HẰNG NGÀY "))
        self.btnXacNhan.setText(_translate("SinhHoatHangNgay", "Xác nhận lập quỹ"))
        self.label_3.setText(_translate("SinhHoatHangNgay", "Ngày bắt đầu "))
        self.label_4.setText(_translate("SinhHoatHangNgay", "Ngày kết thúc"))
        self.btnXemLai.setText(_translate("SinhHoatHangNgay", "Các loại quỹ hiện có"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SinhHoatHangNgay = QtWidgets.QMainWindow()
    ui = Ui_SinhHoatHangNgay()
    ui.setupUi(SinhHoatHangNgay)
    SinhHoatHangNgay.show()
    sys.exit(app.exec())
