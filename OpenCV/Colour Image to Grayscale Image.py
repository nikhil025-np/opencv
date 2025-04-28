import cv2
img = cv2.imread("shinchan-wallpaper-v0-bi1ma4oqprtd1.webp")
cv2.imshow("shinchan", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
