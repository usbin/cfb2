import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import binascii
import json
from pn532pi import Pn532
from pn532pi import Pn532I2c
from pn532pi import Pn532Spi
from module_coffeebox_door import CoffeeboxDoor
from module_door import Door
from module_weight import MeasureModule
import RPi.GPIO as GPIO
import math

from main import Ui_StackedWidget
import asyncio


__DEBUG__ = False




# PN532_SPI = Pn532Spi(Pn532Spi.SS0_GPIO8)
# nfc = Pn532(PN532_SPI)
# PN532_HSU = Pn532Hsu(Pn532Hsu.RPI_MINI_UART)
# nfc = Pn532(PN532_HSU)

if __DEBUG__:
    print("[DEBUG MODE]")

PN532_I2C = Pn532I2c(1)
nfc = Pn532(PN532_I2C)
g_user_id = ""

COFFEEBOX_DOOR = CoffeeboxDoor()
DOOR = Door()
MEASURE_MODULE = MeasureModule()

[IDX_IDLE, IDX_PLEASE_TOUCH_NFC, IDX_OPEN_DOOR, IDX_DOOR_CLOSE_WARNING, IDX_MEASURE_WEIGHT, IDX_RESULT] = [0,1,2,3,4,5]

def 안쓰는코드():
# def open_door():
#     if DOOR.open():
#         print("┌────────────────────────────────────┐")
#         print("│            DOOR OPENED!            │")
#         print("└────────────────────────────────────┘")
#     return True
# def close_door():
#     if DOOR.close():
#         print("┌────────────────────────────────────┐")
#         print("│            DOOR CLOSED!            │")
#         print("└────────────────────────────────────┘")
#     return True
# def determine_weight():

#     print("┌────────────────────────────────────┐")
#     print("│       Determining weight...        │")
#     print("└────────────────────────────────────┘")
#     weight = MEASURE_MODULE.measure()

#     print('''┌────────────────────────────────────┐''')
#     print('''│          Weight : %4dg            │'''%weight)
#     print('''└────────────────────────────────────┘''')
#     return True, weight

# def something_wrong():
#   print("!Something wrong...!")
#   reset()

# def done(point):
#     global g_user_id
#     print('''┌────────────────────────────────────┐''')
#     print('''│         Your id: %-10s        │'''%g_user_id)
#     print('''│         Your point: +%-5d         │'''%point)
#     print('''└────────────────────────────────────┘''')
#     reset()

# def reset():
#    global g_user_id
#    close_door()
#    g_user_id = ""
#    print("!All reseted!")


# def loop():
#     global g_user_id
#     # set shield to inListPassiveTarget
#     success = nfc.inListPassiveTarget()

#     if (success):
#         print("Found something!")
#         selectApdu = bytearray([0x00,                                     # CLA
#                                 0xA4,                                     # INS
#                                 0x04,                                     # P1
#                                 0x00,                                     # P2
#                                 0x05,                                     # Length of AID
#                                 0xF1, 0x23, 0x45, 0x67, 0x89,            # AID defined on Android App
#                                 0x00 # Le
#                                 ])

#         success, response = nfc.inDataExchange(selectApdu)
#         if (success):
#             # 연결 후 데이터 송수신 루프
#             # 1. userid 요청
#             json_object = {
#                 "method" : "GET",
#                 "param" : "user_id"
#             }
#             json_str = json.dumps(json_object)
#             command_get_userid = bytes(json_str, "utf-8")# bytearray(b)
#             success, resp = nfc.inDataExchange(command_get_userid)
#             str = resp.decode('utf-8')
#             print("json: %s"%str)
#             try:
#                 userid_dict: dict = json.loads(str)
#                 g_user_id = userid_dict.get("param")
#                 print("user id: %s"%g_user_id)
#                 success = len(g_user_id) == 8
#             except:
#                 pass

#             if(success):
#                 # 2. 투입구 개방
#                 if (open_door()):
#                     # 버튼 입력 대기
#                     input()
#                     # 3. 투입구 폐쇄
#                     if (close_door()):
#                         # 4. 무게 측정
#                         success, weight = determine_weight()
#                         point = weight*2
#                         if(success):
#                             # 5. 아이디, 무게 정보 휴대폰으로 전송
#                             inner_json_object = {
#                                 "user_id" : g_user_id,
#                                 "point" : point
#                             }
#                             inner_json_str = json.dumps(inner_json_object)
#                             json_object = {
#                                 "method" : "PUT",
#                                 "param" : inner_json_str
#                             }

