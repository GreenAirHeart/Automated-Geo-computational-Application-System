# # # # # # # # # # # # # # # from selenium import webdriver
# # # # # # # # # # # # # # # from selenium.webdriver.common.by import By
# # # # # # # # # # # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # # # # # # # # # # from selenium.webdriver.support import expected_conditions as EC
# # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Initialize the Chrome driver
# # # # # # # # # # # # # # # driver = webdriver.Chrome()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Load the HTML page
# # # # # # # # # # # # # # # driver.get("D:/arcpy_project/Scripts/method/map.html")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Wait for the elements to load
# # # # # # # # # # # # # # # time.sleep(5)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Find the input fields for top left and bottom right coordinates
# # # # # # # # # # # # # # # top_left_input = driver.find_element("css selector", "#topLeftInput")
# # # # # # # # # # # # # # # bottom_right_input = driver.find_element("css selector", "#bottomRightInput")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Input coordinates values (for demonstration, you can change these values)
# # # # # # # # # # # # # # # # top_left_input.send_keys("40.7128,-74.0060")
# # # # # # # # # # # # # # # # bottom_right_input.send_keys("34.0522,-118.2437")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Find the draw button and click on it
# # # # # # # # # # # # # # # draw_button = driver.find_element("css selector", "#drawButton")
# # # # # # # # # # # # # # # draw_button.click()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Wait for the drawn rectangle to appear (you can adjust the time if needed)
# # # # # # # # # # # # # # # # In this case, we'll use explicit wait for the save button to become clickable
# # # # # # # # # # # # # # # save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#saveButton")))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Click the save button
# # # # # # # # # # # # # # # save_button.click()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Wait for the save operation to complete and the coordinates to be updated
# # # # # # # # # # # # # # # # We'll wait until the input fields are not empty
# # # # # # # # # # # # # # # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#topLeftInput"), ""))
# # # # # # # # # # # # # # # WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#bottomRightInput"), ""))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Extract the coordinates values from the input fields
# # # # # # # # # # # # # # # top_left_value = top_left_input.get_attribute('value')
# # # # # # # # # # # # # # # bottom_right_value = bottom_right_input.get_attribute('value')
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print("Top Left Coordinates:", top_left_value)
# # # # # # # # # # # # # # # print("Bottom Right Coordinates:", bottom_right_value)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Close the browser
# # # # # # # # # # # # # # # driver.quit()
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # import bs4 as bs
# # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # import urllib.request
# # # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import QWebEnginePage
# # # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # class Page(QWebEnginePage):
# # # # # # # # # # # # # #     def __init__(self, url):
# # # # # # # # # # # # # #         self.app = QApplication(sys.argv)
# # # # # # # # # # # # # #         QWebEnginePage.__init__(self)
# # # # # # # # # # # # # #         self.html = ''
# # # # # # # # # # # # # #         self.loadFinished.connect(self._on_load_finished)
# # # # # # # # # # # # # #         self.load(QUrl(url))
# # # # # # # # # # # # # #         self.app.exec_()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def _on_load_finished(self):
# # # # # # # # # # # # # #         self.html = self.toHtml(self.Callable)
# # # # # # # # # # # # # #         print('Load finished')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     def Callable(self, html_str):
# # # # # # # # # # # # # #         self.html = html_str
# # # # # # # # # # # # # #         self.app.quit()
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # def main():
# # # # # # # # # # # # # #     # page = Page('http://localhost:63342/arcpy_project/Scripts/method/map.html?_ijt=30926svl4iabrjpeek6fq43dm9')
# # # # # # # # # # # # # #     # soup = bs.BeautifulSoup(page.html, 'html.parser')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     with open("D:/arcpy_project/Scripts/method/map.html") as fp:
# # # # # # # # # # # # # #         soup = bs.BeautifulSoup(fp, 'html.parser')
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     print(soup)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     # js_test = json.loads(soup.find('script', id="coordinate").text)
# # # # # # # # # # # # # #     # print (js_test.text)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # if __name__ == '__main__': main()
# # # # # # # # # # # # #
# # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import *
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # from PyQt5.QtWebKitWidgets import QWebView
# # # # # # # # # # # # # from PyQt5.QtWebKit import QWebSettings
# # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import QWebEnginePage
# # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # class HTMLParameterExtractor(QWebEngineView):
# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # #         self.loadFinished.connect(self.onLoadFinished)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def onLoadFinished(self, success):
# # # # # # # # # # # # #         if success:
# # # # # # # # # # # # #             # Inject JavaScript to extract dynamic parameters
# # # # # # # # # # # # #             script = """
# # # # # # # # # # # # #                 const topLeftInput = document.getElementById('topLeftInput').value;
# # # # # # # # # # # # #                 const bottomRightInput = document.getElementById('bottomRightInput').value;
# # # # # # # # # # # # #             """
# # # # # # # # # # # # #             self.page().runJavaScript(script, self.printResult)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def printResult(self, result):
# # # # # # # # # # # # #         print("Dynamic Parameter:", result)
# # # # # # # # # # # # #
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # #     browser = HTMLParameterExtractor()
# # # # # # # # # # # # #     browser.load(QUrl("D:/arcpy_project/Scripts/method/map.html"))
# # # # # # # # # # # # #     browser.show()
# # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import QWebEngineView
# # # # # # # # # # # # #
# # # # # # # # # # # # # class HTMLParameterExtractor(QWebEngineView):
# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # #         self.loadFinished.connect(self.onLoadFinished)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def onLoadFinished(self, success):
# # # # # # # # # # # # #         if success:
# # # # # # # # # # # # #             # Inject JavaScript to retrieve coordinates
# # # # # # # # # # # # #             script = """
# # # # # # # # # # # # #                 var inputField = document.getElementById('coordinates_input');
# # # # # # # # # # # # #                 var coordinates = inputField.value;
# # # # # # # # # # # # #                 coordinates;
# # # # # # # # # # # # #             """
# # # # # # # # # # # # #             self.page().runJavaScript(script, self.printCoordinates)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def printCoordinates(self, coordinates):
# # # # # # # # # # # # #         print("Coordinates:", coordinates)
# # # # # # # # # # # # #
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # #     browser = HTMLParameterExtractor()
# # # # # # # # # # # # #     browser.load(QUrl.fromLocalFile("D:/arcpy_project/Scripts/method/test.html"))
# # # # # # # # # # # # #     browser.show()
# # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import QWebEngineView
# # # # # # # # # # # # #
# # # # # # # # # # # # # class HTMLParameterExtractor(QWebEngineView):
# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # #         self.loadFinished.connect(self.onLoadFinished)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def onLoadFinished(self, success):
# # # # # # # # # # # # #         if success:
# # # # # # # # # # # # #             self.page().runJavaScript("document.getElementById('save_button').addEventListener('click', saveCoordinates)")
# # # # # # # # # # # # #             # You can add further initialization code here if needed
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def printCoordinates(self, coordinates):
# # # # # # # # # # # # #         print("Coordinates:", coordinates)
# # # # # # # # # # # # #
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # #     browser = HTMLParameterExtractor()
# # # # # # # # # # # # #     browser.load(QUrl.fromLocalFile("D:/arcpy_project/Scripts/method/test.html"))
# # # # # # # # # # # # #     browser.show()
# # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # from PyQt5.QtWidgets import QApplication
# # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # from PyQt5.QtWebEngineWidgets import QWebEngineView
# # # # # # # # # # # # #
# # # # # # # # # # # # # class HTMLParameterExtractor(QWebEngineView):
# # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # # #         self.loadFinished.connect(self.onLoadFinished)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def onLoadFinished(self, success):
# # # # # # # # # # # # #         if success:
# # # # # # # # # # # # #             # Inject JavaScript to retrieve coordinates
# # # # # # # # # # # # #             script = """
# # # # # # # # # # # # #                 function saveCoordinates() {
# # # # # # # # # # # # #                     var coordinates = document.getElementById('coordinates_input').value;
# # # # # # # # # # # # #                     if (coordinates.trim()) {
# # # # # # # # # # # # #                         console.log("User saved");
# # # # # # # # # # # # #                     }
# # # # # # # # # # # # #                     return coordinates;
# # # # # # # # # # # # #                 }
# # # # # # # # # # # # #                 var result = saveCoordinates();
# # # # # # # # # # # # #                 result;
# # # # # # # # # # # # #             """
# # # # # # # # # # # # #     def js_callback(result):
# # # # # # # # # # # # #         print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # #     def complete_name():
# # # # # # # # # # # # #         view.page().runJavaScript('completeAndReturnName();', js_callback)
# # # # # # # # # # # # #
# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # # # #     browser = HTMLParameterExtractor()
# # # # # # # # # # # # #     browser.load(QUrl.fromLocalFile("D:/arcpy_project/Scripts/method/test.html"))
# # # # # # # # # # # # #     browser.show()
# # # # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # # # #
# # # # # # # # # # # # # from PyQt5 import QtWidgets, QtGui, QtCore
# # # # # # # # # # # # # from PyQt5 import QtWebEngineWidgets
# # # # # # # # # # # # # from PyQt5.QtCore import QUrl
# # # # # # # # # # # # # from PyQt5.QtCore import *
# # # # # # # # # # # # # # Create an application
# # # # # # # # # # # # # app = QtWidgets.QApplication([])
# # # # # # # # # # # # #
# # # # # # # # # # # # # # And a window5
# # # # # # # # # # # # # win = QtWidgets.QWidget()
# # # # # # # # # # # # # win.setWindowTitle('QWebView Interactive Demo')
# # # # # # # # # # # # #
# # # # # # # # # # # # # # And give it a layout
# # # # # # # # # # # # # layout = QtWidgets.QVBoxLayout()
# # # # # # # # # # # # # win.setLayout(layout)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Create and fill a QWebView
# # # # # # # # # # # # # #view = QtWebKitWidgets.QWebView()  # depecated?
# # # # # # # # # # # # # view = QtWebEngineWidgets.QWebEngineView()
# # # # # # # # # # # # # view.load(QUrl(QFileInfo("D:/arcpy_project/Scripts/method/map.html").absoluteFilePath()))
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # A button to call our JavaScript
# # # # # # # # # # # # # button = QtWidgets.QPushButton('Set Full Name')
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Interact with the HTML page by calling the completeAndReturnName
# # # # # # # # # # # # # # function; print its return value to the console
# # # # # # # # # # # # # def js_callback(result):
# # # # # # # # # # # # #     print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # # def complete_name():
# # # # # # # # # # # # #     view.page().runJavaScript('collectCoordinates();', js_callback)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Connect 'complete_name' to the button's 'clicked' signal
# # # # # # # # # # # # # button.clicked.connect(complete_name)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Add the QWebView and button to the layout
# # # # # # # # # # # # # layout.addWidget(view)
# # # # # # # # # # # # # layout.addWidget(button)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # Show the window and run the app
# # # # # # # # # # # # # win.show()
# # # # # # # # # # # # # app.exec_()
# # # # # # # # # # # #
# # # # # # # # # # # # from PyQt5 import QtWidgets, QtWebEngineWidgets
# # # # # # # # # # # # from PyQt5.QtCore import QUrl, pyqtSlot
# # # # # # # # # # # #
# # # # # # # # # # # # class MainWindow(QtWidgets.QMainWindow):
# # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # #         super().__init__()
# # # # # # # # # # # #
# # # # # # # # # # # #         self.setWindowTitle("HTML Interactive Demo")
# # # # # # # # # # # #
# # # # # # # # # # # #         self.browser = QtWebEngineWidgets.QWebEngineView()
# # # # # # # # # # # #         self.browser.load(QUrl.fromLocalFile("D:/arcpy_project/Scripts/method/map.html"))
# # # # # # # # # # # #
# # # # # # # # # # # #         self.button = QtWidgets.QPushButton("Get Coordinates")
# # # # # # # # # # # #         self.button.clicked.connect(self.get_coordinates)
# # # # # # # # # # # #
# # # # # # # # # # # #         layout = QtWidgets.QVBoxLayout()
# # # # # # # # # # # #         layout.addWidget(self.browser)
# # # # # # # # # # # #         layout.addWidget(self.button)
# # # # # # # # # # # #
# # # # # # # # # # # #         central_widget = QtWidgets.QWidget()
# # # # # # # # # # # #         central_widget.setLayout(layout)
# # # # # # # # # # # #         self.setCentralWidget(central_widget)
# # # # # # # # # # # #
# # # # # # # # # # # #     @pyqtSlot()
# # # # # # # # # # # #     def get_coordinates(self):
# # # # # # # # # # # #         self.browser.page().runJavaScript('document.getElementById("topLeftInput").value;', self.handle_top_left)
# # # # # # # # # # # #         self.browser.page().runJavaScript('document.getElementById("bottomRightInput").value;', self.handle_bottom_right)
# # # # # # # # # # # #
# # # # # # # # # # # #     @pyqtSlot(result=str)
# # # # # # # # # # # #     def handle_top_left(self, value):
# # # # # # # # # # # #         print("Top Left:", value)
# # # # # # # # # # # #
# # # # # # # # # # # #     @pyqtSlot(result=str)
# # # # # # # # # # # #     def handle_bottom_right(self, value):
# # # # # # # # # # # #         print("Bottom Right:", value)
# # # # # # # # # # # #
# # # # # # # # # # # # app = QtWidgets.QApplication([])
# # # # # # # # # # # # window = MainWindow()
# # # # # # # # # # # # window.show()
# # # # # # # # # # # # app.exec_()
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # import sys
# # # # # # # # # # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
# # # # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # # # #
# # # # # # # # # # # class CalculatorPage(QWidget):
# # # # # # # # # # #     def __init__(self):
# # # # # # # # # # #         super().__init__()
# # # # # # # # # # #         self.initUI()
# # # # # # # # # # #
# # # # # # # # # # #     def initUI(self):
# # # # # # # # # # #         self.setWindowTitle('Calculator')
# # # # # # # # # # #
# # # # # # # # # # #         self.result_display = QLineEdit()
# # # # # # # # # # #         self.result_display.setReadOnly(True)
# # # # # # # # # # #         self.result_display.setAlignment(Qt.AlignRight)
# # # # # # # # # # #
# # # # # # # # # # #         # Buttons for numbers and operations
# # # # # # # # # # #         buttons_layout = QVBoxLayout()
# # # # # # # # # # #         buttons = [
# # # # # # # # # # #             '7', '8', '9', '/',
# # # # # # # # # # #             '4', '5', '6', '*',
# # # # # # # # # # #             '1', '2', '3', '-',
# # # # # # # # # # #             '0', '.', '=', '+'
# # # # # # # # # # #         ]
# # # # # # # # # # #
# # # # # # # # # # #         for label in buttons:
# # # # # # # # # # #             button = QPushButton(label)
# # # # # # # # # # #             button.clicked.connect(self.on_button_clicked)
# # # # # # # # # # #             buttons_layout.addWidget(button)
# # # # # # # # # # #
# # # # # # # # # # #         # Next Page button
# # # # # # # # # # #         next_page_button = QPushButton("Next Page")
# # # # # # # # # # #         next_page_button.clicked.connect(self.next_page)
# # # # # # # # # # #
# # # # # # # # # # #         layout = QVBoxLayout()
# # # # # # # # # # #         layout.addWidget(self.result_display)
# # # # # # # # # # #         layout.addLayout(buttons_layout)
# # # # # # # # # # #         layout.addWidget(next_page_button)
# # # # # # # # # # #
# # # # # # # # # # #         self.setLayout(layout)
# # # # # # # # # # #
# # # # # # # # # # #     def on_button_clicked(self):
# # # # # # # # # # #         clicked_button = self.sender()
# # # # # # # # # # #         if clicked_button:
# # # # # # # # # # #             text = clicked_button.text()
# # # # # # # # # # #             if text == '=':
# # # # # # # # # # #                 try:
# # # # # # # # # # #                     result = eval(self.result_display.text())
# # # # # # # # # # #                     self.result_display.setText(str(result))
# # # # # # # # # # #                 except Exception as e:
# # # # # # # # # # #                     self.result_display.setText("Error")
# # # # # # # # # # #             else:
# # # # # # # # # # #                 self.result_display.setText(self.result_display.text() + text)
# # # # # # # # # # #
# # # # # # # # # # #     def next_page(self):
# # # # # # # # # # #         result = self.result_display.text()
# # # # # # # # # # #         page_b = DisplayPage(result)
# # # # # # # # # # #         page_b.show()
# # # # # # # # # # #         self.close()
# # # # # # # # # # #
# # # # # # # # # # # class DisplayPage(QWidget):
# # # # # # # # # # #     def __init__(self, result):
# # # # # # # # # # #         super().__init__()
# # # # # # # # # # #         self.result = result
# # # # # # # # # # #         self.initUI()
# # # # # # # # # # #
# # # # # # # # # # #     def initUI(self):
# # # # # # # # # # #         self.setWindowTitle('Display')
# # # # # # # # # # #
# # # # # # # # # # #         display_layout = QVBoxLayout()
# # # # # # # # # # #         self.display_label = QLineEdit()
# # # # # # # # # # #         self.display_label.setReadOnly(True)
# # # # # # # # # # #         self.display_label.setAlignment(Qt.AlignCenter)
# # # # # # # # # # #         self.display_label.setText(self.result)
# # # # # # # # # # #         display_layout.addWidget(self.display_label)
# # # # # # # # # # #
# # # # # # # # # # #         self.setLayout(display_layout)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # def main():
# # # # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # # # #     page_a = CalculatorPage()
# # # # # # # # # # #     page_a.show()
# # # # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # # #
# # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # #     main()
# # # # # # # # # # import sys
# # # # # # # # # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
# # # # # # # # # # from PyQt5.QtCore import Qt, pyqtSignal
# # # # # # # # # #
# # # # # # # # # # class CalculatorPage(QWidget):
# # # # # # # # # #     next_page_signal = pyqtSignal(str)
# # # # # # # # # #
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #         super().__init__()
# # # # # # # # # #         self.initUI()
# # # # # # # # # #
# # # # # # # # # #     def initUI(self):
# # # # # # # # # #         self.setWindowTitle('Calculator')
# # # # # # # # # #
# # # # # # # # # #         self.result_display = QLineEdit()
# # # # # # # # # #         self.result_display.setReadOnly(True)
# # # # # # # # # #         self.result_display.setAlignment(Qt.AlignRight)
# # # # # # # # # #
# # # # # # # # # #         # Buttons for numbers and operations
# # # # # # # # # #         buttons_layout = QVBoxLayout()
# # # # # # # # # #         buttons = [
# # # # # # # # # #             '7', '8', '9', '/',
# # # # # # # # # #             '4', '5', '6', '*',
# # # # # # # # # #             '1', '2', '3', '-',
# # # # # # # # # #             '0', '.', '=', '+'
# # # # # # # # # #         ]
# # # # # # # # # #
# # # # # # # # # #         for label in buttons:
# # # # # # # # # #             button = QPushButton(label)
# # # # # # # # # #             button.clicked.connect(self.on_button_clicked)
# # # # # # # # # #             buttons_layout.addWidget(button)
# # # # # # # # # #
# # # # # # # # # #         layout = QVBoxLayout()
# # # # # # # # # #         layout.addWidget(self.result_display)
# # # # # # # # # #         layout.addLayout(buttons_layout)
# # # # # # # # # #
# # # # # # # # # #         self.setLayout(layout)
# # # # # # # # # #
# # # # # # # # # #     def on_button_clicked(self):
# # # # # # # # # #         clicked_button = self.sender()
# # # # # # # # # #         if clicked_button:
# # # # # # # # # #             text = clicked_button.text()
# # # # # # # # # #             if text == '=':
# # # # # # # # # #                 try:
# # # # # # # # # #                     result = eval(self.result_display.text())
# # # # # # # # # #                     self.result_display.setText(str(result))
# # # # # # # # # #                 except Exception as e:
# # # # # # # # # #                     self.result_display.setText("Error")
# # # # # # # # # #             else:
# # # # # # # # # #                 self.result_display.setText(self.result_display.text() + text)
# # # # # # # # # #
# # # # # # # # # #     def pass_result_to_main(self):
# # # # # # # # # #         result = self.result_display.text()
# # # # # # # # # #         self.next_page_signal.emit(result)
# # # # # # # # # #
# # # # # # # # # # class DisplayPage(QWidget):
# # # # # # # # # #     def __init__(self, result):
# # # # # # # # # #         super().__init__()
# # # # # # # # # #         self.result = result
# # # # # # # # # #         self.initUI()
# # # # # # # # # #
# # # # # # # # # #     def initUI(self):
# # # # # # # # # #         self.setWindowTitle('Display')
# # # # # # # # # #
# # # # # # # # # #         display_layout = QVBoxLayout()
# # # # # # # # # #         self.display_label = QLineEdit()
# # # # # # # # # #         self.display_label.setReadOnly(True)
# # # # # # # # # #         self.display_label.setAlignment(Qt.AlignCenter)
# # # # # # # # # #         self.display_label.setText(self.result)
# # # # # # # # # #         display_layout.addWidget(self.display_label)
# # # # # # # # # #
# # # # # # # # # #         self.setLayout(display_layout)
# # # # # # # # # import sys
# # # # # # # # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
# # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # # from page_b import PageB
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class PageA(QWidget):
# # # # # # # # #     def __init__(self):
# # # # # # # # #         super().__init__()
# # # # # # # # #         self.setWindowTitle("Page A: Calculator")
# # # # # # # # #         self.setGeometry(200, 200, 300, 200)
# # # # # # # # #
# # # # # # # # #         layout = QVBoxLayout()
# # # # # # # # #         self.input_line = QLineEdit()
# # # # # # # # #         self.input_line.setAlignment(Qt.AlignRight)
# # # # # # # # #         layout.addWidget(self.input_line)
# # # # # # # # #
# # # # # # # # #         buttons = [
# # # # # # # # #             ('7', self.add_text),
# # # # # # # # #             ('8', self.add_text),
# # # # # # # # #             ('9', self.add_text),
# # # # # # # # #             ('+', self.add_text),
# # # # # # # # #             ('4', self.add_text),
# # # # # # # # #             ('5', self.add_text),
# # # # # # # # #             ('6', self.add_text),
# # # # # # # # #             ('-', self.add_text),
# # # # # # # # #             ('1', self.add_text),
# # # # # # # # #             ('2', self.add_text),
# # # # # # # # #             ('3', self.add_text),
# # # # # # # # #             ('*', self.add_text),
# # # # # # # # #             ('0', self.add_text),
# # # # # # # # #             ('.', self.add_text),
# # # # # # # # #             ('C', self.clear_text),
# # # # # # # # #             ('/', self.add_text),
# # # # # # # # #             ('=', self.calculate_result)
# # # # # # # # #         ]
# # # # # # # # #
# # # # # # # # #         for btn_text, btn_method in buttons:
# # # # # # # # #             btn = QPushButton(btn_text)
# # # # # # # # #             if btn_text == '=':
# # # # # # # # #                 btn.setStyleSheet("background-color: #4CAF50; color: white;")
# # # # # # # # #             layout.addWidget(btn)
# # # # # # # # #             btn.clicked.connect(btn_method)
# # # # # # # # #
# # # # # # # # #         self.setLayout(layout)
# # # # # # # # #         self.result = None
# # # # # # # # #
# # # # # # # # #     def add_text(self):
# # # # # # # # #         sender = self.sender()
# # # # # # # # #         self.input_line.setText(self.input_line.text() + sender.text())
# # # # # # # # #
# # # # # # # # #     def clear_text(self):
# # # # # # # # #         self.input_line.clear()
# # # # # # # # #         self.result = None
# # # # # # # # #
# # # # # # # # #     def calculate_result(self):
# # # # # # # # #         expression = self.input_line.text()
# # # # # # # # #         try:
# # # # # # # # #             self.result = eval(expression)
# # # # # # # # #             self.input_line.setText(str(self.result))
# # # # # # # # #         except Exception as e:
# # # # # # # # #             print(e)
# # # # # # # # #             self.input_line.setText("Error")
# # # # # # # # #
# # # # # # # # #         page_b = PageB(self.result)
# # # # # # # # #         page_b.show()
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # #     page_a = PageA()
# # # # # # # # #     page_a.show()
# # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # # import sys
# # # # # # # # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
# # # # # # # # # from PyQt5.QtCore import Qt
# # # # # # # # #
# # # # # # # # # class CalculatorPage(QWidget):
# # # # # # # # #     def __init__(self):
# # # # # # # # #         super().__init__()
# # # # # # # # #         self.initUI()
# # # # # # # # #
# # # # # # # # #     def initUI(self):
# # # # # # # # #         self.setWindowTitle('Calculator')
# # # # # # # # #
# # # # # # # # #         self.result_display = QLineEdit()
# # # # # # # # #         self.result_display.setReadOnly(True)
# # # # # # # # #         self.result_display.setAlignment(Qt.AlignRight)
# # # # # # # # #
# # # # # # # # #         # Buttons for numbers and operations
# # # # # # # # #         buttons_layout = QVBoxLayout()
# # # # # # # # #         buttons = [
# # # # # # # # #             '7', '8', '9', '/',
# # # # # # # # #             '4', '5', '6', '*',
# # # # # # # # #             '1', '2', '3', '-',
# # # # # # # # #             '0', '.', '=', '+'
# # # # # # # # #         ]
# # # # # # # # #
# # # # # # # # #         for label in buttons:
# # # # # # # # #             button = QPushButton(label)
# # # # # # # # #             button.clicked.connect(self.on_button_clicked)
# # # # # # # # #             buttons_layout.addWidget(button)
# # # # # # # # #
# # # # # # # # #         # Next Page button
# # # # # # # # #         next_page_button = QPushButton("Next Page")
# # # # # # # # #         next_page_button.clicked.connect(self.next_page)
# # # # # # # # #
# # # # # # # # #         layout = QVBoxLayout()
# # # # # # # # #         layout.addWidget(self.result_display)
# # # # # # # # #         layout.addLayout(buttons_layout)
# # # # # # # # #         layout.addWidget(next_page_button)
# # # # # # # # #
# # # # # # # # #         self.setLayout(layout)
# # # # # # # # #
# # # # # # # # #     def on_button_clicked(self):
# # # # # # # # #         clicked_button = self.sender()
# # # # # # # # #         if clicked_button:
# # # # # # # # #             text = clicked_button.text()
# # # # # # # # #             if text == '=':
# # # # # # # # #                 try:
# # # # # # # # #                     result = eval(self.result_display.text())
# # # # # # # # #                     self.result_display.setText(str(result))
# # # # # # # # #                 except Exception as e:
# # # # # # # # #                     self.result_display.setText("Error")
# # # # # # # # #             else:
# # # # # # # # #                 self.result_display.setText(self.result_display.text() + text)
# # # # # # # # #
# # # # # # # # #     def next_page(self):
# # # # # # # # #         result = self.result_display.text()
# # # # # # # # #         page_b = DisplayPage(result)
# # # # # # # # #         page_b.show()
# # # # # # # # #         self.close()
# # # # # # # # #
# # # # # # # # # class DisplayPage(QWidget):
# # # # # # # # #     def __init__(self, result):
# # # # # # # # #         super().__init__()
# # # # # # # # #         self.result = result
# # # # # # # # #         self.initUI()
# # # # # # # # #
# # # # # # # # #     def initUI(self):
# # # # # # # # #         self.setWindowTitle('Display')
# # # # # # # # #
# # # # # # # # #         display_layout = QVBoxLayout()
# # # # # # # # #         self.display_label = QLineEdit()
# # # # # # # # #         self.display_label.setReadOnly(True)
# # # # # # # # #         self.display_label.setAlignment(Qt.AlignCenter)
# # # # # # # # #         self.display_label.setText(self.result)
# # # # # # # # #         display_layout.addWidget(self.display_label)
# # # # # # # # #
# # # # # # # # #         self.setLayout(display_layout)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def main():
# # # # # # # # #     app = QApplication(sys.argv)
# # # # # # # # #     page_a = CalculatorPage()
# # # # # # # # #     page_a.show()
# # # # # # # # #     sys.exit(app.exec_())
# # # # # # # # #
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     main()
# # # # # # # #
# # # # # # # #
# # # # # # # # import sys
# # # # # # # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
# # # # # # # # from PyQt5.QtCore import Qt, pyqtSignal
# # # # # # # #
# # # # # # # # class CalculatorPage(QWidget):
# # # # # # # #     next_page_signal = pyqtSignal(str)
# # # # # # # #
# # # # # # # #     def __init__(self):
# # # # # # # #         super().__init__()
# # # # # # # #         self.initUI()
# # # # # # # #
# # # # # # # #     def initUI(self):
# # # # # # # #         self.setWindowTitle('Calculator')
# # # # # # # #
# # # # # # # #         self.result_display = QLineEdit()
# # # # # # # #         self.result_display.setReadOnly(True)
# # # # # # # #         self.result_display.setAlignment(Qt.AlignRight)
# # # # # # # #
# # # # # # # #         # Buttons for numbers and operations
# # # # # # # #         buttons_layout = QVBoxLayout()
# # # # # # # #         buttons = [
# # # # # # # #             '7', '8', '9', '/',
# # # # # # # #             '4', '5', '6', '*',
# # # # # # # #             '1', '2', '3', '-',
# # # # # # # #             '0', '.', '=', '+'
# # # # # # # #         ]
# # # # # # # #
# # # # # # # #         for label in buttons:
# # # # # # # #             button = QPushButton(label)
# # # # # # # #             button.clicked.connect(self.on_button_clicked)
# # # # # # # #             buttons_layout.addWidget(button)
# # # # # # # #
# # # # # # # #         # Next Page button
# # # # # # # #         next_page_button = QPushButton("Next Page")
# # # # # # # #         next_page_button.clicked.connect(self.next_page)
# # # # # # # #
# # # # # # # #         layout = QVBoxLayout()
# # # # # # # #         layout.addWidget(self.result_display)
# # # # # # # #         layout.addLayout(buttons_layout)
# # # # # # # #         layout.addWidget(next_page_button)
# # # # # # # #
# # # # # # # #         self.setLayout(layout)
# # # # # # # #
# # # # # # # #     def on_button_clicked(self):
# # # # # # # #         clicked_button = self.sender()
# # # # # # # #         if clicked_button:
# # # # # # # #             text = clicked_button.text()
# # # # # # # #             if text == '=':
# # # # # # # #                 try:
# # # # # # # #                     result = eval(self.result_display.text())
# # # # # # # #                     self.result_display.setText(str(result))
# # # # # # # #                 except Exception as e:
# # # # # # # #                     self.result_display.setText("Error")
# # # # # # # #             else:
# # # # # # # #                 self.result_display.setText(self.result_display.text() + text)
# # # # # # # #
# # # # # # # #     def next_page(self):
# # # # # # # #         result = self.result_display.text()
# # # # # # # #         print(f"calculator",result)
# # # # # # # #         self.next_page_signal.emit(result)
# # # # # # # #
# # # # # # # # class DisplayPage(QWidget):
# # # # # # # #     def __init__(self):
# # # # # # # #         super().__init__()
# # # # # # # #         self.initUI()
# # # # # # # #
# # # # # # # #     def initUI(self):
# # # # # # # #         self.setWindowTitle('Display')
# # # # # # # #
# # # # # # # #         display_layout = QVBoxLayout()
# # # # # # # #         self.display_label = QLineEdit()
# # # # # # # #         self.display_label.setReadOnly(True)
# # # # # # # #         self.display_label.setAlignment(Qt.AlignCenter)
# # # # # # # #         display_layout.addWidget(self.display_label)
# # # # # # # #
# # # # # # # #         self.setLayout(display_layout)
# # # # # # # #
# # # # # # # #     def display_result(self, result):
# # # # # # # #         self.display_label.setText(result)
# # # # # # # #
# # # # # # # #
# # # # # # # # def main():
# # # # # # # #     app = QApplication(sys.argv)
# # # # # # # #     calculator_page = CalculatorPage()
# # # # # # # #     display_page = DisplayPage()
# # # # # # # #
# # # # # # # #     calculator_page.next_page_signal.connect(display_page.display_result)
# # # # # # # #     calculator_page.show()
# # # # # # # #
# # # # # # # #     sys.exit(app.exec_())
# # # # # # # #
# # # # # # # #
# # # # # # # def update_label_with_coordinates( top_left, bottom_right):
# # # # # # #     text = f"  Top Left:\n {top_left}\n Bottom Right:\n {bottom_right}"
# # # # # # #     # self.label_c_result.setText(text)
# # # # # # #     top_left_lat_coordinates1 = top_left.split(",")[0].split()
# # # # # # #     lat_1 = top_left_lat_coordinates1[0]
# # # # # # #     top_left_lon_coordinates1 = top_left.split(",")[1].split()
# # # # # # #     lon_1 = top_left_lon_coordinates1[0]
# # # # # # #     print(lat_1,lon_1)
# # # # # # #
# # # # # # #     top_left_lat_coordinates2 = bottom_right.split(",")[0].split()
# # # # # # #     lat_2 = top_left_lat_coordinates2[0]
# # # # # # #     top_left_lon_coordinates2 = bottom_right.split(",")[1].split()
# # # # # # #     lon_2 = top_left_lon_coordinates2[0]
# # # # # # #     print(lat_2, lon_2)
# # # # # # #
# # # # # # #
# # # # # # import re
# # # # # # # update_label_with_coordinates("32.25578142390457,113.3184814453125","32.25578142390457,113.3184814453125")
# # # # # # def replace_extent_coordinates(extent, coordinates):
# # # # # #     pattern = re.compile(r'\b(a|b|c|d)\b')
# # # # # #     extent_replaced = re.sub(pattern, lambda match: str(coordinates[match.group(0)]), extent)
# # # # # #     return extent_replaced
# # # # # #
# # # # # #
# # # # # # def expected_INPUT(reso):
# # # # # #     with open('H:/DEM/expected_DEM/expected_DEM.ttl', 'r') as file:
# # # # # #         ttl_content = file.read()
# # # # # #
# # # # # #     # Replace the extent coordinates placeholders
# # # # # #
# # # # # #     # Replace the extent coordinates placeholders
# # # # # #     extent_match = re.search(r'data:extent "(.*?)"\^\^geo:wktLiteral', ttl_content)
# # # # # #     if extent_match:
# # # # # #         extent = extent_match.group(1)
# # # # # #         # a_lat, b_lat = coordinates1(coordinates1[0], coordinates1[1])
# # # # # #         # c_lat, d_lat = coordinates2(coordinates2[0], coordinates2[1])
# # # # # #         extent_coordinates = {
# # # # # #             'a': 10,
# # # # # #             'b': 20,
# # # # # #             'c': 30,
# # # # # #             'd': 40
# # # # # #         }
# # # # # #
# # # # # #     def replace_placeholder(ttl_content, placeholder, value):
# # # # # #         return ttl_content.replace(placeholder, value)
# # # # # #
# # # # # #     spatial_resolution_value = reso
# # # # # #     new_extent = replace_extent_coordinates(extent, extent_coordinates)
# # # # # #
# # # # # #     # Replace the old extent with the new one in the TTL content
# # # # # #     new_ttl_content = ttl_content.replace(extent, new_extent)
# # # # # #     # Update the spatial resolution placeholder 'e' with the true numeric value
# # # # # #     ttl_content1 = new_ttl_content.replace('dcat:spatialResolutionInMeters e',
# # # # # #                                            f'dcat:spatialResolutionInMeters {spatial_resolution_value}')
# # # # # #
# # # # # #     # Write the modified TTL content back to the file
# # # # # #     with open('H:/DEM/expected_DEM/expected_DEM2.ttl', 'w') as file:
# # # # # #         file.write(ttl_content1)
# # # # # # expected_INPUT(90)
# # # # #
# # from owlready2 import *
# # import math
# # import csv
# # from collections import Counter
# # import arcpy
# # from arcpy import env
# # from arcpy.sa import *
# # ontology="H:/SHACL/framework_geocomputation_geomorphology_test_fullname_TEST.owl"
# # from algorithm_model import RASTER_CLIP
# #
# # def knowledge_graph_data(ontology,data_name):
# #     a = get_ontology(ontology).load()
# #     on_class=a.classes()
# #     on_object_property=a.object_properties()
# #     on_data_property=a.data_properties()
# #     on_individual=a.individuals()
# #     on_anxioms=a.general_axioms()
# #     # on=a.get_triples()
# #     on=a.variables()
# #     on_rule=a.rules()
# #     l_object_property=list(on_object_property)
# #     l_class=list(on_class)
# #     l_rules=list(on_rule)
# #     l_individuals=list(on_individual)
# #     my_dict = {str(item).split('.')[1]: item for item in l_individuals}
# #     my_object_project = {str(item).split('.')[1]: item for item in l_object_property}
# #     data=(my_dict[str(data_name)].path)[0]
# #     return data
# #
# #
# # def clear_folder(folder_path):
# #     # Iterate over all files in the folder
# #     for file_name in os.listdir(folder_path):
# #         file_path = os.path.join(folder_path, file_name)
# #
# #         # Check if it's a file
# #         if os.path.isfile(file_path):
# #             # Delete the file
# #             os.remove(file_path)
# # output="H:/DEM/application_clip/raster_clip_input.tif"
# # path="H:/DEM/application_clip"
# # data=knowledge_graph_data(ontology,"SRTM_90")
# # # print(type(my_dict['FABDEM_30'].path))
# # x_min=113.12210083007812
# # y_min=31.85423130442635
# # x_max=113.83346557617188
# # y_max=32.29641979896909
# # clear_folder(path)
# # # RASTER_CLIP(data,output,x_min,y_min,x_max,y_max)
# # # #
# # # #
# # # # from PyQt5 import QtWidgets, QtCore
# # # #
# # # # class MyWidget(QtWidgets.QWidget):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #
# # # #         self.setWindowTitle("Action with Progress Bar Example")
# # # #         self.setGeometry(300, 300, 300, 150)
# # # #
# # # #         self.run_button = QtWidgets.QPushButton("Run Action", self)
# # # #         self.run_button.setGeometry(30, 40, 120, 30)
# # # #         self.run_button.clicked.connect(self.start_action)
# # # #
# # # #         self.progress_bar = QtWidgets.QProgressBar(self)
# # # #         self.progress_bar.setGeometry(30, 90, 250, 20)
# # # #         self.progress_bar.setValue(0)
# # # #
# # # #     def start_action(self):
# # # #         self.run_button.setEnabled(False)  # Disable button during action
# # # #         self.progress_bar.setValue(0)  # Reset progress bar
# # # #         self.long_running_action()  # Call the long-running action
# # # #         self.run_button.setEnabled(True)  # Re-enable button when action is finished
# # # #
# # # #     def long_running_action(self):
# # # #         # Simulate a time-consuming action
# # # #         for i in range(10):
# # # #             print("Action in progress...")
# # # #             QtCore.QThread.msleep(1000)  # Simulate some work (1 second)
# # # #             progress = (i + 1) * 10  # Calculate progress percentage
# # # #             self.progress_bar.setValue(progress)  # Update progress bar
# # # #         print("Action finished")
# # # #
# # # # if __name__ == "__main__":
# # # #     import sys
# # # #     app = QtWidgets.QApplication(sys.argv)
# # # #     window = MyWidget()
# # # #     window.show()
# # # #     sys.exit(app.exec_())
# # # #
# # #
# # #
# # #
# # # from PyQt5 import QtWidgets, QtCore
# # #
# # # class MyWidget(QtWidgets.QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.setWindowTitle("Action Finished Example")
# # #         self.setGeometry(300, 300, 300, 150)
# # #
# # #         self.run_button = QtWidgets.QPushButton("Run Action", self)
# # #         self.run_button.setGeometry(30, 40, 120, 30)
# # #         self.run_button.clicked.connect(self.start_action)
# # #
# # #     def start_action(self):
# # #         # Simulate a time-consuming action
# # #         self.run_button.setEnabled(False)  # Disable button during action
# # #         QtCore.QTimer.singleShot(3000, self.action_finished)  # Simulate action finishing after 3 seconds
# # #
# # #     def action_finished(self):
# # #         print("Action finished")
# # #         self.run_button.setEnabled(True)  # Re-enable button when action is finished
# # #
# # # if __name__ == "__main__":
# # #     import sys
# # #     app = QtWidgets.QApplication(sys.argv)
# # #     window = MyWidget()
# # #     window.show()
# # #     sys.exit(app.exec_())
# #
# # #
# # # import sys
# # # from PyQt5 import QtWidgets, QtCore
# # #
# # # class MyWidget(QtWidgets.QWidget):
# # #     calculation_finished = QtCore.pyqtSignal()  # Define a custom signal
# # #
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.setWindowTitle("Calculation Finished Example")
# # #         self.setGeometry(300, 300, 300, 150)
# # #
# # #         self.run_button = QtWidgets.QPushButton("Run Action", self)
# # #         self.run_button.setGeometry(30, 40, 120, 30)
# # #         self.run_button.clicked.connect(self.start_calculation)
# # #
# # #         self.calculation_finished.connect(self.action_finished)  # Connect the signal to the slot
# # #
# # #     def start_calculation(self):
# # #         # Simulate a time-consuming calculation
# # #         self.run_button.setEnabled(False)  # Disable button during calculation
# # #
# # #         # Start the calculation in a separate thread
# # #         self.thread = QtCore.QThread()
# # #         self.worker = Worker()
# # #         self.worker.moveToThread(self.thread)
# # #         self.thread.started.connect(lambda: self.worker.run(data, output, x_min, y_min, x_max, y_max))
# # #         self.worker.finished.connect(self.thread.quit)
# # #         self.worker.finished.connect(self.worker.deleteLater)
# # #         self.thread.finished.connect(self.thread.deleteLater)
# # #         self.calculation_finished.connect(self.thread.quit)  # Quit the thread when calculation is finished
# # #         self.thread.start()
# # #
# # #     def action_finished(self):
# # #         print("Action finished")
# # #         self.run_button.setEnabled(True)  # Re-enable button when action is finished
# # #
# # # class Worker(QtCore.QObject):
# # #     finished = QtCore.pyqtSignal()
# # #
# # #     @QtCore.pyqtSlot(object, str, int, int, int, int)
# # #     def run(self, data, output, x_min, y_min, x_max, y_max):
# # #         # Run the RASTER_CLIP function
# # #         RASTER_CLIP(data, output, x_min, y_min, x_max, y_max)
# # #         self.finished.emit()  # Emit the finished signal when the calculation is done
# # #
# # # # def RASTER_CLIP(data, output, x_min, y_min, x_max, y_max):
# # # #     # Replace this with the actual implementation of RASTER_CLIP
# # # #     print("Running RASTER_CLIP function")
# # #
# # # if __name__ == "__main__":
# # #     app = QtWidgets.QApplication(sys.argv)
# # #     window = MyWidget()
# # #     window.show()
# # #     sys.exit(app.exec_())
# # import sys
# # import os
# # from PyQt5 import QtWidgets, QtCore
# #
# # # Simulated function to generate a TIFF file
# # # def generate_tiff_file():
# # #     # Simulate generating a TIFF file
# # #     with open("output.tif", "w") as f:
# # #         f.write("Some example TIFF data")
# #
# # class MyWidget(QtWidgets.QWidget):
# #     calculation_finished = QtCore.pyqtSignal()  # Define a custom signal
# #
# #     def __init__(self):
# #         super().__init__()
# #
# #         self.setWindowTitle("Action with File Check Example")
# #         self.setGeometry(300, 300, 300, 150)
# #
# #         self.run_button = QtWidgets.QPushButton("Run Action", self)
# #         self.run_button.setGeometry(30, 40, 120, 30)
# #         self.run_button.clicked.connect(self.start_action)
# #
# #         self.calculation_finished.connect(self.action_finished)  # Connect the signal to the slot
# #
# #     def start_action(self):
# #         self.run_button.setEnabled(False)  # Disable button during action
# #         self.thread = QtCore.QThread()
# #         self.worker = Worker()
# #         self.worker.moveToThread(self.thread)
# #         self.thread.started.connect(self.worker.run)
# #         self.worker.finished.connect(self.calculation_finished)
# #         self.worker.finished.connect(self.thread.quit)
# #         self.worker.finished.connect(self.worker.deleteLater)
# #         self.thread.finished.connect(self.thread.deleteLater)
# #         self.thread.start()
# #
# #     def action_finished(self):
# #             print("Action finished")
# #             self.run_button.setEnabled(True)  # Re-enable button when action is finished
# #             QtCore.QCoreApplication.quit()  # Quit the application event loop
# # class Worker(QtCore.QObject):
# #     finished = QtCore.pyqtSignal()
# #
# #     @QtCore.pyqtSlot()
# #     def run(self):
# #         # Simulate generating a TIFF file
# #         # RASTER_CLIP(data, output, x_min, y_min, x_max, y_max)
# #         # Check if the file exists
# #         while not os.path.exists(output):
# #             QtCore.QThread.msleep(100)  # Wait for 0.1 second
# #         self.finished.emit()  # Emit finished signal when the file is found
# #
# # if __name__ == "__main__":
# #     app = QtWidgets.QApplication(sys.argv)
# #     window = MyWidget()
# #     window.show()
# #     sys.exit(app.exec_())
#
from owlready2 import *
ontology="H:/SHACL/framework_geocomputation_geomorphology_test_fullname_TEST.owl"
def kg_class(ontology):
    a = get_ontology(ontology).load()
    on_class=a.classes()
    on_object_property=a.object_properties()
    on_data_property=a.data_properties()
    # on_individual=a.individuals()
    on_anxioms=a.general_axioms()
    # on=a.get_triples()
    on=a.variables()
    on_rule=a.rules()
    l_object_property=list(on_object_property)
    l_class=list(on_class)
    l_rules=list(on_rule)
    instance=on_class
    my_dict = {str(item).split('.')[1]: item for item in l_class}
    return my_dict


