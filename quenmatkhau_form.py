# Form implementation generated from reading ui file 'quenmatkhau_form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_quenmatkhau_form(object):
    def setupUi(self, quenmatkhau_form):
        quenmatkhau_form.setObjectName("quenmatkhau_form")
        quenmatkhau_form.resize(480, 351)
        quenmatkhau_form.setMinimumSize(QtCore.QSize(480, 351))
        quenmatkhau_form.setMaximumSize(QtCore.QSize(480, 351))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        quenmatkhau_form.setFont(font)
        quenmatkhau_form.setStyleSheet("background-color: rgb(224, 243, 253)")
        self.centralwidget = QtWidgets.QWidget(parent=quenmatkhau_form)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_hotro = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_hotro.setGeometry(QtCore.QRect(130, 10, 231, 301))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.lbl_hotro.setFont(font)
        self.lbl_hotro.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"border-radius: 10px\n"
"")
        self.lbl_hotro.setText("")
        self.lbl_hotro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_hotro.setObjectName("lbl_hotro")
        self.txtemail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtemail.setGeometry(QtCore.QRect(150, 120, 191, 31))
        self.txtemail.setStyleSheet("border-radius: 10px\n"
"")
        self.txtemail.setText("")
        self.txtemail.setObjectName("txtemail")
        self.txtnhapmaotp = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtnhapmaotp.setGeometry(QtCore.QRect(150, 190, 191, 31))
        self.txtnhapmaotp.setStyleSheet("border-radius: 10px\n"
"")
        self.txtnhapmaotp.setText("")
        self.txtnhapmaotp.setObjectName("txtnhapmaotp")
        self.btnnhanmaotp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnnhanmaotp.setGeometry(QtCore.QRect(200, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btnnhanmaotp.setFont(font)
        self.btnnhanmaotp.setStyleSheet("background-color: rgb(250, 219, 227)")
        self.btnnhanmaotp.setObjectName("btnnhanmaotp")
        self.btndangky = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btndangky.setGeometry(QtCore.QRect(130, 280, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btndangky.setFont(font)
        self.btndangky.setStyleSheet("background-color: rgba(245, 40, 145, 0)")
        self.btndangky.setObjectName("btndangky")
        self.btnlogo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnlogo.setGeometry(QtCore.QRect(190, 30, 111, 71))
        self.btnlogo.setStyleSheet("background-color: rgba(245, 40, 145, 0);\n"
"border-radius: 10px")
        self.btnlogo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ic_logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnlogo.setIcon(icon)
        self.btnlogo.setIconSize(QtCore.QSize(40, 50))
        self.btnlogo.setObjectName("btnlogo")
        self.btntieptuc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btntieptuc.setGeometry(QtCore.QRect(200, 230, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btntieptuc.setFont(font)
        self.btntieptuc.setStyleSheet("background-color: rgb(250, 219, 227)")
        self.btntieptuc.setObjectName("btntieptuc")
        self.btn_return = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(132, 13, 30, 30))
        self.btn_return.setStyleSheet("background-color: rgba(245, 40, 145, 0)")
        self.btn_return.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ic_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_return.setIcon(icon1)
        self.btn_return.setObjectName("btn_return")
        quenmatkhau_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=quenmatkhau_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        quenmatkhau_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=quenmatkhau_form)
        self.statusbar.setObjectName("statusbar")
        quenmatkhau_form.setStatusBar(self.statusbar)

        self.retranslateUi(quenmatkhau_form)
        QtCore.QMetaObject.connectSlotsByName(quenmatkhau_form)

    def retranslateUi(self, quenmatkhau_form):
        _translate = QtCore.QCoreApplication.translate
        quenmatkhau_form.setWindowTitle(_translate("quenmatkhau_form", "Quên mật khẩu"))
        quenmatkhau_form.setWhatsThis(_translate("quenmatkhau_form", "<html><head/><body><p><img src=\":/newPrefix/i_chat.png\"/></p></body></html>"))
        self.txtemail.setPlaceholderText(_translate("quenmatkhau_form", "   Email"))
        self.txtnhapmaotp.setPlaceholderText(_translate("quenmatkhau_form", "   Nhập mã OTP"))
        self.btnnhanmaotp.setText(_translate("quenmatkhau_form", "Nhận mã OTP"))
        self.btndangky.setText(_translate("quenmatkhau_form", "Bạn chưa có tài khoản?                                   Đăng ký"))
        self.btntieptuc.setText(_translate("quenmatkhau_form", "Tiếp tục"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quenmatkhau_form = QtWidgets.QMainWindow()
    ui = Ui_quenmatkhau_form()
    ui.setupUi(quenmatkhau_form)
    quenmatkhau_form.show()
    sys.exit(app.exec())
