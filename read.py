#!/usr/bin/python3

import csv, os, time, math
import roll as load

def checkBreach(password):
    path = "assets/password-breach-data/"
    with open(path + (os.listdir(path)[0])) as csv_object:
        password_data = csv.reader(csv_object)
        try:
            load.check()
            for row in password_data:
                breached = f"{str(row[0])}" 
                if password.lower()==breached or password.title()==breached or password.upper()==breached:
                    print("                                                                            ", end="\r")
                    print('\033[1m' + f'\t{breached}' + '\033[0m', end = "\r")
                    print("\n\n\nOops! This password or a similar password was found in a data breach.")
                    time.sleep(1)
                    input("Press <ENTER> to continue...")
                    break          
                else:
                    if breached != "luve12":
                        print("                                                                            ", end="\r")
                        print(f"\t{breached}", end = "\r")
                        time.sleep(0.000001)
                    else:
                        print('\033[1m' + '\tNot found' + '\033[0m', end = "\r")
                        print("\n\nPassword not found among most used passwords in data breaches")
                        time.sleep(1)
                        input("Press <ENTER> to continue...")
        except KeyboardInterrupt:
            print("\nExiting...")
            time.sleep(1)

def entropy(P, password):
    L = len(password)
    entropy = math.log2(math.pow(P,L))
    print(f"\nPassword entropy is: " + '\033[1m' + f"{entropy:.2f} bits" + '\033[0m')
    time.sleep(2)

def dicewareEntropy():
    P = 7776
    L = 5
    entropy = math.log2(math.pow(P,L))
    print(f"\n\t• entropy: " + '\033[1m' + f"{entropy:.2f} bits" + '\033[0m')
    

def dicewareCharacterLength(passphrase):
    print(f"\t• length: " + '\033[1m' + f"{len(passphrase)} characters" + '\033[0m')


def get(password):
    P = 0
    ranges = []
    with open("assets/range_characters.txt", "r") as file_obj:
        characters = file_obj.readlines()
        for line in characters:
            line = line.replace("\n", "")
            for character in password:
                if character in line:
                    if line not in ranges:
                        ranges.append(line)
    for line in ranges:
        P += len(line)
    entropy(P, password)
    dicewareCharacterLength(password)
