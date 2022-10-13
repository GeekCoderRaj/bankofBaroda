from flask import Flask, request, jsonify, Response
import cv2 as cv
import os
import m



def break_image():
   img=cv.imread("Cheque083654.jpeg")
   img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   edged = cv.Canny(img, 50, 500)
   contours, hierarchy = cv.findContours(edged, 
    cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
   cv.drawContours(img, contours, -1, (0, 255, 0), 2) 
   size=img.shape
   datebox=img[0:size[0]//5,size[1]-(size[1]//4):size[1]]
   payee_name=img[size[0]//6:size[0]//2,0:size[1]-(size[1]//5)]
   bottom_box=img[size[0]-(size[0]//5):size[0],size[1]//5:size[1]-size[1]//5]
   amt_box=img[size[0]//3:size[0]//2,size[1]-(size[1]//3):size[1]]
   bank_name=img[0:size[0]//5,0:size[1]-(size[1]//3)]
   ac_no=img[size[0]//2:size[0]-(size[0]//5*2),0:size[1]]
   sign_box=img[size[0]//2:size[0]-(size[0]//6),size[1]-(size[1]//3):size[1]]
   parent_dir=os.getcwd()
   image_dir="Images"
   path=os.path.join(parent_dir,image_dir)
   os.mkdir(path)
   cv.imwrite(os.path.join(path , 'Date.jpeg'), datebox)
   Date = m.azure_ocr_api("Date.jpeg")

   cv.imwrite(os.path.join(path , 'sign.jpeg'),sign_box)
   sign = m.azure_ocr_api("sign.jpeg")
   
   cv.imwrite(os.path.join(path , 'Payee_name.jpeg'),payee_name)
   Payee_name = m.azure_ocr_api("Payee_name.jpeg")
   
   cv.imwrite(os.path.join(path , 'Account_no.jpeg'),ac_no)
   Account_no = m.azure_ocr_api("Account_no.jpeg")
   
   cv.imwrite(os.path.join(path , 'Bank_name.jpeg'),bank_name)
   Bank_name = m.azure_ocr_api("Bank_name.jpeg")
   
   cv.imwrite(os.path.join(path , 'Bottom_digits.jpeg'),bottom_box)
   Bottom_digits = m.azure_ocr_api("Bottom_digits.jpeg")
   
   cv.imwrite(os.path.join(path , 'Amount.jpeg'),amt_box)
   Amount = m.azure_ocr_api("Amount.jpeg")
   
   print("Enter of operation")
   

def process_image():

    break_image()
   
process_image()
