try:
    import os, requests, io, aiohttp, bs4
    import nmap, socket, sys, threading, concurrent.futures, pprint, codecs, urllib3
    from bs4 import BeautifulSoup
    import discord
    import pyfiglet
    from datetime import *
    from discord.ext import commands
    from multiprocessing import context
    from discord import Color, message
    from discord.enums import Status
    from discord.utils import get
    from PIL import Image
    from io import BytesIO
    from colorama import Fore
except ModuleNotFoundError:
    os.system("cls")
    os.system("clear")
    print("[-] Modulo no encontrado porfavor instalar 'requirements.txt \n > pip install -r requirements.txt \n > pip3 install -r requirements.txt")



os.system("cls")

print((Fore.RED) + """
    ╔╗╔╔═╗╔╦╗╔═╗╦ ╦╔╗╔╔╦╗╔═╗═╗ ╦
    ║║║║ ║ ║ ╚═╗╚╦╝║║║ ║ ╠═╣╔╩╦╝
    ╝╚╝╚═╝ ╩ ╚═╝ ╩ ╝╚╝ ╩ ╩ ╩╩ ╚═
    ╔═╗╔═╗╦  ╔═╗  ╔╗ ╔═╗╔╦╗     
    ╚═╗║╣ ║  ╠╣───╠╩╗║ ║ ║      
    ╚═╝╚═╝╩═╝╚    ╚═╝╚═╝ ╩   

""")

client = commands.Bot(command_prefix="..", self_bot=True, help_command=None)
try:
    token = "token"
except:
    print("[-] No existe el token o no hay red")

@client.event
async def on_ready():
    print((Fore.WHITE) +"[+] Online")

async def self_check(ctx):
    if client.user.id == ctx.message.author.id:
        return True
    else:
        return False

@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("""```
┌─┐┌─┐┬  ┌─┐  ┌┐ ┌─┐┌┬┐  ┌┬┐┌─┐┌┬┐┌─┐
└─┐├┤ │  ├┤   ├┴┐│ │ │   │││├─┤ ││├┤ 
└─┘└─┘┴─┘└    └─┘└─┘ ┴   ┴ ┴┴ ┴─┴┘└─┘
┌┐ ┬ ┬  ┌─┐┌─┐┬  ┬  ┌─┐              
├┴┐└┬┘  ├─┘│ ││  │  │ │              
└─┘ ┴   ┴  └─┘┴─┘┴─┘└─┘           

1. ..commands

```"""
    )

@client.command()
async def commands(ctx):
    await ctx.message.delete()
    await ctx.send("""
    ```fix
┌─┐┌─┐┬  ┌─┐  ┌┐ ┌─┐┌┬┐  ┌┬┐┌─┐┌┬┐┌─┐
└─┐├┤ │  ├┤   ├┴┐│ │ │   │││├─┤ ││├┤ 
└─┘└─┘┴─┘└    └─┘└─┘ ┴   ┴ ┴┴ ┴─┴┘└─┘
┌┐ ┬ ┬  ┌─┐┌─┐┬  ┬  ┌─┐              
├┴┐└┬┘  ├─┘│ ││  │  │ │              
└─┘ ┴   ┴  └─┘┴─┘┴─┘└─┘           
```""")
    await ctx.send("""```css

~ [info] | Obtener informacion de un miembro
~ [ascii] | Hacer un texto en forma ascii
~ [areyoufemboy] | Eres femboy?
~ [purge] | Borrar cantidad de mensajes determinados
~ [playing] | Poner en la lista de "jugando" un texto
~ [watching] | Poner en la lista de "viendo" un texto
~ [listening] | Poner en la lista de "escuchando" un texto
~ [streaming] | Poner en la lista de "Streameando" un texto
~ [stopactivity] | Apagar la actividad que esta haciendo
~ [avatar] | Ver el avatar de un miembro
~ [shutdown] | Apagar la conexion con el servidor
~ [msgsniper] (value) | Ver mensajes borrados de miembros 

```""")
    await ctx.send("https://cdn.discordapp.com/attachments/890295666457329684/994750721918509147/standard.gif")

@client.command()
async def info(ctx, *, member: discord.Member):
    await ctx.message.delete()
    """Tells you some info about the member."""
    fmt = '{0} se a unido en {0.joined_at} y tiene {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('No se puede localizar este usuario...')

@client.command()
async def areyoufemboy(ctx):
    await ctx.message.delete()
    await ctx.send(f"https://tenor.com/view/wait-cat-are-you-afemboy-cute-femboy-gif-17221762")

@client.command()
async def ascii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')

@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@client.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=message))

@client.command()
async def streaming(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=1, name=f"{status}", url="https://www.twitch.tv/meomounstro")
            await client.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Streaming {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")

@client.command()
async def avatar(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    author = ctx.author

    if not user:
        user = author

    if user.is_avatar_animated():
        url = user.avatar_url_as(format="gif")
    if not user.is_avatar_animated():
        url = user.avatar_url_as(static_format="png")

    await ctx.send("{} avatar: {}".format(user.name, url))

@client.command()
async def shutdown(ctx):
    await ctx.message.delete()
    await client.logout()

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await client.change_presence(activity=None, status=discord.Status.dnd)

@client.command()
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        client.msgsniper = True
        await ctx.send('Selfbot Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        client.msgsniper = False
        await ctx.send('Selfbot Message-Sniper is now **disabled**')

client.run(token, bot=False)
