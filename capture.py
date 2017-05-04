# -*- coding:utf-8 -*-

# from PIL import ImageGrab
import pyscreenshot as ImageGrab
import pyautogui as gui
import numpy as np
import cv2
import time


cv2.namedWindow('test', cv2.WINDOW_NORMAL)
if __name__ == '__main__':
    start = time.time()
    print('start:', start)
    while(True):
        # bbox specifies specific region (bbox= x,y,width,height)
        # img = ImageGrab.grab(bbox=(0, 50, 1800, 1800))
        # img = gui.screenshot(region = (0, 50, 1800, 1800))
        img  = ImageGrab.grab(bbox=(0, 50, 1800, 1800))
        print(img)
        print('screenshot:', time.time() - start)
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        print('convert gray scale:', time.time() - start)
        resize = cv2.resize(frame, (500, 500))
        print('resize:', time.time() - start)
        cv2.imshow('test', resize)
        print('shown:', time.time() - start)
        if 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
