
from PIL import Image,ImageTk
import tkinter as tk

import cv2
import numpy as np
import time
sum1=1


def adj(file_name,c):
    print("影像處理中")
    img = cv2.imread(file_name)
    resImg1 = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)
    print("影像顯示")
    cv2.imwrite(c,resImg1)
    #cv2.imshow('img', img)
    #cv2.imshow('resImg', resImg1)
    cv2.waitKey()


def make_photo(c):
    """使用opencv拍照"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("capture", frame)  # 弹窗口
            # 等待按键q操作关闭摄像头

            if cv2.waitKey(1) & 0xFF == ord('q'):
                file_name =c
                cv2.imwrite(file_name, frame)
                break
            '''
            time.sleep(1)
            print(c)
            file_name =c
            cv2.imwrite(file_name, frame)  
            break 
            '''
        else:
            break
    adj(file_name,c)
    cap.release()
    cv2.destroyAllWindows()
    p(c)


def p(c):
    win = tk.Tk()
    im=Image.open(c)
    img=ImageTk.PhotoImage(im)
    imLabel=tk.Label(win,image=img).pack()
    win.mainloop()



if __name__ == '__main__':
    sum1=input("請輸入sum1值：")
    c="test"+str(sum1)+".jpg"
    print(c)
    make_photo(c)
    #p(c)
    
'''
from PIL import Image,ImageTk
import tkinter as tk

# 简单插入显示
def show_jpg():
    root = tk.Tk()
    im=Image.open("test2.jpg")
    img=ImageTk.PhotoImage(im)
    imLabel=tk.Label(root,image=img).pack()
    root.mainloop()

if __name__ == '__main__':
    show_jpg()
'''
