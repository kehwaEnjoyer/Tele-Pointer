from threading import Lock
from queue import Queue

class Pipe:
    def __init__(self):
        self.LatestPos=None
        self.lock=Lock()

        self.EQueue= Queue()
    
    

