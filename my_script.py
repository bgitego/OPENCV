import numpy as np
import cv2
import os


#Define Useful Variables
dir_name = 'POINT_Index'
file_name = dir_name + '/Capture_'

#For Grayscale Image
gray_dir_name = 'clean_image/gray'
gray_file_name = gray_dir_name + "/Gray_"

#For Binary Image
binary_dir_name = 'clean_image/binary'
binary_file_name = binary_dir_name + "/Binary_"


#Get quantity of files in direcotry POINT_Index

#create a log file object to read pixel data
f = open('log_file.txt','w')
log_str =""
f_list =os.listdir(dir_name)
qty_files = len(f_list)
print('Quantity of files ' + str(qty_files))

#Loop to all the files in the direcotry and convert them to grayscale
#qty_files = 2
for count in range(1,qty_files+1,1):


        #Update file name to have the Index Number
        img_name = file_name + str(count) + '.PNG'
        gray_img_name = gray_file_name + str(count) + '.PNG'
        binary_img_name = binary_file_name + str(count) + '.PNG'
  
        print(img_name)
        #Read Image as grayscale  
        img=cv2.imread(img_name,0)

        #save image in new direcotry as grayscale
        #ret,img = cv2.threshold(img,240,255,cv2.THRESH_BINARY)         

        cv2.imwrite(gray_img_name,img)
        #cv2.imshow(('image_'+str(count)),img)

        #Convert gray image to binary        
        ret,clean_img = cv2.threshold(img,240,255,cv2.THRESH_BINARY_INV)
      
        #save image in new direcotry as grayscale
        #Change dimmension of the picture
        clean_img = clean_img[0:700,5:345]
        #Do an expension transformation on the image
        #clean_img =  cv2.resize(clean_img,None,fx=4,fy=4,interpolation=cv2.INTER_LINEAR)
        #ret,clean_img = cv2.threshold(clean_img,220,255,cv2.THRESH_BINARY)         

        cv2.imwrite(binary_img_name,clean_img)
        #cv2.imshow(('Binary_Image_'+str(count)),clean_img)

        #acess individual pixel properties
        print("Image Shape is: " + str(img.shape))
        print("Image Size is: " + str(img.size))
        print("Image width is: " + str(img.shape[0]))
        print("Image Height is: " + str(img.shape[1]))
        print("Image Datatype is: " + str(img.dtype))

        #Pixel manipulation codes
        #Extract image dimmension
        width = img.shape[1]
        height = img.shape[0]

        #Print all pixel in the image
        for y in range(0,height-1):
                for x in range(0,width-1):
                        #Add a a new pixel object to the string
                        f.write(str(img.item(y,x)))
                        f.write(',')
                        #print(img.item(x,y),sep=",",end='',file='log.txt')
                #Add a new line for each row
		#write the string to the log file
                f.write('\n')

        cv2.waitKey()
        cv2.destroyAllWindows()
#close log file
f.close()

