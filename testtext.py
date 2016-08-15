#!/usr/bin/env python2.3

import wx
# from wxPython.wx  import *
# from   wxPython.html  import *

#-------------------------------------------------------------------

class MyPanel(wx.Panel):   

    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)

        sty = wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_DONTWRAP | wx.HSCROLL
        self.tc = wx.TextCtrl(self, -1, '', (8, 8), wx.Size(300, 200), sty)
        attrib1 = wx.TextAttr('RED', 'WHITE', wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))
        attrib2 = wx.TextAttr('BLACK', 'WHITE', wx.Font(12, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        attrib3 = wx.TextAttr('BLACK', 'WHITE', wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.tc.SetDefaultStyle(attrib1)
        self.tc.AppendText("This is a line of text\n")
        self.tc.AppendText("This is another line of text\n")
        self.tc.SetDefaultStyle(attrib2)
        self.tc.AppendText("This is a third line of text\n")
        self.tc.SetDefaultStyle(attrib3)
        self.tc.AppendText("This is a fourth line of text\n")

        self.Html = wx.HTMLDataObject(self, -1 , (8, 220), wx.Size(300, 200),wx.NO_FULL_REPAINT_ON_RESIZE )
        text = """
        <html><body><tt>
        <pre>
This is a line of text<br>
This is another line of text<br>
This is a third line of text<br>
This is a fourth line of text<br>
123  456  56  3432<br>
 34   32 123    34<br>
         </pre>
        </tt>
        </body></html>"""
        self.Html.SetPage(text)
        
#-------------------------------------------------------------------

class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        title = 'atextctrl'
        style = wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX
        wx.Frame.__init__(self, parent, id, title, wx.Point(0, 0),
                            wx.Size(350, 500), style)
        self.panel = MyPanel(self, -1)

#-------------------------------------------------------------------

class MyApp(wx.App):

    def OnInit(self):
        frame = MyFrame(None, -1)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

#-------------------------------------------------------------------

def main():
    app = MyApp(0)
    app.MainLoop()

#-------------------------------------------------------------------

if __name__ == "__main__" :
    main()

#eof-------------------------------------------------------------------
