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
                print(f"get from microbit  {name} = {value}")
                yield int(value)
            except ValueError:
                pass


def PushToCloud(api_key):
    def push_to_cloud(val):
        r = requests.get(CLOUD_URL, params={'api_key': api_key, 'field1': val})
        print(f'request on {r.url} status {r.status_code} body "{r.text}"')
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
