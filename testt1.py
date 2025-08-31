import cv2
img = cv2.imread("pexels-jonaskakaroto-736230.jpg",cv2.IMREAD_GRAYSCALE)
img1=cv2.resize(img,(500,500))
img2=cv2.Canny(img1,0,200)
cv2.imshow("helo",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
