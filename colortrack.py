''' v 0.1 - It tracks two objects of blue and yellow color each '''

import cv2
import numpy as np
def getthresholdedimg(hsv):
    #2/22/14 Musti
    orange = cv2.inRange(hsv,np.array((10,50,50)),np.array((15,255,255)))
    #red = cv2.inRange(hsv,np.array((0,0,255)),np.array((255,102,102)))
    #yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((30,255,255)))

    #blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((120,255,255)))
    #both = cv2.add(yellow,blue)
    return orange

c = cv2.VideoCapture(0)
width,height = c.get(3),c.get(4)
print "frame width and height : ", width, height

while(1):
    _,f = c.read()
    f = cv2.flip(f,1)
    blur = cv2.medianBlur(f,5)
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    both = getthresholdedimg(hsv)
    erode = cv2.erode(both,None,iterations = 3)
    dilate = cv2.dilate(erode,None,iterations = 10)

    contours,hierarchy = cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        radius = int(radius)
        if(radius > 350):
            circle = cv2.circle(f,center,radius,(0,255,0),2)
            print "orange(x, y, radius) :", y,(640-x), radius
    cv2.imshow('img',f) #opens camera

    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
c.release()
