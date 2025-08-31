import cv2
img1=cv2.imread("white_background_1920x1080.png")
img2=cv2.resize(img1,(800,800))
pt1=(0,400)
pt2=(400,800)
pt3=(800,400)
pt4=(400,0)
coor=(255,0,0)
cv2.line(img2,pt1,pt2,coor,2)
cv2.line(img2,pt2,pt3,coor,2)
cv2.line(img2,pt3,pt4,coor,2)
cv2.line(img2,pt4,pt1,coor,2)
cv2.imshow("hello",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
i=0
centre=(400,400)
'''while i<=360:
    hj=cv2.getRotationMatrix2D(centre,i,1.0)
    img3=cv2.warpAffine(img2,hj,(800,800))
    cv2.imshow("hello",img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows

   '''