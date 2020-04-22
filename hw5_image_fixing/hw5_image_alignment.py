"""
    Author:     Jonathan Schwartz
    GW ID:      G20740593
    Course:     MAE 6194 - Mechactronics Design

    Description:
        This program averages a series of image together. This works best with images that
        have a lot of noise in them, for instance a series of blurry pictures.
"""

# Impoering libraries needed. cv2 for importing and processing image, numpy to
# perform linear algebra on arrays of data from imagess, and pathlib to get the path to
# the current directory (i.e. the directory this script is in.
import cv2
import numpy as np
import pathlib

# Finding path of the current directory
path = str(pathlib.Path(__file__).parent.absolute()) + "\\"
# Listing names of files to be averaged
file_names = ['OUT_0001.png', 'OUT_0002.png', 'OUT_0003.png', 'OUT_0004.png', 'OUT_0005.png', 'OUT_0006.png', 'OUT_0007.png', 'OUT_0008.png', 'OUT_0009.png', 'OUT_0000.png']
# Finding number of images to import
count = len(file_names)

# Importing images
imgs = [ ]
for i in range(0, count):
    imgs.append(cv2.imread(path + file_names[i]))

#find dimensions of each image file in order to initialize sum array
img_shape = imgs[0].shape
# Initialize empty numpy array to hold sum of all pictures
sum = np.zeros(((img_shape)))

# Loop through list of images and add their values to the sum array. Values are summed
# Individually for each channel of each pixel
for i in range(1,count):
    sum += imgs[i]

# Create an array of averages for each channel on each pixel by dividing sum array
# by the number of images that were added together
#  NOTE: array is converted to a uint8 because the averaging changes the array's type from
#        uint8 to double, so we must set it back to that for the opencv library
#        to work properly
avg = np.array(sum / count).astype(np.uint8)

# Saving averaged image as a jpeg file to the current directory
cv2.imwrite(path + "averaged_image.jpg", avg)

# Use the opencv library to show averaged image. The window is resized because it is
# way too zoomed in otherwise.
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 650,750)
cv2.imshow('image',avg)
cv2.waitKey(0)
cv2.destroyAllWindows()
