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




class Application(QDialog,Ui_application_page):
    def __init__(self):
        super(Application,self).__init__()
        self.setupUi(self)




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
    application = Application()
    model = Model()
    data = Data ()
    processing = Processing ()
    result = Result ()
    
    
    application.show()

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


    #model page
    model.pushButton_3.clicked.connect(model.hide)
    model.pushButton_3.clicked.connect(data.show)
    model.pushButton_4.clicked.connect(model.hide)
    model.pushButton_4.clicked.connect(application.show)


    #data page
    data.pushButton_3.clicked.connect(data.hide)
    data.pushButton_3.clicked.connect(processing.show)
    data.pushButton_4.clicked.connect(data.hide)
    data.pushButton_4.clicked.connect(model.show)
    data.data_ready.connect(processing.update_label_with_data)


    #processing page
    processing.pushButton_4.clicked.connect(processing.hide)
    processing.pushButton_4.clicked.connect(data.show)
    processing.pushButton_2.clicked.connect(processing.hide)
    processing.pushButton_2.clicked.connect(result.show)

    



    def show_result(processing, result):
        processing.hide()



    sys.exit(app.exec_())

