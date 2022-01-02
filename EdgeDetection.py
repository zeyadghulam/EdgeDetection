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
cv2.imshow('Frame View', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
