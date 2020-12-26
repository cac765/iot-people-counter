
import numpy as np
import cv2


class object():
#Object class for pixel count storage, proportions are calculated and stored here to save processing in later steps
#The object inputs are in the order that opencv stores its pixel values if they are to be directly uploaded to this class later
    def __init__(self, Blue_Count, Green_Count, Red_Count):
        self.Blue_Count = Blue_Count
        self.Green_Count = Green_Count
        self.Red_Count = Red_Count
        self.Blue_Proportion = (Blue_Count)/(Blue_Count + Green_Count + Red_Count)
        self.Green_Proportion = (Green_Count)/(Blue_Count + Green_Count + Red_Count)
        self.Red_Proportion = (Red_Count)/(Blue_Count + Green_Count + Red_Count)

#print the object's pixel counts and proportion of each color as a percent
    def show(self):
        print("Object Blue Count is: ", self.Blue_Count, ", Proportion is: ", 100*self.Blue_Proportion, "%")
        print("Object Green Count is: ", self.Green_Count, ", Proportion is: ", 100*self.Green_Proportion, "%")
        print("Object Red Count is: ", self.Red_Count, ", Proportion is: ", 100*self.Red_Proportion, "%")


def Color_Count(img, x_min, y_min, x_max, y_max ):
#This function is given self for the image, and the four bounding box points
#The color values are counted for certain thresholds and reported as an array
    BLUE_THRESHOLD = 128
    GREEN_THRESHOLD = 128
    RED_THRESHOLD = 128

    Blue_Count = 1
    Green_Count = 1
    Red_Count = 1

    for i in range(int(x_min), int(x_max)):
        for j in range(int(y_min), int(y_max)):
            k = img[i,j]
            if(k[0] > BLUE_THRESHOLD):
                Blue_Count = Blue_Count + 1
            if(k[1] > GREEN_THRESHOLD):
                Green_Count = Green_Count + 1
            if(k[2] > RED_THRESHOLD):
                Red_Count = Red_Count + 1

    Object_BGR_Color_Count = [Blue_Count, Green_Count, Red_Count]
    print('Color Count within bounding box is: ', Object_BGR_Color_Count)
    #return Object_BGR_Color_Count;
    return Blue_Count, Green_Count, Red_Count;


def Color_Count_V2(img, x_min, y_min, x_max, y_max ):
#This function is given self for the image, and the four bounding box points
#The color values are counted for total value of each color in the box
#This version is meant to account for darker clothing colors and still count it, hopefully increasing overall accuracy
    Blue_Count = 1
    Green_Count = 1
    Red_Count = 1

    for i in range(int(x_min), int(x_max)):
        for j in range(int(y_min), int(y_max)):
            k = img[i,j]
            Blue_Count = Blue_Count + k[0]
            Green_Count = Green_Count + k[1]
            Red_Count = Red_Count + k[2]

    Object_BGR_Color_Count = [Blue_Count, Green_Count, Red_Count]
    print('Color Count within bounding box is: ', Object_BGR_Color_Count)
    #return Object_BGR_Color_Count;
    return Blue_Count, Green_Count, Red_Count;


def Similarity_Compare(Object_1, Object_2):
#
    Blue_Diff = abs((Object_1.Blue_Proportion - Object_2.Blue_Proportion)/(Object_1.Blue_Proportion))*((Object_1.Blue_Proportion+Object_2.Blue_Proportion)/2)
    print("Weighted difference in object Blue color proportions is: ", Blue_Diff)

    Green_Diff = abs((Object_1.Green_Proportion - Object_2.Green_Proportion)/(Object_1.Green_Proportion))*((Object_1.Green_Proportion+Object_2.Green_Proportion)/2)
    print("Weighted difference in object Green color proportions is: ", Green_Diff)

    Red_Diff = abs((Object_1.Red_Proportion - Object_2.Red_Proportion)/(Object_1.Red_Proportion))*((Object_1.Red_Proportion+Object_2.Red_Proportion)/2)
    print("Weighted difference in object Red color proportions is: ", Red_Diff)

    Match_Percent = 1 - (Blue_Diff + Green_Diff + Red_Diff)
    return Match_Percent;

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    People = {}
    obj_cnt = 0
    for (x,y,w,h) in faces:
        B, G, R = Color_Count_V2(img, x, y, x+w, y+h)
        People[obj_cnt] = object(B, G, R )
        text = "Percent Blue: {:.2f}%, Percent Green: {:.2f}%, Percent Red: {:.2f}%".format(People[obj_cnt].Blue_Proportion * 100, People[obj_cnt].Green_Proportion * 100, People[obj_cnt].Red_Proportion * 100 )
        Y = y - 10 if y - 10 > 10 else y + 10
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
        cv2.putText(img, text, (x, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        obj_cnt = obj_cnt+1
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xFF
    if k== 27:
        break

cap.release()
cv2.destroyAllWindows()