#                             result_str = json.dumps(json_object)
#                             print(result_str)
#                             command_put_result = bytes(result_str, "utf-8")

#                             success, str = nfc.inDataExchange(command_put_result)
#                             if(success):
#                                 # 6. 처음으로
#                                 done(point)
#                                 return
#                                 # if (success):
#                                 #   print("responseLength: {:d}".format(len(back)))
#                                 #   print(binascii.hexlify(back))
#                                 # else:
#                                 #   print("Broken connection?")

#         something_wrong() # 리셋 후 처음으로
#         return
#     else:
#         print("Waiting...")

#     time.sleep(1)
    pass



class Evt(QObject):
    nfcDetected = pyqtSignal()
    weightMeasured = pyqtSignal()
    doorOpened = pyqtSignal()
    doorClosed = pyqtSignal()

class Cfb(QWidget):
    ui:Ui_StackedWidget = None
    stackedWidget:QtWidgets.QStackedWidget = None
    evt = None
    m_user_id = None
    m_weight = None
    m_added_point = None
    def __init__(self):
        super().__init__()
        self.evt = Evt()
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self.stackedWidget)
        self.stackedWidget.show()
        self.center()
        if not __DEBUG__:
            self.setupHardware()

        self.ui.page1_layout.mousePressEvent = self.onTouch
        self.evt.nfcDetected.connect(self.open_door)
        self.evt.doorOpened.connect(self.ui_door_opened)
        self.ui.pushButton.clicked.connect(self.ui_on_done_clicked)
        self.evt.doorClosed.connect(self.determine_weight)
        self.evt.weightMeasured.connect(self.save_coffee)
        self.ui.page6_result.mousePressEvent = self.reset


    def setupHardware(self):
        print("-------Peer to Peer HCE--------")
        #------------------------------------------------#
        #               NFC 초기화                        #
        #------------------------------------------------#
        nfc.begin()
        time.sleep(1)

        versiondata = nfc.getFirmwareVersion()
        time.sleep(1)
        if not versiondata:
            print("Didn't find PN53x board")
            raise RuntimeError("Didn't find PN53x board")  # halt

        # Got ok data, print it out!
        print("Found chip PN5 {:#x} Firmware ver. {:d}.{:d}".format((versiondata >> 24) & 0xFF, (versiondata >> 16) & 0xFF,
                                                                    (versiondata >> 8) & 0xFF))

        # configure board to read RFID tags
        nfc.SAMConfig()

        #------------------------------------------------#
        #               로드셀 초기화                     #
        #------------------------------------------------#


    # STEP 1: 화면 터치 대기
    def onTouch(self, pos):
        self.stackedWidget.setCurrentIndex(IDX_PLEASE_TOUCH_NFC)
        #self.onNfcDetecting()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.onNfcDetecting())


    # STEP 2: NFC 대기 (30초)
    async def onNfcDetecting(self):

        # 테스트환경에선 nfc detecting 스킵
        if __DEBUG__:
            self.evt.nfcDetected.emit()
            self.stackedWidget.setCurrentIndex(IDX_OPEN_DOOR)
            return

        totalMs = 0
        while(totalMs < 10000):
            QApplication.processEvents()
            success = nfc.inListPassiveTarget()
            # gui 프리징 방지
            QApplication.processEvents()
            time.sleep(0.5)
            if (success):
                print("Found something!")
                selectApdu = bytearray([0x00,                                     # CLA
                                        0xA4,                                     # INS
                                        0x04,                                     # P1
                                        0x00,                                     # P2
                                        0x05,                                     # Length of AID
                                        0xF1, 0x23, 0x45, 0x67, 0x89,            # AID defined on Android App
                                        0x00 # Le
                                        ])

                success, response = nfc.inDataExchange(selectApdu)
                # nfc 발견하면 문 오픈
                if (success):
                    self.evt.nfcDetected.emit()
                    self.stackedWidget.setCurrentIndex(IDX_OPEN_DOOR)
                    QApplication.processEvents()
                    return
            else:
                print("Waiting...")


            await asyncio.sleep(1)
            totalMs += 1000
        if(totalMs >= 10000):
            #처음으로
            self.something_wrong()
            #self.evt.nfcDetected.emit()
            #self.stackedWidget.setCurrentIndex(IDX_DOOR_OPEN)

    def onPutCoffeeWaiting(self):
        QApplication.processEvents()
        self.close_door()
        QApplication.processEvents()
        self.determine_weight()
        QApplication.processEvents()
        self.save_coffee()


    def open_door(self):

        MEASURE_MODULE.zero()
        if __DEBUG__ or DOOR.open():
            print("┌────────────────────────────────────┐")
            print("│            DOOR OPENED!            │")
            print("└────────────────────────────────────┘")
            QApplication.processEvents()
            self.evt.doorOpened.emit()
            QApplication.processEvents()


        return True
    def ui_door_opened(self):
        QApplication.processEvents()



    # done 버튼 클릭됨 -> 3초 카운트다운
    def ui_on_done_clicked(self):
        self.stackedWidget.setCurrentIndex(IDX_DOOR_CLOSE_WARNING)
        self.ui.label_5.setText("3")
        QApplication.processEvents()
        time.sleep(1)
        self.ui.label_5.setText("2")
        QApplication.processEvents()
        time.sleep(1)
        self.ui.label_5.setText("1")
        QApplication.processEvents()
        time.sleep(1)
        self.ui.label_5.setText("0")
        QApplication.processEvents()
        self.close_door()

    # 문짝 닫기
    def close_door(self):
        if __DEBUG__ or DOOR.close():
            print("┌────────────────────────────────────┐")
            print("│            DOOR CLOSED!            │")
            print("└────────────────────────────────────┘")
            QApplication.processEvents()
            self.evt.doorClosed.emit()
            QApplication.processEvents()
            return True
    def determine_weight(self):

        print("┌────────────────────────────────────┐")
        print("│       Determining weight...        │")
        print("└────────────────────────────────────┘")


        QApplication.processEvents()
        self.stackedWidget.setCurrentIndex(IDX_MEASURE_WEIGHT)
        QApplication.processEvents()
        if __DEBUG__ :
            self.m_weight = 99
        else :
            self.m_weight = MEASURE_MODULE.measure()
            print('''┌────────────────────────────────────┐''')
            print('''│          Weight : %4dg            │'''%self.m_weight)
            print('''└────────────────────────────────────┘''')

            self.evt.weightMeasured.emit()


        return True, self.m_weight
    def save_coffee(self):
        if __DEBUG__ or COFFEEBOX_DOOR.open():
            print("┌────────────────────────────────────┐")
            print("│             BOX OPENED!            │")
            print("└────────────────────────────────────┘")

            time.sleep(2)
            if __DEBUG__ or COFFEEBOX_DOOR.close():
                print("┌────────────────────────────────────┐")
                print("│            BOX CLOSED!            │")
                print("└────────────────────────────────────┘")
                self.stackedWidget.setCurrentIndex(IDX_RESULT)
                self.done( self.m_weight)

        return True


    def something_wrong(self):
        print("!Something wrong...!")
        self.reset()

    def done(self, weight):
        self.m_added_point = weight*0.2
        print('''┌────────────────────────────────────┐''')
        print('''│         Your id: %-10s        │'''%self.m_user_id)
        print('''│         Your point: +%-5d         │'''%self.m_added_point)
        print('''└────────────────────────────────────┘''')
        self.ui.tb_weight.setText("%.1fg"%self.m_weight)
        self.ui.tb_add_point.setText("%d"%self.m_added_point)
        self.ui.tb_total_point.setText("%sP"%format(math.floor( self.m_added_point+10260), ','))
        QApplication.processEvents()

    def reset(self, pos=None):
        self.m_user_id = ""
        self.stackedWidget.setCurrentIndex(IDX_IDLE)
        QApplication.processEvents()
        GPIO.cleanup()
        print("!All reseted!")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Cfb()
    GPIO.cleanup()
    sys.exit(app.exec_())