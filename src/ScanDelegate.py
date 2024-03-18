#declare library
from __future__ import print_function
import sys
import binascii

from TagFactory import Tagfactory

from bluepy3.btle import Scanner, DefaultDelegate

from datetime import *


CONST_LOCAL_NAME = "Complete Local Name"
## 
# @class ScanDelegate
# @brief scan delegate to catch and interpret bluetooth advertising events
class ScanDelegate(DefaultDelegate):

## @brief list of tags formatted values
    tags_formatted_values = []

    ## 
    # @fn __init__ 
    def __init__(self):
        DefaultDelegate.__init__(self)
    
    ##
    # @fn handleDiscovery
    # @brief handle the discovery of a new advertising
    # @param [in] dev : device advertising informations
    # @param [in] isNewDev : is this value a new one
    # @param [in] isNewData : is this value a new data (and the device has already seen once)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        #
        # get a formatted timestamp
        date_time = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
       
        if isinstance(dev.rawData, bytes):
            #
            # find localname into bluetooth properties
            name = ""
            for (adtype, desc, value) in dev.getScanData():
                if (desc == CONST_LOCAL_NAME):
                    name = value
            #
            Temp_measu = Tagfactory.getInstance().getTag(dev.rawData).formattedDataSensor
            if  Temp_measu != "VOID":
                if name.startswith('P T') == True:  
                    entry = "{DATE};{ADDR};{ADDRTYPE};{NAME};{RSSI};{TEMPERATURE};{RAWDATA}".format(ADDR=dev.addr,ADDRTYPE=dev.addrType,RSSI=dev.rssi, NAME=name,TEMPERATURE=Tagfactory.getInstance().getTag(dev.rawData).formattedDataSensor,RAWDATA=binascii.b2a_hex(dev.rawData).decode('ascii'), DATE=date_time)
                    print("Received data from", dev.addr, name)
                    self.tags_formatted_values.append(entry)
def Scan_Method():
    
    scanDelegate = ScanDelegate()
    
    #define object for scanning and define the callback 
    scanner = Scanner().withDelegate(scanDelegate)

    #store the scanned devices
    devices = scanner.scan(0.1)
    return scanDelegate.tags_formatted_values