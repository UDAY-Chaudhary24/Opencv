import cv2
import numpy as mp
li=[]
li1=[]
li2=[]
li3=[]
li4=[]
li5=[]
li6=[]
li7=[]
li8=[]
li9=[]
j=0
c_star=0
li_pad1=[]
li_pad2=[]
li_pad3=[]
out_pink=[]
out_blue=[]
out_gray=[]

img1=cv2.imread("1.png")
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_,Thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
contores,hie=cv2.findContours(Thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img1,contores,1,(0,255,0,),2) 
'''cv2.imshow("hello",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
i=0
for contour in contores:
    apr=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cor=len(apr)
    m=mp.zeros_like(img1)
    cv2.drawContours(m,[contour],-1,(255,255,255),-1)
    h= cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    avg = cv2.mean(h, m=m[:, :, 0]) 
    h1, s, v, _ = avg
    if(cor==10):
        if(0<=h<15)or(160<=h<=180):
            nine=9
            li.insert(0,nine)
            x,y,w,h=cv2.boundingRect(contour)
            li1.insert(j,x)
            li1.insert(j+1,y)
            j=j+2
        elif(15<=h<35):
            six=6
            li.insert(0,six)
            x,y,w,h=cv2.boundingRect(contour)
            li2.insert(j,x)
            li2.insert(j+1,y)
            j=j+2
        elif(35<=h<=85):
            three=3
            li.insert(0,three)
            x,y,w,h=cv2.boundingRect(contour)
            li3.insert(j,x)
            li3.insert(j+1,y)
            j=j+2
    if(cor==3):
        if(0<=h<15)or(160<=h<=180):
            six1=6
            li.insert(0,six1)
            x,y,w,h=cv2.boundingRect(contour)
            li4.inset(j,x)
            li4.insert(j+1,y)
            j=j+2
        elif(15<=h<35):
            four=4
            li.insert(0,four)
            x,y,w,h=cv2.boundingRect(contour)
            li5.insert(j,x)
            li5.insert(j+1,y)
            j=j+2
        elif(35<=h<=85):
            two=2
            li.insert(0,two)
            x,y,w,h=cv2.boundingRect(contour)
            li6.insert(j,x)
            li6.insert(j+1,y)
            j=j+2
    if (cor==4):
        if(0<=h<15)or(160<=h<=180):
         three1=3
         li.insert=(0,three1)  
         x,y,w,h=cv2.boundingRect(contour)
         li7.insert(j,x)
         li7.insert(j+1,y)
         j=j+2
        elif(15<=h<35):
            two1=2
            li.insert(0,two1)
            x,y,w,h=cv2.boundingRect(contour)
            li8.insert(j,x)
            li8.insert(j+1,y)
            j=j+2
        elif(35<=h<=85):
            one=1
            li.insert(0,one)
            x,y,w,h=cv2.boundingRect(contour)
            li9.insert(j,x)
            li9.insert(j+1,y)
            j=j+2
    if(cor>10):
        if(150<=h<=180):
            x,y,w,h=cv2.boundingRect(contour)
            li_pad1.insert(0,x)
            li_pad1.insert(1,y)
        elif(100<=h<=140):
            x,y,w,h=cv2.boundingRect(contour)
            li_pad2.insert(0,x)
            li_pad2.insert(1,y)
        else:
            x,y,w,h=cv2.boundingRect(contour)
            li_pad3.insert(0,x)
            li_pad3.insert(0,y)
q=(len(li1)+1)/2
while i<q:
    pad1=pow((li_pad1[0]*li_pad1[0]-li1[i]*li1[i]+li_pad1[1]*li_pad1[1]-li1[i+1]*li1[i+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li1[i]*li1[i]+li_pad2[1]*li_pad2[1]-li1[i+1]*li1[i+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li1[i]*li1[i]+li_pad3[1]*li_pad3[1]-li1[i+1]*li1[i+1]),1/2)
    if(pad1>pad2)and(pad1>pad3):
        out_pink.insert(0,"[3,3]")
    if(pad2>pad1)and(pad2>pad3):
        out_blue.insert(0,"[3,3]")
    if(pad3>pad1)and(pad3>pad2):
        out_gray(0,"[3,3]")
        i=i+1
qq=(len(li2)+1)/2
n=0
while n <qq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li2[n]*li2[n]+li_pad1[1]*li_pad1[1]-li2[n+1]*li2[n+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li2[n]*li2[n]+li_pad2[1]*li_pad2[1]-li2[n+1]*li2[n+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li2[n]*li2[n]+li_pad3[1]*li_pad3[1]-li2[n+1]*li2[n+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[3,2]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[3,2]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[3,2]")
       n=n+1
qqq=(len(li4)+1)/2
k=0
while k <qqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li4[k]*li4[k]+li_pad1[1]*li_pad1[1]-li4[k+1]*li4[k+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li4[k]*li4[k]+li_pad2[1]*li_pad2[1]-li4[k+1]*li4[k+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li4[k]*li4[k]+li_pad3[1]*li_pad3[1]-li4[k+1]*li4[k+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[2,3]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[2,3]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[2,3]")
       k=k+1
qqqq=(len(li5)+1)/2
l=0
while l <qqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li5[l]*li5[l]+li_pad1[1]*li_pad1[1]-li5[l+1]*li5[l+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li5[l]*li5[l]+li_pad2[1]*li_pad2[1]-li5[l+1]*li5[l+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li5[l]*li5[l]+li_pad3[1]*li_pad3[1]-li5[l+1]*li5[l+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[2,2]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[2,2]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[2,2]")
       l=l+1

qqqqq=(len(li3)-1)/2
v=0
while v <qqqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li3[v]*li3[v]+li_pad1[1]*li_pad1[1]-li3[v+1]*li3[v+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li3[v]*li3[v]+li_pad2[1]*li_pad2[1]-li3[v+1]*li3[v+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li3[v]*li3[v]+li_pad3[1]*li_pad3[1]-li3[v+1]*li3[v+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[3,1]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[3,1]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[3,1]")
       v=v+1
qqqqqq=(len(li7)+1)/2
z=0
while z <qqqqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li7[z]*li7[z]+li_pad1[1]*li_pad1[1]-li7[z+1]*li7[z+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li7[z]*li7[z]+li_pad2[1]*li_pad2[1]-li7[z+1]*li7[z+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li7[z]*li7[z]+li_pad3[1]*li_pad3[1]-li7[z+1]*li7[z+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[1,3]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[1,3]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[1,3]")
       z=z+1
qqqqqqq=(len(li6)+1)/2
o=0
while o <qqqqqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li6[o]*li6[o]+li_pad1[1]*li_pad1[1]-li6[o+1]*li6[o+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li6[o]*li6[o]+li_pad2[1]*li_pad2[1]-li6[o+1]*li6[o+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li6[o]*li6[o]+li_pad3[1]*li_pad3[1]-li6[o+1]*li6[o+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[2,1]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[2,1]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[2,1]")
       o=o+1
qqqqqqqq=(len(li8)+1)/2
h=0
while h <qqqqqqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li8[h]*li8[h]+li_pad1[1]*li_pad1[1]-li8[h+1]*li8[h+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li8[h]*li8[h]+li_pad2[1]*li_pad2[1]-li8[h+1]*li8[h+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li8[h]*li8[h]+li_pad3[1]*li_pad3[1]-li8[h+1]*li8[h+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[1,2]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[1,2]")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[1,2]")
       h=h+1
qqqqqqqqq=(len(li9)+1)/2
e=0
while e <qqqqqqqqq:
    pad1=pow((li_pad1[0]*li_pad1[0]-li9[e]*li9[e]+li_pad1[1]*li_pad1[1]-li9[e+1]*li9[e+1]),1/2)
    pad2=pow((li_pad2[0]*li_pad2[0]-li9[e]*li9[e]+li_pad2[1]*li_pad2[1]-li9[e+1]*li9[e+1]),1/2)
    pad3=pow((li_pad3[0]*li_pad3[0]-li9[e]*li9[e]+li_pad3[1]*li_pad3[1]-li9[e+1]*li9[e+1]),1/2)
    if(pad1>pad2)and(pad1>pad3)and(len(out_pink)<3):
        out_pink.append("[1,1]")
    if(pad2>pad1)and(pad2>pad3)and(len(out_blue)<4):
        out_blue.append("[1,1")
    if(pad3>pad1)and(pad3>pad2)and(len(out_gray)<2):
       out_gray.append("[1,1]")
       e=e+1
print("for pink")
print(out_pink)
print("for blue")
print(out_blue)
print("for gray")
print(out_gray)








