import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('qrcode.png')
cap = cv2.VideoCapture(0)

with open('mydatafile.txt') as f:
    myDataList = f.read().splitlines()
print(myDataList)
while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
            print(myOutput)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
            print(myOutput)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
    cv2.imshow('QR CODE Scanner by Shubharthak', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
