# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 60, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 180, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 370, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 370, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 370, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 280, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 280, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.no_of_clicks_1 = QtWidgets.QLabel(self.centralwidget)
        self.no_of_clicks_1.setGeometry(QtCore.QRect(40, 450, 151, 41))
        self.no_of_clicks_1.setObjectName("no_of_clicks_1")
        self.no_of_clicks_2 = QtWidgets.QLabel(self.centralwidget)
        self.no_of_clicks_2.setGeometry(QtCore.QRect(310, 450, 131, 41))
        self.no_of_clicks_2.setObjectName("no_of_clicks_2")
        self.no_of_clicks_3 = QtWidgets.QLabel(self.centralwidget)
        self.no_of_clicks_3.setGeometry(QtCore.QRect(560, 450, 131, 41))
        self.no_of_clicks_3.setObjectName("no_of_clicks_3")
        self.submit_1 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_1.setGeometry(QtCore.QRect(60, 510, 75, 23))
        self.submit_1.setObjectName("submit_1")
        self.submit_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_2.setGeometry(QtCore.QRect(320, 510, 75, 23))
        self.submit_2.setObjectName("submit_2")
        self.submit_3 = QtWidgets.QPushButton(self.centralwidget)
        self.submit_3.setGeometry(QtCore.QRect(580, 510, 75, 23))
        self.submit_3.setObjectName("submit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Random Text Generator"))
        self.label_2.setText(_translate("MainWindow", "\"?\""))
        self.label_3.setText(_translate("MainWindow", "\"?\""))
        self.label_4.setText(_translate("MainWindow", "\"?\""))
        self.pushButton.setText(_translate("MainWindow", "Click ME"))
        self.pushButton_2.setText(_translate("MainWindow", "Click ME"))
        self.pushButton_3.setText(_translate("MainWindow", "Click ME"))
        self.label_5.setText(_translate("MainWindow", "No Of Clicks :"))
        self.label_6.setText(_translate("MainWindow", "No Of Clicks :"))
        self.label_7.setText(_translate("MainWindow", "No Of Clicks :"))
        self.no_of_clicks_1.setText(_translate("MainWindow", "Total No Of Clicks : 0"))
        self.no_of_clicks_2.setText(_translate("MainWindow", "Total No Of Clicks : 0"))
        self.no_of_clicks_3.setText(_translate("MainWindow", "Total No Of Clicks : 0"))
        self.submit_1.setText(_translate("MainWindow", "Submit"))
        self.submit_2.setText(_translate("MainWindow", "Submit"))
        self.submit_3.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
