# PyOS Libraries
from installer import *
from file import *
# Other
import hashlib
instm = -1
version = [
    [1,0,2], # Internal Version
    "", # IV String
    "Build 2", # Shown Version
    True # Beta Tag
]
version[1] = str(version[0])
for x_ in range(1, len(version[0])):
    version[1] += f".{str(x_)}"

def parse(commandi):
    out = []
    tmp = ""
    i = 0
    if commandi == "":
        return [""]
    for x in commandi:
        if x == " " or i >= len(commandi)-1:
            tmp += x
            out.append(tmp)
            tmp = ""
        else:
            tmp += x
        i += 1
    return out

def run_command(command):
    parsedcmd = parse(command)
    instm = int(fread("INSM.OS", "-1"))
    if instm == -1 and parsedcmd[0] == "install":
        install()
        instm = 1
    elif parsedcmd[0] == "exit":
        exit()
    elif instm > -1 and parsedcmd[0] == "help":
        if instm == 0:
            print("help\nver\nexit")
        else:
            print("help\nver\nexit")
    elif instm > -1 and parsedcmd[0] == "ver":
        if instm == 0:
            print(f"PyShell {version[2]} ({version[1]})\nUsername: {fread("USER.OS")}\nFailed to verify.")
        else:
            print(f"PyShell {version[2]} ({version[1]})\nUsername: {fread("USER.OS")}\nVerification String: {fread("INST.OS")}")
    else:
        print(f"Command '{parsedcmd[0]}' not found!")

if fread("INST.OS", "no") != "no":
    if hashmd5(fread("USER.OS")) == fread("INST.OS"):
        fwrite("INSM.OS", "1")
    else:
        fwrite("INSM.OS", "0")
else:
    fwrite("INSM.OS", "-1")
if int(fread("INSM.OS", "-1")) == -1:
    print("Please install PyShell by using the 'install' command.")
elif int(fread("INSM.OS", "-1")) == 0:
    print("PyShell failed to verify you installed this software correctly.\nSome features may be limited or disabled.")
else:
    print(f"Welcome, {fread("USER.OS")}, to PyShell.")
while True:
    run_command(input("> "))