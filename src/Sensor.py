#import abstract class base defiition 
from abc import ABC, abstractmethod
from ScanDelegate import *
#Define Global constants

#define indecies of mac address, time stamp, ble id, rssi value, temperature value per record 
#as the received record fromate is "timestamp,addr,addrType,localName,rssi,temperature,rawdata"
#timestamp      --> TIME_STAMP          ,   index 0 
#addr           --> MAC_ADDRESS         ,   index 1
#localName      --> BLE_ID              ,   index 3
#rssi           --> RSSI_VAL            ,   index 4
#temperature    --> TEMPERATURE_VAL     ,   index 5

TIME_STAMP      = 0
MAC_ADDRESS     = 1
BLE_ID          = 3
RSSI_VAL        = 4
TEMPERATURE_VAL = 5

#Abstract class to define base for sensors
class Sensor(ABC):
    #the constuctor of class sensor takes the type of sensor "which is ELA for now"
    def __init__(self,Mac,container_id,lo_hard_thresh,hi_hard_thresh,lo_soft_thres,hi_soft_thres):
        self.sensor_mac_address = Mac
        self.sensor_warn_lo_hard_thresh = lo_hard_thresh
        self.sensor_warn_hi_hard_thresh = hi_hard_thresh
        self.sensor_warn_lo_soft_thres  = lo_soft_thres
        self.sensor_warn_hi_soft_thres  = hi_soft_thres
        self.sensor_container_id = container_id
        devices = Scan_Method()
        for dev in devices:
            tag=dev.split(";")
            if tag [1] == Mac:
                self.sensor_bit_id = tag[3]
                self.sensor_measurement = tag[5]
        super().__init__()
    #---------------------------------------------------------------
    def isMeasWithinSoftThresh(self):
        if self.sensor_measurement > self.sensor_lo_soft_thres and self.sensor_measurement < self.sensor_hi_soft_thres :
            return True
        else:
            return False
    def isMeasWithinHardThresh(self):
        if self.sensor_measurement > self.sensor_lo_hard_thres and self.sensor_measurement < self.sensor_hi_hard_thres :
            return True
        else:
            return False
    @abstractmethod
    def getScannedDevices():
        pass

    @abstractmethod
    def getMeasurements(Mac):
        pass

    @abstractmethod
    def getRssi(Mac):
        pass

    @abstractmethod
    def getSensorId(Mac):
        pass