# -*- coding: utf-8 -*-


from PyQt5.QtGui import QIcon
from jsonschema import validate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import json
import Sql
import JSONSchema
import JsonSql
from functions import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 775)
        Form.setMinimumSize(QtCore.QSize(899, 555))
        #Initialisation of tree-view
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(700, 10, 461, 331))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.visB = QtWidgets.QPushButton(Form)
        self.visB.setGeometry(QtCore.QRect(490, 50, 181, 101))
        self.visB.setObjectName("visB")
        self.valViewer = QtWidgets.QTextBrowser(Form)
        self.valViewer.setGeometry(QtCore.QRect(480, 10, 201, 31))
        self.valViewer.setObjectName("valViewer")
        self.javacB = QtWidgets.QPushButton(Form)
        self.javacB.setGeometry(QtCore.QRect(490, 160, 181, 101))
        self.javacB.setObjectName("javacB")
        self.jschemaB = QtWidgets.QPushButton(Form)
        self.jschemaB.setGeometry(QtCore.QRect(490, 270, 181, 101))
        self.jschemaB.setObjectName("jschemaB")
        self.sqlB = QtWidgets.QPushButton(Form)
        self.sqlB.setGeometry(QtCore.QRect(490, 380, 181, 101))
        self.sqlB.setObjectName("sqlB")
        self.schemaViewer = QtWidgets.QTextBrowser(Form)
        self.schemaViewer.setGeometry(QtCore.QRect(10, 60, 461, 231))
        self.schemaViewer.setObjectName("schemaViewer")
        self.loadB = QtWidgets.QPushButton(Form)
        self.loadB.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.loadB.setObjectName("loadB")
        self.schemaEdit = QtWidgets.QTextEdit(Form)
        self.schemaEdit.setGeometry(QtCore.QRect(10, 450, 461, 321))
        self.schemaEdit.setObjectName("schemaEdit")
        self.sqlreqB = QtWidgets.QPushButton(Form)
        self.sqlreqB.setGeometry(QtCore.QRect(490, 720, 181, 51))
        self.sqlreqB.setObjectName("sqlreqB")
        self.sqlrecViewer = QtWidgets.QTextBrowser(Form)
        self.sqlrecViewer.setGeometry(QtCore.QRect(700, 350, 461, 421))
        self.sqlrecViewer.setObjectName("sqlrecViewer")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 300, 461, 141))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.valB = QtWidgets.QPushButton(Form)
        self.valB.setGeometry(QtCore.QRect(490, 560, 181, 51))
        self.valB.setObjectName("valB")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 520, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(490, 650, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 490, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 620, 171, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.visB.setText(_translate("Form", "Визуализировать"))
        self.javacB.setText(_translate("Form", "Генерация Java-класса"))
        self.jschemaB.setText(_translate("Form", "JSON из JSON-schema"))
        self.sqlB.setText(_translate("Form", "SQL-запрос"))
        self.schemaViewer.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON-schema JSON файла:</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.loadB.setText(_translate("Form", "Выбрать JSON файл"))
        self.schemaEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON-schema:</p>\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sqlreqB.setText(_translate("Form", "Валидация"))
        self.sqlrecViewer.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SQL-запрос:</p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">JSON из JSON-schema</p></body></html>"))
        self.valB.setText(_translate("Form", "Выгрузить JSON"))
        self.label.setText(_translate("Form", "Введите название:"))
        self.label_2.setText(_translate("Form", "Введите название:"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadB.clicked.connect(self.load)
        self.ui.visB.clicked.connect(self.vis)
        self.ui.sqlreqB.clicked.connect(self.sqlreq)
        self.ui.sqlB.clicked.connect(self.sql)
        self.ui.jschemaB.clicked.connect(self.jschema)
        self.ui.valB.clicked.connect(self.val)
        self.sql_connect = Sql.Sql("Buffer", "DESKTOP-1EDGED1\SQLEXPRESS")

    @pyqtSlot()
    def load(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.file = self.file.replace(str("\\"), "/")
        with open(self.file, 'r+') as f:
            self.d = f.read()
        self.dd = json.loads(self.d)

    @pyqtSlot()
    def vis(self):
        fill_widget(self.ui.treeWidget, self.dd)

    @pyqtSlot()
    def val(self):
        schema = self.ui.schemaEdit.toPlainText()
        js = self.d
        if len(str(schema)) == 0:
            answ = validator_for_vizual_app(js)
        else:
            answ = validator_for_vizual_app1(js, schema)

        if len(answ) == 2:
            self.ui.valViewer.setText('Схема валидна')
            self.ui.schemaViewer.setText(str(answ[1]))
        elif answ == "Schema Error":
            self.ui.valViewer.setText("Schema Error")
        elif answ == 'True':
            self.ui.valViewer.setText('Схема валидна')
        elif answ == 'False':
            self.ui.valViewer.setText('Схема невалидна')

    @pyqtSlot()
    def sql(self):
        json_s = JSONSchema.JSONSchema(self.d)
        table = self.ui.textEdit_2.toPlainText()
        json_sql = JsonSql.JsonSql()
        sql_request = json_sql.getSql(json_s.serialized, json_s.schema['properties'], table, table)
        self.sql_connect.cursor.execute(
            " CREATE TABLE " + table + " (Type VARCHAR(10), Name VARCHAR(100), Value NVARCHAR(250)) ")
        self.sql_connect.cursor.execute(sql_request)
        self.ui.sqlrecViewer.setText(sql_request)

    @pyqtSlot()
    def jschema(self):
        schema = self.ui.schemaEdit.toPlainText()
        self.ui.textBrowser_4.setText(str(generate_json_from_schema(schema)))

    @pyqtSlot()
    def sqlreq(self):
        qwe = JsonSql.JsonSql()
        json_answer = qwe.unpack(self.sql_connect.cursor, self.ui.textEdit_3.toPlainText())
        self.ui.sqlrecViewer.setText(json_answer)


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Json-parser")
widget.setWindowIcon(QIcon("icon.png"))
widget.addWidget(mainWindow)
widget.setFixedHeight(780)
widget.setFixedWidth(1180)
widget.show()

sys.exit(app.exec_())
