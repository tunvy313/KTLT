# Form implementation generated from reading ui file 'giaodienhotro.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Giaodienhotro(object):
    def setupUi(self, Giaodienhotro):
        Giaodienhotro.setObjectName("Giaodienhotro")
        Giaodienhotro.resize(480, 351)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(13)
        Giaodienhotro.setFont(font)
        Giaodienhotro.setStyleSheet("background-color: rgb(224, 243, 253)")
        self.centralwidget = QtWidgets.QWidget(parent=Giaodienhotro)
        self.centralwidget.setObjectName("centralwidget")
        self.lblhotro = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblhotro.setGeometry(QtCore.QRect(0, 0, 480, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.lblhotro.setFont(font)
        self.lblhotro.setStyleSheet("background-color: rgb(154, 205, 244)")
        self.lblhotro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblhotro.setObjectName("lblhotro")
        self.lblxinchao = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblxinchao.setGeometry(QtCore.QRect(70, 50, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lblxinchao.setFont(font)
        self.lblxinchao.setStyleSheet("background-color: rgb(150, 210, 240);\n"
"border-radius: 10px")
        self.lblxinchao.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblxinchao.setObjectName("lblxinchao")
        self.btnchat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnchat.setGeometry(QtCore.QRect(120, 110, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnchat.sizePolicy().hasHeightForWidth())
        self.btnchat.setSizePolicy(sizePolicy)
        self.btnchat.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnchat.setFont(font)
        self.btnchat.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnchat.setStyleSheet("background-color: rgb(171, 200, 223)")
        self.btnchat.setIconSize(QtCore.QSize(18, 18))
        self.btnchat.setCheckable(False)
        self.btnchat.setAutoRepeatDelay(300)
        self.btnchat.setObjectName("btnchat")
        self.btnlienhetongdai = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnlienhetongdai.setGeometry(QtCore.QRect(120, 160, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnlienhetongdai.setFont(font)
        self.btnlienhetongdai.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnlienhetongdai.setStyleSheet("background-color: rgb(171, 200, 223)\n"
"")
        self.btnlienhetongdai.setIconSize(QtCore.QSize(18, 18))
        self.btnlienhetongdai.setObjectName("btnlienhetongdai")
        self.btncauhoithuonggap = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btncauhoithuonggap.setGeometry(QtCore.QRect(120, 210, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btncauhoithuonggap.setFont(font)
        self.btncauhoithuonggap.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btncauhoithuonggap.setStyleSheet("background-color: rgb(171, 200, 223)")
        self.btncauhoithuonggap.setIconSize(QtCore.QSize(18, 18))
        self.btncauhoithuonggap.setObjectName("btncauhoithuonggap")
        self.btnmuiten = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnmuiten.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.btnmuiten.setStyleSheet("background-color: rgb(154, 205, 244)")
        self.btnmuiten.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/angle-left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnmuiten.setIcon(icon)
        self.btnmuiten.setObjectName("btnmuiten")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 31, 31))
        self.pushButton.setStyleSheet("background-color: rgba(245, 54, 145, 0);\n"
"border-radius: 10px")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/i_canhan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 33))
        self.pushButton.setObjectName("pushButton")
        self.btn_chat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_chat.setGeometry(QtCore.QRect(124, 115, 41, 31))
        self.btn_chat.setStyleSheet("background-color: rgba(245, 54, 145, 0);\n"
"border-radius: 10px")
        self.btn_chat.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/i_chat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_chat.setIcon(icon2)
        self.btn_chat.setIconSize(QtCore.QSize(20, 20))
        self.btn_chat.setObjectName("btn_chat")
        self.btn_tuvan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_tuvan.setGeometry(QtCore.QRect(124, 165, 41, 31))
        self.btn_tuvan.setStyleSheet("background-color: rgba(245, 54, 145, 0);\n"
"border-radius: 10px")
        self.btn_tuvan.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/i_lienhe.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_tuvan.setIcon(icon3)
        self.btn_tuvan.setIconSize(QtCore.QSize(20, 20))
        self.btn_tuvan.setObjectName("btn_tuvan")
        self.btn_cauhoi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_cauhoi.setGeometry(QtCore.QRect(124, 215, 41, 31))
        self.btn_cauhoi.setStyleSheet("background-color: rgba(245, 54, 145, 0);\n"
"border-radius: 10px")
        self.btn_cauhoi.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/i_tuvan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_cauhoi.setIcon(icon4)
        self.btn_cauhoi.setIconSize(QtCore.QSize(20, 20))
        self.btn_cauhoi.setObjectName("btn_cauhoi")
        Giaodienhotro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Giaodienhotro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        Giaodienhotro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Giaodienhotro)
        self.statusbar.setObjectName("statusbar")
        Giaodienhotro.setStatusBar(self.statusbar)

        self.retranslateUi(Giaodienhotro)
        QtCore.QMetaObject.connectSlotsByName(Giaodienhotro)

    def retranslateUi(self, Giaodienhotro):
        _translate = QtCore.QCoreApplication.translate
        Giaodienhotro.setWindowTitle(_translate("Giaodienhotro", "MainWindow"))
        Giaodienhotro.setWhatsThis(_translate("Giaodienhotro", "<html><head/><body><p><img src=\":/newPrefix/i_chat.png\"/></p></body></html>"))
        self.lblhotro.setText(_translate("Giaodienhotro", "<html><head/><body><p>Hỗ trợ</p></body></html>"))
        self.lblxinchao.setText(_translate("Giaodienhotro", " Xin chào, tôi có thể giúp gì cho bạn?"))
        self.btnchat.setText(_translate("Giaodienhotro", "Chat"))
        self.btnlienhetongdai.setText(_translate("Giaodienhotro", "Liên hệ tổng đài"))
        self.btncauhoithuonggap.setText(_translate("Giaodienhotro", "Câu hỏi thường gặp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Giaodienhotro = QtWidgets.QMainWindow()
    ui = Ui_Giaodienhotro()
    ui.setupUi(Giaodienhotro)
    Giaodienhotro.show()
    sys.exit(app.exec())
