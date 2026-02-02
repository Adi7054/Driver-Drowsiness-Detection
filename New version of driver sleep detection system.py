import cv2
import time
import winsound
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
cam=cv2.VideoCapture(0)
if cam.isOpened()==False:
    print("Camera error")
    exit()
eye_close_time=None
ALERT_TIME=0.5
miss=0
MAX_MISS=4
while True:
    ret,frame=cam.read()
    if ret==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray=gray[y:y+h,x:x+w]
        face_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(face_gray,1.05,3)
        if len(eyes)==0:
            miss+=1
        else:
            miss=0
            eye_close_time=None
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        if miss>=MAX_MISS:
            if eye_close_time is None:
                eye_close_time=time.time()
            t=time.time()-eye_close_time
            if t>=ALERT_TIME:
                cv2.putText(frame,"DROWSY ALERT",(40,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                winsound.Beep(2000,500)
        status="AWAKE" if miss<MAX_MISS else "EYES CLOSED"
        col=(0,255,0) if status=="AWAKE" else (0,0,255)
        cv2.putText(frame,status,(40,40),cv2.FONT_HERSHEY_SIMPLEX,0.9,col,2)
    cv2.imshow("Drowsiness Detection",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()