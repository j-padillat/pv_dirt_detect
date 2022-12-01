import cv2


# we load in the image
img = cv2.imread("images/image1.jpg")

h, w, c = img.shape
print(f"Height: {h}, width: {w}, channels: {c}")

# we create a window and display the image
cv2.imshow("Image 1", img)
# we click the window created and press any key to close the window
cv2.waitKey(0)