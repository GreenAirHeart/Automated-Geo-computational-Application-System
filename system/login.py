from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QFrame, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Ui_login_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Automatic Geomorphological Classification Tool")
        MainWindow.setWindowIcon(QIcon("dde.ico"))
        self.layout = QVBoxLayout()
        MainWindow.resize(1400, 1000)
        MainWindow.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1400, 1000))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 775, 300, 70))
        self.pushButton_2.setStyleSheet("background-color: rgb(12, 59, 46);\n""font: 75 20pt \"Agency FB\";""color:white;")
        self.pushButton_2.setObjectName("start_button")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 875, 300, 70))
        self.pushButton_3.setStyleSheet("background-color: rgb(12, 59, 46);\n""font: 75 20pt \"Agency FB\";""color:white;")
        self.pushButton_3.setObjectName("signin_button")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 22))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.label_1 = QtWidgets.QLabel(MainWindow)
        self.label_1.setGeometry(QtCore.QRect(440, 340, 421, 51))
        self.label_1.setStyleSheet("font: 75 20pt \"Agency FB\";\n""\n""")
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(440, 540, 421, 51))
        self.label_2.setStyleSheet("font: 75 20pt \"Agency FB\";\n""\n""")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(515, 100, 421, 200))
        self.label_3.setStyleSheet("font: 75 45pt \"Agency FB\";\n""\n""")
        self.label_3.setObjectName("label_3")

        # username
        self.username=QtWidgets.QLineEdit(MainWindow)
        self.username.setGeometry(QtCore.QRect(440, 410, 520, 50))
        #
        # self.textBrowser_4 = QtWidgets.QFrame(MainWindow)
        #
        # self.textBrowser_4.setObjectName("textBrowser_4")
        # self.textBrowser_4.setMidLineWidth(1)  # 设置中线宽度
        # self.textBrowser_4.setFrameShadow(QFrame.Plain)  # 设置阴影效果：凸起
        # self.textBrowser_4.setFrameShape(QFrame.Box)
        # self.textBrowser_4.setLineWidth(1)


        # password
        self.password = QtWidgets.QLineEdit(MainWindow)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(440, 610, 520, 50))

        #
        # self.textBrowser_5 = QtWidgets.QFrame(MainWindow)
        # self.textBrowser_5.setGeometry(QtCore.QRect(440, 610, 520, 50))
        # self.textBrowser_5.setObjectName("textBrowser_4")
        # self.textBrowser_5.setMidLineWidth(1)  # 设置中线宽度
        # self.textBrowser_5.setFrameShadow(QFrame.Plain)  # 设置阴影效果：凸起
        # self.textBrowser_5.setFrameShape(QFrame.Box)
        # self.textBrowser_5.setLineWidth(1)








        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        button_object_names = ["pushButton_2", "pushButton_3"]  # Add more button object names if needed

        for button_name in button_object_names:
            # Find the button by its object name
            button = getattr(self, button_name)
            if isinstance(button, QPushButton):
                # Set default cursor shape to arrow
                button.setCursor(Qt.ArrowCursor)

                # Connect signals to slots
                button.enterEvent = lambda event, button=button: self.changeCursorToHand(button)
                button.leaveEvent = lambda event, button=button: self.changeCursorToArrow(button)


    def changeCursorToHand(self, button):
        button.setCursor(Qt.PointingHandCursor)  # Change cursor to pointing hand when mouse enters button area


    def changeCursorToArrow(self, button):
        button.setCursor(Qt.ArrowCursor)






    def closeEvent(self, event):
        confirm = QMessageBox.question(self, "Confirm Close","Are you sure you want to close the application?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Automatic Geomorphological Classification Tool", "Automatic Geomorphological Classification Tool"))
#         self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:26pt; font-weight:600;\">Automatic Geo-computation Driven by Knowledge Graph</span></p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">Geographic computation (geo-computation) uncovers the distribution patterns, simulates the evolution process, and predicts the development trends of geographic entities, events, and phenomena by using geographic model (geo-model) and geographic data (geo-data). The three concepts: geographic application, geographic model, and geographic data are conceptualized as the three concepts of &quot;application-model-data&quot; at the ontology level. Consequently, an ontological framework for geo-computation is established with the three concepts of &quot;application-model-data&quot; as the main concepts.</span> </p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                              <img src=\":/start_page/geocomputation-ontology.png\" width=\"650\" height=\"650\" /></p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">We propose a method whose basic idea is integrating application knowledge, model knowledge, and data knowledge within a knowledge graph, then relying on the knowledge in the knowledge graph to realize the automatic geo-computation. As a case study of the proposed method, </span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600; color:#000000;\">geomorphological classification</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\"> is selected. </span> </p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))
        self.pushButton_3.setText(_translate("MainWindow", "Sign In"))
        self.label_1.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label_3.setText(_translate("MainWindow", "User Login"))
import start_page_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_login_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())