import cv2
face_cap= cv2.CascadeClassifier("D:\Shinobu Python for Prac\haarcascade_frontalface_alt.xml")
video_cap=cv2.VideoCapture(0)
print("The camera will open in few seconds , please wait ....")
while True :
    ret , video_new = video_cap.read()
    col = cv2.cvtColor(video_new,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_new,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("video_live" , video_new)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()

    
