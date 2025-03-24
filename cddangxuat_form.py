# Form implementation generated from reading ui file 'cddangxuat_form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cddangxuat_form(object):
    def setupUi(self, cddangxuat_form):
        cddangxuat_form.setObjectName("cddangxuat_form")
        cddangxuat_form.resize(480, 351)
        cddangxuat_form.setStyleSheet("background-color: rgb(224, 243, 253);")
        self.centralwidget = QtWidgets.QWidget(parent=cddangxuat_form)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_return = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.btn_return.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.btn_return.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ic_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_return.setIcon(icon)
        self.btn_return.setObjectName("btn_return")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 31))
        self.label.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"font: 16pt \"Cambria\";")
        self.label.setObjectName("label")
        self.lbl_doimk = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_doimk.setGeometry(QtCore.QRect(110, 90, 261, 141))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_doimk.setFont(font)
        self.lbl_doimk.setStyleSheet("border-radius:10px;\n"
"font: 13pt \"Cambria\";\n"
"background-color: rgb(146, 214, 255);")
        self.lbl_doimk.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lbl_doimk.setObjectName("lbl_doimk")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 130, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:10px;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_huybo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_huybo.setGeometry(QtCore.QRect(150, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_huybo.setFont(font)
        self.btn_huybo.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_huybo.setObjectName("btn_huybo")
        self.btn_dangxuat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_dangxuat.setGeometry(QtCore.QRect(260, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dangxuat.setFont(font)
        self.btn_dangxuat.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_dangxuat.setObjectName("btn_dangxuat")
        self.label.raise_()
        self.btn_return.raise_()
        self.lbl_doimk.raise_()
        self.label_2.raise_()
        self.btn_huybo.raise_()
        self.btn_dangxuat.raise_()
        cddangxuat_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=cddangxuat_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        cddangxuat_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=cddangxuat_form)
        self.statusbar.setObjectName("statusbar")
        cddangxuat_form.setStatusBar(self.statusbar)

        self.retranslateUi(cddangxuat_form)
        QtCore.QMetaObject.connectSlotsByName(cddangxuat_form)

    def retranslateUi(self, cddangxuat_form):
        _translate = QtCore.QCoreApplication.translate
        cddangxuat_form.setWindowTitle(_translate("cddangxuat_form", "Đăng xuất"))
        self.label.setText(_translate("cddangxuat_form", "<html><head/><body><p align=\"center\">Tài khoản và bảo mật</p></body></html>"))
        self.lbl_doimk.setText(_translate("cddangxuat_form", "Đăng xuất"))
        self.label_2.setText(_translate("cddangxuat_form", "Bạn xác nhận đăng xuất khỏi thiết bị?"))
        self.btn_huybo.setText(_translate("cddangxuat_form", "Hủy bỏ"))
        self.btn_dangxuat.setText(_translate("cddangxuat_form", "Đăng xuất"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cddangxuat_form = QtWidgets.QMainWindow()
    ui = Ui_cddangxuat_form()
    ui.setupUi(cddangxuat_form)
    cddangxuat_form.show()
    sys.exit(app.exec())
