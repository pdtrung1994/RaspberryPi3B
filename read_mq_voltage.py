# from mq2 import *
from send_data_gg import *
import sys, time
from MCP3008 import MCP3008

file_name = "data_" + str(time.strftime("%Y_%m_%d_%H_%M_%S"))  + ".csv"; 
file_path = "/home/pi/FTP/data/air/" + file_name;

def air_quality_convert(gas_level):
    return ((gas_level/ 1024.)*5)

def file_creation():
    name = "data_" + str(time.strftime("%Y_%m_%d_%H_%M_%S")) + ".csv"
    path = "/home/pi/FTP/data/air/" + name
    with open(path, "a") as log:
        log.write("{0},{1},{2},{3},{4},{5},{6}\n".format("Date","MQ2","MQ3","MQ5","MQ7","MQ8","MQ135"))
    return path, name

if __name__ == "__main__":
    #define time per record
    TIME_RECORD_PERIOD = 100
    ##
    count = 0
    file_path, file_name = file_creation()
    try:
        # print("Press CTRL+C to abort.")
        adc = MCP3008()
        # mq2 = MQ2();
        while True:
            with open(file_path, "a") as log:
                # perc = mq2.MQPercentage()
                MQ2_level = air_quality_convert(adc.read(0));
                MQ3_level = air_quality_convert(adc.read(1));
                MQ5_level = air_quality_convert(adc.read(2));
                MQ7_level = air_quality_convert(adc.read(3));
                MQ8_level = air_quality_convert(adc.read(4));
                MQ135_level = air_quality_convert(adc.read(5));
                log.write("%s,%0.2g,%0.2g,%0.2g,%0.2g,%0.2g,%0.2g \n" % (str(time.strftime("%Y-%m-%d %H:%M:%S")),MQ2_level, MQ3_level, MQ5_level, MQ7_level, MQ8_level, MQ135_level))
                count +=1           
                time.sleep(1)
            if count >= TIME_RECORD_PERIOD:
                upload(file_path, file_name)
                file_path, file_name = file_creation()
                count = 0
    except Exception as X:
        
        print("\nX\n")
        file_name = "errorlog" + ".txt"
        file_path = "/home/pi/FTP/data/air/" + file_name
        with open(file_path, "a") as log:
            log.write("Something happen! \n")
            log.write(X)
        # upload(file_path, file_name)
