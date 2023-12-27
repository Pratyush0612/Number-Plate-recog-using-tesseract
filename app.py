import cv2
import imutils
import pytesseract


image=cv2.imread('CarPictures/carimgs.jpg')
image=imutils.resize(image,width=500)
cv2.imshow("first img",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("second img",gray)

gray=cv2.bilateralFilter(gray,11,17,17)
cv2.imshow("third img",gray)

edged=cv2.Canny(gray,170,200)
cv2.imshow("fourth img",edged)

cnts,new=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("fifth img",image1)


cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
NumberPlateCount=None

image2=image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("six img",image2)


count=0
name=1

for i in cnts:
    perimeter=cv2.arcLength(i,True)
    approx=cv2.approxPolyDP(i,0.02*perimeter,True)
    if(len(approx)==4):
        NumberPlateCount=approx
        x , y , w , h =cv2.boundingRect(i)
        crp_img=image[y:y+h,x:x+w]
        cv2.imwrite(str(name)+'.png',crp_img)
        name+=1

        break

cv2.drawContours(image,[NumberPlateCount],-1,(0,255,0),3)
cv2.imshow("seven img",image)


crop_img_loc='1.png'
cv2.imshow("eight img",cv2.imread(crop_img_loc))


text=pytesseract.image_to_string(crop_img_loc,lang='eng')
print("Number is : ",text)
cv2.waitKey(0)
text = ''.join(e for e in text if e.isalnum())


def check_if_string_in_file(file_nam, string_to_search):
    with open(file_nam, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

