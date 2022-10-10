import wx

class GameDef():
    def GetItem(self):
        return self._item

    def SetItem(self, item):
        self._item = item

    def GetGameDir(self):
        return self._gameDir

    def SetGameDir(self, gameDir):
        self._gameDir = gameDir

    def GetExec(self):
        return self._exec

    def SetExec(self, exec):
        self._exec = exec

    def __init__(self, item, gameDir):
        self._item = item
        self._gameDir = gameDir
        _item.SetId(0)
        _item.SetText("")

    def __init__ (self, id, str, dir, exec = './vkquake'):
        self._item = wx.ListItem()
        self._item.SetId(id)
        self._item.SetText(str)
        self._gameDir = dir
        self._exec = exec
