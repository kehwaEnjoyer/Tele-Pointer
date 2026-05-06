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
        self.cStatus=False

    def movePointer(self, Xchange=0, Ychange=0, sen=5, delay=0.01):
        if abs(Xchange)>sen:
            self.ui.write(e.EV_REL, e.REL_X, Xchange)
        if abs(Ychange)>sen:
            self.ui.write(e.EV_REL, e.REL_Y, Ychange)
        self.ui.syn()
        time.sleep(delay)

    def click(self):
        if not self.cStatus:
            self.ui.write(e.EV_KEY, e.BTN_LEFT, 1) # Press
            self.ui.syn()
            self.cStatus=True
            time.sleep(0.1) 
       
    def release(self):
        if self.cStatus:
            self.ui.write(e.EV_KEY, e.BTN_LEFT, 0) # Release
            self.ui.syn()
            self.cStatus=False
            time.sleep(0.1) 

    def scroll(self,Ychange,delay=0.01):
        self.ui.write(e.EV_REL,e.REL_WHEEL,Ychange)
        self.ui.syn()
        time.sleep(delay)

    def kill(self):
        self.ui.close()

