# wearable.py
from testHR import Max_read
from mlxread import temp_read
# import HTTP api


main():
	HR_spo2 = testHR.Max_read(5)
	temp = mlxread.temp_read(5)
	HTTP.post(url, HR_spo2, temp)