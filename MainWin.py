# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FaceDetect(object):
    def setupUi(self, FaceDetect):
        FaceDetect.setObjectName("FaceDetect")
        FaceDetect.resize(690, 589)
        self.centralwidget = QtWidgets.QWidget(FaceDetect)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 510, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 691, 501))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 510, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 510, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        FaceDetect.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FaceDetect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 23))
        self.menubar.setObjectName("menubar")
        FaceDetect.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FaceDetect)
        self.statusbar.setObjectName("statusbar")
        FaceDetect.setStatusBar(self.statusbar)
        self.open = QtWidgets.QAction(FaceDetect)
        self.open.setObjectName("open")

        self.retranslateUi(FaceDetect)
        self.open.triggered.connect(FaceDetect.close)
        self.pushButton.clicked.connect(FaceDetect.openimage)
        self.pushButton_2.clicked.connect(FaceDetect.recognize)
        self.pushButton_3.clicked.connect(FaceDetect.HaarDetect)
        QtCore.QMetaObject.connectSlotsByName(FaceDetect)

    def retranslateUi(self, FaceDetect):
        _translate = QtCore.QCoreApplication.translate
        FaceDetect.setWindowTitle(_translate("FaceDetect", "FaceDetect"))
        self.pushButton.setText(_translate("FaceDetect", "打开图片"))
        self.pushButton_2.setText(_translate("FaceDetect", "YOLO人脸识别"))
        self.pushButton_3.setText(_translate("FaceDetect", "Haar人脸识别"))
        self.open.setText(_translate("FaceDetect", "打开"))

