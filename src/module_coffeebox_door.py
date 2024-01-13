import RPi.GPIO as GPIO
from time import sleep

PUL_COFFEE_DOOR = 10  # Stepper Drive Pul_Ases
DIR_COFFEE_DOOR = 9  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA_COFFEE_DOOR = 11  # Controller Enable Bit (High to Enable / LOW to Disable).

class CoffeeboxDoor:

    def __init__(self, m_duration_total=0, m_delay=0, m_cycles=0, m_current_pos=0):
        GPIO.setmode(GPIO.BCM)
        # GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only.
        #
        GPIO.setup(PUL_COFFEE_DOOR, GPIO.OUT)
        GPIO.setup(DIR_COFFEE_DOOR, GPIO.OUT)
        GPIO.setup(ENA_COFFEE_DOOR, GPIO.OUT)
        self.m_duration_total = 3000
        self.m_delay = 0.00005
        self.m_cycles = 1
        self.m_current_pos = 0
        print('[COFFEE BOX] Duration Total set to ' + str(self.m_duration_total))

        print('[COFFEE BOX] Speed set to ' + str(self.m_delay))
        print('[COFFEE BOX] number of Cycles to Run set to ' + str(self.m_cycles))

    def open(self):
        if(self.m_current_pos == self.m_duration_total):
            print("[COFFEE BOX] Already opened!")
            return False
        return self.move(self.m_duration_total-self.m_current_pos)


    def close(self):
        if(self.m_current_pos == 0):
            print("[COFFEE BOX] Already closed!")
            return False
        return self.move(-self.m_current_pos)

    def move(self, dist):
        self.__init__()
        GPIO.output(ENA_COFFEE_DOOR, GPIO.HIGH)
        print('ENA_A set to HIGH - Controller Enabled')
        print('dist : %d'%dist)

        sleep(.5) # pause due to a possible change direction
        # door랑 방향이 반대임.
        GPIO.output(DIR_COFFEE_DOOR, GPIO.HIGH)
        step = 1
        if(dist<0):
            GPIO.output(DIR_COFFEE_DOOR, GPIO.LOW)
            step = -1

        if(dist>self.m_duration_total):
            dist = self.m_duration_total

        cur_pos = self.m_current_pos
        for x in range(0, dist, step):
            GPIO.output(PUL_COFFEE_DOOR, GPIO.HIGH)
            sleep(self.m_delay)
            GPIO.output(PUL_COFFEE_DOOR, GPIO.LOW)
            sleep(self.m_delay)
            cur_pos = self.m_current_pos + x + step
        self.m_current_pos = cur_pos

        GPIO.output(ENA_COFFEE_DOOR, GPIO.LOW)
        print('ENA_A set to LOW - Controller Disabled')
        print('Current Pos : %d'%self.m_current_pos)
        sleep(.5) # pause for possible change direction
        return True

