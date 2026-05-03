

class optimizer:
    def __init__(self):
        self.prevX=0
        self.prevY=0
        pass


    def noOPT(self, x , y):
        return (x,y)

    def prvMean(self ,x,y):
        mX=int((self.prevX+x)/2)
        mY=int((self.prevY+y)/2)
        self.prevX,self.prevY=mX,mY
        return (mX,mY)

