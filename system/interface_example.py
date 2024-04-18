# import tkinter as tk
# from tkinterweb import HtmlFrame
# try:
#   import tkinter as tk #python3
# except ImportError:
#   import Tkinter as tk #python2
# html_content = "file://D:/arcpy_project/Scripts/method/map_test.html"
#
# root = tk.Tk()
# root.title("HTML Content Viewer")
# root.geometry("1800x1600")
#
# html_frame = HtmlFrame(root)
# html_frame.load_file(html_content,decode='utf-8', force=True)
# html_frame.pack(fill=tk.BOTH, expand=True)
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkhtmlview import HTMLLabel
#
# class WebpageApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Webpage Viewer")
#         self.geometry("800x600")
#
#         # Create an HTMLLabel widget
#         self.webview = HTMLLabel(self, html="")
#         self.webview.pack(fill=tk.BOTH, expand=True)
#
#         # Load the webpage into the HTMLLabel widget
#         webpage_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
#             <title>open123</title>
#             <script type="text/javascript" src="http://api.tianditu.gov.cn/api?v=4.0&tk=23a9a63f3a584ee405db4e1147945e1e"></script>
#             <style type="text/css">body,html{width:100%;height:100%;margin:0;font-family:"Microsoft YaHei"}#mapDiv{width :100%;height:400px}input,b,p{margin-left:5px;font-size:14px}</style>
#             <script>
#                 var map;
#                 var zoom = 8;
#                 var lay;
#                 var onlyMapLay;
#                 function onLoad() {
#                     var imageURL = "http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&tk=23a9a63f3a584ee405db4e1147945e1e";
#                     lay = new T.TileLayer(imageURL, {minZoom: 1, maxZoom: 18});
#                     var config = {layers: [lay]};
#                     map = new T.Map("mapDiv", config);
#                     map.centerAndZoom(new T.LngLat(116.40969, 39.89945), zoom);
#                     map.enableScrollWheelZoom();
#                 }
#
#             </script>
#         </head>
#         <body onLoad="onLoad()">
#         <div id="mapDiv"></div>
#         <p>open</p>
#         <div style="position:absolute;left:520px;">
#         </div>
#         </body>
#         </html>
#         """
#         self.webview.set_html(webpage_content)
#
# if __name__ == "__main__":
#     app = WebpageApp()
#     app.mainloop()


