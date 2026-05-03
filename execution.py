import threading 
import queue
import time
from detection import Detector
from commands import GestureMouse

cmd= queue.Queue()

def CamDetector():
    try:
        det=Detector(cmd)
        det.Start()
    except:
        print("error\n")

def Commander():
    prevX=0
    prevY=0
    Factor=6
    resync_frames = 0
    mouse=GestureMouse()
    while True:
        inst= cmd.get()

        if inst[0]=="KILL":
            mouse.kill()
            break

        if inst[0] == "MOVE":
            x, y = inst[1]

            if resync_frames > 0:
                prevX, prevY = x, y
                resync_frames -= 1
                continue        

            dx = int((x - prevX) * Factor)
            dy = int((y - prevY) * Factor)

            mouse.movePointer(dx, dy, 8, 0.01)
            prevX, prevY = x, y
        
        if inst[0]=="CLICK":
            mouse.click()

        if inst[0]=="RELEASE":
            mouse.release()
        
        if inst[0]=="BREAK":
            resync_frames = 4

thread1=threading.Thread(target=CamDetector)
thread2=threading.Thread(target=Commander)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("program ender\n")