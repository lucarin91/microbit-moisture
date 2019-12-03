import time

import serial
import requests

CLOUD_URL = 'https://api.thingspeak.com/update'


def ReadSerial(port):
    with serial.Serial(port, 115200) as s:
        print("connected")
        while True:
            byte = s.readline()
            line = byte.decode().strip()
            try:
                name, value = line.split(':')
                # do not work on Python<3.6
                # print(f"get from microbit  {name} = {value}")
                print("get from microbit  {} = {}".format(name, value))
                yield name, int(value)
            except ValueError:
                pass


def PushToCloud(api_key):
    def push_to_cloud(val):
        r = requests.get(CLOUD_URL, params={'api_key': api_key, 'field1': val})
        # do not work on Python<3.6
        # print(f'request on {r.url} status {r.status_code} body "{r.text}"')
        print('request on {0.url} status {0.status_code} body "{0.text}"'
              ''.format(r))
        return r.status_code == requests.codes.ok
    return push_to_cloud


def TimePassed(every):
    before = time.monotonic()
    while True:
        now = time.monotonic()
        if before + every < now:
            before = now
            yield True
        else:
            yield False
