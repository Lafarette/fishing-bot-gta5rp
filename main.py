from tkinter import *
import threading
from mss import mss
import cv2
import pyautogui
import time
from fishing import fishing

def run_action():
    global work
    w = open('log.txt', 'w', encoding='UTF-8')
    while work:
        fishing(w)
    w.close()

        
def start_bot():
    global work
    thread = threading.Thread(target=run_action, daemon=True)
    if work == False:
        label_status['text'] = "Статус: Работает"
        btn_on_off['text'] = "Остановить"
        work = True
        thread.start()
    elif work == True:
        work = False
        label_status['text'] = "Статус: Не работает"
        btn_on_off['text'] = "Запустить"


work = False

window = Tk()
window.title("BRBRBRB")
window.geometry('500x250')

label_status = Label(window, text="Статус: Не работает", font=("Arial Bold", 10))
label_status.place(x=10, y=10)

btn_on_off = Button(text="Запустить", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=start_bot)
btn_on_off.place(x=10, y=50)

window.mainloop()