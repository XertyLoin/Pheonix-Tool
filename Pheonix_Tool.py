import os
import platform
import random
import string
import time

import discord
from colorama import *
from discord.ext import commands
import pygame

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
pygame.init()


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
        desc = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Titre de  l'Embed {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        Token = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Ton token {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        Embed = discord.Embed(Title='petit test', description=desc, color=808080, inline=True)
        qyt = input(f"voulais vous ajouter votre chaîne youtube [oui-non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        qtw = input(f"voulais vous ajouter votre twitter [oui-non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        qgg = input(f"voulait vous mettre ajouter votre serveur discord [oui-non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
        qtwt = input(f"voulais vous ajouter une chaîne twitch [oui-non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}]")
        qgit = input(f"voulais vous ajouter un github [oui-non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}]")
        qgif = input(f"voulais vous ajouter un gif [oui-non]")
        if qyt == "oui":
            ytchanel = input(f'{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Le liens de votre chaine youtube {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ')
            Embed.add_field(name='Youtube', value=f"[youtube]({ytchanel})", inline=True)
        if qtw =="oui":
            tw = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}donner le liens de votre Twitter {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
            Embed.add_field(name='Twitter', value=f"[Twitter]({tw})", inline=True)
        if qgg == "oui":
            gg = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}donner le liens de votre serveur discord {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
            Embed.add_field(name='Discord serveur', value=f"[Discord]({gg})", inline=True)
        if qtwt == "oui":
             twt = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Le lien vers votre chaine twitch {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
             Embed.add_field(name='Tiwtch', value=f"[Twitch]({twt})", inline=True)
        if qgit == "oui":
            git = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}le lien de votre Github {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
            Embed.add_field(name='Github', value=f"[GitHub]({git})", inline=True)
        if qgif == "oui":
            url = input(f"{Fore.BLUE}[{Fore.GREEN}{time}{Fore.BLUE}]{Fore.BLUE}Le lien vers votre image / gif {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
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
    choix1 = input(f"voulais vous des caratères spéciaux Dans le mot de passe ?[oui - non] {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
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

    retour = input(f"apuyer sur [m] pour revenir au menu principal {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
    if retour == "m":
        clear()
        main()

def soundbord():
    global Token
    print(f"""{Fore.MAGENTA}
    ██╗     ███████╗ ██████╗████████╗███████╗██╗   ██╗██████╗      █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ 
    ██║     ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║   ██║██╔══██╗    ██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗
    ██║     █████╗  ██║        ██║   █████╗  ██║   ██║██████╔╝    ███████║██║   ██║██║  ██║██║██║   ██║
    ██║     ██╔══╝  ██║        ██║   ██╔══╝  ██║   ██║██╔══██╗    ██╔══██║██║   ██║██║  ██║██║██║   ██║
    ███████╗███████╗╚██████╗   ██║   ███████╗╚██████╔╝██║  ██║    ██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝
    ╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ 
    """)
    print(f"{Fore.BLUE}n'oublié pas de le mettre dans le fichier ou se trouve le pheonix tool")
    print("il est possible d'éxécuter que des son en .mp3 et vous devais le préciser ex : MusicDuPain.mp3")
    pathsong = input(f"{Fore.RED}ajouter le liens vers votre son {Fore.RED}[{Fore.GREEN}>{Fore.RED}]")
    pygame.mixer.music.load(pathsong)
    pygame.mixer.music.play(-1)
    Token = input("apuyer sur [m] pour retourner au menu principal")
    if Token == "m":
        clear()
        main()
    else:
        clear()
        main()


def main():
    clear()
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
    if quoi1 == "3":
        clear()
        soundbord()
    if quoi1 not in ["1", "2", "3"]:
        clear()
        main()

main ()

bot.run(Token, bot=False)

""""

        
        
        
        
        
       
       
        
        
        
        
        
        
        
        
"""