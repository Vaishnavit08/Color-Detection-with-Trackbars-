# Color Detection with trackbars

import cv2
import numpy as np

frame= cv2.imread('color_balls.jpg')
frame=cv2.resize(frame,(600,400))

def nothing(x):
    pass

cv2.namedWindow('Color Adjustments')

# creating Trackbars

cv2.createTrackbar('Lower_H','Color Adjustments',0,255,nothing)
cv2.createTrackbar('Lower_S','Color Adjustments',0,255,nothing)
cv2.createTrackbar('Lower_V','Color Adjustments',0,255,nothing)


cv2.createTrackbar('Upper_H','Color Adjustments',255,255,nothing)
cv2.createTrackbar('Upper_S','Color Adjustments',255,255,nothing)
cv2.createTrackbar('Upper_V','Color Adjustments',255,255,nothing)

# Binding Trackbars

while True:
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos('Lower_H','Color Adjustments')
    l_s=cv2.getTrackbarPos('Lower_S','Color Adjustments')
    l_v=cv2.getTrackbarPos('Lower_V','Color Adjustments')

    u_h=cv2.getTrackbarPos('Upper_H','Color Adjustments')
    u_s=cv2.getTrackbarPos('Upper_S','Color Adjustments')
    u_v=cv2.getTrackbarPos('Upper_V','Color Adjustments')

    lower_bound=np.array([l_h,l_s,l_v])
    upper_bound=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower_bound,upper_bound)

    # filter mask with image
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Original frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)

    k=cv2.waitKey(1)
    if k==ord('v'):
        break

cv2.destroyAllWindows()

