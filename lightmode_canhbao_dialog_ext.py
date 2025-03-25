from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QMainWindow
from thongbao_chinh_ext import thongbao_chinh_ext
from lightmode_canhbao_dialog import Ui_Dialog

class lightmode_canhbao_dialog_ext(QDialog, Ui_Dialog):
    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.MyDialog = Dialog

        #Connect events
        self.btn_exit.clicked.connect(self.exit)

        self.btn_exit.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        font-size: 16px;
                        border-radius: 5px;
                    }
                """)
        self.btn_exit.installEventFilter(self)
        self.MyDialog.mousePressEvent = self.close_and_open_main

    def close_and_open_main(self, event):
        """Đóng cửa sổ hiện tại và mở cửa sổ mới"""
        self.MyDialog.close()  # Đóng giao diện cảnh báo
        self.open_main_window()  # Mở giao diện chính

    def open_main_window(self):
        """Mở giao diện chính"""
        main_window = QMainWindow()
        ui = thongbao_chinh_ext()
        ui.setupUi(main_window)
        main_window.show()
    def eventFilter(self, obj, event):
        # Xử lý sự kiện chuột
        if obj == self.btn_exit:
            if event.type() == QtCore.QEvent.Type.Enter:
                # Khi di chuột vào nút
                self.btn_exit.setStyleSheet("""
                        QPushButton {
                            background-color: #E0E0E0;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            font-size: 16px;
                            border-radius: 5px;
                        }
                    """)
            elif event.type() == QtCore.QEvent.Type.Leave:
                # Khi di chuột ra khỏi nút
                self.btn_exit.setStyleSheet("""
                        QPushButton {
                            background-color: white;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            font-size: 16px;
                            border-radius: 5px;
                        }
                    """)
            elif event.type() == QtCore.QEvent.Type.MouseButtonPress:
                # Khi nhấn nút
                self.btn_exit.setStyleSheet("""
                        QPushButton {
                            background-color: #BDBDBD;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            font-size: 16px;
                            border-radius: 5px;
                        }
                    """)
            elif event.type() == QtCore.QEvent.Type.MouseButtonRelease:
                # Khi thả nút
                self.btn_exit.setStyleSheet("""
                        QPushButton {
                            background-color: white;
                            color: white;
                            border: none;
                            padding: 10px 20px;
                            font-size: 16px;
                            border-radius: 5px;
                        }
                    """)
        return super().eventFilter(obj, event)
    def exit(self):
        self.MyDialog.close()

