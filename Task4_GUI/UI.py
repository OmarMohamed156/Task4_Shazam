# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from lib.slider import Slider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Wheighted_Average_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Wheighted_Average_GroupBox.setObjectName("Wheighted_Average_GroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Wheighted_Average_GroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.Wheighted_Average_GroupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 1, 1, 1)
        self.Mixing_Slider = Slider(self.Wheighted_Average_GroupBox)
        self.Mixing_Slider.setObjectName("Mixing_Slider")
        self.gridLayout_3.addWidget(self.Mixing_Slider, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.Wheighted_Average_GroupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 2, 1, 1)
        self.Mix_Button = QtWidgets.QPushButton(self.Wheighted_Average_GroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Mix_Button.setFont(font)
        self.Mix_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mix_Button.setObjectName("Mix_Button")
        self.gridLayout_3.addWidget(self.Mix_Button, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 2)
        self.gridLayout_4.addWidget(self.Wheighted_Average_GroupBox, 0, 1, 1, 1)
        self.Normal_Audio_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Normal_Audio_GroupBox.setObjectName("Normal_Audio_GroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Normal_Audio_GroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Listen_Button = QtWidgets.QPushButton(self.Normal_Audio_GroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Listen_Button.setFont(font)
        self.Listen_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Listen_Button.setObjectName("Listen_Button")
        self.gridLayout_2.addWidget(self.Listen_Button, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.Normal_Audio_GroupBox, 0, 0, 1, 1)
        self.Similarity_Check_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Similarity_Check_GroupBox.setObjectName("Similarity_Check_GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.Similarity_Check_GroupBox)
        self.gridLayout.setObjectName("gridLayout")

        self.tableWidget = QtWidgets.QTableWidget(10, 2)
        self.tableWidget.setHorizontalHeaderLabels(["song name","similarity index"])

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.Similarity_Check_GroupBox, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Wheighted_Average_GroupBox.setTitle(_translate("MainWindow", "Weighted Average "))
        self.label.setText(_translate("MainWindow", "0%"))
        self.label_2.setText(_translate("MainWindow", "100%"))
        self.Mix_Button.setText(_translate("MainWindow", "Mix"))
        self.Normal_Audio_GroupBox.setTitle(_translate("MainWindow", "Normal Audio"))
        self.Listen_Button.setText(_translate("MainWindow", "Listen"))
        self.Similarity_Check_GroupBox.setTitle(_translate("MainWindow", "Similarity Check Table"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())