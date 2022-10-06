#!/usr/bin/env python
import wx
import os

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        self.itens = []
        self.itemId = 0

        frame = wx.Frame.__init__(self, parent, title=title, size=(480,480))
        self.panel = wx.Panel(self, wx.ID_ANY)
        btnOk = wx.Button(self.panel, wx.ID_ANY, 'OK')
        btnCancel = wx.Button(self.panel, wx.ID_ANY, 'Cancelar')
        self.listCtrl = wx.ListCtrl(self.panel, id=wx.ID_ANY, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER)

        #Bind Events
        self.Bind(wx.EVT_BUTTON, self.btnCancelOnPress, btnCancel)
        self.Bind(wx.EVT_BUTTON, self.btnOkOnPress, btnOk)
        self.listCtrl.Bind(wx.EVT_KEY_DOWN, self.listCtrlOnKeyDown)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.listCtrl, 1, wx.EXPAND | wx.ALL,0)
        box.AddSpacer(10)

        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box2.Add(btnOk,0, wx.RIGHT)
        box2.AddSpacer(4)
        box2.Add(btnCancel,0, wx.RIGHT)
        box.Add(box2, 0, wx.ALIGN_RIGHT | wx.ALL)
        box.AddSpacer(8)

        self.listCtrl.AppendColumn('Levels', width=self.listCtrl.GetSize().GetWidth())
        itens = self.itens
        itens.append(GameDef(id = 0, str = "Quake - First Episodes", dir = "id1"))
        itens.append(GameDef(id = 1, str = "Scourge of Armagon", dir = "hipnotic"))
        itens.append(GameDef(id = 2, str = "Dissolution of Eternity", dir = "rogue"))
        itens.append(GameDef(id = 3, str = "Dimension of the Pastn", dir = "dopa"))
        itens.append(GameDef(id = 4, str = "Dimension of the Machine", dir = "mg1"))
        itens.append(GameDef(id = 5, str = "Arcane Dimensions", dir = "ad"))

        for i in range(len(itens)):
            self.listCtrl.InsertItem(itens[i].GetItem())
            print(itens[i].GetItem().GetText())
        self.listCtrl.Select(0)

        self.panel.SetSizer(box)
        #box.SetSizeHints(self)
        self.Show(True)

    def btnCancelOnPress(self, event):
        self.Close()

    def btnOkOnPress(self, event):
        self.lauchGame()

    def listCtrlOnKeyDown(self, event):
        event.DoAllowNextEvent()
        if (event.GetKeyCode() == 13):
            self.lauchGame()
        else:
            event.Skip()

    def lauchGame(self):
        item = self.itens[self.listCtrl.GetFocusedItem()]
        os.popen("./vkquake -game " + item.GetGameDir())
        self.listCtrl.SetFocus()




class GameDef():
    def GetItem(self):
        return self._item

    def SetItem(self, item):
        self._item = item

    def GetGameDir(self):
        return self._gameDir

    def SetGameDir(self, gameDir):
        self._gameDir = gameDir

    def __init__(self, item, gameDir):
        self._item = item
        self._gameDir = gameDir
        _item.SetId(0)
        _item.SetText("")

    def __init__ (self, id, str, dir):
        self._item = wx.ListItem()
        self._item.SetId(id)
        self._item.SetText(str)
        self._gameDir = dir


app = wx.App(False)
frame = MyFrame(None, 'Quake Launcher')
app.MainLoop()
