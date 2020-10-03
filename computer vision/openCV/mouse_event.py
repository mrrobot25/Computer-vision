import cv2
import numpy as np


events=[i for i in dir(cv2) if 'EVENT' in i]
print(events)


def mouse_click(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDOWN:
		print(x,',',y)
		XY=str(x)+' '+str(y)
		font=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(image,XY,(x,y),font,0.5,(0,0,255),2)
		cv2.imshow('image',image)

image=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',image)
text='this is a test image'
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,text,(120,255),font,1,(0,255,255),2)
cv2.imshow('image',image)

cv2.setMouseCallback('image',mouse_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
