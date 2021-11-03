import cv2
import numpy as np
import pyautogui as pag
from system import screenshot
import time
import os


def find_template(img_name, template_name, threshold, scale_factor,
            scale_size, return_coords = False):
    """ Находит шаблон на изображении
    Возвращает координаты середины шаблона, если найден, иначе пустой список"""
    img_rgb = cv2.imread(img_name, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_name)
    resize_img = cv2.resize(img_rgb, scale_size)
    resize_img.astype(np.uint8)
    template.astype(np.uint8)
    res = cv2.matchTemplate(resize_img,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    pt = loc[::-1]
    x, y = ((pt[0] + int(template.shape[0] / 2))*scale_factor,
                (pt[1] + int(template.shape[0] / 2))*scale_factor)
    if return_coords:
        if len(x) != 0:
            return x[0], y[0]
        else:
            return 0, 0
    else:
        if len(x) != 0:
            return True
        else:
            return False
