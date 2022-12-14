# Created on Windows using Python3.
    # required WxPython: py -m pip install wxPython
    # AWS SDK for Python (boto3): py -m pip install boto3
    
    
    ######## NOTES #########
"""
    Current command to get JSON data 
    aws ec2 describe-instances --profile sl --query Reservations[*].Instances[*]
    
    Additional filtering to list InstanceIds
    aws ec2 describe-instances --profile sl --filters 'Name=tag:Name,Values=*' --output json  --query Reservations[*].Instances[*].InstanceId
    
    # Show private IP, InstanceId and Name(tag)
    #aws ec2 describe-instances --profile sl --query 'Reservations[*].Instances[*].[InstanceId, PrivateIpAddress, Tags[?Key==`Name`].Value | [0]]' --output text
"""
    
    #######################

from urllib import response
from warnings import filters
import wx
import subprocess, sys
import boto3
import jmespath
import awscli

# If default profile is not specified in ~\.aws\credentials, your preferred profile will need to be entered here.
boto3.setup_default_session(profile_name='sl')

class HelloFrame(wx.Frame):

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
       result = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', r'.\\ps-scripts\\pstest.ps1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
       #print(type(result.stdout.decode('utf-8')))
       
       
       

       #p = subprocess.Popen(["powershell.exe", ".\\ps-scripts\\pstest.ps1"], stdout=sys.stdout)
       #print(type(p))
       #q = p.communicate()
       #print(q)
       
       # ec2 = boto3.client('ec2')
       #response = ec2.describe_instances(
       #    Filters=[{
       #        'Name': 'tag:owner',
       #         'Values': ['syoungs']
       #    }]
       #)
       
       #print(response)
       #print(type(response))

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Script Launcher TESTING')
    frm.Center()
    frm.Show()
    app.MainLoop()