import cv2
ing3=cv2.imread("hhe.png",1)
ing4=ing3[1000:1500,1500:1700]
cv2.imshow("hello",ing4)
cv2.waitKey(0)
cv2.destroyAllWindows()