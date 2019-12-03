from fog_lib import ReadSerial, PushToCloud

# WINDOWS: 'COM4
# LINUX:   '/dev/ttyACM0'
MICROBIT_PORT = '/dev/ttyACM0'

UPDATE_TIME = 10  # seconds

THINGSPEAK_APIKEY = 'YTAD44SADKLSJ312'

'''
VERSION1
'''
# if __name__ == "__main__":
#     push_to_cloud = PushToCloud(THINGSPEAK_APIKEY)

#     for name, val in ReadSerial(MICROBIT_PORT):
#         push_to_cloud(val)


'''
VERSION2
'''
# if __name__ == "__main__":
#     import time
#     push_to_cloud = PushToCloud(THINGSPEAK_APIKEY)

#     total = 0
#     n = 0
#     before = time.monotonic()

#     for name, val in ReadSerial(MICROBIT_PORT):
#         total += val
#         n += 1

#         now = time.monotonic()
#         if now > before + UPDATE_TIME:
#             before = now
#             push_to_cloud(total / n)
#             total = 0
#             n = 0


'''
VERSION3
'''
if __name__ == "__main__":
    from fog_lib import TimePassed
    push_to_cloud = PushToCloud(THINGSPEAK_APIKEY)

    total = 0
    n = 0
    is_time_passed = TimePassed(UPDATE_TIME)

    for name, val in ReadSerial(MICROBIT_PORT):
        total += val
        n += 1

        if next(is_time_passed):
            push_to_cloud(total / n)
            total = 0
            n = 0
