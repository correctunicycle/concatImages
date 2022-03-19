import cv2 as cv
import numpy as np
import glob
import os

# A little script to read images of identical dimensions from a folder and 
# combine them into a grid of any desired dimension and then output that grid as an image.



#create list of all images in folder
images = []
for filepath in glob.iglob('testFolder/*.png'):
    img = cv.imread(filepath)
    images.append(img)
    


# puts images into strips of desired width w
secondImgArr = []
imageWidth = 5
for x in range(0,len(images)-imageWidth,imageWidth):
    MiddleImage = np.concatenate(images[x:x+imageWidth],axis = 1)
    secondImgArr.append(MiddleImage)



#combine strips together and save output
FinalImage1 = np.concatenate(secondImgArr,axis = 0)



cv.imwrite('OutputImage.png',FinalImage1)



    