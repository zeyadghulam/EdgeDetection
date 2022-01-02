########import dependencies############

# Import opencv for computer vision
import cv2
# import os for file paths
import os


########Load Image############
# Import matplot lib for visualization
from matplotlib import pyplot as plt

# Define the file path to the image
IMG_PATH = os.path.join('data', 'images', 'street.jpeg')

# Read the image
image = cv2.imread(IMG_PATH)

#Resize Image
resized_img = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

# View image using OpenCV
#cv2.imshow('Frame View', resized_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


########Edge Detection############

# Apply Canny
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(blur, threshold1=180, threshold2=200)    #wider threshold == more edges

#Resize Image
#resized_img = cv2.resize(canny, (int(image.shape[1]/2), int(image.shape[0]/2)))

# View image using OpenCV
cv2.imshow('Frame View', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()