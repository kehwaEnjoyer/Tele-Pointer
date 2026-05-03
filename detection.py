import cv2
import mediapipe as mp
import sys
from optimizations import optimizer

class Detector:
    def __init__(self,cmd):
        self.cmd=cmd
        #camera 
        self.src = 0
        if len(sys.argv) > 1:
            self.src = sys.argv[1]
        self.source = cv2.VideoCapture(self.src)
        #camera preview
        self.win_name = 'Preview'

        #loading mediapipe model for inferencing 
        self.MPhands=mp.solutions.hands
        self.MPdraw=mp.solutions.drawing_utils
        self.hands=self.MPhands.Hands(static_image_mode=False,max_num_hands=2)


    #finger detection logic stored in a array with a binary representation
    def fingersUp(self,hand,handType):
        fingers=[]
        if handType=="Right":
            if hand.landmark[4].x<hand.landmark[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if hand.landmark[4].x>hand.landmark[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

        for tip,base in zip([8,12,16,20],[5,9,13,17]):
            if hand.landmark[tip].y< hand.landmark[base].y:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def RightPresent(self,hands):
        for handMarks, handType in zip(hands.multi_hand_landmarks,hands.multi_handedness):
                if handType.classification[0].label == "Right":
                    return True
        return False

    def LeftPointPresent(self,hands):
        for handMarks, handType in zip(hands.multi_hand_landmarks,hands.multi_handedness):
                if handType.classification[0].label == "Left" and self.fingersUp(handMarks,handType)==[0,1,0,0,0]:
                    return True
        return False

    def ToPixel(self,landmark, frame):
        height, width, _ = frame.shape

        x_pixel = int(landmark.x * width)
        y_pixel = int(landmark.y * height)

        return x_pixel, y_pixel

    def isContact(self, Tx, Ty, Fx, Fy, Bhold):
        if abs(Tx - Fx) <= Bhold and abs(Ty - Fy) <= Bhold:
            print("CONTACT\n")
            return True
        return False

    def Start(self):
        #loading optimizer object
        opt=optimizer()
        cv2.namedWindow(self.win_name, cv2.WINDOW_NORMAL)
        cStatus=False

        while cv2.waitKey(1) !=27: #27=esc key
            #reading and checking frame
            framePresent, frame = self.source.read()
            if not framePresent:
                break

            #fliping and correcting color format for model
            frame=cv2.flip(frame,1)
            rgbFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            #inferencing the model
            result=self.hands.process(rgbFrame)

            if result.multi_hand_landmarks and result.multi_handedness:
                #run only when left hand is detected point up
                if self.LeftPointPresent(result) and self.RightPresent(result):
                    for handMarks, handType in zip(result.multi_hand_landmarks,result.multi_handedness):
                        self.MPdraw.draw_landmarks(frame,handMarks,self.MPhands.HAND_CONNECTIONS)
                        if handType.classification[0].label=="Right":
                            print("sending ",(handMarks.landmark[9].x,handMarks.landmark[9].y))
                            x,y=self.ToPixel(handMarks.landmark[9],frame)
                            self.cmd.put(("MOVE",opt.prvMean(x,y)))
                            fx,fy=self.ToPixel(handMarks.landmark[8],frame)
                            tx,ty=self.ToPixel(handMarks.landmark[4],frame)
                            cv2.rectangle(frame,(fx+20,fy-20),(fx-20,fy+20), (255, 0, 0), 3)
                            if self.isContact(tx,ty,fx,fy,20) and not cStatus:
                                self.cmd.put((("CLICK"),None))
                                cStatus=True
                            elif not self.isContact(tx,ty,fx,fy,20) and cStatus:
                                self.cmd.put((("RELEASE"),None))
                                cStatus=False
                else:
                    self.cmd.put(("BREAK",None))
                    print("sent break\n")           

            cv2.imshow(self.win_name,frame)
        self.cmd.put(("KILL",None))
        self.kill()
        return


    def kill():
        #mouse.kill()
        self.source.release()
        cv2.destroyWindow(self.win_name)