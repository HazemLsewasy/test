# importing libraries
import paho.mqtt.client as paho
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os
import socket
import ssl
import random
import string
import json
from time import sleep
from random import uniform
 
connflag = True
 
def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
     
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
def getEthName():
  # Get name of the Ethernet interface
  try:
    for root,dirs,files in os.walk('/sys/class/net'):
      for dir in dirs:
        if dir[:3]=='enx' or dir[:3]=='eth':
          interface=dir
  except:
    interface="None"
  return interface
 
def on_log(client, userdata, level, buf):
   print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client(paho.CallbackAPIVersion.VERSION2)                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
mqttc.on_log = on_log

### Change following parameters #### 
awshost = "a9lwl7f2xpfcf-ats.iot.us-east-1.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "CoolAndTrack"                                     # Thing_Name
thingName = "CoolAndTrack"                                    # Thing_Name
caPath = "/home/Hazem/Desktop/src/AmazonRootCA1.pem"                                      # Root_CA_Certificate_Name
certPath = "/home/Hazem/Desktop/src/certificate.pem.crt"                            # <Thing_Name>.cert.pem
keyPath = "/home/Hazem/Desktop/src/private.pem.key"                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start()    

myMQTTClient = AWSIoTMQTTClient("CoolAndTrack") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a9lwl7f2xpfcf-ats.iot.us-east-1.amazonaws.com", 8883)

myMQTTClient.configureCredentials("/home/Hazem/Desktop/src/AmazonRootCA1.pem", "/home/Hazem/Desktop/src/private.pem.key", "/home/Hazem/Desktop/src/certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(50) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()  

# def loop():
#     while True:
#         randomNumber = uniform(20.0,25.0)
#         #time.sleep(.5)
#         print("Sending Temperature: ", randomNumber)


#         myMQTTClient.publish(
#             topic="RealTimeDataTrasfer/Temperature",
#             QoS=1,
#             payload='{"Temperature":"'+str(randomNumber)+'"}')

# if __name__ == '__main__':
    # try:
    #     loop()
    # except KeyboardInterrupt:
    #     pass                                    # Start the loop
 
  # while 1==1:
  #     sleep(5)
  #     if connflag == True:
  #         ethName=getEthName()
  #         ethMAC=getMAC(ethName)
  #         macIdStr = ethMAC
  #         randomNumber = uniform(20.0,25.0)
  #         region_id= 1
  #         paylodmsg0="{"
  #         paylodmsg1 = "\"mac_Id\": \""
  #         paylodmsg2 = "\", \"random_number\":"
  #         paylodmsg3 = ", \"region_id\": \""
  #         paylodmsg4="\"}"
  #         paylodmsg = "{} {} {} {} {} {} {} {}".format(paylodmsg0, paylodmsg1, macIdStr, paylodmsg2, randomNumber, paylodmsg3, '''random_string''', paylodmsg4)
  #         paylodmsg = json.dumps(paylodmsg) 
  #         paylodmsg_json = json.loads(paylodmsg)       
  #         mqttc.publish("CoolAndTrack", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
  #         print("msg sent: CoolAndTrack" ) # Print sent temperature msg on console
  #         print(paylodmsg_json)

  #     else:
  #         print("waiting for connection...")                      