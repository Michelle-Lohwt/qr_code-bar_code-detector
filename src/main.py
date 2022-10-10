import cv2
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol

# img = cv2.imread('src\sample_img\qr.png')
# code = decode(img)
# print(code)

capture = cv2.VideoCapture(0)
capture.set(3,640) # 3 is width
capture.set(4,480) # 4 is height

while True:
  success, img = capture.read()
  for bytecode in decode(img):
    data = bytecode.data.decode('utf-8')
    print(data)
    pts = np.array([bytecode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (255,0,255), 5)
    pts2 = bytecode.rect
    cv2.putText(img, data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)

  cv2.imshow('Result', img)
  cv2.waitKey(1)