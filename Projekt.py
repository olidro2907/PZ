# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APIprzetwarzanie_obrazu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(772, 501)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 12000000))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(6, 6, 6, 80)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.View = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.View.sizePolicy().hasHeightForWidth())
        self.View.setSizePolicy(sizePolicy)
        self.View.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.View.setObjectName("View")
        self.gridLayout.addWidget(self.View, 0, 1, 1, 1)
        self.Tools = QtWidgets.QTabWidget(self.centralwidget)
        self.Tools.setObjectName("Tools")
        self.Overlap1 = QtWidgets.QWidget()
        self.Overlap1.setObjectName("Overlap1")
        self.Tools.addTab(self.Overlap1, "")
        self.OverLap2 = QtWidgets.QWidget()
        self.OverLap2.setObjectName("OverLap2")
        self.Tools.addTab(self.OverLap2, "")
        self.gridLayout.addWidget(self.Tools, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NameImage = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.NameImage.setFont(font)
        self.NameImage.setObjectName("NameImage")
        self.horizontalLayout.addWidget(self.NameImage)
        self.Load = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.Load.setFont(font)
        self.Load.setAutoFillBackground(True)
        self.Load.setObjectName("Load")
        self.horizontalLayout.addWidget(self.Load)
        self.Remove = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.Remove.setFont(font)
        self.Remove.setObjectName("Remove")
        self.horizontalLayout.addWidget(self.Remove)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.Tools.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Photo Processing"))
        self.Tools.setTabText(self.Tools.indexOf(self.Overlap1), _translate("MainWindow", "Tab 1"))
        self.Tools.setTabText(self.Tools.indexOf(self.OverLap2), _translate("MainWindow", "Tab 2"))
        self.Load.setText(_translate("MainWindow", "Załaduj"))
        self.Remove.setText(_translate("MainWindow", "Usuń"))


