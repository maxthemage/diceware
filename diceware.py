#!/usr/bin/python3

diceware_banner = """
\t\t     ____  _
\t\t    |  _ \(_) ___ _____      ____ _ _ __ ___
\t\t    | | | | |/ __/ _ \ \ /\ / / _` | '__/ _ \\
\t\t    | |_| | | (_|  __/\ V  V / (_| | | |  __/
\t\t    |____/|_|\___\___| \_/\_/ \__,_|_|  \___|
"""
version = "\t\t\t\t   BETA Version\n"
mainscreen_text = """\t\t\t\tCoded by: Gecko <3\n       Utility For Generating Secure Passphrases Using The Diceware Method
\t\t\t\t   BETA Version\n"""

import secrets, math, os, time, sys
import roll as rl
import read as pswd

random = secrets.SystemRandom()

def clear():
    os.system("clear")

def banner(var):
    clear()
    print(var)

def secondaryHeading():
    banner(diceware_banner)
    print(version)

def diceRoll(array, num):
    random = secrets.SystemRandom()
    mult = 10000
    dice_num = 0
    if num == 4:
        mult = 1000
    for i in range(0, num):
        dice_num += (random.randint(1,6)) * mult
        mult /= 10
    array.append(str(int(dice_num)))


def matchWords(load_file, array, number):
    words = {}
    phrase = ""
    with open(load_file, "r") as file_object:
        file_data = file_object.readlines()
    for line in file_data:
        for num in array:
            if num in line:
                line = line.strip("\n")
                print("\t"+line)
                if number == 5:
                    words.update({line[:5]: line[6:]})
                    phrase = phrase + (line[6:])
                elif number == 4:
                    words.update({line[:4]: line[5:]})
                    phrase = phrase + (line[5:])
    print(f"\n\t" + '\033[1m' + f"{phrase}\n" + '\033[0m')


def matchWordsTwo(load_file, array):
    words = {}
    passphrase = ""
    with open(load_file, "r") as file_object:
        file_data = file_object.readlines()
    for line in file_data:
        for num in array:
            if num in line:
                line = line.strip("\n")
                words.update({line[:5]: line[6:]})
                passphrase = passphrase + (line[6:])
    print(f"\n\nYour passphrase is " + '\033[1m' + f"{passphrase}" + '\033[0m')
    pswd.dicewareEntropy()
    pswd.dicewareCharacterLength(passphrase)


def entropy(psswd):
    R = 26
    L = len(psswd)
    entropy = math.log2(math.pow(R, L))
    print(str(entropy)+" bits")
    input("\nPress <ENTER> to continue...")


def getEffWordlist(directory):
    try:
        banner(diceware_banner)
        print(version)
        print("\n\t[1]: General Short Wordlist\n\t[2]: Short Wordlist\n\t[3]: Large Wordlist\n\t[4]: Back")
        #print("\nWhich EFF wordlist would you like to use?")
        value = int(input("\n~$ "))
        if value == 1:
            wordlist = directory + "eff_general_short_wordlist.txt"
            generatePhrase(wordlist)
        elif value == 2:
            wordlist = directory + "eff_short_wordlist.txt"
            generatePhrase(wordlist)
        elif value == 3:
            wordlist = directory + "eff_large_wordlist.txt"
            generatePhrase(wordlist)
        elif value == 4:
            #doLoop = False
            diceware()
        else:
            print("Choose either between 1,2 or 3")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")


def generatePhrase(filename):
    dice_array = []
    num = 5
    if filename == "assets/wordlists/eff_short_wordlist.txt" or filename == "assets/wordlists/eff_general_short_wordlist.txt":
        num = 4
    try:
        banner(diceware_banner)
        print(version)
        print("\nHow many words would you like to generate")
        no_of_rolls = int(input("\n~$: "))
        print("\n")
        rl.roll()
        clear()
        banner(diceware_banner)
        print(version)
        print("\nYour diceware generated words are: \n")
        for i in range(0, no_of_rolls):
            diceRoll(dice_array, num)
        matchWords(filename, dice_array, num)
        input("\nPress <ENTER> to continue...")
    except ValueError:
        print("\nError! Please enter an number.")
        time.sleep(1)


def generatePassword():
    directory = "assets/wordlists/"
    wordlists = [wordlist for wordlist in os.listdir(directory)]
    with open((directory+wordlists[(random.randint(0,len(wordlists)))]), "r") as wordlist_obj:
        diceware_wl = wordlist_obj.readlines()
    print(wordlist_obj)
    time.sleep(5)


def generatePassphrase():
    secondaryHeading()
    rolled_nums = []
    directory = "assets/wordlists/eff_large_wordlist.txt"
    print("\n")
    rl.roll()
    banner(diceware_banner)
    print(version)
    for i in range(0, 5):
        diceRoll(rolled_nums, 5)
    matchWordsTwo(directory, rolled_nums)
    input("\nPress <ENTER> to continue...")


def psswdOptions():
    banner(diceware_banner)
    print(version)
    print("\n\n\t[1]: Random Password\n\t[2]: Random Passphrase\n\t[3]: Back\n")
    option = int(input("~$ "))
    if option == 1:
        generatePassword()
    elif option == 2:
        generatePassphrase()
    elif option == 3:
        doLoop = False
    else:
        print("Choose between 1 and 2")
        time.sleep(1.5)

def settings():
    pass

def diceware():
        filename = "assets/wordlists/"
        try:
            try:
                banner(diceware_banner)
                print(version)
                print("\n\t[1]: Beale wordlist\n\t[2]: Diceware wordlist\n\t[3]: EFF wordlists (recommended)\n\t[4]: Back")
                #print("Which wordlist would you like to use?")
                option = int(input("\n~$ "))
                if option == 1:
                    generatePhrase(filename + "beale_wordlist.txt")
                elif option == 2:
                    generatePhrase(filename + "diceware_wordlist.txt")
                elif option == 3:
                    getEffWordlist(filename)
                elif option == 4:
                    doLoop = False
                else:
                    print("Choose between 1, 2, or 3")
                    time.sleep(1)
            except ValueError:
                    print("\nError! Choose between 1, 2, 3 or 4")
                    time.sleep(1.5)
        except:
            print("\n\nExiting...")
            doLoop = False
            time.sleep(0.65)
            clear()


def mainMenu():
    doLoop = True
    while doLoop == True:
        try:
            try:
                banner(diceware_banner)
                print(mainscreen_text)
                print("""
                \n\t[1]: Generate Diceware Words\n\t[2]: Generate Random Password\n\t[3]: Test Password Strength\n\t[4]: Help\n\t[5]: Exit""")
                response = int(input("\n~$ "))
                if response == 1:
                    diceware()
                elif response == 2:
                    psswdOptions()
                elif response == 3:
                    banner(diceware_banner)
                    print(version)
                    print("\nEnter password for evaluation: ")
                    password = input("\n~$ ")
                    clear()
                    banner(diceware_banner)
                    print(version)
                    pswd.get(password)
                    pswd.checkBreach(password)
                elif response == 4:
                    banner(diceware_banner)
                    print(version)
                    time.sleep(1)
                    abt.printHelp()
                    time.sleep(1)
                elif response == 5:
                    clear()
                    quit()
                    doLoop = False
                else:
                    print("\nChoose between 1, 2, 3, 4 or 5.")
                    time.sleep(1)
            except ValueError:
                print("\nError! Choose between 1, 2, 3, 4 or 5.")
                time.sleep(1.2)
        except:
            print("\n\nExiting...")
            doLoop = False
            time.sleep(0.7)
            clear()
mainMenu()
