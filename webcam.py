import cv2
import matplotlib.pyplot as plt
import sys

def main():
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
    else:
        ret = False

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(img1)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('C:/Users/ronoy/OneDrive/Documents/Python/image/pic.png')

    cap.release()


for i in range(0,2):
    main()
