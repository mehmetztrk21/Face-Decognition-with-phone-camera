import cv2

front=cv2.CascadeClassifier("front.xml")  #cascade folder

video=cv2.VideoCapture(0)
URL = "http://192.168.0.19:8080//video"  #Your IP cameras adress
video.open(URL)

while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fronts=front.detectMultiScale(gray,1.8,3)

    for (i,j,w,h) in fronts:
        cv2.rectangle(frame,(i,j),(i+w,j+h),(0,255,0),3)

    cv2.imshow("frame",frame)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break


video.release()
cv2.destroyAllWindows()



