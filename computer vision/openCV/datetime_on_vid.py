import cv2
import datetime

cap=cv2.VideoCapture(0)
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(height,width)
while(cap.isOpened()):
	ret,frame=cap.read()
	
	if ret==True:
		gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		text='WIDTH:'+ str(width) +' '+ 'HEIGHT:' + str(height)
		font=cv2.font = cv2.FONT_HERSHEY_SIMPLEX
		frame=cv2.putText(frame,text,(30,30),font,1,
						(0,255,255),2)
		date=str(datetime.datetime.now())
		frame=cv2.putText(frame,date,(440,30),font,0.5,(0,0,255),2)
		cv2.imshow('vid',frame)

		if cv2.waitKey(1) & 0xff==ord('q'):
			break	
	
			
	else:
		break
cap.release()
cv2.destroyAllWindows()
