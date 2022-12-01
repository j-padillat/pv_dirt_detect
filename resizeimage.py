import cv2


image=cv2.imread("./images/image1.jpg")

scale_percent=0.2
print(image.shape)
width=int(image.shape[1]*scale_percent)

height=int(image.shape[0]*scale_percent)

dimension=(width,height)

resized = cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)

print(resized.shape)

cv2.imwrite("./images/panel_2.jpg",resized)