import cv2
import numpy as np
from pylsd.lsd import lsd
from module import *

def main():
    img = cv2.imread('./../../Manga109_released_2023_12_07/images/ARMS/009.jpg')
    cut_img = cut_page(img)
    for i, img in enumerate(cut_img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        gaus = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(gaus, 50, 150)
        lsd_lines = lsd(gaus)
        img2 = np.zeros_like(img)
        img3 = np.zeros_like(img)
        for line in lsd_lines:
            x0, y0, x1, y1 = map(int, line[:4])
            cv2.line(img2, (x0, y0), (x1, y1), (0, 0, 255), 3)
            if (x1-x0)**2 + (y1-y0)**2 > 500:
                cv2.line(img3, (x0, y0), (x1, y1), (0, 0, 255), 3)
        # cv2.imshow('img', img2)
        # cv2.imshow('img2', img3)
        # cv2.imshow('src', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # img2に輪郭抽出
        contours = []
        hierarchy = []
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
        result = np.zeros_like(img)
        result = cv2.drawContours(result, contours, -1, (0, 0, 255), 3)
        #外接矩形の描画
        # for i in range(len(contours)):
        #     x, y, w, h = cv2.boundingRect(contours[i])
        #     cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cv2.imshow('src', img)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main()