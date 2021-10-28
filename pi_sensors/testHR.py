\
import max30102
import hrcalc
import time
#from scipy import stats
import numpy as np

m = max30102.MAX30102()

#dataHR=[]
#hr_list = []
#spo2_list = []
#time.sleep(5)   # Wait 5 seconds to place finger on the sensor.
#trimmed_sum = 0
#sum = 0
#sum1 = 0
#count = 0
#array=0
#count1 = 0
#n = len(hr)
#for i in range(5):
#init

# len(dataHR)
#while len(hr_list) < 10:

    #red, ir = m.read_sequential()

    #dataHR[i*100:(i+1)*100] = red    # For raw data capturing. Not required!
    #hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])  # Calculating heart rate and SpO2 values from raw data.
    # hr checks, also check if over maximum
    #if hr < 0: 
	#continue
    #hr_list.append(hr)

    # spo2 checks, min, max, maximum samples
    #if spo2 < 0: 
	#continue
 #   spo2_list.append(spo2)
#hr_list.sort()
#hr_list = hr_list[1:-1]
#spo2_list.sort()
#spo2_list = spo2_list[1:-1]

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
#print "hr list: ", hr_list
#print "spo2 list: ",spo2_list
#summer = 0
#for i in hr_list:
 #   summer = summer + i
#l = len(hr_list)

#avg = summer/l

#summer2 = 0
#for i in spo2_list:
 #   summer2 = summer2 + i
#l2 = len(spo2_list)

#avg2 = summer2/l2
#    if dataHR > 0:
#	count = count + hr
 #   	sum = sum + hr
  #  	avg = sum/3
#	stats.trim_mean(hr,0.1)
   # if spo2 > 0:
#	count1 = count1 + spo2
#	sum1 = sum1 + spo2
#	avg1 = sum1/5
#	stats.trim_mean(spo2,0.1)
#print "Heart Rate: ", hr, ", Blood Oxygen: ", spo2
#print trimmed_avg
#print "Average Heart Rate: ", avg
#print "Average Blood Oxygen: ", avg2


##########################################################################
import numpy as np

for n in range(2): 
	def Max_read(seconds):
    		#dataHR=[]
    		print("Starting Max_read")
    		hr_list = []
    		spo2_list = []
    		time.sleep(5)   # Wait 5 seconds to place finger on the sensor.
    		start_time = time.time()
    		collect = True
    
    		while collect:
        		#print("In collect")
    
        		current_time = time.time()
        		elapsed_time = current_time - start_time
	#print (elapsed_time)
        #print (start_time)
	#print (current_time)
	#print (hr_list)
	#print (spo2_list)
        		if elapsed_time < seconds:
	#    print ("jiwoo")
            			red, ir = m.read_sequential()
        #dataHR[i*100:(i+1)*100] = red    # For raw data capturing. Not required!
            			hr, hr_valid, spo2, spo2_valid = hrcalc.calc_hr_and_spo2(ir[:100], red[:100])  # Calculating heart rate and SpO2 values from raw data.
        # hr checks, also check if over maxium
            # to replkace
            			if hr > 0:
#		print ("Im  kwame ")
                			hr_list.append(hr)
            			if spo2 > 0:
                			spo2_list.append(spo2)
                
            #if hr < 0: 
             #   continue
            #hr_list.append(hr)

        # spo2 checks, min, max, maximum samples
            #if spo2 < 0: 
             #   continue
            #spo2_list.append(spo2)
        		else:
            			collect = False
            			break
    		avg = 0
    		avg2 = 0
    		if (len(hr_list) > 0):
        		hr_list.sort()
        		n = len(hr_list)
        		k = int(round(n))
#	print ("im david")
        		hr = hr_list
        #per=int(input('Enter your percentage: '))
        #hr = hr[(per/2)*len(hr):-(per/2)*len(hr)]
        		summer = 0
        		for i in hr:
            			summer = summer + i
            			l = len(hr)

            			avg = summer/l
    		if (len(spo2_list) > 0):
        		spo2_list.sort()
        		n2 = len(spo2_list)
        		k2 = int(round(n2))
        #spo2 = spo2[(per/2)*len(spo2):-(per/2)*len(spo2)]
        		spo2 = spo2_list
        		summer2 = 0
        		for x in spo2:
            			summer2 = summer2 + x
            			l2 = len(spo2)

            			avg2 = summer2/l2
    
    #		print("hr list: ", hr)
    #		print("spo2 list: ",spo2)
    #summer = 0
    #for i in hr:
     #   summer = summer + i
    #l = len(hr)

    #avg = summer/l

    #summer2 = 0
    #for x in spo2:
     #   summer2 = summer2 + x
    #l2 = len(spo2)

    #avg2 = summer2/l2

    #		print("Heart Rate: ", hr)
    #		print("Blood Oxygen: ", spo2)
    		print('Average Heart Rate: ', avg)
    		print("Average Blood Oxygen: ", avg2)
    		return avg, avg2
    # requests.post(url, dic)
    
#	Max_read(10)
