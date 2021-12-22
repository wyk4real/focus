import cv2 as cv
import numpy as np
import sympy
from matplotlib import pyplot as plt


def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0) #高斯模糊，去噪声

    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)

    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)

    edge_output = cv.Canny(xgrad,ygrad,50,361) #先求梯度，然后在边缘提取
    # edge_output = cv.Canny(gray,50,150) #直接对二值图像边缘提取，高低阈值3:1 or 2:1
    cv.imshow('Canny Edge',edge_output)

    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow('Color Edge',dst)



src = cv.imread(r'C:\Intro ML\openCV\image\5.jpg')
cv.imshow('src', src)

edge_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
