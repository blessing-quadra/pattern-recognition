import cv2
import numpy as np


# Load Yolo
net = cv2.dnn.readNet("./model/test3.weights", "./model/yolov3_custom.cfg")

# getting image layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

# model classes
classes = ['faceup', 'facedown']

def detect_sample(sample):
    # get samples dimension
    height, width, channels = sample.shape
    # Detecting objects
    blob = cv2.dnn.blobFromImage(sample, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
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
                cv2.rectangle(sample, (x, y), (x + w, y + h), colorGreen, 2)
                cv2.putText(sample, label, (x, y + 30), font, 1, colorGreen, 3)
            elif(label == 'facedown'):
                downsideCowrieCount = downsideCowrieCount + 1
                cv2.rectangle(sample, (x, y), (x + w, y + h), colorRed, 2)
                cv2.putText(sample, label, (x, y + 30), font, 1, colorRed, 3)

    print(str(upsideCowriesCount) + " Cowrie(s) found facing up")
    print(str(downsideCowrieCount) + " Cowrie(s) found facing down")
    cv2.imshow("Image", sample)
    return (upsideCowriesCount, downsideCowrieCount)