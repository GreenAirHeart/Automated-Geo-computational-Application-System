# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebChannel import QWebChannel
from bs4 import BeautifulSoup
import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import QWebEngineHttpRequest
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QUrl, pyqtSlot
import expected_DEM as eDEM



class Ui_application_page(object):
    coordinates_ready = QtCore.pyqtSignal(str, str)
    task_ready = QtCore.pyqtSignal(str)
    resolution_ready = QtCore.pyqtSignal(str)
    # def __init__(self):
    #     self.signal_handler = SignalHandler()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Automatic Geomorphological Classification Tool")
        Dialog.setWindowIcon(QIcon("dde.ico"))
        Dialog.resize(2000, 1400)
        Dialog.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)

        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1200, 1400))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 421, 51))
        self.label_2.setStyleSheet("font: 75 20pt \"Agency FB\";\n""\n""")
        self.label_2.setObjectName("label_2")
        self.label_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(530, 100, 421, 51))
        self.label_6.setStyleSheet("font: 75 20pt \"Agency FB\";\n""color: rgb(188, 188, 188);\n""color: rgb(191, 191, 191);\n""\n""")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(900, 100, 421, 51))
        self.label_7.setStyleSheet("font: 75 20pt \"Agency FB\";\n""color: rgb(188, 188, 188);\n""color: rgb(191, 191, 191);\n""\n""")
        self.label_7.setObjectName("label_7")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 180, 421, 51))
        self.label_5.setStyleSheet("font: 75 20pt \"Agency FB\";\n""color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")

        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(1200, 0, 800, 1400))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(1200, 55, 421, 51))
        self.label_8.setStyleSheet("font: 75 18pt \"Agency FB\";\n""color: rgb(0, 0, 0);\n""\n""")
        self.label_8.setObjectName("label_8")

        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(1200, 150, 800, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 200, 421, 51))
        self.label.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 310, 421, 51))
        self.label_3.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(100, 300, 421, 51))
        self.label_9.setStyleSheet("font: 75 20pt \"Agency FB\";\n""color: rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")

        self.textBrowser_4 = QtWidgets.QFrame(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(110, 395, 1060, 700))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.textBrowser_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_4.setLineWidth(9)
        self.textBrowser_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)




        self.web_view =QtWebEngineWidgets.QWebEngineView(self.textBrowser_4)
        self.web_view.load(QUrl.fromLocalFile("D:/arcpy_project/Scripts/method/map.html"))


        self.web_view.resize(1060, 700)
        self.web_view.move(0, 0)



        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1030, 1025, 100, 40))
        self.pushButton_2.setStyleSheet("background-color: rgb(109, 151, 115);\n""font: 75 15pt \"Agency FB\";""color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.get_coordinates)
 

       # resolution
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(120, 1150, 421, 51))
        self.label_10.setStyleSheet("font: 75 18pt \"Agency FB\";")
        self.label_10.setObjectName("label_10")



        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(1030, 1300, 152, 52))
        self.pushButton_3.setStyleSheet("background-color: rgb(12, 59, 46);\n""font: 75 20pt \"Agency FB\";""color: white;")
        self.pushButton_3.setObjectName("pushButton_3")







        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(535, 200, 635, 65))
        self.comboBox.setStyleSheet("font: 75 15pt \"Agency FB\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)


     # resolution
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(535, 1150, 401,65))
        self.comboBox_2.setStyleSheet("font: 75 15pt \"Agency FB\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.currentIndexChanged.connect(self.on_combobox2_changed)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        button_object_names = ["pushButton_2","pushButton_3"]  # Add more button object names if needed

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




    def get_coordinates(self):
        self.web_view.page().runJavaScript('document.getElementById("topLeftInput").value;', self.handle_top_left)
        self.web_view.page().runJavaScript('document.getElementById("bottomRightInput").value;', self.handle_bottom_right)

    def handle_top_left(self, value):
        self.top_left_value = value
        self.check_and_emit_coordinates()
        print("Top Left:", value)



    def handle_bottom_right(self, value):
        self.bottom_right_value = value
        self.check_and_emit_coordinates()
        print("Bottom Right:", value)

    def check_and_emit_coordinates(self):
        if hasattr(self, 'top_left_value') and hasattr(self, 'bottom_right_value'):
            self.emit_coordinates_ready()

    def emit_coordinates_ready(self):
        try:

            self.coordinates_ready.emit(self.top_left_value, self.bottom_right_value)
            print("Emitting coordinates_ready signal")
        except Exception as e:
            print("Error emitting coordinates_ready signal:", e)


  


    def closeEvent(self, event):
            confirm = QMessageBox.question(
                self, "Confirm Close",
                "Are you sure you want to close the application?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if confirm == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Automatic Geomorphological Classification Tool", "Automated Geo-morphological Classification Driven By A Knowledge Graph"))
        self.label_2.setText(_translate("Dialog", "Application Setting"))
        self.label_6.setText(_translate("Dialog", "Model Selecting"))
        self.label_7.setText(_translate("Dialog", "Data Matching"))
        self.label_5.setText(_translate("Dialog", "*"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Agency FB\',\'serif\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Agency FB\',\'serif\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:80px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:20pt; font-weight:600;\">Application Knowledge Graph</span> </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Agency FB\',\'serif\'; font-size:15pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt;\">Basic Morphological Classification references the classification indices in the </span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt; font-weight:600; text-decoration: underline; color:rgb(15,59,46);\">Digital Geomorphological Classification System of China</span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt;\"> (R: relief; A: altitude) to categorize the basic morphological landforms.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:-160px;\">          <img src=\":/pic/application.png\" width=\"752\" height=\"500\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt;\">According to the constraints defined for the “application” concept in geo-computation ontology, a user needs to select the study region, study temporal feature, and granularity (such as resolution). For application - Basic Morphological Classification, </span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt; font-weight:600;\">study region</span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt;\">, and </span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt; font-weight:600;\">resolution</span><span style=\" font-family:\'Agency FB\',\'serif\'; font-size:15pt;\"> need to be specified, no temporal feature is required. When user selects different regions and solutions, individual knowledge graphs of specified applications are generated.  </span> </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "Description"))
        self.label.setText(_translate("Dialog", "Please Select an Application:"))
        self.label_3.setText(_translate("Dialog", "Please Select Study Region:"))
        self.label_9.setText(_translate("Dialog", "*"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))


        self.label_10.setText(_translate("Dialog", "Please Select Resolution:"))
        self.pushButton_3.setText(_translate("Dialog", "Next"))
        self.comboBox.setItemText(0, _translate("Dialog", "(None)"))
        self.comboBox.setItemText(1, _translate("Dialog", "Basic Morphological Classification"))
        self.comboBox.setItemText(2, _translate("Dialog", "Distribution of Population"))
        self.comboBox.setItemText(3, _translate("Dialog", "Annual Rainfall"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "(None)"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "30 meter"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "90 meter"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "250 meter"))
      

    def on_combobox_changed(self, index):
        self.task_selected_value = self.comboBox.currentText()
        # mp.Ui_model_page.label_a_result(self, selected_value)
        print("Selected application value:", self.task_selected_value)
        self.check_and_emit_task()

    def on_combobox2_changed(self, index):
        self.resolution_selected_value = self.comboBox_2.currentText()
        print("Selected spatial resolution value:", self.resolution_selected_value)
        self.check_and_emit_resolution()

    def check_and_emit_task(self):
        if hasattr(self, 'task_selected_value'):
            self.emit_task_ready()

    def check_and_emit_resolution(self):
        if hasattr(self, 'resolution_selected_value'):
            self.emit_resolution_ready()

    def emit_task_ready(self):
        try:
           
            self.task_ready.emit(self.task_selected_value)
            print("Emitting task_ready signal")
        except Exception as e:
            print("Error emitting task_ready signal:", e)

    def emit_resolution_ready(self):
            try:
          
                self.resolution_ready.emit(self.resolution_selected_value)
                print("Emitting task_ready signal")
            except Exception as e:
                print("Error emitting task_ready signal:", e)





import application_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_application_page()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
