# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 595)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.le_folder_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_folder_name.setEnabled(True)
        self.le_folder_name.setGeometry(QtCore.QRect(20, 30, 961, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.le_folder_name.setFont(font)
        self.le_folder_name.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.le_folder_name.setText("")
        self.le_folder_name.setReadOnly(True)
        self.le_folder_name.setObjectName("le_folder_name")
        self.btn_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyze.setEnabled(False)
        self.btn_analyze.setGeometry(QtCore.QRect(170, 60, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setObjectName("btn_analyze")
        self.btn_select_folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select_folder.setGeometry(QtCore.QRect(20, 60, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_select_folder.setFont(font)
        self.btn_select_folder.setObjectName("btn_select_folder")
        self.tb_information = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_information.setGeometry(QtCore.QRect(20, 170, 961, 401))
        self.tb_information.setObjectName("tb_information")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(880, 60, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_exit.setFont(font)
        self.btn_exit.setFlat(False)
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ???????????? ??????????????????????????"))
        self.le_folder_name.setPlaceholderText(_translate("MainWindow", "???????????????? ?????????? ?????? ??????????????"))
        self.btn_analyze.setText(_translate("MainWindow", "????????????"))
        self.btn_select_folder.setText(_translate("MainWindow", "??????????????\n"
"??????????"))
        self.btn_exit.setText(_translate("MainWindow", "??????????"))
