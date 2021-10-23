#!/usr/bin/python3

import time, os

def check():
    chars = ("|", "/", "—", "\\", "|", "|")
    loading = "\rChecking data breaches..."
    for i in range(len(chars)):
        time.sleep(0.3)
        print(loading+chars[i], end="")
    print("\n")

def roll():
    chars = ("|", "/", "—", "\\", "|", "|")
    loading = "\rRolling dice...."
    for i in range(len(chars)):
        time.sleep(0.35)
        print(loading+chars[i], end="")
    print("\n")

def printLn():
    path = "assets/"
    wordlists = os.listdir(path)
    for wordlist in wordlists:
        if wordlist.endswith(".txt"):
            with open(path+wordlist, "r") as wordlistobj:
                wordliss = wordlistobj.read()
                print("Length of "+wordlist+" is: "+str(len(wordliss)))
