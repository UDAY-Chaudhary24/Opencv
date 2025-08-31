import cv2
'''print("enter file location")
x=str(input())'''
img1=cv2.imread("white_background_1920x1080.png",1)
img2=cv2.resize(img1,(800,800))
coor=(225,0,0)
'''y=int(input("enter value"))
coor=(255,0,0)'''
'''if(y==1):
    cv2.putText(img2,"purani battie bhool ja mere land pe jhool ja ",(0,0),cv2.FONT_HERSHEY_SIMPLEX,0.5,coor,1)
if(y==2):'''
cv2.circle(img2,(50,600),50,coor,1)
cv2.circle(img2,(150,600),50,coor,1)
cv2.line(img2,(120,560),(120,360),coor,1)
cv2.line(img2,(80,560),(80,360),coor,1)
cv2.circle(img2,(100,360),20,coor,1)
cv2.line(img2,(100,340),(100,355),coor,2)
cv2.imshow("hello",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
