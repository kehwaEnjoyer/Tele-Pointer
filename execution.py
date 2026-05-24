import threading 
import time
from detection import Detector
from commands import GestureMouse
from pipeline import Pipe
from optimizations import optimizer

CState= Pipe()

def CamDetector():
    try:
        det=Detector(CState)
        det.Start()
    except:
        print("error\n")

def Commander():
    prevX=0
    prevY=0
    Factor=8
    scrollSen=6
    br=False
    bg=True
    sc=False
    mouse=GestureMouse()
    #loading optimizer object
    opt=optimizer()
    while True:
        time.sleep(0.01) #cpu Throttle
        try:
            event = CState.EQueue.get_nowait()
        except:
            event = None

        if event:
            if event[0]=="KILL":
                mouse.kill()
                break

            elif event[0]=="CLICK":
                mouse.click()

            elif event[0]=="RELEASE":
                mouse.release()
            
            elif event[0]=="BREAK":
                br = True

            elif event[0]=="BEGIN":
                br=False
                bg=True

            elif event[0]=="SCROLLSTART":
                sc=True

            elif event[0]=="SCROLLEND":
                sc=False

        if br:
            continue

        with CState.lock:
            pos = CState.LatestPos

        if pos is None:
            print("None\n")
            continue

        x, y = pos
        if bg:
            prevX, prevY = x, y
            opt.setPrevPos(x,y)
            bg=False
            continue        

        x,y=opt.prvMean(x,y)
        dx = int((x - prevX) * Factor)
        dy = int((y - prevY) * Factor)

        if not sc:
            mouse.movePointer(dx, dy, 8, 0.01)

        if sc:
            mouse.scroll(int(dy/scrollSen))

        prevX, prevY = x, y

thread1=threading.Thread(target=CamDetector)
thread2=threading.Thread(target=Commander)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("program ender\n")