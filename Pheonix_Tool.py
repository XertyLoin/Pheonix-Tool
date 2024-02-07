import os
import platform
import random
import string
import time
import webbrowser
import sys
from colorama import *
import pygame
import inquirer
import ctypes

now = time.localtime(time.time())
time = time.strftime("%H:%M:%S", now)

if platform.system() == "Windows":
    def clear():
        os.system("cls")
if platform.system() == 'Linux':
    def clear():
        os.system("clear")

pygame.init()

def chronometre():
   # Chemin absolu du fichier Python en cours d'exécution
    chemin_absolu = os.path.abspath(__file__)

    # Dossier parent
    dossier_parent = os.path.dirname(chemin_absolu)
    print(f"""{Fore.CYAN}
     ██████╗██╗  ██╗██████╗  ██████╗ ███╗   ██╗ ██████╗ ███╗   ███╗███████╗████████╗██████╗ ███████╗
    ██╔════╝██║  ██║██╔══██╗██╔═══██╗████╗  ██║██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
    ██║     ███████║██████╔╝██║   ██║██╔██╗ ██║██║   ██║██╔████╔██║█████╗     ██║   ██████╔╝█████╗  
    ██║     ██╔══██║██╔══██╗██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══██╗██╔══╝  
    ╚██████╗██║  ██║██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
    {Fore.RESET}                                                                                            
            """)
    questionsd = [
        inquirer.List('share', 
            message="Que voulais faire ? ",
            choices=['Open It', 'Menu Principal', 'Quiter']
            )
        ]
    answersd = inquirer.prompt(questionsd)['share']
    if answersd == "Quiter":
        sys.exit()
    if answersd == "Menu Principal":
        clear()
        main()
    if answersd == "Open It":

        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        webbrowser.get('chrome').open_new_tab(rf'{dossier_parent}/chronoH/index.html')
        clear()
        chronometre()



def gpassword():
    print (f"""{Fore.GREEN}
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝ 
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║  ███╗
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║   ██║
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝EN
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚═════╝ 
    {Fore.RESET}""")
    questions = [
    inquirer.List('share',
            message="Voulais vous ajouter des caractère spéciaux",
            choices=['oui','non'],
        ),
    ]
    answers = inquirer.prompt(questions)['share']
    if answers == "oui":
        number_of_strings = 1
        length_of_string = 8
        for x in range (number_of_strings):
            print (''.join (random.choice (string.ascii_letters + string.digits + string.punctuation) for _ in range (length_of_string)))
    elif answers == "non":
        number_of_strings = 1
        length_of_string = 8
        for x in range (number_of_strings):
            print (''.join (random.choice (string.ascii_letters + string.digits) for _ in range (length_of_string)))

    retour = input(f"apuyer sur [m] pour revenir au menu principal {Fore.RED}[{Fore.GREEN}>{Fore.RED}] ")
    
    if retour == "m":
        clear()
        main()
    else:
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
    questions = [
        inquirer.List('share',
                message="Que voulais faire ? ",
                choices=['Generate Password', 'SoundBord', 'Chronométre'],
            ),
    ]
    answers = inquirer.prompt(questions)['share']
    if answers == "Generate Password":
        clear()
        gpassword()
    elif answers == "SoundBord":
        clear()
        soundbord()
    elif answers == "Chronométre":
        clear()
        chronometre()
    else:
        clear()
        main()


main ()
