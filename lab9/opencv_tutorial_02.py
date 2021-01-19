import argparse
import imutils
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("chonkers_gray.jpg", gray)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

edged = cv2.Canny(gray, 30, 150)
cv2.imwrite("chonkers_edged.jpg", edged)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imwrite("chonkers_thresh.jpg", thresh)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
output = image.copy()

for c in contours:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

cv2.imwrite("chonkers_contours.jpg", output)

text = f"I found {len(contours)} object(s)!"
cv2.putText(output, text, (10, 25), cv2.FONT_ITALIC, 0.7, (240, 0, 159), 2)
cv2.imwrite("chonkers_contours_text.jpg", output)
cv2.imshow("Contours text", output)
cv2.waitKey(0)

mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imwrite("chonkers_eroded.jpg", mask)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imwrite("chonkers_dilated.jpg", mask)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite("chonkers_bitwise.jpg", output)
cv2.imshow("Output", output)
cv2.waitKey(0)