# import tkinter as tk
# from tkinterweb import HtmlFrame
#
# class WebpageApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Webpage Viewer")
#         self.geometry("800x600")
#
#         # Create an HtmlFrame widget
#         self.webview = HtmlFrame(self)
#         self.webview.pack(fill=tk.BOTH, expand=True)
#
#         # Load the webpage into the HtmlFrame widget
#         webpage_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#         <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
#         <title>open123</title>
#             <script type="text/javascript" src="http://api.tianditu.gov.cn/api?v=4.0&tk=23a9a63f3a584ee405db4e1147945e1e"></script>
#             <style type="text/css">body,html{width:100%;height:100%;margin:0;font-family:"Microsoft YaHei"}#mapDiv{width :100%;height:400px}input,b,p{margin-left:5px;font-size:14px}</style>
#             <script>
#                 var map;
#                 var zoom = 8;
#                 var lay;
#                 var onlyMapLay;
#                 function onLoad() {
#                     var imageURL = "http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&tk=23a9a63f3a584ee405db4e1147945e1e";
#                     lay = new T.TileLayer(imageURL, {minZoom: 1, maxZoom: 18});
#                     var config = {layers: [lay]};
#                     map = new T.Map("mapDiv", config);
#                     map.centerAndZoom(new T.LngLat(116.40969, 39.89945), zoom);
#                     map.enableScrollWheelZoom();
#                 }
#             </script>
#         </head>
#         <body onLoad="onLoad()">
#         <div id="mapDiv"></div>
#         <p>open</p>
#         <div style="position:absolute;left:520px;">
#         </div>
#         </body>
#         </html>
#         """
#         self.webview.load_html(webpage_content)
#
# if __name__ == "__main__":
#     app = WebpageApp()
#     app.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from tkwebview2.tkwebview2 import WebView2
#
# class WebpageApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Webpage Viewer")
#         self.geometry("800x600")
#
#         # Create a WebView widget
#         self.webview = WebView2(self)
#         self.webview.pack(fill=tk.BOTH, expand=True)
#
#         # Load the webpage into the WebView widget
#         webpage_content = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>My Webpage</title>
#         </head>
#         <body>
#             <h1>Welcome to my webpage!</h1>
#             <p>This is a sample webpage content.</p>
#
#             <button onclick="showAlert()">Click Me</button>
#
#             <script>
#                 function showAlert() {
#                     alert("Button clicked!");
#                 }
#             </script>
#         </body>
#         </html>
#         """
#         self.webview.set_content(webpage_content, base_uri="http://localhost/")
#
# if __name__ == "__main__":
#     app = WebpageApp()
#     app.mainloop()
#
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl
#
# class WebpageApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Create a QWebEngineView widget
#         self.webview = QWebEngineView(self)
#         self.setCentralWidget(self.webview)
#
#         # Load the webpage into the QWebEngineView widget
#         self.webview.setUrl(QUrl("https://www.baidu.com"))
#
#         # Add a button to execute JavaScript
#         button = QPushButton("Execute JavaScript")
#         button.clicked.connect(self.execute_javascript)
#
#         # Create a layout to hold the button
#         layout = QVBoxLayout()
#         layout.addWidget(button)
#
#         # Create a central widget to add the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#
#         # Set the central widget
#         self.setCentralWidget(central_widget)
#
#     def execute_javascript(self):
#         # JavaScript code to be executed
#         js_code = """
#         // Example JavaScript code
#         var header = document.querySelector('h1');
#         header.style.color = 'red';
#         """
#
#         # Execute the JavaScript code in the QWebEngineView widget
#         self.webview.page().runJavaScript(js_code)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = WebpageApp()
#     window.setGeometry(100, 100, 800, 600)
#     window.show()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("打开网页")
#         MainWindow.resize(1640, 700)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit.setGeometry(QtCore.QRect(20, 10, 630, 30))
#         self.lineEdit.setObjectName("lineEdit")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(690, 10, 90, 30))
#         self.pushButton.setObjectName("pushButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         ## 创建web窗体
#         self.qwebengine = QtWebEngineWidgets.QWebEngineView(MainWindow)
#         self.qwebengine.setGeometry(20, 50, 1600, 600)
#
#         ## 创建连接
#         self.pushButton.clicked.connect(self.open_url)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "打开网页"))
#         self.lineEdit.setText(_translate("MainWindow", "http://www.baidu.com"))
#         self.pushButton.setText(_translate("MainWindow", "打开"))
#
#
#     def open_url(self):
#         url=self.lineEdit.text()
#         self.qwebengine.load(QtCore.QUrl(url))
#
# import sys
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
#     ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
#     ui.setupUi(MainWindow)  # 调用窗体的方法对对象进行初始化设置
#     MainWindow.show()  # 显示窗体
#     sys.exit(app.exec_())  # 程序关闭时退出进程

# whole ------- part-----------------------------------------------------------------------------------------------


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Geo Computation')
        self.setGeometry(700,700,1520,1000)#窗口的初始位置和大小
        self.browser=QWebEngineView() #加载本地html
        self.browser.load(QUrl(QFileInfo("D:/arcpy_project/Scripts/method/map_test.html").absoluteFilePath()))
        self.setCentralWidget(self.browser)



        # self.button = QPushButton("Click Me", self)
        # self.button.setGeometry(900, 500, 100, 30)
        # self.button.clicked.connect(self.onButtonClick)

        # self.upload_button = QPushButton("Upload File", self)
        # self.upload_button.setGeometry(900, 900, 100, 30)
        # self.upload_button.clicked.connect(self.onUploadButtonClick)

    # def onButtonClick(self):
    #     self.label.setText("Button Clicked!")
    #
    # def onUploadButtonClick(self):
    #     options = QFileDialog.Options()
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)",
    #                                                options=options)
    #     if file_path:
    #         self.label.setText(f"File uploaded: {file_path}")




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()

    app.exit(app.exec_())


