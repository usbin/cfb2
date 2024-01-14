# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1000, 625)
        StackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page1_idle = QtWidgets.QWidget()
        self.page1_idle.setObjectName("page1_idle")
        self.page1_layout = QtWidgets.QWidget(self.page1_idle)
        self.page1_layout.setGeometry(QtCore.QRect(0, 0, 1000, 625))
        self.page1_layout.setStyleSheet("")
        self.page1_layout.setObjectName("page1_layout")
        self.horizontalWidget = QtWidgets.QWidget(self.page1_layout)
        self.horizontalWidget.setGeometry(QtCore.QRect(160, 310, 664, 34))
        self.horizontalWidget.setStyleSheet("background-color: transparent")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_10 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Light")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.frame_3 = QtWidgets.QFrame(self.page1_layout)
        self.frame_3.setGeometry(QtCore.QRect(-210, 360, 671, 391))
        self.frame_3.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.page1_layout)
        self.frame_4.setGeometry(QtCore.QRect(270, 80, 731, 461))
        self.frame_4.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.horizontalWidget.raise_()
        StackedWidget.addWidget(self.page1_idle)
        self.page2_nfc = QtWidgets.QWidget()
        self.page2_nfc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page2_nfc.setObjectName("page2_nfc")
        self.frame_5 = QtWidgets.QFrame(self.page2_nfc)
        self.frame_5.setGeometry(QtCore.QRect(0, 280, 671, 391))
        self.frame_5.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.page2_nfc)
        self.frame_6.setGeometry(QtCore.QRect(480, 0, 731, 461))
        self.frame_6.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page2_nfc)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 300, 512, 34))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Light")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Light")
        font.setPointSize(22)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.frame_6.raise_()
        self.frame_5.raise_()
        StackedWidget.addWidget(self.page2_nfc)
        self.page3_push_coffee = QtWidgets.QWidget()
        self.page3_push_coffee.setObjectName("page3_push_coffee")
        self.frame_7 = QtWidgets.QFrame(self.page3_push_coffee)
        self.frame_7.setGeometry(QtCore.QRect(-200, 240, 671, 391))
        self.frame_7.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_8 = QtWidgets.QFrame(self.page3_push_coffee)
        self.frame_8.setGeometry(QtCore.QRect(300, -40, 731, 461))
        self.frame_8.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.widget = QtWidgets.QWidget(self.page3_push_coffee)
        self.widget.setGeometry(QtCore.QRect(350, 370, 301, 101))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-08.png);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.page3_push_coffee)
        self.label_3.setGeometry(QtCore.QRect(317, 170, 408, 32))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: transparent")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page3_push_coffee)
        self.label_4.setGeometry(QtCore.QRect(300, 230, 442, 32))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: transparent")
        self.label_4.setObjectName("label_4")
        self.frame_7.raise_()
        self.frame_8.raise_()
        StackedWidget.addWidget(self.page3_push_coffee)
        self.page4_door_closing = QtWidgets.QWidget()
        self.page4_door_closing.setObjectName("page4_door_closing")
        self.frame_10 = QtWidgets.QFrame(self.page4_door_closing)
        self.frame_10.setGeometry(QtCore.QRect(130, -10, 731, 461))
        self.frame_10.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-01.png);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_6 = QtWidgets.QLabel(self.page4_door_closing)
        self.label_6.setGeometry(QtCore.QRect(150, 443, 699, 35))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.page4_door_closing)
        self.label_5.setGeometry(QtCore.QRect(463, 147, 74, 145))
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(99)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent\n"
"")
        self.label_5.setObjectName("label_5")
        self.frame_10.raise_()
        StackedWidget.addWidget(self.page4_door_closing)
        self.page5_measuring = QtWidgets.QWidget()
        self.page5_measuring.setObjectName("page5_measuring")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.page5_measuring)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 1000, 625))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-02.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)
        self.verticalLayout_5.setStretch(3, 2)
        self.verticalLayout_5.setStretch(4, 1)
        StackedWidget.addWidget(self.page5_measuring)
        self.page6_result = QtWidgets.QWidget()
        self.page6_result.setObjectName("page6_result")
        self.frame = QtWidgets.QFrame(self.page6_result)
        self.frame.setGeometry(QtCore.QRect(160, 180, 681, 391))
        self.frame.setStyleSheet("image: url(:/rc/커피박 디스플레이-요소분리-12.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.page6_result)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 1001, 621))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: transparent;\n"
"color: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 981, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(36)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        spacerItem8 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.lb_add_point = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.lb_add_point.setFont(font)
        self.lb_add_point.setStyleSheet("color: rgb(0, 0, 0);")
        self.lb_add_point.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_add_point.setObjectName("lb_add_point")
        self.verticalLayout_6.addWidget(self.lb_add_point)
        self.lb_weight = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.lb_weight.setFont(font)
        self.lb_weight.setStyleSheet("color: rgb(0, 0, 0);")
        self.lb_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_weight.setObjectName("lb_weight")
        self.verticalLayout_6.addWidget(self.lb_weight)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.lb_total_point = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("KoPub돋움체 Bold")
        font.setPointSize(22)
        self.lb_total_point.setFont(font)
        self.lb_total_point.setStyleSheet("color: rgb(0, 0, 0);")
        self.lb_total_point.setObjectName("lb_total_point")
        self.horizontalLayout_2.addWidget(self.lb_total_point)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.verticalLayout_6.setStretch(0, 4)
        self.verticalLayout_6.setStretch(1, 2)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 4)
        self.verticalLayout_6.setStretch(4, 1)
        self.verticalLayout_6.setStretch(5, 1)
        self.verticalLayout_6.setStretch(7, 4)
        self.verticalLayout_6.setStretch(8, 1)
        StackedWidget.addWidget(self.page6_result)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "커피박 회수"))
        self.label_10.setText(_translate("StackedWidget", "를 진행하시려면"))
        self.label_12.setText(_translate("StackedWidget", "화면을 터치해주세요."))
        self.label_2.setText(_translate("StackedWidget", "우측에 위치한"))
        self.label_13.setText(_translate("StackedWidget", "NFC를 태그"))
        self.label_14.setText(_translate("StackedWidget", "해주세요."))
        self.pushButton.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("StackedWidget", "문이 열리면 커피박을 투입해주세요."))
        self.label_4.setText(_translate("StackedWidget", "투입 후 [투입 완료] 버튼을 눌러주세요."))
        self.label_6.setText(_translate("StackedWidget", "잠시 후 문이 닫힙니다. 안전에 주의해 주시기 바랍니다."))
        self.label_5.setText(_translate("StackedWidget", "3"))
        self.label_7.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><img src=\":/img/bg.gif\"/></p></body></html>"))
        self.label_8.setText(_translate("StackedWidget", "투입하신 커피박을 측정 중입니다."))
        self.label_9.setText(_translate("StackedWidget", "감사합니다!"))
        self.label_11.setText(_translate("StackedWidget", "회수가 정상적으로 처리되었습니다."))
        self.lb_add_point.setText(_translate("StackedWidget", "120 포인트의 탄소포인트가 적립되었습니다."))
        self.lb_weight.setText(_translate("StackedWidget", "무게 : 1.2kg 부피 : 60"))
        self.label_17.setText(_translate("StackedWidget", "철저한 고양이님"))
        self.lb_total_point.setText(_translate("StackedWidget", "총 적립 포인트 : 10,260"))
import cfb_rc
