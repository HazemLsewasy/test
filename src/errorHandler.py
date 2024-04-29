WITHIN_RANGE       = 1

LOW_HARD_THRESH    = 8
HIGH_HARD_THRESH   = 9
LOW_SOFT_THRESH    = 10
HIGH_SOFT_THRESH   = 11

UNDEFINED_MEASURE_STATE = 0

CONNECTION_LOST    = 12
CONNECTION_STABLE  = 13

def Check_Sensor_Measurement(sensor_object):
    if sensor_object.isMeasWithinSoftThresh() == True and sensor_object.isMeasWithinHardThresh() == True:
        return WITHIN_RANGE
    elif sensor_object.isMeasWithinHardThresh() == False:
        if sensor_object.sensor_measurement < sensor_object.sensor_warn_lo_hard_thresh :
            return LOW_HARD_THRESH
        elif sensor_object.sensor_measurement > sensor_object.sensor_warn_hi_hard_thresh :
            return HIGH_HARD_THRESH
    elif sensor_object.isMeasWithinSoftThresh() == False:
        if sensor_object.sensor_measurement < sensor_object.sensor_warn_lo_soft_thresh :
            return LOW_SOFT_THRESH
        elif sensor_object.sensor_measurement > sensor_object.sensor_warn_hi_soft_thresh :
            return HIGH_SOFT_THRESH
    else:
        return UNDEFINED_MEASURE_STATE
    
def Check_Region_Cloud_Connection(Region_object):
    return CONNECTION_STABLE