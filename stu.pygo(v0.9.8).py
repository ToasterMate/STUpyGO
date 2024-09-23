import time
import os
import random
import tkinter 
from tkinter import filedialog
import subprocess
import sys

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ///////////////////////////////
# LOCALIZATION
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

translations = {
    "en": {
        "installprompt": "Do you want to install",
        "installY": "has been installed. A PC restart may be required.",
        "installN": "will not be installed. The script may not work without it.",
        "unevenerror": "List contains an uneven amount of items, exiting...",
        "filecriteria": "Please keep in mind that the list must contain an even amount of items and it has to be a .txt file. \nFor the format, please look at the README.",
        "givetranslation": "Input the translation to:",
        "complete": "PRACTICE COMPLETE!",
        "modes": "\n1: First to second\n2: Second to first\n3: First to second RANDOM\n4: Second to first RANDOM"
    },
    "nl": {
        "installprompt": "Wil je het volgende installeren:",
        "installY": "is geinstalleerd, het is geadviseerd om je computer opnieuw op te starten.",
        "installN": "wordt niet geinstalleerd. Het programma kan mogelijk niet goed functioneren zonder.",
        "unevenerror": "Lijst bevat een oneven aantal woorden, uitschakelen...",
        "filecriteria": "Hou er rekenening mee dat het bestand een even aantal woorden moet bevatten en een .txt bestand moet zijn. \nVoor het gewenste formaat, lees A.U.B de README.",
        "givetranslation": "Geef de vertaling van:",
        "complete": "OEFENING COMPLEET!",
        "modes": "\n1: Eerste naar tweede\n2: Tweede naar eerste\n3: Eerste naar tweede WILLEKEURIG\n4: Tweede naar eerste WILLEKEURIG"
    }
}

def translate(language, message_id):
    """Retrieve translation based on language and message ID."""
    return translations.get(language, translations["en"]).get(message_id, message_id)

def get_user_language():
    """Prompt user to select language."""
    languages = ["en", "nl"]
    print("Select a language:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    choice = input("Enter the number corresponding to your language/Vul het getal in dat gelijk staat aan jouw taal: ")
    
    try:
        return languages[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Defaulting to English (en).")
        return "en"

user_language = get_user_language()

# ///////////////////////////////
# PACKAGE INSTALLING (FOR EASY ACCESSIBILITY)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"The module '{package}' is not installed.")
        user_input = input(f"{translate(user_language, 'installprompt')} '{package}'? (Y/N): ").strip().lower()
        
        if user_input == 'y':
            print(f"Installing '{package}'...")
            install_package(package)
            print(f"'{package}' {translate(user_language, 'installY')}")
        else:
            print(f"'{package}' {translate(user_language, 'installN')}")

required_modules = ['tkinter'] 

for module in required_modules:
    check_and_install(module)

print("All required modules are installed. Running the script...")
time.sleep(1)
clear_screen()

# ///////////////////////////////
# GET PLAYERS LIST
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print(f"\n{translate(user_language, 'filecriteria')}\n \n \n© TOBIAS L.\nSTU.PYGO V.0.9.5, 19-9-2024")
root = tkinter.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file = open(file_path, "r")
itemlist = file.readlines()
file.close()

def get_even_number():
    if (len(itemlist) % 2) == 1:
        print(translate(user_language, "unevenerror"))
        time.sleep(2)
        os._exit()
get_even_number()

# ///////////////////////////////
# MODES
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def exit():
    time.sleep(3)
    clear_screen()
    input(f"{translate(user_language, 'complete')}")
    os._exit()

activeitem = 0
wordamount = int(len(itemlist)/2)
def one_two():
    global activeitem
    for x in range(wordamount):
        clear_screen()
        print(f"{int(activeitem/2 + 1)}/{wordamount}")
        answer = input(f"{translate(user_language, 'givetranslation')} {itemlist[activeitem]}").strip().lower()
        goal = itemlist[activeitem + 1].strip().lower()
        if answer == goal:
            print("correct!")
            time.sleep(2)
        else:
            print(f'false, "{goal}"')
            time.sleep(2)
        activeitem += 2
    exit()

def two_one():
    global activeitem
    activeitem = 1
    for x in range(wordamount):
        clear_screen()
        print(f"{int(activeitem/2 + 1)}/{wordamount}")
        answer = input(f"{translate(user_language, 'givetranslation')} {itemlist[activeitem]}").strip().lower()
        goal = itemlist[activeitem - 1].strip().lower()
        if answer == goal:
            print("correct!")
            time.sleep(2)
        else:
            print(f'false, "{goal}"')
            time.sleep(2)
        activeitem += 2
    exit()

def one_two_random():
    global activeitem
    Ractiveitem = 1
    for x in range(wordamount):
        clear_screen()
        Rwordamount = int(len(itemlist)/2)
        print(f"{int(Ractiveitem)}/{wordamount}")
        answer = input(f"{translate(user_language, 'givetranslation')} {itemlist[activeitem]}").strip().lower()
        goal = itemlist[activeitem + 1].strip().lower()
        if answer == goal:
            print("correct!")
            time.sleep(2)
        else:
            print(f'false, "{goal}"')
            time.sleep(2)
        itemlist.pop(activeitem)
        itemlist.pop(activeitem)
        if Ractiveitem >= wordamount: exit()
        while True:
            activeitem = random.randint(0, Rwordamount)
            if activeitem % 2 == 0 and activeitem <= len(itemlist):
                Ractiveitem += 1
                break 

def two_one_random():
    global activeitem
    Ractiveitem = 1
    activeitem = 1
    for x in range(wordamount):
        clear_screen()
        Rwordamount = int(len(itemlist)/2)
        print(f"{int(Ractiveitem)}/{wordamount}")
        answer = input(f"{translate(user_language, 'givetranslation')} {itemlist[activeitem]}").strip().lower()
        goal = itemlist[activeitem - 1].strip().lower()
        if answer == goal:
            print("correct!")
            time.sleep(2)
        else:
            print(f'false, "{goal}"')
            time.sleep(2)
        itemlist.pop(activeitem)
        itemlist.pop(activeitem - 1)
        if Ractiveitem >= wordamount: exit()
        while True:
            activeitem = random.randint(0, Rwordamount)
            if activeitem % 2 == 1 and activeitem <= len(itemlist):
                Ractiveitem += 1
                break 

modes = {
    1: one_two,
    2: two_one,
    3: one_two_random,
    4: two_one_random,
}

def get_mode():
    while True:
        try:
            print(translate(user_language, 'modes'))
            player_input = int(input("Choose an option (1-4): "))
            if player_input in modes:
                modes[player_input]()  # Call the corresponding function
            else:
                print("Invalid choice, please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
get_mode()