def kg_input(model_name):

    mydict=kg_class(ontology)
    input_of_model=mydict[model_name].hasInput
    function_name=(mydict[model_name].function)[0]
    # print(function_name)
    if len(input_of_model)==1:
        pathdic1={}
        input_example=input_of_model[0].instances()
        # =my_dict[name1].instances()
        input_path=input_example[0].path
        key=input_of_model[0]
        print(key)
        key_split= str(key).split('.')
        key_part = key_split[-1]
        pathdic1[key_part] = input_path[0]
        # print(input_of_model,input_example,input_path)
        return pathdic1,function_name
    else:
        inputdic = {str(item).split('.')[1]: item for item in input_of_model}  # Assuming input_of_model is a dictionary
        # print(inputdic)
        function_name = (mydict[model_name].function)[0]
        pathdic = {}
        for key in inputdic:
            input_ins = (inputdic[key]).instances()
            input_path = input_ins
            int=input_path[0].path
            pathdic[key] = int[0]
        print(pathdic)
        return pathdic,function_name
# from algorithm_model import Identify_water_net,test





# print(input[0]['DEM_boundary'],input[1])
# func = globals().get(input[1])
# work_space="H:/DEM/application/application_result/"
# dem_name='DEM1'
# result=func(input[0],work_space,dem_name,ontology)
#
#
#


