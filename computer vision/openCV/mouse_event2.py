import cv2
import numpy as np

events=[i for i in dir(cv2) if "EVENT" in i]
print(events)

def mouse_click(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		points.append((x,y))
		if len(points) >=2:
			cv2.line(image,points[-1],points[-2],(0,0,255),3)
		cv2.imshow('image',image)
	

image=m=np.zeros((512,512,3),np.uint8)
font=cv2.FONT_HERSHEY_SIMPLEX
text='this is a test image'
cv2.putText(image,text,(120,255),font,1,(0,255,255),2)
cv2.imshow('image',image)
points=[]
cv2.setMouseCallback('image',mouse_click)

cv2.waitKey(0)
cv2.destrotyAllWindows()
