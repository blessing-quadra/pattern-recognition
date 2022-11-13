

import cv2
import numpy as np
import random
import glob
import importlib

# import output mapper with text and speech
mapper = importlib.import_module("odu-ifa") 

# Load Yolo
# net = cv2.dnn.readNet("./model/yolov3_training_last.weights", "./model/cfg/yolov3_testing.cfg")
net = cv2.dnn.readNet("./model/test3.weights", "./model/yolov3_custom.cfg")
# net = cv2.dnn.readNet("./model/final_model.weights", "./model/yolov3_custom.cfg")

classes = ['faceup', 'facedown']
# classes = ['faceup', 'facedown']
# classes = ['CowrieUp', 'CowrieDown']
# images_path = glob.glob(r"./test-sample/*.jpg") + glob.glob(r"./test-sample/*.png") + glob.glob(r"./test-sample/*.jpeg")
images_path = glob.glob(r"./test-sample3/*.jpg") + glob.glob(r"./test-sample3/*.png") + glob.glob(r"./test-sample3/*.jpeg")

# with open("./model/coco.names", "r") as f:
#     classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
# print(images_path)

# output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


# Loading image
random.shuffle(images_path)
for image_path in images_path:
    img = cv2.imread(image_path)
    img = cv2.resize(img,(416,416), interpolation=cv2.INTER_AREA)
    # 1280,720;   896,504;    3024,4032
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    
    for out in outs:
        for detection in out:
            # scores = detection[6:]
            scores = detection[5:]
            # scores = detection[4:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
            # if confidence > 0.45:
                # print(class_id)
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.60, 0.35)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size =(len(boxes),3))
    
    colorRed = (255, 0, 0)
    colorGreen = (0, 255, 0)

    upsideCowriesCount = 0
    downsideCowrieCount = 0
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            # cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            # cv2.putText(img, label, (x, y + 30), font, 1, color, 3)
            if(label=='faceup'):
                upsideCowriesCount = upsideCowriesCount + 1
                cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 2)
                cv2.putText(img, label, (x, y + 30), font, 1, colorGreen, 3)
            elif(label == 'facedown'):
                downsideCowrieCount = downsideCowrieCount + 1
                cv2.rectangle(img, (x, y), (x + w, y + h), colorRed, 2)
                cv2.putText(img, label, (x, y + 30), font, 1, colorRed, 3)

    print(str(upsideCowriesCount) + " Cowrie(s) found facing up")
    print(str(downsideCowrieCount) + " Cowrie(s) found facing down")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    mapper.outputMapper(upsideCowriesCount, downsideCowrieCount)
    cv2.destroyAllWindows()