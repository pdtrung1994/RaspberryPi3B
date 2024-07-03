from mq2 import *
import sys, time
from MCP3008 import MCP3008

# print("Waiting 5 seconds...")
# time.sleep(5)
# mq2 = MQ2();
# while True:
#     MQ2_level = readadc(MQ2_APIN, SPICLK, SPIMOSI, SPIMISO, SPICS) 
#     MQ2_air_quality = air_quality_convert(MQ2_level);
#     MQ3_level = readadc(MQ3_APIN, SPICLK, SPIMOSI, SPIMISO, SPICS) 
#     MQ5_level = readadc(MQ5_APIN, SPICLK, SPIMOSI, SPIMISO, SPICS) 
#     MQ7_level = readadc(MQ7_APIN, SPICLK, SPIMOSI, SPIMISO, SPICS) 
#     MQ8_level = readadc(MQ8_APIN, SPICLK, SPIMOSI, SPIMISO, SPICS) 
#     if MQ2_air_quality > 1.5:
#         print("! GAS LEAKAGE !")            
#         # print(MQ2_air_quality);
#     print("Current MQ2 value = "+str("%.2f" %(MQ2_air_quality))+" V") 
#     print("Current MQ3 value = "+str("%.2f" %(air_quality_convert(MQ3_level)))+" V") 
#     print("Current MQ5 value = "+str("%.2f" %(air_quality_convert(MQ5_level)))+" V") 
#     print("Current MQ7 value = "+str("%.2f" %(air_quality_convert(MQ7_level)))+" V") 
#     print("Current MQ8 value = "+str("%.2f" %(air_quality_convert(MQ8_level)))+" V") 
#     print("-----------------------------");
#     time.sleep(5)

def air_quality_convert(gas_level):
     return ((gas_level/ 1024.)*5)

try:
    print("Press CTRL+C to abort.")
    adc = MCP3008()
    mq2 = MQ2();
    while True:
        perc = mq2.MQPercentage()
        MQ2_level = air_quality_convert(adc.read(0));
        MQ3_level = air_quality_convert(adc.read(1));
        MQ5_level = air_quality_convert(adc.read(2));
        MQ7_level = air_quality_convert(adc.read(3));
        MQ8_level = air_quality_convert(adc.read(4));
        MQ135_level = air_quality_convert(adc.read(5));

        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %0.2g ppm, CO: %0.2g ppm, Smoke: %0.2g ppm ||||||||||||||| " % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
        # sys.stdout.write("\r")
        sys.stdout.write("MQ2: %0.2g V, MQ3: %0.2g V, MQ5: %0.2g V, MQ7: %0.2g V, MQ8: %0.2g V, MQ135: %0.2g V" % (MQ2_level, MQ3_level, MQ5_level, MQ7_level, MQ8_level, MQ135_level))
        sys.stdout.write("\r")
        
        time.sleep(0.1)
        sys.stdout.flush()        
        sys.stdout.write("-------------------------------")
except Exception as X:
    print(X)
    print("\nAbort by user")