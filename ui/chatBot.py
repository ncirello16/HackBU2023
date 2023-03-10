# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/chatBot.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(874, 508)
        MainWindow.setStyleSheet("background-color: rgb(47, 49, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.output_lineEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.output_lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.output_lineEdit.setFont(font)
        self.output_lineEdit.setStyleSheet("background-color: rgb(54, 57, 63);\n"
"color: rgb(234, 234, 234);")
        self.output_lineEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output_lineEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_lineEdit.setLineWidth(1)
        self.output_lineEdit.setReadOnly(True)
        self.output_lineEdit.setObjectName("output_lineEdit")
        self.verticalLayout.addWidget(self.output_lineEdit)
        self.input_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.input_lineEdit.setFont(font)
        self.input_lineEdit.setStyleSheet("background-color: rgb(64, 68, 75);\n"
"color: rgb(227, 227, 227);")
        self.input_lineEdit.setText("")
        self.input_lineEdit.setFrame(False)
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.verticalLayout.addWidget(self.input_lineEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dic_switch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dic_switch.setFont(font)
        self.dic_switch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 88, 97);")
        self.dic_switch.setObjectName("dic_switch")
        self.verticalLayout_2.addWidget(self.dic_switch)
        self.meal_switch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.meal_switch.setFont(font)
        self.meal_switch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 88, 97);")
        self.meal_switch.setObjectName("meal_switch")
        self.verticalLayout_2.addWidget(self.meal_switch)
        self.cat_swItch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cat_swItch.setFont(font)
        self.cat_swItch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 88, 97);")
        self.cat_swItch.setObjectName("cat_swItch")
        self.verticalLayout_2.addWidget(self.cat_swItch)
        self.dog_switch_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dog_switch_3.setFont(font)
        self.dog_switch_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 88, 97);")
        self.dog_switch_3.setObjectName("dog_switch_3")
        self.verticalLayout_2.addWidget(self.dog_switch_3)
        self.human_switch = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.human_switch.setFont(font)
        self.human_switch.setStyleSheet("background-color: rgb(84, 88, 97);")
        self.human_switch.setObjectName("human_switch")
        self.verticalLayout_2.addWidget(self.human_switch)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.send = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.send.setFont(font)
        self.send.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(84, 88, 97);")
        self.send.setObjectName("send")
        self.verticalLayout_4.addWidget(self.send)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dic_switch.setText(_translate("MainWindow", "Dic"))
        self.meal_switch.setText(_translate("MainWindow", "Meal"))
        self.cat_swItch.setText(_translate("MainWindow", "Cat"))
        self.dog_switch_3.setText(_translate("MainWindow", "Dog"))
        self.human_switch.setText(_translate("MainWindow", "Human"))
        self.send.setText(_translate("MainWindow", "send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