#whole part ------------------------------------------------------------------------------------------------------------------------







# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle('Geo Computation')
#         self.setGeometry(700, 700, 1520, 1000)  # 窗口的初始位置和大小
#         self.browser = QWebEngineView()  # 加载本地html
#         self.browser.load(QUrl(QFileInfo("D:/arcpy_project/Scripts/method/map_test.html").absoluteFilePath()))
#         self.setCentralWidget(self.browser)
#
#         self.steps = [
#             {"name": "Step 1", "text": "First Step", "next_text": "Next"},
#             {"name": "Step 2", "text": "Second Step", "next_text": "Next"},
#             {"name": "Step 3", "text": "Third Step", "next_text": "Next"},
#             {"name": "Step 4", "text": "Fourth Step", "next_text": "Finish"},
#         ]
#         self.current_step = 0
#
#         self.next_button = QPushButton("Next", self)
#         self.next_button.setGeometry(900, 500, 100, 30)
#         self.next_button.clicked.connect(self.onNextButtonClick)
#
#         self.upload_button = QPushButton("Upload File", self)
#         self.upload_button.setGeometry(900, 900, 100, 30)
#         self.upload_button.clicked.connect(self.onUploadButtonClick)
#
#         self.update_step()
#
#     def onNextButtonClick(self):
#         self.current_step += 1
#         if self.current_step >= len(self.steps):
#             self.current_step = 0
#         self.update_step()
#
#     def onUploadButtonClick(self):
#         options = QFileDialog.Options()
#         file_path, _ = QFileDialog.getOpenFileName(
#             self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options
#         )
#         if file_path:
#             QMessageBox.information(self, "File Uploaded", f"File uploaded: {file_path}")
#
#     def update_step(self):
#         step_info = self.steps[self.current_step]
#         self.browser.page().runJavaScript(f"document.getElementById('step').innerText = '{step_info['name']}'")
#         self.browser.page().runJavaScript(f"document.getElementById('step_text').innerText = '{step_info['text']}'")
#         self.next_button.setText(step_info["next_text"])
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     app.exit(app.exec_())




