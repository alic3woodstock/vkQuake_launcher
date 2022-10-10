#!/usr/bin/env python
import wx
import os
import csv
import gameDef

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        self.itens = []
        self.itemId = 0

        frame = wx.Frame.__init__(self, parent, title=title, size=(480,480))
        #self.Centre(wx.VERTICAL)
        self.panel = wx.Panel(self, wx.ID_ANY)
        btnOk = wx.Button(self.panel, wx.ID_ANY, 'OK')
        btnCancel = wx.Button(self.panel, wx.ID_ANY, 'Cancelar')
        self.listCtrl = wx.ListCtrl(self.panel, id=wx.ID_ANY, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER)

        #Bind Events
        self.Bind(wx.EVT_BUTTON, self.btnCancelOnPress, btnCancel)
        self.Bind(wx.EVT_BUTTON, self.btnOkOnPress, btnOk)
        self.listCtrl.Bind(wx.EVT_KEY_DOWN, self.listCtrlOnKeyDown)
        self.panel.Bind(wx.EVT_CHAR_HOOK, self.panelOnKeyHook)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(self.listCtrl, 1, wx.EXPAND | wx.ALL, border=4)
        box.AddSpacer(6)

        box2 = wx.BoxSizer(wx.HORIZONTAL)
        box2.Add(btnOk,0, wx.RIGHT)
        box2.AddSpacer(4)
        box2.Add(btnCancel,0, wx.RIGHT, border=4)
        box.Add(box2, 0, wx.ALIGN_RIGHT | wx.ALL)
        box.AddSpacer(8)

        if (not(os.path.exists('games.csv'))):
            self.writeDefaultCSV()


        self.listCtrl.AppendColumn('Levels', width=self.listCtrl.GetSize().GetWidth() - 4)
        self.readCSV(self.itens)

        for i in range(len(self.itens)):
            self.listCtrl.InsertItem(self.itens[i].GetItem())

        item = self.itens[self.listCtrl.GetFirstSelected()]
        self.listCtrl.Select(0)
        self.listCtrl.SetFocus()
        self.listCtrl.Focus(0)

        self.panel.SetSizer(box)
        box.SetSizeHints(self)
        self.Centre()
        self.Show(True)

    def btnCancelOnPress(self, event):
        self.Close()

    def btnOkOnPress(self, event):
        self.lauchGame()

    def listCtrlOnKeyDown(self, event):
        if (event.GetKeyCode() == 13):
            self.lauchGame()
        else:
            event.Skip()

    def panelOnKeyHook(self, event):
        event.DoAllowNextEvent()
        if (event.GetKeyCode() == 27):
            self.Close()
        event.Skip()

    def lauchGame(self):
        item = self.itens[self.listCtrl.GetFirstSelected()]
        os.popen(item.GetExec() + " -game " + item.GetGameDir())
        self.listCtrl.SetFocus()

    def writeDefaultCSV(self):
        with open ('games.csv', 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile, dialect = 'unix')
            if (os.name == "nt"):
                exec = ".\\vkquake.exe"
            else:
                exec = "./vkquake"
            writer.writerow(['id', 'Title', 'Directory', 'Executable'])
            writer.writerow([0, 'Quake - First Episodes','id1', exec])
            writer.writerow([1, 'Scourge of Armagon', 'hipnotic', exec])
            writer.writerow([2, 'Dissolution of Eternity', 'rogue', exec])
            writer.writerow([3, 'Dimension of the Pastn', 'dopa', exec])
            writer.writerow([4, 'Dimension of the Machine', 'mg1', exec])
            writer.writerow([5, 'Arcane Dimensions', 'ad', exec])

    def readCSV(self, itens):
        with open ('games.csv', newline = '') as csvfile:
            reader = csv.reader(csvfile, dialect='unix')
            i = 0
            for row in reader:
                if (i > 0):
                    itens.append(gameDef.GameDef(int(row[0]), row[1], row[2], row[3]))
                i += 1

app = wx.App(False)
frame = MyFrame(None, 'Quake Launcher')
app.MainLoop()
