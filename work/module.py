# 共通する関数
# このファイルをimportして使う
import os
import sys
import numpy as np
import cv2
import xml.etree.ElementTree as ET


def func():
    print('module.pyのfunc()が呼ばれました')

def get_manga109():
    path = './../../Manga109_released_2023_12_07/'
    ano_path = './../../Manga109_released_2023_12_07/annotations/'
    img_path = './../../Manga109_released_2023_12_07/images/'
    ano_list = os.listdir(ano_path)
    title_list = os.listdir(img_path)
    if '.DS_Store' in ano_list:
        ano_list.remove('.DS_Store')
    if '.DS_Store' in title_list:
        title_list.remove('.DS_Store')
    ano_list.sort()
    title_list.sort()
    return ano_path, img_path, ano_list, title_list

def get_imgs_from_path(img_path):
    img_list = os.listdir(img_path)
    img_list.sort()
    return img_list

def cut_page(img):
    pageImg = []
    if img.shape[1] > img.shape[0]:  # 縦 < 横の場合: 見開きだと判断し真ん中で切断
        cut_img_left = img[:, : img.shape[1] // 2]  # 右ページ
        cut_img_right = img[:, img.shape[1] // 2 :]  # 左ページ
        pageImg.append(cut_img_right)
        pageImg.append(cut_img_left)
    else:  # 縦 > 横の場合: 単一ページ画像だと判断しそのまま保存
        pageImg.append(img)
    return pageImg

def get_framebbox(xml_file: str) -> list:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    pages = root.findall('.//page')
    page_objects = {}
    for page in pages:
        page_index = page.get('index')
        page_index = int(page_index)
        objects = []
        for obj in page:
            if obj.tag in ["frame"]:
                obj_data = {
                    "type": obj.tag,
                    "id": obj.get("id"),
                    "xmin": obj.get("xmin"),
                    "ymin": obj.get("ymin"),
                    "xmax": obj.get("xmax"),
                    "ymax": obj.get("ymax"),
                }
                objects.append(obj_data)
        page_objects[page_index] = objects
    return page_objects

def get_textbbox(xml_file: str) -> list:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    pages = root.findall('.//page')
    page_objects = {}
    for page in pages:
        page_index = page.get('index')
        page_index = int(page_index)
        objects = []
        for obj in page:
            if obj.tag in ["text"]:
                obj_data = {
                    "type": obj.tag,
                    "id": obj.get("id"),
                    "xmin": obj.get("xmin"),
                    "ymin": obj.get("ymin"),
                    "xmax": obj.get("xmax"),
                    "ymax": obj.get("ymax"),
                }
                objects.append(obj_data)
        page_objects[page_index] = objects
    return page_objects

def get_facebbox(xml_file: str) -> list:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    pages = root.findall('.//page')
    page_objects = {}
    for page in pages:
        page_index = page.get('index')
        page_index = int(page_index)
        objects = []
        for obj in page:
            if obj.tag in ["face"]:
                obj_data = {
                    "type": obj.tag,
                    "id": obj.get("id"),
                    "xmin": obj.get("xmin"),
                    "ymin": obj.get("ymin"),
                    "xmax": obj.get("xmax"),
                    "ymax": obj.get("ymax"),
                }
                objects.append(obj_data)
        page_objects[page_index] = objects
    return page_objects

def get_bboxs(xml_file: str) -> list:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    pages = root.findall('.//page')
    page_objects = {}
    face_bboxs = {}
    frame_bboxs = {}
    text_bboxs = {}
    body_bboxs = {}
    for page in pages:
        page_index = page.get('index')
        page_index = int(page_index)
        objects = []
        for obj in page:
            obj_data = {
                    "type": obj.tag,
                    "id": obj.get("id"),
                    "xmin": obj.get("xmin"),
                    "ymin": obj.get("ymin"),
                    "xmax": obj.get("xmax"),
                    "ymax": obj.get("ymax"),
                }
            if obj.tag in ["face"]:
                face_bboxs[obj.get("id")] = obj_data
            elif obj.tag in ["frame"]:
                frame_bboxs[obj.get("id")] = obj_data
            elif obj.tag in ["text"]:
                text_bboxs[obj.get("id")] = obj_data
            elif obj.tag in ["body"]:
                body_bboxs[obj.get("id")] = obj_data
            objects.append(obj_data)
        page_objects[page_index] = objects
    return page_objects, face_bboxs, frame_bboxs, text_bboxs, body_bboxs
