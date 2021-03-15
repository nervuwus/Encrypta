from cx_Freeze import setup, Executable
import locale as loc
import json
import os.path

LocalNorm = loc.getdefaultlocale(0)

Path = "lang/"+LocalNorm[0]+".json"

if os.path.exists(Path):
    with open("lang/"+LocalNorm[0]+".json") as f:
        data = json.load(f)
        setup(
            name=data['name'],
            version="1.0",
            description=data['description'],
            executables=[Executable("mouse.py")]
        )
else:
    with open("lang/en_US.json") as f:
        data = json.load(f)
        setup(
            name=data['name'],
            version="1.0",
            description=data['description'],
            executables=[Executable("mouse.py")]
        )