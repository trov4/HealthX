from smbus2 import SMBus
from mlx90614 import MLX90614
import time
#while 1:
count = 0
sum = 0
for n in range(10):
        bus = SMBus(1)
        sensor = MLX90614(bus, address=0x5A)
        #print "Ambient Temperature :", sensor.get_ambient()
	time.sleep(1)
        temp = sensor.get_object_1()
        temp = ((temp*(9/5))+32)+31.5
        count = count + 1
        time.sleep(.5)
        temp = float(temp)
        sum = sum + temp
        avg = (sum/count)+5
        print "Wrist Temperature :", temp
print "Final Temperature: ",avg
        #temp = sensor.get_object_1()
        #temp = (temp*(9/5))+32
bus.close()
time.sleep(1)
