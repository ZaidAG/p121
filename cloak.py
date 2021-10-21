import cv2
import time
import numpy as np
#Saving files as 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#Start the Webcam
cap=cv2.VideoCapture(0)
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=cap.read()
bg=np.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    #Converting the color from bgr to hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #Generating Mask of red color
    upper_black=np.array([104,153,70])
    lower_black=np.array([30,30,0])
    mask_1=cv2.inRange(hsv,lower_black,upper_black)
    upper_black=np.array([104,153,70])
    lower_black=np.array([30,30,0])
    mask_2=cv2.inRange(hsv,lower_black,upper_black)
    mask_1=mask_1+mask_2
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask_2=cv2.bitwise_not(mask_1)

    res_1=cv2.bitwise_and(img,img,mask=mask_2)
    res_2=cv2.bitwise_and(bg,bg,mask=mask_1)
    final_output=cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)
    cv2.imshow("colors dissapears",final_output)
    cv2.waitKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()