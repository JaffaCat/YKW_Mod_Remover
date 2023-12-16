"""
A Yo-kai Watch cleanup tool.
"""


import os
import json


def readRemoverSettings():
    with open("Config.json", "r") as ConfigJSON:
        data = json.load(ConfigJSON)
        Citra_Path = data["citra_path"]
        USA_Title = data["USA_Title"]
        EU_Title = data["EU_Title"]
        USA_Save = data["USA_Save"]
        EU_Save = data["EU_Save"]
    return Citra_Path, USA_Title, EU_Title, USA_Save, EU_Save


def removeMod(User, Citra_Path, EU_Title, USA_Title, USA_Save, EU_Save):
    Mods_Path = User + Citra_Path + "/load/mods/"
    EU_Mod = User + Citra_Path + "/load/mods/" + EU_Title + "/romfs/yw1_a.fa"
    USA_Mod = User + Citra_Path + "/load/mods/" + USA_Title + "/romfs/yw1_a.fa"
    EsaveFile = User + Citra_Path + EU_Save
    UsaveFile = User + Citra_Path + USA_Save

    for file in os.listdir(Mods_Path):
        if os.path.join(USA_Title):
            os.remove(USA_Mod)
            os.remove(UsaveFile)



def main():
    User = os.environ["USERPROFILE"]
    Citra_Path, USA_Title, EU_Title, USA_Save, EU_Save = readRemoverSettings()
    try:
        removeMod(User, Citra_Path, EU_Title, USA_Title, USA_Save, EU_Save)
    except Exception as err:
        print(err)

main()
