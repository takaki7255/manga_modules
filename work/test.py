import cv2

img = cv2.imread('./../Manga109_released_2023_12_07/images/ARMS/000.jpg')
cv2.imwrite('./../out/out.jpg', img)