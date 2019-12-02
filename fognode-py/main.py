from fog_lib import ReadSerial, TimePassed, PushToCloud

# WINDOWS: 'COM4
# LINUX:   '/dev/ttyACM0'
MICROBIT_PORT = '/dev/ttyACM0'

UPDATE_TIME = 10  # seconds

THINGSPEAK_APIKEY = 'YTAD44SADKLSJ312'


if __name__ == "__main__":
    total = 0
    n = 0
    is_time_passed = TimePassed(UPDATE_TIME)
    push_to_cloud = PushToCloud(THINGSPEAK_APIKEY)

    for val in ReadSerial(MICROBIT_PORT):
        total += val
        n += 1

        if next(is_time_passed):
            avg = total / n
            push_to_cloud(avg)
            total = 0
            n = 0
