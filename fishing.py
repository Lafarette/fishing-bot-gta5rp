import mss
from system import screenshot, write_key
import pyautogui as pag
from helper import find_template
import datetime
import time


def fishing(w):
    fish = False
    now = time.time()
    write_key(0x17) 
    time.sleep(0.5) # Waiting for inventory to open
    screenshot(1446,219,1817,683)
    res = find_template('screen.png', 'Images/mk2.jpg', 0.8)
    if len(res[0]) != 0:
        res[0][0], res[1][0] = res[0][0] + 1449, res[1][0] + 228
        w.write('[{}]Нашли удочку\n'.format(datetime.datetime.now()))
        pag.moveTo(res[0][0], res[1][0])
        pag.click(button='right')
        fish = True
        # Checking the need to press the LMB and the end of fishing
        while fish:
            screenshot(1034,890,1084,942)
            res = find_template('screen.png', 'Images/need_click.jpg', 0.9)
            if len(res[0]) != 0:
                w.write('[{}]ЛКМ\n'.format(datetime.datetime.now()))
                for i in range(13):
                    pag.click()
            screenshot(848,1002,1056,1110)
            res = find_template('screen.png', 'Images/end_fishing.jpg', 0.8)
            later = time.time()
            if len(res[0]) != 0 and int(later - now) > 5:
                w.write('[{}]Конец цикла\n'.format(datetime.datetime.now()))
                break
    else:
        w.write('[{}]Удочка не найдена\n'.format(datetime.datetime.now()))