# -*- coding: utf-8 -*-

  # Form implementation generated from reading ui file 'Form.ui'
  #
  # Created by: PyQt5 UI code generator 5.10.1
  #
  # WARNING! All changes made in this file will be lost!
  #要注意的是跳转界面第二个必须使用QDialog类，不能使用QWidget，我也不知道为什么，特别注意
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QApplication
# import Dialog1
# import Dialog2
# import sys
#
# class Ui_Form(object):  #这是用PyQt Designer生成的代码，很简单的，拖动控件，生成ui文件，然后UIC转换成py文件
#      def setupUi(self, Form):
#          Form.setObjectName("Form")
#          Form.resize(440, 310)
#          self.form = Form
#          self.btn_d1 = QtWidgets.QPushButton(Form)
#          self.btn_d1.setGeometry(QtCore.QRect(60, 140, 75, 23))
#          self.btn_d1.setObjectName("btn_d1")
#          self.btn_d2 = QtWidgets.QPushButton(Form)
#          self.btn_d2.setGeometry(QtCore.QRect(180, 140, 75, 23))
#          self.btn_d2.setObjectName("btn_d2")
#          self.btn_exit = QtWidgets.QPushButton(Form)
#          self.btn_exit.setGeometry(QtCore.QRect(310, 140, 75, 23))
#          self.btn_exit.setObjectName("btn_exit")
#
#          self.retranslateUi(Form)
#          QtCore.QMetaObject.connectSlotsByName(Form)
#      def retranslateUi(self, Form):
#          _translate = QtCore.QCoreApplication.translate
#          Form.setWindowTitle(_translate("Form", "Form"))
#          self.btn_d1.setText(_translate("Form", "Demo1"))
#          self.btn_d1.clicked.connect(self.jump_to_demo1)
#          self.btn_d2.setText(_translate("Form", "Demo2"))
#          self.btn_d2.clicked.connect(self.jump_to_demo2)
#          self.btn_exit.setText(_translate("Form", "Exit"))
#          self.btn_exit.clicked.connect(self.exit)
#
#      def jump_to_demo1(self):        #这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
#          self.form.hide()            #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
#          form1 = QtWidgets.QDialog()
#          ui = Dialog1.Ui_Dialog1()
#          ui.setupUi(form1)
#          form1.show()
#          form1.exec_()
#          self.form.show()
#
#      def jump_to_demo2(self):
#          self.form.hide()
#          form2 = QtWidgets.QDialog()
#          ui = Dialog2.Ui_Dialog2()
#          ui.setupUi(form2)
#          form2.show()
#          form2.exec_()
#          self.form.show()
#
#      def exit(self):
#          self.form.close()
#
#
#  if __name__ == "__main__":
#      app = QApplication(sys.argv)
#      form = QtWidgets.QWidget()
#      window = Ui_Form()
#      window.setupUi(form)
#      form.show()
#      sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import uic, QtCore
# from PyQt5 import QtWidgets
#
# class win1(QWidget):
#     switch_win2 = QtCore.pyqtSignal()
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("./win1.ui")
#         self.ui.pushButton.clicked.connect(self.todobtn1)
#
#
#     def todobtn1(self):
#         self.switch_win2.emit()
#         self.ui.close()
#
# class win2(QWidget):
#
#     switch_win3 = QtCore.pyqtSignal()
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("./win2.ui")
#         self.ui.pushButton.clicked.connect(self.write1)
#         self.ui.pushButton_3.clicked.connect(self.tobtn3)
#
#     def write1(self):
#         text = self.ui.textEdit.toPlainText()
#         fp = open("./test.txt", 'a')
#         fp.write(text)
#         fp.write("\n")
#         self.ui.textEdit.clear()
#         fp.close()
#
#     def tobtn3(self):
#         self.switch_win3.emit()
#
# class win3(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("./win3.ui")
#         self.read1()
#
#     def read1(self):
#         fp = open("./test.txt", 'r')
#         for line in fp:
#             self.ui.textBrowser.append(line)
#         fp.close()
#
#
#
# class controller:
#
#     def __init__(self):
#         pass
#
#     def show_win1(self):
#         self.win1 = win1()
#         self.win1.switch_win2.connect(self.show_win2)
#         self.win1.ui.show()
#
#     def show_win2(self):
#         self.win2 = win2()
#         self.win2.switch_win3.connect(self.show_win3)
#         self.win2.ui.show()
#
#     def show_win3(self):
#         self.win3 = win3()
#         self.win3.ui.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     w = controller()
#     w.show_win1()
#
#     app.exec_()


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/QT/start_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/QT/start_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/QT/start_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/QT/start_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1100, 900)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1100, 750))
#         self.textBrowser.setObjectName("textBrowser")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(850, 800, 150, 50))
#         self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
# "font: 75 20pt \"Agency FB\";")
#         self.pushButton_2.setObjectName("pushButton_2")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:26pt; font-weight:600;\">Automatic Geo-computation Driven by Knowledge Graph</span></p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">Geo-computation is the process of using geoscientific models and geoscientific data to uncover the distribution patterns of geoscientific phenomena and to simulate and predict the development trends in the field of geoscience. The three concepts: geoscientific phenomena, geoscientific models, and geoscientific data are conceptualized as the three concepts of &quot;application-model-data&quot; at the ontology level. Consequently, an ontological framework for geo-computation is established with the three concepts of &quot;application-model-data&quot; as the main concepts.</span> </p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                              <img src=\":/start_page/geocomputation-ontology.png\" width=\"350\" height=\"350\" /></p>\n"
# "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\"><br /></p>\n"
# "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\">We propose a method whose basic idea is integrating application knowledge, model knowledge, and data knowledge within a knowledge graph, then relying on the knowledge in the knowledge graph to realize the automatic geo-computation. To showcase our proposed method, we select </span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; font-weight:600; color:#000000;\">geomorphological classification</span><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt; color:#000000;\"> as the research domain, which is the foundation for understanding geographical science.</span> </p></body></html>"))
#         self.pushButton_2.setText(_translate("MainWindow", "Start"))
# import start_page_rc
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())