from algorithm_model import *
ontology="H:/SHACL/framework_geocomputation_geomorphology_test_fullname_TEST.owl"
# input="H:/DEM/application/application_clip/raster_clip_input.tif"
# output="DEM1"
# workpath="H:/DEM/application/application_result/"
# Project_DEM(input,output,workpath,ontology)
#
# Identify_water_net()
work_space="H:/DEM/app/test/"
dem_name='DEM1'

# model_name ='Identify_water_net'   #change HERE
# # 'Division_of_mountain_unit'
# input=kg_input(ontology,model_name)
# print(input[0],input[1])
# func = globals().get(input[1])
# result=func(input[0],work_space,dem_name,ontology)
#
#
# model_name1 ='Validate_DEM'   #change HERE
# # 'Division_of_mountain_unit'
# input1=kg_input(ontology,model_name1)
# print(input1[0],input1[1])
# func1 = globals().get(input1[1])
# result1=func1(input1[0],work_space,dem_name,ontology)
def action(model_name2):   #change HERE
    # 'Division_of_mountain_unit'
    input2=kg_input(ontology,model_name2)
    print(input2[0],input2[1])
    func2 = globals().get(input2[1])
    func2(input2[0],work_space,dem_name,ontology)
import arcpy
# action("Identify_water_net")
# action("Validate_DEM")
# action("Identify_DEM_boundary")
# action("Calculate_slope_value")
# Detect_mountain_unit(work_space,dem_name,ontology)
# action("Rough_Classification_of_mountain_and_plain")
# action("Identify_plain_within_mountains")
# action('Merge_area_of_mountain_and_plain')
# action('Vectorize_Merge_area_of_mountain_and_plain')
action('Vectorize_Complete_mountain_and_plain')


# out_table='H:/DEM/app/test/outflowacctable'
# outFlowAccumulation_name='H:/DEM/app/test/outflowacc.tif'
#
# stats = arcpy.GetRasterProperties_management(outFlowAccumulation_name,  "MAXIMUM","")
#
# # Print statistics
# print("Raster Statistics:")
# print(f"Max: {stats[0]}")



# arcpy.analysis.Statistics(outFlowAccumulation_name, out_table, [["", "MAX"]], "")
# with arcpy.da.SearchCursor(out_table, ["MAX_Value"]) as cursor:
#     for row in cursor:
#         max_value = row[0]
#         print(max_value)
#     if max_value<=4000:
#         deep= 3000
#     else:
#         deep=4444