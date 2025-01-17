import cv2


body_classifier= cv2.CascadeClassifier('haarcascade_fullbody.xml')


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    bodies= body_classifier.detectMultiScale(gray, 1.2, 3)
    
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,234),2)
        cv2.imshow("Web cam frame", frame)
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
