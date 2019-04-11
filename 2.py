from PIL import Image,ImageTk
import tkinter as tk
import cv2
import numpy as np
import time
   
def p(c):
    print("進入Tk頁面")
    win3 = tk.Tk()
    win3.geometry("800x470")
    print(c)
    img1=ImageTk.PhotoImage(Image.open(c))
    print("開啟圖片")
    imLabel=tk.Label(win3,image=img1)
    imLabel.place(x=290,y=213)
    print("顯示圖片")
    win3.mainloop()

def adj(c):
    print("影像處理中")
    img = cv2.imread(c)
    resImg1 = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(c, resImg1) 
    p(c)


def make_photo():
    while True:
        sum1=input("請輸入sum1值：")
        if sum1=='q':
            break
        else:
            c="test"+str(sum1)+".jpg"
            print(c)
            """使用opencv拍照"""
            cap = cv2.VideoCapture(0)  
            while True:
                ret, frame = cap.read()
                if ret:
                    print("拍照成功")
                    time.sleep(1)
                    cv2.imwrite(c, frame)  
                    break 
                else:
                    print("拍照失敗")
                    break
            adj(c)
            cap.release()
            cv2.destroyAllWindows()
 
if __name__ == '__main__':
    
    make_photo()
