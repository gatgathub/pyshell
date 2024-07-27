def fread(fil, empty=""):
    try:
        with open(fil, "r") as file_:
            out = file_.read()
            file_.close()
    except Exception:
        out = empty
    return out

def fwrite(fil, cont):
    with open(fil, "w") as file_:
        file_.write(cont)
        file_.close()

def fappend(fil, cont):
    with open(fil, "a") as file_:
        file_.write(cont)
        file_.close()