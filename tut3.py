import cv2

img = cv2.imread("img.png", 0)
print(img)
cv2.imshow("image", img)
k = cv2.waitKey(0) & 0xFF

if k == 27: # 27 = esc key ascii
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite("img_greyscale.png", img)
	cv2.destroyAllWindows()