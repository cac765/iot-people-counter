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





################################################################################
# just testing from this point forth...

#load image
#img = cv2.imread('Color_Array.jpg')
img = cv2.imread('Color_Venn.jpg')
#img = cv2.imread('Green.png')

#get middle box of image as example
Q1_x = (img.shape[0])/2 - (img.shape[0])/4
Q1_y = (img.shape[1])/2 - (img.shape[1])/4
Q3_x = (img.shape[0])/2 + (img.shape[0])/4
Q3_y = (img.shape[1])/2 + (img.shape[1])/4

#Testing the medians of the box for color analysis
BGR = Color_Count_V2(img, Q1_x, Q1_y, Q3_x, Q3_y)
#cv2.rectangle(img, (int(Q1_x), int(Q1_y)), (int(Q3_x), int(Q3_y)), (0, 0, 0), 7 )


#Testing a blue box for color analysis
print("Testing Blue Box...")

#x_min, y_min, x_max, y_max = 475, 150, 500, 175 #use these for color_array.jpg
x_min, y_min, x_max, y_max = 200, 300, 250, 350 #use this for Color_Venn.jpg
#x_min, y_min, x_max, y_max = 50, 50, 100, 100 #use this for Red.png

B = Color_Count_V2(img, x_min, y_min, x_max, y_max)
cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 0), 2)
Blue = object(B[0], B[1], B[2])
Blue.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Testing a green box for color analysis
print("Testing Green Box...")

#x_min, y_min, x_max, y_max = 475, 100, 500, 125 #use these for color_array.jpg
x_min, y_min, x_max, y_max = 300, 150, 350, 200 #use this for Color_Venn.jpg
#x_min, y_min, x_max, y_max = 50, 50, 100, 100 #use this for Red.png

G = Color_Count_V2(img, x_min, y_min, x_max, y_max)
cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 0), 2)
Green = object(G[0], G[1], G[2])
Green.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#G = Color_Count_V2(img, 10, 10, 20, 20) #use this for Red.png
#cv2.rectangle(img, (10, 10), (20, 20), (0, 0, 0), 2)

##Testing a red box for color analysis
print("Testing Red Box")

#x_min, y_min, x_max, y_max = 425, 100, 450, 125 #use these for color_array.jpg
x_min, y_min, x_max, y_max = 100, 150, 150, 200 #use this for Color_Venn.jpg
#x_min, y_min, x_max, y_max = 50, 50, 100, 100 #use this for Red.png

R = Color_Count_V2(img, x_min, y_min, x_max, y_max)
cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 0), 2)
Red = object(R[0], R[1], R[2])
Red.show()

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

Objects = {}
Objects[0] = (10, 10, 20, 20)
Objects[1] = (50, 50, 100, 100)
Objects[2] = (25, 25, 200, 200)

A = {}
obj_cnt = 0
for Item in Objects:
    x, y, w, h = Objects[Item]
    B, G, R = Color_Count_V2(img, x, y, w, h)
    A[obj_cnt] = object(B, G, R )
    A[obj_cnt].show()
    obj_cnt = obj_cnt+1


#show image, wait for key press to end program
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()