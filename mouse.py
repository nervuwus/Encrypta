from win32api import GetCursorPos
from time import sleep
from hashlib import sha256

with open("position.txt", "x", encoding="utf-8"):

    iterNum = int(input("how many iteration you want ?: ")) #300 or more recommended
    i = 0

    print("move randomly and quickly as possible your mouse !")
    sleep(3)

    while i != iterNum:
        x, y = GetCursorPos()
        print({"x :", x, "y :", y})
        with open("position.txt", "a") as f:
            f.write(str(x)+str(y))
            i += 1
    file = open("position.txt")
    encryption = sha256(file.read().encode("utf-8")).hexdigest()
    print(encryption)