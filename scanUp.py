import cv2
from pyzbar.pyzbar import decode
from csv import writer
import random
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

counter = random.randint(2, 10000)
LOCATION = "EVENT"

def BarcodeReader(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
    
    if not detectedBarcodes:
        return -1
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
             
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
                return (barcode.data)
                #print(barcode.type)

while True:

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


    if data == -1:
        print("Barcode invalid")
    else:
        data = data.decode()
        #print(data)
        id = []
        iter = 1
        while iter < len(data) - 2:
            id.append(data[iter])
            iter = iter + 1
        data = ''.join(id)
        #print(data)
        
        try:
            item = {
                "_id": random.randint(2, 10000),
                "user": hash(data),
                "loca": LOCATION
            }
    
            db = client['people']
            coll = db["users"]
        
            coll.insert_many([item])
        except Exception as e:
            quit()

