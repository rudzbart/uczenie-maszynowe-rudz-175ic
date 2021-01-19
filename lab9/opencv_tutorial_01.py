import imutils
import cv2

image = cv2.imread("chonkers.jpg")
(h, w, d) = image.shape
print(f"Width = {w}, Height = {h}, Depth = {d}")

cv2.imshow("Image", image)
cv2.waitKey(0)

(b, g, r) = image[100, 50]
print(f"R = {r}, G = {g}, B = {b}")

roi = image[100:150, 100:200]
cv2.imwrite("chonkers_roi.jpg", roi)
cv2.imshow("ROI", roi)
cv2.waitKey(0)

resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed resizing", resized)
cv2.waitKey(0)

ratio = 300.0 / w
dimension = (300, int(h * ratio))
resized = cv2.resize(image, dimension)
cv2.imshow("Aspect ratio resize", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width=300)
cv2.imwrite("chonkers_resized.jpg", resized)
cv2.imshow("Imutils resize", resized)
cv2.waitKey(0)

center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow("OpenCV rotation", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, -45)
cv2.imwrite("chonkers_rotated.jpg", rotated)
cv2.imshow("Imutils rotation", rotated)
cv2.waitKey(0)

rotated = imutils.rotate_bound(image, 45)
cv2.imwrite("chonkers_bound_rotated.jpg", rotated)
cv2.imshow("Imutils bound rotation", rotated)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imwrite("chonkers_blurred.jpg", blurred)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imwrite("chonkers_rectangle.jpg", output)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imwrite("chonkers_circle.jpg", output)
cv2.imshow("Circle", output)
cv2.waitKey(0)

output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imwrite("chonkers_line.jpg", output)
cv2.imshow("Line", output)
cv2.waitKey(0)

output = image.copy()
cv2.putText(output, "OpenCV + Chonkers", (10, 25), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 2)
cv2.imwrite("chonkers_text.jpg", output)
cv2.imshow("Text", output)
cv2.waitKey(0)