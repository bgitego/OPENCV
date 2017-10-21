import numpy as np
import cv2
import os


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
  
  #Operation on Frame
  #gray = cv2.cvtColor(frame)
  
  #Display current frame
  cv2.imshow('frame',frame)

  #Get out of loop condition from user command prompt
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

#Release Video Capture
cap.release()
cv2.destroyAllWindows()

