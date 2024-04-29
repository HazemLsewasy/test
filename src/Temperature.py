from Sensor import Sensor
import time
from datetime import *
from ScanDelegate import *
from datetime import datetime

class Temperature(Sensor):
    
    def __init__(self, Mac,container_id,lo_hard_thresh,hi_hard_thresh,lo_soft_thresh,hi_soft_thresh):
        super().__init__(Mac,container_id,lo_hard_thresh,hi_hard_thresh,lo_soft_thresh,hi_soft_thresh)

    #scan and store all avialable Temperature devices in a list the return it 
    #takes Interpreted_data as a list to store the whole record in it
    @staticmethod
    def getScannedDevices():
        #Mac_Addresses is a list to carry list of scanned devices 
        Mac_Addresses = []

        devices = Scan_Method()

        #loop on all found devices and store Mac_addresses in a list, and the whole record 
        # is stored in Interpreted_data list
        for dev in devices:
            tag = dev.split(";")
            Mac_Addresses.append(tag[1])
        return Mac_Addresses 
    #---------------------------------------------------

    #Return measurements based onthe Mac address and takes also the4 records that the function will search in it
    def getMeasurements(self):

        devices = Scan_Method()
        for dev in devices:
            tag = dev.split(";")
            if tag[1] == self.sensor_mac_address:
                self.timeStamp = tag[0]
                self.sensor_measurement = tag[5]
                return self.sensor_measurement

    #------------------------------------------------------
    
    #Return Rssi based onthe Mac address and takes also the4 records that the function will search in it
    def getRssi(self):
        devices = Scan_Method()

        for dev in devices:
            tag = dev.split(";")
            if tag[1] == self.sensor_mac_address:
                Rssi_measure = tag[4]
                return Rssi_measure

    #------------------------------------------------------
    
    #Return BLE_ID based onthe Mac address and takes also the4 records that the function will search in it
    def getSensorId(self):
        return self.sensor_bit_id
    #--------------------------------------------------------
        
    def getTime(self):
        time = self.timeStamp[1]
        return time 
    
    def getDate(self):
        date = self.timeStamp
        return date
