import cv2
cap=cv2.VideoCapture(0)
print(cap.i0sOpened())
height=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
width=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height,width)
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('test.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
	ret,frame=cap.read()
	out.write(frame)
	cv2.imshow('original',frame)
	
 	
	if cv2.waitKey(1) & 0xff==ord('q'):
		break
	

cap.release()
out.release()
cv2.destroyAllWindows()
