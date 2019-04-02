
import cv2
import numpy as np
import adj


    

def make_photo():
    """使用opencv拍照"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("capture", frame)  # 弹窗口
            # 等待按键q操作关闭摄像头
            if cv2.waitKey(1) & 0xFF == ord('q'):
                file_name = "test1.jpeg"
                cv2.imwrite(file_name, frame)
                break
        else:
            break
    adj.img = cv2.imread(file_name)
    adj.resImg1 = cv2.resize(adj.img, (100,100), interpolation=cv2.INTER_CUBIC)

    #cv2.imshow('img', img)
    adj.cv2.imshow('resImg', adj.resImg1)
    adj.cv2.waitKey()
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    make_photo()

