import cv2

src = cv2.imread("prasahnt.jpeg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

#percent by which the image is resized
scale_percent = int(input("By what percentage would you like to resize the image? "))

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize

dsize = (width, height)

#resize image

output = cv2.resize(src, dsize)

cv2.imwrite('newimg.png', output)
# cv2.waitKey(0)
