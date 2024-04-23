import time
import pyautogui as pg
import pyperclip as pc

def _workaround_write(text):
    pc.copy(text)
    pg.hotkey('ctrl', 'v')
    pc.copy('')



occ = 0

txt = "Titouan imprime STP !!!!!".split()

time.sleep(5) 
while occ < 100000:
    _workaround_write(txt)
    pg.press(enter)
    time.sleep(0.5)
    occ += 1