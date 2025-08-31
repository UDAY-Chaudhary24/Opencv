import cv2
yss=cv2.imread("hhe.png",1)
yss1=cv2.resize(yss,(1920,1080))
cv2.imshow("hello",yss1)
cv2.waitKey(0)
cv2.destroyAllWindows()