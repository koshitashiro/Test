import subprocess as sproc
import time
import win32gui
import pygetwindow as pgw
#import pyautogui as pag

def getPoint():
    
    memo = pgw.getWindowsWithTitle("メモ帳")[0]
    if memo.activate() == False:
        sproc.Popen(r"\WINDOWS\system32\notepad.exe")
    top, left = memo.topleft
    #for elm in lst:
    #   print(elm.title)