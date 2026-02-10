import cv2
print(cv2.__version__)
img1 = cv2.imread("ani.jpeg")
print(type(img1))
cv2.imshow("image test", img1)


cv2.imwrite("ani2.jpeg",img1)
cv2.imwrite("ani3.jpeg",img1,[cv2.IMWRITE_JPEG_QUALITY, 3])
img2 = cv2.imread("ani2.jpeg")
img3 = cv2.imread("ani3.jpeg")
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)

cv2.waitKey()
cv2.destroyAllWindows()