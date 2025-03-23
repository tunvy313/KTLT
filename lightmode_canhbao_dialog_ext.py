# from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QGraphicsScene, QGraphicsEllipseItem
# from PyQt6.QtGui import QColor
from PyQt6 import QtCore
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QDialog
from pywin.Demos.sliderdemo import MyDialog

from lightmode_canhbao_dialog import Ui_Dialog
import matplotlib.pyplot as plt
import numpy as np
import json
import os

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


