import cv2 
import numpy as np
import pyautogui as pag
from system import screenshot
import time
import os


def find_template(img_name, template_name, threshold):
    """ Находит шаблон на изображении
    Возвращает координаты середины шаблона, если найден, иначе пустой список"""
    img_rgb = cv2.imread(img_name, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_name)
    resize_img = img_rgb
    resize_img.astype(np.uint8)
    template.astype(np.uint8)
    res = cv2.matchTemplate(resize_img,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    pt = loc[::-1]
    x, y = (pt[0] + 22), (pt[1] + 22)
    return x, y

