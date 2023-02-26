import GetWindowPoint
import OpenApplication
import pygetwindow as gw



def main():
    
    w = None
    for t in gw.getAllTitles():
        if 'Foo Bar' in t:
            w = gw.getWindowsWithTitle(t)[0]
            break
    
    # bug workaround
    w.minimize()
    w.maximize()
    #OpenApplication.OpenApplication()
    #GetWindowPoint.getPoint()
    

if __name__ == '__main__':
    main()