#!/usr/bin/env python2.3

"""
This version is double buffered
"""

import wx
import time

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "DrawLines Test",
                         wx.DefaultPosition,
                         size=(500,500),
                         style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)

        ## Set up the MenuBar
        MenuBar = wx.MenuBar()
        
        file_menu = wx.Menu()

        ID_CLEAR_MENU = wx.NewId()
        file_menu.Append(ID_CLEAR_MENU, "&Clear","Clear the Screen")
        wx.EVT_MENU(self, ID_CLEAR_MENU, self.Clear)

        ID_ANIMATE_MENU = wx.NewId()
        file_menu.Append(ID_ANIMATE_MENU, "&Animate","Animate the Screen")
        wx.EVT_MENU(self, ID_ANIMATE_MENU, self.Animate)

        ID_EXIT_MENU = wx.NewId()
        file_menu.Append(ID_EXIT_MENU, "E&xit","Terminate the program")
        wx.EVT_MENU(self, ID_EXIT_MENU, self.OnQuit)

        MenuBar.Append(file_menu, "&File")
        self.SetMenuBar(MenuBar)

        wx.EVT_PAINT(self, self.OnPaint)
        wx.EVT_MOTION(self, self.OnMouseMove )
        wx.EVT_LEFT_DOWN(self, self.OnLeftDown )
        wx.EVT_SIZE(self, self.OnSize)

        self.LineData = []
        self.OnSize(None)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self._Buffer,(0,0))

    def OnSize(self,event):
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        Size  = self.GetClientSizeTuple()
        self._Buffer = wx.EmptyBitmap(Size[0],Size[1])
        self.Draw()
        
    def Draw(self):
        dc = wx.MemoryDC()
        dc.SelectObject(self._Buffer)
        dc.SetBackground( wx.Brush("Purple") )
        dc.Clear()
        dc.SetPen(wx.Pen("Red", 3))
        for Line in self.LineData:
            dc.DrawLines(Line)
        self.Refresh()

    def Clear(self, event = None):
        self.LineData = []
        self.Draw()

    def OnLeftDown(self,event):
        xy = event.GetPosition()
        self.LineData.append( [xy] )

    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            xy = event.GetPosition()
            self.LineData[-1].append(xy)
            dc = wx.MemoryDC()
            dc.SelectObject(self._Buffer)
            dc.SetPen(wx.Pen("Red", 3))
            dc.DrawLine(self.LineData[-1][-2],self.LineData[-1][-1])
            self.Refresh()

    def Animate(self, event):
        self.Refresh()
        self.LineData.append( [(0,0)] )
        dc = wx.MemoryDC()
        dc.SelectObject(self._Buffer)
        dc.SetPen(wx.Pen("Red", 3))
        for i in xrange(10,500,5):
            self.LineData[-1].append((i,i))
            dc.DrawLine(self.LineData[-1][-2],self.LineData[-1][-1])
            self.Refresh()
            self.Update()
            time.sleep(0.01)

    def OnQuit(self,event):
        self.Close(True)

class DemoApp(wx.App):
    def OnInit(self):
        frame = TestFrame()
        frame.Show(True)
        self.SetTopWindow(frame)

        return True

if __name__ == "__main__":
    app = DemoApp(0)
    app.MainLoop()



















