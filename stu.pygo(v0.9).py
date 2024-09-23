import time
import os
import tkinter 
from tkinter import filedialog
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install(package):
    try:
        # Try to import the package
        __import__(package)
    except ImportError:
        # Package not installed
        print(f"The module '{package}' is not installed.")
        user_input = input(f"Do you want to install '{package}'? (Y/N): ").strip().lower()
        
        if user_input == 'y':
            print(f"Installing '{package}'...")
            install_package(package)
            print(f"'{package}' has been installed.")
        else:
            print(f"'{package}' will not be installed. The script may not work without it.")

# Check if specific modules are installed
required_modules = ['tkinter']  # Add any module you want to check

for module in required_modules:
    check_and_install(module)

# Rest of your script goes here
print("All required modules are installed. Running the script...")

translations = {
    "en": {
        "unevenerror": "List contains an uneven amount of items, exiting...",
        "filecriteria": "Please keep in mind that the list must contain an even amount of items and it has to be a .txt file. \nFor the format, please look at the README.",
        "givetranslation": "Input the translation to:"
    },
    "nl": {
        "unevenerror": "Lijst bevat een oneven aantal woorden, uitschakelen...",
        "filecriteria": "Hou er rekenening mee dat het bestand een even aantal woorden moet bevatten en een .txt bestand moet zijn. \nVoor het gewenste formaat, lees A.U.B de README.",
        "givetranslation": "Geef de vertaling van:"
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


print(f"\n{translate(user_language, 'filecriteria')}\n \n \nTOBIAS L.\nSTU.PYGO V.0.9, 19-9-2024")
root = tkinter.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file = open(file_path, "r")
itemlist = file.readlines()
file.close()

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_even_number():
    if (len(itemlist) % 2) == 1:
        print(translate(user_language, "unevenerror"))
        time.sleep(2)
        os._exit()
get_even_number()


activeitem = 0
for x in itemlist:
    clear_screen()
    print(f"{int(activeitem/2)}/{int(len(itemlist)/2)}")
    answer = input(f"{translate(user_language, 'givetranslation')} {itemlist[activeitem]}")
    goal = itemlist[activeitem + 1].strip()
    if answer == goal:
        print("correct!")
        time.sleep(2)
    else:
        input(f'false, "{goal}"')
    activeitem += 2

time.sleep(5)