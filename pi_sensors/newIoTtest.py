import max30102
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#from random import seed
#from random import randint
#from random import random
import logging
import time
import argparse
import json
#import max30102
import hrcalc
import time

#from testHR import *
#new_avg, new_avg2 = testHR.Max_read(avg, avg2)
#avg = testHR.avg
#avg2 = testHR.avg2

#avg, avg2 = Max_read(10)
#avg2 = Max_read(10)

#print (avg)

#m = max30102.MAX30102()
set_serve = False
host = "a39nu1xs62gahx-ats.iot.us-east-1.amazonaws.com"
certPath = "/home/pi/AppFolder/cert/"
clientId = "pizerow"
topic = "sensor"
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)

#print (hr)
def setup():
	# Init AWSIoTMQTTClient
	#myAWSIoTMQTTClient = None
	#myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
	myAWSIoTMQTTClient.configureEndpoint(host, 8883)
	myAWSIoTMQTTClient.configureCredentials("{}RootCA1.pem".format(certPath), "{}Rpi-private.pem.key".format(certPath), "{}Rpi-cert.pem.crt".format(certPath))

	# AWSIoTMQTTClient connection configuration
	myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
	myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
	myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
	myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
	myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

	set_serve = True
setup()
myAWSIoTMQTTClient.connect()
def push(avg, avg2, Tavg):
	#host = "a39nu1xs62gahx-ats.iot.us-east-1.amazonaws.com"
	#certPath = "/home/pi/AppFolder/cert/"
	#clientId = "pizerow"
	#topic = "sensor"
	#topic = "$aws/things/myRPi/shadow/update"
	#if (not set_serve):
		#setup()
	#myAWSIoTMQTTClient.connect()

#	messageJson = json.dumps({"HRvalue": hr, "HTvalid": hr_valid, "SpO2value":spo2,"SpO2valid":spo2_valid})
	id='1876'
	#temp='98'

	messageJson = json.dumps({"ID": id,"HRvalue": avg,"SpO2value":avg2,"Temperature":Tavg})
	myAWSIoTMQTTClient.publish(topic, messageJson, 1)
	print('Published topic %s: %s\n' % (topic, messageJson))
	#print("hello")
	time.sleep(3)
#myAWSIoTMQTTClient.disconnect()

for n in range(90):
	from testHR import *
	from mlxread import *
	avg, avg2 = Max_read(10)
	Tavg = temp_read(10)
	push(avg, avg2, Tavg)
#from testHR import *
#avg, avg2 = Max_read(10)
#push(avg, avg2, 98)
myAWSIoTMQTTClient.disconnect()

