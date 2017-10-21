import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

#Define Useful Variables
dir_name = 'Video_Capture'
file_name = dir_name + '/Capture_'

#For Grayscale Video
gray_dir_name = 'clean_video/gray'
gray_file_name = gray_dir_name + "/Gray_"

#For Binary Video
binary_dir_name = 'clean_video/binary'
binary_file_name = binary_dir_name + "/Binary_"

cap = cv2.VideoCapture(0)


#Change Camera Aspects Ratio WitdthxHeight
ret = cap.set(3,320)
ret = cap.set(4,240)
ret = cap.set(5,30)
print("Video Frame's Width: " + str(cap.get(3 )))
print("Video Frame's Height: " + str(cap.get(4)))
print("Video Frame's Frame Rate: " + str(cap.get(5))) 
while(True):
  
  #Capture Video Frame by Frame
  ref,frame = cap.read()
  
  img = frame
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
  faces = face_cascade.detectMultiScale(gray,1.3,5)
  eyes = faces #Initialised the varialbe with some values

  print(faces)
  for (x,y,w,h) in faces:
      img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray)
      print(eyes)      
  for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
      roi_eye = roi_color[ey:ey+eh, ex:ex+ew]
  #Display current frame
  cv2.imshow('frame',roi_color)
  cv2.imshow('frame2',roi_eye)

  #Get out of loop condition from user command prompt
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

#Release Video Capture
cap.release()
cv2.destroyAllWindows()

