import cv2
img0 = cv2.imread("hhe.png",1)
h,w,c=img0.shape
centre=(h/2,w/2)
hj=cv2.getRotationMatrix2D(centre,90,1.0)
img1=cv2.warpAffine(img0,hj,(w,h ))
cv2.imshow("hello",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()