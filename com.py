
import cv2
import numpy as np
import time
sum1=1
def adj(c):
    print("影像處理中")
    img = cv2.imread(c)
    resImg1 = cv2.resize(img, (100,100), interpolation=cv2.INTER_CUBIC)
    #cv2.imshow('img', img)
    cv2.imwrite(c, resImg1) 
    cv2.imshow('resImg', resImg1)
    #cv2.waitKey()


def make_photo(sum1):
    """使用opencv拍照"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    while True:
        ret, frame = cap.read()
        if ret:
            # cv2.imshow("capture", frame)  # 弹窗口
            # 等待按键q操作关闭摄像头12313
            '''
            if cv2.waitKey(1) & 0xFF == ord('q'):
                file_name = "test.jpg"
                cv2.imwrite(file_name, frame)

                break
            '''   
            time.sleep(1)
            c="test"+str(sum1)+".jpg"
            
            cv2.imwrite(c, frame)  
            break 
            
        else:
            break
    adj(c)
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    sum1=input("請輸入sum1值：")
    make_photo(sum1)

