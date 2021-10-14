# wearable.py
from testHR import Max_read
from mlxread import temp_read
# import HTTP api
import newIottest as iot

while(True):
	hr, spo2 = testHR.Max_read(5)
	temp = mlxread.temp_read(5)
	iot.push(hr, spo2, temp)