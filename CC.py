import webbrowser
import pyHook
import pythoncom
import sys
import win32api
import win32con
import time
import threading

def click(mouse):
    win32api.SetCursorPos(mouse)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,mouse[0],mouse[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,mouse[0],mouse[1],0,0)

def start(event):
    print "Starting"
    mousePos = event.Position
    print "Got Mouse position, beginning loop"
    mainThread = threading.Thread(target=loopClick, args=(mousePos,))
    mainThread.daemon = True
    mainThread.start()

def stop(event):
    if (event.KeyID == 27):
        hm.UnhookMouse()
        hm.UnhookKeyboard()
        sys.exit("You quit")

def checkStop():
    time.sleep(1)

def loopClick(mouse):
    while(True):
        click(mouse)

cookieClickerURL = "http://orteil.dashnet.org/cookieclicker/"
mousePos = (0,0)

webbrowser.open(cookieClickerURL)

print "Initializing Hook Manager"
hm = pyHook.HookManager()
print "HM initialized"
print "Subscribing keydown to stop"
hm.KeyDown = stop
print "keydown subscribed"
print "Subscribing Mouse buttons to start"
hm.MouseAllButtons = start
print "Mouse subscribed!"
print "Hooking Mouse"
hm.HookMouse()
print "Mouse Hooked"
print "Hooking Keyboard"
hm.HookKeyboard()
print "Keyboard Hooked"
pythoncom.PumpMessages()

    
