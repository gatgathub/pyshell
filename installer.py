from file import *
import hashlib

def hashmd5(inp):
    h = hashlib.new("md5")
    h.update(inp.encode())
    return h.hexdigest()

def install():
    fwrite("USER.OS", input("User: "))
    fwrite("INST.OS", hashmd5(fread("USER.OS")))
    fwrite("INSM.OS", "1")
    fwrite("OGOS.OS", hashmd5(fread("main.py"))
