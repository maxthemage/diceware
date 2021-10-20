#!/usr/bin/python3

import csv, os, time, math

def checkBreach(password):
    path = "assets/password-breach-data/"
    with open(path + (os.listdir(path)[0])) as csv_object:
        password_data = csv.reader(csv_object)
        try:
            for row in password_data:
                print(password+" = "+str(row[0]))
                time.sleep(0.01)
                if password.lower()==str(row[0]) or password.title()==str(row[0]) or password.upper()==str(row[0]):
                    #print(True)
                    print("\nOops! This password or a similar password was found in a data breach.")
                    time.sleep(2)
                    input("Press <ENTER> to continue...")
                    break
        except:
            print("\nExiting...")

def entropy(P, password):
    L = len(password)
    entropy = math.log2(math.pow(P,L))
    print(f"Password entropy is: {entropy:.2f} bits")
    time.sleep(2)


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
        

#os.system("clear")
#password = input("Enter a password to check: ").strip()
#get(password)
