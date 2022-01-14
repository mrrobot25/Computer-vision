import cv2
import numpy as np


#img=np.zeros([512,512,3],np.uint8) # for the black img

img=cv2.imread('/home/lenovo/opencv/opencv-master/samples/data/lena.jpg',1)
cv2.imshow('original',img)

img=cv2.line(img,(0,0),(365,322),(255,0,0),5)

img=cv2.arrowedLine(img,(0,360),(233,255),(0,0,255),5)
img=cv2.rectangle(img,(0,122),(255,255),(0,255,0),5)
#img=cv2.rectangle(img,(0,122),(255,114),(0,255,0),-1)  # for fill in rectangle
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'openCV',(300,240),font,1,(112,0,179),2)
#img=cv2.rectangle(img,(0,122),(255,114),(0,255,0),,,1)  # for fill in rectangle
img=cv2.circle(img,(301,320),40,(0,102,255),5)
cv2.imshow('test',img)
if cv2.waitKey(0) & 0xff==ord('q'):
	cv2.destroyAllWindows()
