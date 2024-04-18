from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Ui_start_page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Automatic Geomorphological Classification Tool")
        MainWindow.setWindowIcon(QIcon("dde.ico"))
        self.layout = QVBoxLayout()
        MainWindow.resize(1400, 1200)
        MainWindow.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1400, 1000))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 1075, 150, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n""font: 75 20pt \"Agency FB\";")
        self.pushButton_2.setObjectName("start_button")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 22))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Automatic Geomorphological Classification Tool", "Automatic Geomorphological Classification Tool"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:26pt; font-weight:600;\">Automatic Geo-computation Driven by Knowledge Graph</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">Geographic computation (geo-computation) uncovers the distribution patterns, simulates the evolution process, and predicts the development trends of geographic entities, events, and phenomena by using geographic model (geo-model) and geographic data (geo-data). The three concepts: geographic application, geographic model, and geographic data are conceptualized as the three concepts of &quot;application-model-data&quot; at the ontology level. Consequently, an ontological framework for geo-computation is established with the three concepts of &quot;application-model-data&quot; as the main concepts.</span> </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                              <img src=\":/start_page/geocomputation-ontology.png\" width=\"650\" height=\"650\" /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">We propose a method whose basic idea is integrating application knowledge, model knowledge, and data knowledge within a knowledge graph, then relying on the knowledge in the knowledge graph to realize the automatic geo-computation. As a case study of the proposed method, </span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600; color:#000000;\">geomorphological classification</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\"> is selected. </span> </p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
import start_page_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_start_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())