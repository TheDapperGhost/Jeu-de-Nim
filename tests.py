import os

def clear():
    os.system("cls" if os.name in ("nt", "dos") else "clear")

print("heyhey bruh")
clear()