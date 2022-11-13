import cv2


k = cv2.waitKey(1)
while True:
    cv2.imshow("frame", 0)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        print(k%256)
        break
    