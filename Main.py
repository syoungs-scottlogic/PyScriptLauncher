import wx
import subprocess

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)


        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        pnl.SetSizer(sizer)
        
        self.button1 = wx.Button(pnl, wx.ID_ANY, 'button', (8,72), (75, 23))
        self.button1.Bind(wx.EVT_BUTTON, self.OnClicked)


        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Additional info will be logged here.")


    def OnClicked(self, event):
       # Run PowerShell script to get EC2 instances. 
       result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', r'C:\wxlib\pstest.ps1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
       print(result.stdout.decode('utf-8'))
       

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Script Launcher TESTING')
    frm.Center()
    frm.Show()
    app.MainLoop()