import RPi.GPIO as GPIO # type: ignore
import time

# SPICLK = 11
# SPIMISO = 9
# SPIMOSI = 10 
# SPICS = 8
MQ2_APIN = 0
MQ3_APIN = 1
MQ5_APIN = 2
MQ7_APIN = 3
MQ8_APIN = 4

#port init
  
class MCP3008:
    
    def __init__(self, bus = 0, device = 0, SPICLK = 11, SPIMISO = 9, SPIMOSI = 10, SPICS = 8):
        GPIO.setwarnings(False) 
        GPIO.cleanup()
        GPIO.setmode (GPIO.BCM)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
        self.clockpin = SPICLK
        self.mosipin = SPIMOSI
        self.misopin = SPIMISO
        self.cspin = SPICS

    def read(self, adcnum):
        if ((adcnum > 7) or (adcnum < 0)):
            return -1
        GPIO.output(self.cspin, True)
        GPIO.output(self.clockpin, False) # start clock low
        GPIO.output(self.cspin, False)
        commandout = adcnum
    # bring CS Low
        commandout |= 0x18 # start bit + single-ended bit 
        commandout <<= 3 # we only need to send 5 bits here
        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(self.mosipin, True)
            else:
                GPIO.output(self.mosipin, False)
            commandout <<= 1
            GPIO.output(self.clockpin, True)
            GPIO.output(self.clockpin, False)
        adcout = 0
        for i in range(12):
            GPIO.output(self.clockpin, True) 
            GPIO.output(self.clockpin, False) 
            adcout <<= 1
            if (GPIO.input(self.misopin)):
                    adcout |= 0x1
        GPIO.output(self.cspin, True)
        adcout >>= 1
# first bit is 'null' so drop it
        return adcout