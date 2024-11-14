import cv2
from module import *

def main():
    ano_path, img_path, ano_list, title_list = get_manga109()
    # print(ano_path)
    # print(img_path)
    # print(ano_list)
    # print(title_list)
    img_list = get_imgs_from_path(img_path+title_list[0])
    print(img_list)
    for img_name in img_list:
        img = cv2.imread(img_path+title_list[0]+'/'+img_name)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pageImg = cut_page(img)
        for i, page in enumerate(pageImg):
            cv2.imshow('page'+str(i), page)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == '__main__':
    main()