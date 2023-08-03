
import numpy as np 
import argparse
import cv2
import os
import pyttsx3
engine = pyttsx3.init()
  
from playsound import playsound  
language = 'en'  

image="im1.jpg"
prototxt="MobileNetSSD_deploy.prototxt"
model="MobileNetSSD_deploy.caffemodel"
confidence=0.2
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS=np.random.uniform(0,255,size=(len(CLASSES),3))
net=cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt","MobileNetSSD_deploy.caffemodel")
video=cv2.VideoCapture(0)
count=0
while True:
        
        _,image=video.read()
#         cv2.imshow("input",image)
#         cv2.waitKey(0)
        (h,w)=image.shape[:2]
        blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007843,(300,300),127.5)
        net.setInput(blob)
        detections=net.forward()
        for i in np.arange(0,detections.shape[2]):
            confidence=detections[0,0,i,2]
            if confidence>0.2:
                idx=int(detections[0,0,i,1])
                box=detections[0,0,i,3:7]*np.array([w,h,w,h])
                (startX,startY,endX,endY)=box.astype('int')
                label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
                text_val=CLASSES[idx]+" detected infront of you"
                cv2.rectangle(image,(startX,startY),(endX,endY),COLORS[idx],2)
                if(count%10==0):
                    print(count)
                    engine.say(text_val)
                    engine.runAndWait()

                count+=1
                y=startY-15 if startY-15>15 else startY+15
                cv2.putText(image,label,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,COLORS[idx],2)
                cv2.imshow("IMAGE",image)
                if(cv2.waitKey(1)=='q'):
                    break
video.release()                
cv2.destroyAllWindows()