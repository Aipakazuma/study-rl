# -*- coding:utf-8 -*-

from PIL import ImageGrab
import numpy as np
import cv2


cv2.namedWindow('test', cv2.WINDOW_NORMAL)
if __name__ == '__main__':
    while(True):
        # bbox specifies specific region (bbox= x,y,width,height)
        img = ImageGrab.grab(bbox=(0, 50, 1800, 1800))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        resize = cv2.resize(frame, (500, 500))
        cv2.imshow('test', resize)
        if 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
