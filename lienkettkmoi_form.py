# Form implementation generated from reading ui file 'lienkettkmoi_form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_lienkettkmoi_form(object):
    def setupUi(self, lienkettkmoi_form):
        lienkettkmoi_form.setObjectName("lienkettkmoi_form")
        lienkettkmoi_form.resize(480, 351)
        lienkettkmoi_form.setStyleSheet("background-color: rgb(224, 243, 253);")
        self.centralwidget = QtWidgets.QWidget(parent=lienkettkmoi_form)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 31))
        self.label.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"font: 16pt \"Cambria\";")
        self.label.setObjectName("label")
        self.btn_return = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.btn_return.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.btn_return.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_return.setIcon(icon)
        self.btn_return.setObjectName("btn_return")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 60, 401, 191))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(188, 234, 255);\n"
"font: 12pt \"Cambria\";\n"
"border-radius:5px")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 87, 361, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txt_timnh = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.txt_timnh.setFont(font)
        self.txt_timnh.setStyleSheet("")
        self.txt_timnh.setObjectName("txt_timnh")
        self.verticalLayout.addWidget(self.txt_timnh)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txt_stk = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.txt_stk.setFont(font)
        self.txt_stk.setObjectName("txt_stk")
        self.verticalLayout.addWidget(self.txt_stk)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.txt_ten = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.txt_ten.setFont(font)
        self.txt_ten.setObjectName("txt_ten")
        self.verticalLayout.addWidget(self.txt_ten)
        self.btn_huy = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_huy.setGeometry(QtCore.QRect(90, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_huy.setFont(font)
        self.btn_huy.setStyleSheet("background-color: rgb(255, 194, 209);\n"
"")
        self.btn_huy.setObjectName("btn_huy")
        self.btn_lienket = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_lienket.setGeometry(QtCore.QRect(270, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_lienket.setFont(font)
        self.btn_lienket.setStyleSheet("background-color: rgb(255, 194, 209);\n"
"")
        self.btn_lienket.setObjectName("btn_lienket")
        lienkettkmoi_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=lienkettkmoi_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        lienkettkmoi_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=lienkettkmoi_form)
        self.statusbar.setObjectName("statusbar")
        lienkettkmoi_form.setStatusBar(self.statusbar)

        self.retranslateUi(lienkettkmoi_form)
        QtCore.QMetaObject.connectSlotsByName(lienkettkmoi_form)

    def retranslateUi(self, lienkettkmoi_form):
        _translate = QtCore.QCoreApplication.translate
        lienkettkmoi_form.setWindowTitle(_translate("lienkettkmoi_form", "Liên kết tài khoản mới"))
        self.label.setText(_translate("lienkettkmoi_form", "<html><head/><body><p align=\"center\">Liên kết tài khoản mới</p></body></html>"))
        self.label_6.setText(_translate("lienkettkmoi_form", "  Thông tin liên kết"))
        self.label_4.setText(_translate("lienkettkmoi_form", "Tên ngân hàng:"))
        self.txt_timnh.setPlaceholderText(_translate("lienkettkmoi_form", "Tên ngân hàng"))
        self.label_2.setText(_translate("lienkettkmoi_form", "Số thẻ / tài khoản:"))
        self.txt_stk.setPlaceholderText(_translate("lienkettkmoi_form", "Số thẻ / tài khoản"))
        self.label_3.setText(_translate("lienkettkmoi_form", "Tên chủ thẻ:"))
        self.txt_ten.setPlaceholderText(_translate("lienkettkmoi_form", "Tên chủ thẻ"))
        self.btn_huy.setText(_translate("lienkettkmoi_form", "Hủy bỏ"))
        self.btn_lienket.setText(_translate("lienkettkmoi_form", "Liên kết ngay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lienkettkmoi_form = QtWidgets.QMainWindow()
    ui = Ui_lienkettkmoi_form()
    ui.setupUi(lienkettkmoi_form)
    lienkettkmoi_form.show()
    sys.exit(app.exec())
