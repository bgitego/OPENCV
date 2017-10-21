import cv2
import time

cam = cv2.VideoCapture("drop.avi")
time.sleep(4)
print(cam.isOpened())
num_of_frame = int (cam.get(7))
print("Total Number of Frames is: ",num_of_frame)
for count in range(1,num_of_frame + 1,1):
        print("Displaying Frame Number :", str(count))
        ret, frame = cam.read()
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cam.release()
cv2.destroyAllWindows()
