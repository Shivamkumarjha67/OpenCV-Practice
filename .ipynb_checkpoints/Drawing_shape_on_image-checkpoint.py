import cv2
import numpy as np

# Defining the function
def red_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), thickness=5)

cv2.namedWindow(winname = 'Dog Backpack')
cv2.setMouseCallback('Dog Backpack', red_circle)


# Showing image with open-cv
img = cv2.imread('DATA/dog_backpack.jpg')

while True:
    cv2.imshow('Dog Backpack', img)

    if cv2.waitKey(15) & 0xFF == 27:
        break

cv2.destroyAllWindows()