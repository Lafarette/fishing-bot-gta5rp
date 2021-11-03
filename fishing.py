import mss
from system import screenshot, write_key
import pyautogui as pag
from helper import find_template
import datetime
import time


def fishing(w, settings):
    fish = False
    now = time.time()
    write_key(0x17)
    time.sleep(0.5)  # Waiting for inventory to open
    screenshot()
    x, y = find_template(
        img_name='screen.png',
        template_name=settings['path_templateMK2'],
        threshold=0.9,
        scale_factor=settings['scale_factor'],
        scale_size=settings['scale_size'],
        return_coords=True)
    if x:
        w.write('[{}]Нашли удочку\n'.format(datetime.datetime.now()))
        pag.moveTo(x, y)
        pag.click(button='right')
        fish = True
        # Checking the need to press the LMB and the end of fishing
        while fish:
            screenshot()
            res = find_template(
                img_name='screen.png',
                template_name=settings['path_templateNeedClick'],
                threshold=0.9,
                scale_factor=settings['scale_factor'],
                scale_size=settings['scale_size'],
                return_coords=False)
            if res:
                w.write('[{}]ЛКМ\n'.format(datetime.datetime.now()))
                pag.click(button='left', clicks=15, interval=0.25)
            screenshot()
            res = find_template(
                img_name='screen.png',
                template_name=settings['path_templateEndFishing'],
                threshold=0.9,
                scale_factor=settings['scale_factor'],
                scale_size=settings['scale_size'],
                return_coords=False)
            later = time.time()
            if len(res[0]) != 0 and int(later - now) > 5:
                w.write('[{}]Конец цикла\n'.format(datetime.datetime.now()))
                break
    else:
        w.write('[{}]Удочка не найдена\n'.format(datetime.datetime.now()))
