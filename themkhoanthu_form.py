# Form implementation generated from reading ui file 'themkhoanthu_form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_themkhoanthu_form(object):
    def setupUi(self, themkhoanthu_form):
        themkhoanthu_form.setObjectName("themkhoanthu_form")
        themkhoanthu_form.resize(480, 351)
        themkhoanthu_form.setMinimumSize(QtCore.QSize(0, 0))
        themkhoanthu_form.setStyleSheet("\n"
"background-color: rgb(224, 243, 253);")
        self.centralwidget = QtWidgets.QWidget(parent=themkhoanthu_form)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 31))
        self.label.setStyleSheet("background-color: rgb(154, 205, 244);\n"
"font: 16pt \"Cambria\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 12pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"Cambria\";")
        self.label_5.setObjectName("label_5")
        self.txt_ghichu = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_ghichu.setGeometry(QtCore.QRect(80, 80, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.txt_ghichu.setFont(font)
        self.txt_ghichu.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.txt_ghichu.setCursorPosition(0)
        self.txt_ghichu.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txt_ghichu.setObjectName("txt_ghichu")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 201, 61))
        self.label_6.setStyleSheet("background-color: rgb(188, 234, 255);\n"
"font: 12pt \"Cambria\";")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_6.setObjectName("label_6")
        self.txt_sotien = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_sotien.setGeometry(QtCore.QRect(80, 42, 141, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_sotien.setFont(font)
        self.txt_sotien.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.txt_sotien.setCursorPosition(0)
        self.txt_sotien.setObjectName("txt_sotien")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(320, 42, 141, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 50, 21, 20))
        self.label_7.setStyleSheet("font: 10pt \"Cambria\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 12pt \"Cambria\";")
        self.label_3.setObjectName("label_3")
        self.btn_return = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_return.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.btn_return.setStyleSheet("background-color: rgb(154, 205, 244);")
        self.btn_return.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ic_return.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_return.setIcon(icon)
        self.btn_return.setObjectName("btn_return")
        self.cbb_muctieutc = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbb_muctieutc.setGeometry(QtCore.QRect(20, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbb_muctieutc.setFont(font)
        self.cbb_muctieutc.setObjectName("cbb_muctieutc")
        self.trw_khoanthu = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.trw_khoanthu.setGeometry(QtCore.QRect(10, 141, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.trw_khoanthu.setFont(font)
        self.trw_khoanthu.setWordWrap(False)
        self.trw_khoanthu.setObjectName("trw_khoanthu")
        item_0 = QtWidgets.QTreeWidgetItem(self.trw_khoanthu)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.trw_khoanthu)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.trw_khoanthu)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.trw_khoanthu)
        self.trw_khoanthu.header().setVisible(False)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(188, 234, 255);\n"
"font: 12pt \"Cambria\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 290, 461, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_luu = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_luu.setFont(font)
        self.btn_luu.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btn_luu.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_luu.setObjectName("btn_luu")
        self.horizontalLayout.addWidget(self.btn_luu)
        self.btn_capnhat = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_capnhat.setFont(font)
        self.btn_capnhat.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_capnhat.setObjectName("btn_capnhat")
        self.horizontalLayout.addWidget(self.btn_capnhat)
        self.btn_xoa = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_xoa.setFont(font)
        self.btn_xoa.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_xoa.setObjectName("btn_xoa")
        self.horizontalLayout.addWidget(self.btn_xoa)
        self.btn_huy = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_huy.setFont(font)
        self.btn_huy.setStyleSheet("background-color: rgb(255, 194, 209);")
        self.btn_huy.setObjectName("btn_huy")
        self.horizontalLayout.addWidget(self.btn_huy)
        self.tbl_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tbl_table.setGeometry(QtCore.QRect(220, 120, 251, 161))
        self.tbl_table.setRowCount(0)
        self.tbl_table.setColumnCount(5)
        self.tbl_table.setObjectName("tbl_table")
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.txt_ghichu.raise_()
        self.label_6.raise_()
        self.dateEdit.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.btn_return.raise_()
        self.cbb_muctieutc.raise_()
        self.trw_khoanthu.raise_()
        self.label_4.raise_()
        self.horizontalLayoutWidget.raise_()
        self.tbl_table.raise_()
        self.txt_sotien.raise_()
        themkhoanthu_form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=themkhoanthu_form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        themkhoanthu_form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=themkhoanthu_form)
        self.statusbar.setObjectName("statusbar")
        themkhoanthu_form.setStatusBar(self.statusbar)

        self.retranslateUi(themkhoanthu_form)
        QtCore.QMetaObject.connectSlotsByName(themkhoanthu_form)

    def retranslateUi(self, themkhoanthu_form):
        _translate = QtCore.QCoreApplication.translate
        themkhoanthu_form.setWindowTitle(_translate("themkhoanthu_form", "Thêm khoản thu"))
        self.label.setText(_translate("themkhoanthu_form", "Thêm thu nhập"))
        self.label_2.setText(_translate("themkhoanthu_form", "<html><head/><body><p><span style=\" font-size:12pt;\">Số tiền:</span></p></body></html>"))
        self.label_5.setText(_translate("themkhoanthu_form", "<html><head/><body><p><span style=\" font-size:12pt;\">Ghi chú:</span></p></body></html>"))
        self.label_6.setText(_translate("themkhoanthu_form", "<html><head/><body><p>Chọn 1 mục tiêu tài chính:</p></body></html>"))
        self.label_7.setText(_translate("themkhoanthu_form", "<html><head/><body><p><span style=\" font-size:12pt;\">đ</span></p></body></html>"))
        self.label_3.setText(_translate("themkhoanthu_form", "<html><head/><body><p>Ngày:</p></body></html>"))
        self.trw_khoanthu.headerItem().setText(0, _translate("themkhoanthu_form", "Khoản thu"))
        __sortingEnabled = self.trw_khoanthu.isSortingEnabled()
        self.trw_khoanthu.setSortingEnabled(False)
        self.trw_khoanthu.topLevelItem(0).setText(0, _translate("themkhoanthu_form", "Thu nhập chính"))
        self.trw_khoanthu.topLevelItem(0).child(0).setText(0, _translate("themkhoanthu_form", "Lương"))
        self.trw_khoanthu.topLevelItem(0).child(1).setText(0, _translate("themkhoanthu_form", "Tiền thưởng"))
        self.trw_khoanthu.topLevelItem(0).child(2).setText(0, _translate("themkhoanthu_form", "Phụ cấp"))
        self.trw_khoanthu.topLevelItem(1).setText(0, _translate("themkhoanthu_form", "Từ hoạt động kinh doanh & đầu tư"))
        self.trw_khoanthu.topLevelItem(1).child(0).setText(0, _translate("themkhoanthu_form", "Bán hàng"))
        self.trw_khoanthu.topLevelItem(1).child(1).setText(0, _translate("themkhoanthu_form", "Đầu tư chứng khoán / cổ phiếu"))
        self.trw_khoanthu.topLevelItem(1).child(2).setText(0, _translate("themkhoanthu_form", "Lãi suất ngân hàng, tiền gửi tiết kiệm"))
        self.trw_khoanthu.topLevelItem(1).child(3).setText(0, _translate("themkhoanthu_form", "Đầu tư bất động sản"))
        self.trw_khoanthu.topLevelItem(2).setText(0, _translate("themkhoanthu_form", "Tiền trợ cấp"))
        self.trw_khoanthu.topLevelItem(2).child(0).setText(0, _translate("themkhoanthu_form", "Trợ cấp từ gia đình"))
        self.trw_khoanthu.topLevelItem(2).child(1).setText(0, _translate("themkhoanthu_form", "Quà tặng, tiền mừng"))
        self.trw_khoanthu.topLevelItem(2).child(2).setText(0, _translate("themkhoanthu_form", "Bảo hiểm xã hội, trợ cấp thất nghiệp, học bổng,..."))
        self.trw_khoanthu.topLevelItem(3).setText(0, _translate("themkhoanthu_form", "Thu nhập khác"))
        self.trw_khoanthu.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("themkhoanthu_form", "Khoản thu"))
        self.btn_luu.setText(_translate("themkhoanthu_form", "Lưu"))
        self.btn_capnhat.setText(_translate("themkhoanthu_form", "Cập nhật"))
        self.btn_xoa.setText(_translate("themkhoanthu_form", "Xóa"))
        self.btn_huy.setText(_translate("themkhoanthu_form", "Hủy bỏ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    themkhoanthu_form = QtWidgets.QMainWindow()
    ui = Ui_themkhoanthu_form()
    ui.setupUi(themkhoanthu_form)
    themkhoanthu_form.show()
    sys.exit(app.exec())
