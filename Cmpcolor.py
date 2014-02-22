# Raspbery Pi Color Tracking Project
# Code written by Oscar Liang
# 30 Jun 2013

import cv2.cv as cv
def ColorProcess(img):

    # returns thresholded image
    imgHSV = cv.CreateImage(cv.GetSize(img), 8, 3)

    # converts BGR image to HSV
    cv.CvtColor(img, imgHSV, cv.CV_BGR2HSV)
    imgProcessed = cv.CreateImage(cv.GetSize(img), 8, 1)

    # converts the pixel values lying within the range to 255 and stores it in the destination
    cv.InRangeS(imgHSV, (100, 94, 84), (109, 171, 143), imgProcessed)
    return imgProcessed

def main():

    # captured image size, change to whatever you want
    width = 320
    height = 240

    capture = cv.CreateCameraCapture(0)

    # Over-write default captured image size
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)
    cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height)

    cv.NamedWindow( "output", 1 )
    cv.NamedWindow( "processed", 1 )

    while True:

        frame = cv.QueryFrame(capture)
        cv.Smooth(frame, frame, cv.CV_BLUR, 3)

        imgColorProcessed = ColorProcess(frame)
        mat = cv.GetMat(imgColorProcessed)
		
		# Calculating the moments
        moments = cv.Moments(mat, 0)
        area = cv.GetCentralMoment(moments, 0, 0)
        moment10 = cv.GetSpatialMoment(moments, 1, 0)
        moment01 = cv.GetSpatialMoment(moments, 0,1)

        # Finding a big enough blob
        if(area > 60000):

            # Calculating the center postition of the blob
            posX = int(moment10 / area)
            posY = int(moment01 / area)

            # check slave status and send coordinates
            if  (1):
                print 'x: ' + str(posX) + ' y: ' + str(posY)

		# update video windows
        cv.ShowImage("processed", imgColorProcessed)
        cv.ShowImage("output", frame)

        if cv.WaitKey(10) >= 0:
            break

    return;

if __name__ == "__main__":
    main()
