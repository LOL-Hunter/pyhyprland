import os, sys
from pysettings.jsonConfig import JsonConfig
from subprocess import check_output

class Hyprland:
    def __init__(self):
        pass
    @staticmethod
    def getClients():
        out = check_output(["hyprctl", "clients", "-j"])
        out = out.decode()
        js = JsonConfig.fromString(out)
        for cl in js:
            yield {"id":cl["workspace"]["id"], "class":cl["class"]}
    @staticmethod
    def jumpToWorkspaceByClass(clazz:str):
        if type(clazz) is str: clazz = [clazz]
        for cl in Hyprland.getClients():
            if cl["class"] in clazz:
                Hyprland.goToWorkSpaceId(cl["id"])
                return
    @staticmethod
    def goToWorkSpaceId(id):
        os.system("hyprctl dispatch workspace "+str(id))












if __name__ == '__main__':
    Hyprland.jumpToWorkspaceByClass("kitty")