#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import sys

print('\033[93m'+"""
#######################################
#               iMd5Crack             #
#   github.com/ihsansencan/iMd5Crack  #
#             @IhsanSencan            #
#######################################
"""+'\x1b[0m')

while True:
    p_hash = input("MD5 Hash : ")
    if not len(p_hash) == 32 :
        print("\033[91m\033[1mMd5 is wrong, again check it out.\x1b[0m")
        continue
    else:
        break

wlist = input("Wordlist (Default: /usr/share/wordlists/rockyou.txt)\nENTER to select a default file.\nor New File: ")
if len(wlist) == 0 :
    wlist = "/usr/share/wordlists/rockyou.txt"
try:
    pf = open(wlist, 'r')
except FileNotFoundError:
    print("\033[91m\033[1mFile not found.\x1b[0m")
    quit()

def mainMd5():
    count =0

    with open(wlist, "r", encoding="latin-1") as f:
        print(f"In total\033[91m\033[1m",f.read().count("\n"),"\033[0mtrying will be done.")
        print(25*"*")

    for w in pf:
        encoded_w = w.encode('utf-8')
        d = hashlib.md5(encoded_w.strip()).hexdigest()
        sys.stdout.write("Trying: "+str(count)+"\r")
        sys.stdout.flush()
        count+=1

        if d == p_hash:
            print(f"[Pass Line:{count}] Password Found:{p_hash}:\033[32m{w}\x1b[0m")
            break
    else:
        print("\033[91m\033[1mPassword not found.\x1b[0m")
mainMd5()