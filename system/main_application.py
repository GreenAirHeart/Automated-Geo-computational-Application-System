# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QDialog
from login import *
from start_page import *
from application import *
from model_page import *
from data_page import *
from processing_page import *
from result_page import *
from PyQt5.QtCore import QTimer
# /from expected_DEM import *
class Login(QDialog,Ui_login_page):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)


class Start(QDialog,Ui_start_page):
    def __init__(self):
        super(Start,self).__init__()
        self.setupUi(self)




class Application(QDialog,Ui_application_page):
    def __init__(self):
        super(Application,self).__init__()
        self.setupUi(self)

# class Application(QDialog):
#     def __init__(self):
#         super(Application, self).__init__()
#         self.ui = Ui_application_page()  # Create an instance of the UI definition class
#         self.ui.setupUi(self)  # Setup the UI
#
#         # Connect the button click signal to the method in Application class
#         self.ui.pushButton_2.clicked.connect(self.ui.emit_coordinates_ready)




class Model(QDialog,Ui_model_page):
    def __init__(self):
        super(Model,self).__init__()
        self.setupUi(self)


class Data(QDialog,Ui_data_page):
    def __init__(self):
        super(Data,self).__init__()
        self.setupUi(self)


class Processing(QDialog,Ui_processing_page):
    def __init__(self):
        super(Processing,self).__init__()
        self.setupUi(self)








class Result(QDialog,Ui_result_page):
    def __init__(self):
        super(Result,self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    login= Login()
    start = Start ()
    application = Application()
    model = Model()
    data = Data ()
    processing = Processing ()
    result = Result ()
    login.show()

    # app_page = Ui_application_page()
    # model_page = Ui_model_page()

    #login
    login.pushButton_2.clicked.connect(login.hide)
    login.pushButton_2.clicked.connect(application.open)

    #start page
    # start.pushButton_2.clicked.connect(start.hide)
    # start.pushButton_2.clicked.connect(application.open)


    #application page

    # # print(application.handle_top_left.__get__("top_left_value"))
    # application.pushButton_2.clicked.connect(application.get_coordinates)

    # app_page.coordinates_ready.connect(model_page.update_label_with_coordinates)
    application.pushButton_3.clicked.connect(application.hide)
    application.pushButton_3.clicked.connect(model.show)

    application.coordinates_ready.connect(model.update_label_with_coordinates)
    application.task_ready.connect(model.update_label_with_task)
    application.resolution_ready.connect(model.update_label_with_resolution)
    application.task_ready.connect(processing.update_label_with_task)

    application.coordinates_ready.connect(data.update_label_with_coordinates)
    application.coordinates_ready.connect(data.expected_INPUT1)
    application.resolution_ready.connect(data.update_label_with_resolution)
    application.resolution_ready.connect(data.expected_INPUT2)
    application.coordinates_ready.connect(processing.update_label_with_coordinates)
    # application.coordinates_ready.connect(data.trigger_expected_input)
    # application.get_coordinates()
    # application.pushButton_3.clicked.connect()

    #model page
    model.pushButton_3.clicked.connect(model.hide)
    model.pushButton_3.clicked.connect(data.show)
    model.pushButton_4.clicked.connect(model.hide)
    model.pushButton_4.clicked.connect(application.show)

    # model.label_a_result(model,)

    # model.pushButton_4.clicked.connect(data.expected_INPUT())
    #data page
    data.pushButton_3.clicked.connect(data.hide)
    data.pushButton_3.clicked.connect(processing.show)
    data.pushButton_4.clicked.connect(data.hide)
    data.pushButton_4.clicked.connect(model.show)
    data.data_ready.connect(processing.update_label_with_data)
    # data.trigger_input.connect(data.expected_INPUT)
    # data.check_box_4.clicked.connect(model.show)

    #processing page
    processing.pushButton_4.clicked.connect(processing.hide)
    processing.pushButton_4.clicked.connect(data.show)


    #result page
    # time.sleep(5)
    # processing.pushButton_2.clicked.connect(processing.hide)
    # processing.pushButton_2.clicked.connect(result.show)
    processing.pushButton_2.clicked.connect(lambda: QTimer.singleShot(5000, lambda: show_result(processing, result)))


    # Define a function to hide processing and show result
    def show_result(processing, result):
        processing.hide()
        # result.show()
    # processing.calculation_finished.connect(result.update_with_pic)



    sys.exit(app.exec_())

