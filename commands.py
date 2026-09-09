from evdev import UInput, ecodes as e
import time

class GestureMouse:
    def __init__(self):

        self.ui = UInput(
            {
                e.EV_REL: [e.REL_X, e.REL_Y, e.REL_WHEEL],
                e.EV_KEY: [e.BTN_LEFT,e.BTN_RIGHT],
            },
            name="GestureMouse"
        )
        self.LCStatus=False
        self.RCStatus=False

    def movePointer(self, Xchange=0, Ychange=0, sen=5, delay=0.01):
        if abs(Xchange)>sen:
            self.ui.write(e.EV_REL, e.REL_X, Xchange)
        if abs(Ychange)>sen:
            self.ui.write(e.EV_REL, e.REL_Y, Ychange)
        self.ui.syn()
        time.sleep(delay)

    def LeftClick(self):
        if not self.LCStatus:
            self.ui.write(e.EV_KEY, e.BTN_LEFT, 1) # Press
            self.ui.syn()
            self.LCStatus=True
            time.sleep(0.1) 
       
    def LeftRelease(self):
        if self.LCStatus:
            self.ui.write(e.EV_KEY, e.BTN_LEFT, 0) # Release
            self.ui.syn()
            self.LCStatus=False
            time.sleep(0.1) 

    def RightClick(self):
        if not self.RCStatus:
            self.ui.write(e.EV_KEY, e.BTN_RIGHT, 1) # Press
            self.ui.syn()
            self.RCStatus=True
            time.sleep(0.1) 
       
    def RightRelease(self):
        if self.RCStatus:
            self.ui.write(e.EV_KEY, e.BTN_RIGHT, 0) # Release
            self.ui.syn()
            self.RCStatus=False
            time.sleep(0.1) 

    def scroll(self,Ychange,delay=0.01):
        self.ui.write(e.EV_REL,e.REL_WHEEL,Ychange)
        self.ui.syn()
        time.sleep(delay)

    def kill(self):
        self.ui.close()

