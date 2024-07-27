# PyOS Libraries
from commands import *
from installer import *
from file import *
# Other
import hashlib

version = [
    [0,0,1], # Internal Version
    "0.0.1", # Shown Version
    True # Beta Tag
]

def parse(command):
    out = []
    tmp = ""
    i = 0
    for x in command:
        if x == " " or i == len(command)-1:
            out.append(tmp)
        else:
            tmp += x
        i += 1
    return out

def run_command(command):
    parsedcmd = parse(command)
    if instm == -1:
        if parsedcmd[0] == "install":
            install()
    else:
        print(f"Command {parsedcmd[0]} not found!")

if fread("INST.OS", "no") != "no":
    if hashlib.md5(fread("USER.OS")).hexdigest():
        instm = 1
    else:
        instm = 0
else:
    instm = -1