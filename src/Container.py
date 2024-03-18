'''import Sensor

class Container:

	@staticmethod # I think this shall call/check configuration from cloud 
    def getContainerConfig():
        pass


	def __init__(self, container_id="" , container_new_sensor_detected_flag=False , List_of_sensors=[]):
		self.container_id=container_id
		self.container_new_sensor_detected_flag=container_new_sensor_detected_flag
		self.List_of_sensors=List_of_sensors
		#self.container_sensor_num+=1 #not need to be statis or to exist at all we can get the number of sensor from length of the list
	

