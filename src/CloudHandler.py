from __future__ import print_function
import sys
import binascii

from bluepy3.btle import Scanner, DefaultDelegate
from datetime import datetime
import requests
import os
import socket
import ssl
import random
import string
import json
from time import sleep
from random import uniform
import Region
x=0

#myMQTTClient=AWSIoTMQTTClient("CoolAndTrack")
topic_to_be_published="RealTimeDataTrasfer/Temperature_S2"
QoS_to_be_published=1
url = 'https://i7oi4060ma.execute-api.us-east-1.amazonaws.com/AsynPiPublishLambda'    

class CloudHandler:
    __connection_status=0
    __sensor_id=""
    __sensor_mac_add=""
    __sensor_measurement=0.0
    __sensor_rssi=0.0

    @staticmethod
    def publishPayload(passed_payload=""):
        global url
        x = requests.get(url, passed_payload)
        if x.text == "null" :
            print("====================================")
            print("published data: ")
            print(passed_payload)
            print("====================================")
