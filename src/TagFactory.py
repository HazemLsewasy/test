from TagBase import TagBase
from TagTemperature import TagTemperature
import binascii

## 
# Constant declaration to decode Bluetooth Advertising payload
# For more information about the frame format, please consult our website 
UUID_SERVICE_TEMPERATURE = "6e2a"
UUID_SERVICE_HUMIDITY = "6f2a"
UUID_SERVICE_MAG = "3f2a00"
UUID_SERVICE_MOV = "3f2a01"
UUID_SERVICE_ANG = "a12a"
UUID_SERVICE_DI = "3f2a02"
UUID_SERVICE_AI = "582a"
UUID_SERVICE_DO = "3f2a"
UUID_SERVICE_BAT = "0f18"

##
# @class Tagfactory 
# @brief tag factory to create tag object to decode data from Bluetooth advertising
class Tagfactory:
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Tagfactory.__instance == None:
            Tagfactory()
        return Tagfactory.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if Tagfactory.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Tagfactory.__instance = self

    ##
    # @fn getTag
    # @brief getter on the tag object according to his payload 
    def getTag(self, payload):
        """ Getter on the target tag """
        tag = TagBase(payload)
        if( isinstance(payload, bytes)):
            tempString = binascii.b2a_hex(tag.payload).decode('ascii')
            if( UUID_SERVICE_TEMPERATURE in tempString):
                print("Debug Tag Temperature FOUND")
                tag = TagTemperature(payload)  
        return tag