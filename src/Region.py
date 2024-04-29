"""
Region module shall collect scanned sensor's data and map them to cloud handler 
"""

import CloudHandler
import Sensor
import Temperature
import json
import errorHandler
import CloudHandler
import pandas as pd


MacAddressesOfScannedSensors=[]
ScannedSensorsObjects=[]
RecivedSensorsData=[]
RecivedCustomerData={}

# class Region(CloudHandler.CloudHandler):

    # region_containers_num=0					#class variable 

    # def __init__(self, room_id, room_geoloc_latitude, room_geoloc_longitude, region_id, region_mac_address, region_containers_num, region_cfg_status):
    #     self.room_id=room_id								#instance variable
    #     self.room_geoloc_longitude=room_geoloc_longitude	#instance variable
    #     self.room_geoloc_latitude=room_geoloc_latitude		#instance variable	
    #     self.region_id=region_id							#instance variable
    #     self.region_mac_address=region_mac_address			#instance variable
    #     self.region_cfg_status=region_cfg_status			#instance variable





#vague method who shall call it , method shall return what 
def updateRegionConfig(self):
    self.room_id=""						#instance variable
    self.room_geoloc_longitude=0.0		#instance variable
    self.room_geoloc_latitude=0.0		#instance variable	
    self.region_id=""					#instance variable
    self.region_mac_address=""			#instance variable
    self.region_cfg_status=False		#instance variable


def Region_Main():
    global CloudIsCalledBefore
    MacAddressesOfScannedSensors_temp=[]
    MacAddressesOfScannedSensors=[]
    MacAddressesOfScannedSensors_temp=Temperature.Temperature.getScannedDevices()
    MacAddressesOfScannedSensors=list(dict.fromkeys(MacAddressesOfScannedSensors_temp))#to be fixed in lower layer
            
    if(len(MacAddressesOfScannedSensors)==0):
        print("Nothing is deteceted !!")
    else:
        if len(ScannedSensorsObjects)==0:#no objects deteced before
            for i in range(len(MacAddressesOfScannedSensors)):
                lo_hard_thresh=0
                hi_hard_thresh=0
                lo_soft_thresh=0
                hi_soft_thresh=0
                containerID=0
                if(any(MacAddressesOfScannedSensors[i] in d for d in RecivedSensorsData)):
                    for iterator in range(len(RecivedSensorsData)):
                        for key in RecivedSensorsData[iterator]:
                            lo_hard_thresh=RecivedSensorsData[iterator][key]["lo_hard_thresh"]
                            lo_soft_thresh=RecivedSensorsData[iterator][key]["lo_soft_thresh"]
                            hi_hard_thresh=RecivedSensorsData[iterator][key]["hi_hard_thresh"]
                            hi_soft_thresh=RecivedSensorsData[iterator][key]["hi_soft_thresh"]
            ScannedSensorsObjects.append(Temperature.Temperature(MacAddressesOfScannedSensors[i],containerID,lo_hard_thresh,hi_hard_thresh,lo_soft_thresh,hi_soft_thresh))
        else:#check if the same mac is existed before or not 
            for i in range(len(MacAddressesOfScannedSensors)):
                lo_hard_thresh=0
                hi_hard_thresh=0
                lo_soft_thresh=0
                hi_soft_thresh=0
                containerID=0
                existed=False
                for y in range(len(ScannedSensorsObjects)):
                    if(MacAddressesOfScannedSensors[i] == ScannedSensorsObjects[y].sensor_mac_address):
                        existed=True
                    else:
                        pass
                if(existed==False):
                    if(any(MacAddressesOfScannedSensors[i] in d for d in RecivedSensorsData)):
                        for iterator in range(len(RecivedSensorsData)):
                            for key in RecivedSensorsData[iterator]:
                                if key == MacAddressesOfScannedSensors[i]:
                                   lo_hard_thresh=RecivedSensorsData[iterator][key]["lo_hard_thresh"]
                                   hi_hard_thresh=RecivedSensorsData[iterator][key]["hi_hard_thresh"]
                                   lo_soft_thresh=RecivedSensorsData[iterator][key]["lo_soft_thresh"]
                                   hi_soft_thresh=RecivedSensorsData[iterator][key]["hi_soft_thresh"] 
                    ScannedSensorsObjects.append(Temperature.Temperature(MacAddressesOfScannedSensors[i],containerID,lo_hard_thresh,hi_hard_thresh,lo_soft_thresh,hi_soft_thresh))
        for x in range(len(ScannedSensorsObjects)):
            SensorMeasurement=ScannedSensorsObjects[x].getMeasurements()
            SensorRSSI=ScannedSensorsObjects[x].getRssi()
            SensorDate=ScannedSensorsObjects[x].getDate()
            SensorId=ScannedSensorsObjects[x].getSensorId()
            '''
            if CloudIsCalledBefore==False:
                CloudHandler.ConfigMQTT_Init()
                CloudIsCalledBefore=True
            '''
            #CloudHandler.CloudHandler.subscribePayload()
            if SensorMeasurement is not None and SensorRSSI is not None:
                myobj = { 'MAC_Address'  : str(ScannedSensorsObjects[x].sensor_mac_address),
                  'Sensor_ID'    : str(SensorId),
                  'Sensor_Type'  : "Temperature",
                  'Measurements' : str(SensorMeasurement),
                  'Timestamp'    : str(SensorDate),
                  'RSSI'         : str(SensorRSSI)
                  }
                # CloudHandler.CloudHandler.publishPayload(myobj)
        print("scanned sensors list: "+str(MacAddressesOfScannedSensors))
        # for i in range(len(ScannedSensorsObjects)):
        #     print("last "+str((ScannedSensorsObjects[i].sensor_mac_address)))
        #     print("last "+str((ScannedSensorsObjects[i])))
        #     print(type(ScannedSensorsObjects[i]))
            #  errorHandler.Check_Sensor_Measurement(ScannedSensorsObjects[i])
    print(myobj)
            
      
                
            
def parseRecivedData(messagePayload):
    global RecivedSensorsData
    listOfKeys=[]
    dict_temp={}

    try:
        messageDictionary=json.loads(messagePayload)
        # print(messageDictionary)
        # print(type(messageDictionary))
        # print((messageDictionary["de:c1:bc:ce:85:c4"]["lo_hard_thresh"]))
        for x in messageDictionary:
            print("Recived key: "+x)
            if(any(x in d for d in RecivedSensorsData)):
                for index in range(len(RecivedSensorsData)):
                    for key in RecivedSensorsData[index]:
                        if(key == x):
                            RecivedSensorsData[index][key]=messageDictionary[key]
                print("key is already exist "+key)
            else:
                if(":" in x):#colon is part of the mac addresses of the senors
                    dict_temp.update({x:messageDictionary[x]})
                    RecivedSensorsData.append(dict_temp)
                    print("New key")
    except:
        print("Decoding Json has failed, Format maybe wrong!!")

                                                                                                                                                                                                                   

    
