import os
import platform
import random
import string
import time

import discord
from colorama import *
from discord.ext import commands

now = time.localtime(time.time())
bot = commands.Bot(command_prefix='d', self_bot=True)
time = time.strftime("%H:%M:%S", now)

if platform.system() == "Windows":
    def clear():
        os.system("cls")
if platform.system() == 'Linux':
    def clear():
        os.system("clear")

init()


def discord_tool():
    global Embed
    global Token
    global msg
    print(f"""{Fore.BLUE}
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║       ██║   ██║   ██║██║   ██║██║     
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║       ██║   ██║   ██║██║   ██║██║     
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
    (auto mp)
    {Fore.RESET}""")
    print(f"{Fore.RED}1 - Message")
    print(f"{Fore.RED}2 - Embed")
    print(f"{Fore.RED}Apuyer sur {Fore.BLUE}[m] {Fore.RED}pour revenir en arière")
    quoi2 = input (f"{Fore.RED}Que voulais vous faire ? {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")

    if quoi2 == "2":
        ytchanel = input(f'{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Le liens de votre chaine youtube {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ')
        desc = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Titre de  l'Embed {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        git = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}le lien de votre Github {Fore.GREEN}> ")
        twt = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}donner le liens de votre Twitter {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        gg = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}donner le liens de votre serveur discord {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        url = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Le lien vers votre image / gif {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        Token = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Ton token {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        Embed = discord.Embed(Title='petit test', description=desc, color=808080, inline=True)
        Embed.add_field(name='Youtube', value=f"[youtube]({ytchanel})", inline=True)
        Embed.add_field(name='Github', value=f"[GitHub]({git})", inline=True)
        Embed.add_field(name='Twitter', value=f"[Twitter]({twt})", inline=True)
        Embed.add_field(name='Discord serveur', value=f"[Discord]({gg})", inline=True)
        Embed.set_image(url=url)
        @bot.event
        async def on_ready():
            for f in bot.user.friends:
               await f.send(embed=Embed)

    if quoi2 == "1":
        Token = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}quel est votre token ? {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        msg = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Quel est votre message ? {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")

        @bot.event
        async def on_ready():
            for f in bot.user.friends:
                await f.send(msg)
    if quoi2 == "m":
        clear()
        main()





def gpassword():
    print (f"""{Fore.GREEN}
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ 
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝EN
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ 
    {Fore.RESET}""")
    choix1 = input(f"voulais vous des caratères spéciaux Dans le mot de passe ?[oui - non]")
    if choix1 == "oui":
        number_of_strings = 1
        length_of_string = 8
        for x in range (number_of_strings):
            print (''.join (random.choice (string.ascii_letters + string.digits + string.punctuation) for _ in range (length_of_string)))
    if choix1 == "non":
        number_of_strings = 1
        length_of_string = 8
        for x in range (number_of_strings):
            print (''.join (random.choice (string.ascii_letters + string.digits) for _ in range (length_of_string)))

    retour = input("apuyer sur [m] pour revenir au menu principal")
    if retour == "m":
        clear()
        main()


def main():
    print (f"""{Fore.RED}
    ██████╗ ██╗  ██╗███████╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
    ██╔══██╗██║  ██║██╔════╝██╔═══██╗████╗  ██║██║╚██╗██╔╝
    ██████╔╝███████║█████╗  ██║   ██║██╔██╗ ██║██║ ╚███╔╝ 
    ██╔═══╝ ██╔══██║██╔══╝  ██║   ██║██║╚██╗██║██║ ██╔██╗ 
    ██║     ██║  ██║███████╗╚██████╔╝██║ ╚████║██║██╔╝ ██╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
    {Fore.RESET}""")
    print ("1 - discord tool")
    print ("2 - generate password")
    quoi1 = input ("Que voulais vous faire ? [>] ")
    if quoi1 == "1":
        clear ()
        discord_tool ()
    if quoi1 == "2":
        clear ()
        gpassword ()

main ()

bot.run(Token, bot=False)
