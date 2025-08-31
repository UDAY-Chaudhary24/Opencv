import cv2
uj=cv2.imread("hhe.png",1)
if uj is not None:
    print("yes ")
cv2.imshow("hello",uj)
cv2.waitKey(0)
cv2.destroyAllWindows()