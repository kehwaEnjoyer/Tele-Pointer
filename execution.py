import threading 
import time
from detection import Detector
from commands import GestureMouse
from pipeline import Pipe

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
    Factor=6
    br=False
    bg=True
    mouse=GestureMouse()
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

            elif event[0]=="SCROLL":
                if event[1]=="START":
                    sc=True
                elif event[1]=="END":
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
            bg=False
            continue        
        #add scroll exception here :)
        dx = int((x - prevX) * Factor)
        dy = int((y - prevY) * Factor)

        mouse.movePointer(dx, dy, 8, 0.01)
        prevX, prevY = x, y

thread1=threading.Thread(target=CamDetector)
thread2=threading.Thread(target=Commander)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("program ender\n")