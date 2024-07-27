from file import *
import hashlib

def install():
    fwrite("USER.OS", input("User: "))
    fwrite("INST.OS", hashlib.md5(fread("USER.OS")).hexdigest())