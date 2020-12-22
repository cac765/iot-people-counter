import numpy as np
import cv2

def Color_Count(img, P1_V, P2_V, P1_H, P2_H ):
#This function is given self for the image, and the four bounding box points
#The color values are counted for certain thresholds and reported as an array
    BLUE_THRESHOLD = 128
    GREEN_THRESHOLD = 128
    RED_THRESHOLD = 128

    Blue_Count = 0
    Green_Count = 0
    Red_Count = 0

    for i in range(int(P1_V), int(P2_V)):
        for j in range(int(P1_H), int(P2_H)):
            k = img[i,j]
            if(k[0] > BLUE_THRESHOLD):
                Blue_Count = Blue_Count + 1
            if(k[1] > GREEN_THRESHOLD):
                Green_Count = Green_Count + 1
            if(k[2] > RED_THRESHOLD):
                Red_Count = Red_Count + 1

    Object_BGR_Color_Count = [Blue_Count, Green_Count, Red_Count]
    print('Color Count within bounding box is: ', Object_BGR_Color_Count)
    return Object_BGR_Color_Count;

#load image
#img = cv2.imread('Color_Array.jpg')
img = cv2.imread('Red.png')

#get middle box of image as example
Q1_V = (img.shape[0])/2 - (img.shape[0])/4
Q1_H = (img.shape[1])/2 - (img.shape[1])/4
Q3_V = (img.shape[0])/2 + (img.shape[0])/4
Q3_H = (img.shape[1])/2 + (img.shape[1])/4

#Testing the medians of the box for color analysis
BGR = Color_Count(img, Q1_V, Q3_V, Q1_H, Q3_H)
cv2.rectangle(img, (int(Q1_H), int(Q1_V)), (int(Q3_H), int(Q3_V)), (0, 0, 0), 7 )


#Testing a blue box for color analysis
B = Color_Count(img, 420, 450, 100, 125)
cv2.rectangle(img, (420, 100), (450, 125), (0, 0, 0), 2)


#Testing a green box for color analysis
#G = Color_Count(img, 470, 500, 100, 125) #use this for Color_Array.jpg
#cv2.rectangle(img, (470, 100), (500, 125), (0, 0, 0), 2)

G = Color_Count(img, 10, 20, 10, 20) #use this for Red.png
cv2.rectangle(img, (10, 10), (20, 20), (0, 0, 0), 2)

#Testing a red box for color analysis
#R = Color_Count(img, 520, 550, 100, 125) #use this for Color_Array.jpg
#cv2.rectangle(img, (520, 100), (550, 125), (0, 0, 0), 2)

R = Color_Count(img, 50, 100, 50, 100) #use this for Red.png
cv2.rectangle(img, (50, 50), (100, 100), (0, 0, 0), 2)

#show image, wait for key press to end program
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()