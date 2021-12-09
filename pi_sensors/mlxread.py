from smbus2 import SMBus
from mlx90614 import MLX90614
import time
#while 1:
def temp_read(seconds):
    count = 0
    sum = 0
    start_time = time.time()
    collect = True
    #for n in range(10):
    bus = SMBus(1)
    #bus.close()
    sensor = MLX90614(bus, address=0x5a)
    while collect:
    
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        if elapsed_time < seconds:
            #bus = SMBus(1)
            #sensor = MLX90614(bus, address=0x5A)
	    temp = sensor.get_object_1()
    	    temp = ((temp*(9/5))+32)+31.5
	    print (temp)
    	    count = count + 1
    	    time.sleep(.5)
    	    temp = float(temp)
    	    sum = sum + temp
        #print "Ambient Temperature :", sensor.get_ambient()
            #time.sleep(1)
        else:
            collect = False
            break
    #temp = sensor.get_object_1()
    #temp = ((temp*(9/5))+32)+31.5
    #count = count + 1
    #time.sleep(.5)
    #temp = float(temp)
    #sum = sum + temp
    Tavg = (sum/count)+5
    print "Wrist Temperature :", temp
    print "Final Temperature: ",Tavg
        #temp = sensor.get_object_1()
        #temp = (temp*(9/5))+32
    bus.close()
    time.sleep(1)
    return Tavg

temp_read(10)
