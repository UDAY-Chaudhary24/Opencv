import cv2 
cap1=cv2.VideoCapture(0)


while True :
   ret,frame=cap1.read()
   cv2.imshow("agya chutiya",frame)
   if cv2.waitKey(2)&0xFF==ord('j'):
     print("fuck of ")
     break 
   
cap1.release()
cv2.destroyAllWindows()