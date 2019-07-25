# -*- coding: utf-8 -*-
import sys
from MainWin import Ui_FaceDetect
import MainWin
from PyQt5 import  QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import numpy as np
import cv2
import os

class mywindow(QtWidgets.QMainWindow,Ui_FaceDetect):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.f1 = []
        jpg = QtGui.QPixmap("back.jpg").scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def openimage(self):
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
        file, filetype = QFileDialog.getOpenFileName(self, '选择图片', './img', 'Image files(*.jpg *.gif *.png)')
        jpg = QtGui.QPixmap(file).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.f1.append(file)
        self.statusbar.showMessage(file)
        print(self.f1[-1])
    def recognize(self):
        self.statusbar.showMessage("正在识别，请稍等...")
        weightsPath = "face_5000.weights"
        configPath = "face.cfg"
        labelsPath = "face.names"
        # 初始化一些参数
        LABELS = open(labelsPath).read().strip().split("\n")  # 物体类别
        COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")  # 颜色
        boxes = []
        confidences = []
        classIDs = []
        try:
            net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        except:
            self.statusbar.showMessage("请检查网络配置文件！")

        try:
            # 读入待检测的图像
            #image = cv2.imread(self.f1[-1])
            image = cv_imread(self.f1[-1])
        except:
            self.statusbar.showMessage("请检查图片是否载入！")
        else:

            (H, W) = image.shape[:2]
            # 得到 YOLO需要的输出层
            ln = net.getLayerNames()
            ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            # 从输入图像构造一个blob，然后通过加载的模型，给我们提供边界框和相关概率
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            layerOutputs = net.forward(ln)
            # 在每层输出上循环
            for output in layerOutputs:
                # 对每个检测进行循环
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    # 过滤掉那些置信度较小的检测结果
                    if confidence > 0.02:
                        # 框后接框的宽度和高度
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        # 边框的左上角
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        # 更新检测出来的框
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
            # 极大值抑制
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.3)
            if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    # 在原图上绘制边框和类别
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                    # text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                    # cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
            self.statusbar.showMessage("检测到"+str(len(idxs))+"张人脸")
            cv2.imshow("Yolo Detected!", image)
            cv2.waitKey(0)

    def HaarDetect(self):

        try:
            self.statusbar.showMessage("正在识别，请稍等...")
            # detect(filename)img
            face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
        except:
            self.statusbar.showMessage("找不到haarcascade_frontalface_default.xml文件")

        try:
            img = cv_imread(self.f1[-1])

        except:
            self.statusbar.showMessage("请打开图片!")
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            i = 0
            for (x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                i += 1
            self.statusbar.showMessage("检测到" + str(i) + "张人脸")
            cv2.imshow('OpenCV detected!', img)
            cv2.waitKey(0)


def cv_imread(file_path):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

if __name__=="__main__":
    #创建QApplication类的实例
    app = QtWidgets.QApplication(sys.argv)
    #创建一个窗口
    ui = mywindow()
    ui.show()
    #进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

