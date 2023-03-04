import win32com.client
import subprocess as sproc
import os

#exeAplicationsファイル内のショートカットをすべて実行させる
def OpenApplication():
    Lst = makeAppList()
    
    for app in Lst:
        sproc.Popen(app, shell = True)
        
    return
    

#実行ファイルのパスリストを作成する
def makeAppList():
    path  = os.getcwd() + "\\exeAplications"
    Lst   = os.listdir(path)
    apLst = []
    
    for f in Lst:
        if chkShortCut(f) == True:
            exepath = getExePath(path + "\\" + f)
            apLst.append(exepath)
            Eprint(exepath)
    
    return apLst

#ショートカットであることを確認する
def chkShortCut(fname):
    flist = fname.split(".")
    
    if flist[len(flist)- 1] == "lnk" or flist[len(flist) - 1] == "url":
        return True
    else:
        return False
    
#実行ファイルのリンク先パスを取得する
def getExePath(fullpath):
    wshell = win32com.client.Dispatch('WScript.Shell')
    shortcut = wshell.CreateShortcut(fullpath)   
    return shortcut.TargetPath