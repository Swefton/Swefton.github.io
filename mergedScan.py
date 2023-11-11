# merges functionality from barScan.py and pictureClick.py into one script
# also uses a phone camera instead of the inbuilt webcam

import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
    
    if not detectedBarcodes:
        return "Barcode Not Detected or your barcode is blank/corrupted!"
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
             
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
                return (barcode.data)
                #print(barcode.type)

cam = cv2.VideoCapture(0)
# 1 mac webcam
# 0 phone cam

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "scan.jpg"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        break

cam.release()

cv2.destroyAllWindows()

image="scan.jpg"
data = BarcodeReader(image)
print(data)
