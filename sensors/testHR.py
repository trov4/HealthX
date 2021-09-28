
import max30102
import hrcalc
import time
#from scipy import stats
import numpy as np

m = max30102.MAX30102()

dataHR=[]
time.sleep(5)   # Wait 5 seconds to place finger on the sensor.
trimmed_sum = 0
sum = 0
sum1 = 0
count = 0
array=0
count1 = 0
#n = len(hr)
for i in range(5):
#init

# len(dataHR)
#while len (dataHR) < 5:

    red, ir = m.read_sequential()

    dataHR[i*100:(i+1)*100] = red    # For raw data capturing. Not required!
    hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])  # Calculating heart rate and SpO2 values from raw data.
    if dataHR < 0: 
	continue
    dataHR.append(hr)

    dataHR.sort()
    dataHR = dataHR[1:-1]

#    def tmeanHR(hr, alpha):
#    a = arr.array('d', [hr])
#    for n in range(len(hr)):
	#if hr[n] == 
#	if a==0:
#		return sum(hr)/float(len(hr))
# function to calculate max-min
#    def max_min(hr, n):
 #   	hr.sort()
  #  	return min(hr[n - 2] - hr[0],
   #            hr[n - 1] - hr[1])
 
# Driver code

    
   # print(max_min(hr, n))

##########################################################
    #x = hr.get()
   # if hr < 0:
#	continue
 #   dataHR.append(hr)
#dataHR.sort()
#avg(dataHR[1:-1])
##########################################################
   # if hr > 0:
#	continue
 #   dataHR.append(hr)
#dataHR.sort()
#trimmed_list = dataHR[1:-1]
#trimmed_sum = trimmed_sum + trimmed_list
#trimmed_avg = trimmed_sum/3 
#trimmed_avg = sum(trimmed_list)/len(trimmed_list)
	#return float(trimmed_avg)
#	print "Average Heart Rate: ", trimmed_avg
		
    if dataHR > 0:
	count = count + hr
    	sum = sum + hr
    	avg = sum/3
#	stats.trim_mean(hr,0.1)
    if spo2 > 0:
	count1 = count1 + spo2
	sum1 = sum1 + spo2
	avg1 = sum1/5
#	stats.trim_mean(spo2,0.1)
    print "Heart Rate: ", hr, ", Blood Oxygen: ", spo2
#print trimmed_avg
print "Average Heart Rate: ", avg
#print "Average Blood Oxygen: ", avg1
