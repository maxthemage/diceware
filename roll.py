#!/usr/bin/python3

import time, os

def roll():
    chars = ("|", "/", "—", "\\", "|", "|")
    loading = "\rRolling dice...."
    for i in range(len(chars)):
        time.sleep(0.5)
        print(loading+chars[i], end="")
    print("\n")

def rollAnimation():
    one = """
    \r 
    \r   •
    \r 
    """
    two = """
    \r•
    \r
    \r    •
    """
    three = """
    \r•
    \r  •
    \r    •
    """
    four = """
    \r•   •
    \r
    \r•   •
    """
    five =  """
    \r•   •
    \r  •
    \r•   • 
    """
    six = """
    \r•   •
    \r•   •
    \r•   •
    """
    
    dice = [one, two, three, four, five, six]
    for i in range(len(dice)):
        #dice[i] = dice[i].replace("\n", "", 3)
        print("\r"+dice[i], end="")
        time.sleep(1)

def osList():
    print(os.listdir("assets"))

def printLn():
    path = "assets/"
    wordlists = os.listdir(path)
    for wordlist in wordlists:
        if wordlist.endswith(".txt"):
            with open(path+wordlist, "r") as wordlistobj:
                wordliss = wordlistobj.read()
                print("Length of "+wordlist+" is: "+str(len(wordliss)))
