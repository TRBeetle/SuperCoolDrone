## Color Tracking v1.0
## Copyright (c) 2013-2014 Abid K and Jay Edry
## You may use, redistribute and/or modify this program it under the terms of the MIT license (https://github.com/abidrahmank/MyRoughWork/blob/master/license.txt).


''' v 0.1 - It tracks two objects of blue and yellow color each '''

import cv2
import numpy as np

def getthresholdedimg(hsv):
    #yellow = cv2.inRange(hsv,np.array((20,100,100)),np.array((30,255,255)))
    blue = cv2.inRange(hsv,np.array((100,100,100)),np.array((255,255,255)))
    #both = cv2.add(yellow,blue)
    return blue

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
	print f[360][240]
	cv2.circle(f,lcenter,3,(0,255,0),2)
    for cnt in contours:
		(x,y),radius = cv2.minEnclosingCircle(cnt)
        #cx,cy = x+w/2, y+h/2
		lcenter = (int(360),int(240))
		center = (int(x),int(y))
		print f[360][240]
		radius = int(radius)
		cv2.circle(f,lcenter,3,(0,255,0),2)
		#print "blue(x, y, radius) :", y,x, radius
    #    if 20 < hsv.item(cy,cx,0) < 30:
    #        cv2.rectangle(f,(x,y),(x+w,y+h),[0,255,255],2)
    #        print "yellow :", y,x,w,h
    #    elif 100 < hsv.item(cy,cx,0) < 120:
    #        cv2.rectangle(f,(x,y),(x+w,y+h),[255,0,0],2)
            #print "blue :", x,y,w,h

    cv2.imshow('img',f)

    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
c.release()