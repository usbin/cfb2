# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(900, 625)
        # StackedWidget.setStyleSheet("background-image: url(:/rc/bg.gif);")
        self.page1_idle = QtWidgets.QWidget()
        self.page1_idle.setObjectName("page1_idle")
        self.page1_layout = QtWidgets.QWidget(self.page1_idle)
        self.page1_layout.setGeometry(QtCore.QRect(0, 0, 733, 501))
        self.page1_layout.setObjectName("page1_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page1_layout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.page1_layout)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        StackedWidget.addWidget(self.page1_idle)
        self.page2_nfc = QtWidgets.QWidget()
        self.page2_nfc.setObjectName("page2_nfc")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page2_nfc)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 733, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        StackedWidget.addWidget(self.page2_nfc)
        self.page3_push_coffee = QtWidgets.QWidget()
        self.page3_push_coffee.setObjectName("page3_push_coffee")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.page3_push_coffee)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 921, 501))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        StackedWidget.addWidget(self.page3_push_coffee)
        self.page4_door_closing = QtWidgets.QWidget()
        self.page4_door_closing.setObjectName("page4_door_closing")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.page4_door_closing)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 733, 501))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        StackedWidget.addWidget(self.page4_door_closing)
        self.page5_measuring = QtWidgets.QWidget()
        self.page5_measuring.setObjectName("page5_measuring")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.page5_measuring)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 733, 501))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem12)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        StackedWidget.addWidget(self.page5_measuring)
        self.page6_result = QtWidgets.QWidget()
        self.page6_result.setObjectName("page6_result")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.page6_result)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 733, 501))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem15 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem15)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tb_point = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        self.tb_point.setFont(font)
        self.tb_point.setObjectName("tb_point")
        self.verticalLayout_7.addWidget(self.tb_point)
        self.tb_weight_measure = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        self.tb_weight_measure.setFont(font)
        self.tb_weight_measure.setObjectName("tb_weight_measure")
        self.verticalLayout_7.addWidget(self.tb_weight_measure, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem19)
        self.tb_total_point = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        self.tb_total_point.setFont(font)
        self.tb_total_point.setObjectName("tb_total_point")
        self.verticalLayout_6.addWidget(self.tb_total_point, 0, QtCore.Qt.AlignHCenter)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem20)
        self.tb_total_point.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        StackedWidget.addWidget(self.page6_result)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label.setText(_translate("StackedWidget", "Touch to start!"))
        self.label_2.setText(_translate("StackedWidget", "Please tag NFC!"))
        self.label_3.setText(_translate("StackedWidget", "Please put coffee in entrance after the door opened."))
        self.label_4.setText(_translate("StackedWidget", "And click this \"Done\" button."))
        self.pushButton.setText(_translate("StackedWidget", "Done"))
        self.label_5.setText(_translate("StackedWidget", "3"))
        self.label_6.setText(_translate("StackedWidget", "The door is closing. Please be carefull!"))
        self.label_7.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><img src=\":/img/bg.gif\"/></p></body></html>"))
        self.label_8.setText(_translate("StackedWidget", "Measuring..."))
        self.label_9.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><img src=\":/img/bg.gif\"/></p></body></html>"))
        self.label_9.setText(_translate("StackedWidget", "Thank you!"))
        self.label_11.setText(_translate("StackedWidget", "Your points are added successfully."))
        self.tb_point.setText(_translate("StackedWidget", "120 Points added."))
        self.tb_weight_measure.setText(_translate("StackedWidget", "Weight: 1.2Kg / Measure: 60cm^3"))
        self.tb_total_point.setText(_translate("StackedWidget", "Your total points : 10,260P"))
import cfb_rc
