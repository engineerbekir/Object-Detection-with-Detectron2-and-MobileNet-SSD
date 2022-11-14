
# ******* Created by Bekir ÖZTÜRK **********

import threading
import time
import cv2,sys,base64
from PyQt5.QtCore import pyqtSignal,pyqtSlot
from cv2 import imshow
import numpy as np
from PyQt5.QtCore import pyqtSignal,  QThread,QObject


# # *** Detectron2 libraries
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog, DatasetCatalog


class VideoCapture(threading.Thread,QObject):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self,threadID, path):

        threading.Thread.__init__(self)
        QObject.__init__(self)

        self.threadID=int(threadID)
        self.Flag=True

        if len(path)<2:
            self.path=int(path)
        else :
            self.path=path
        
       
        
    def run(self):
        print(self.path)
        self.MobileNetSSDonVideo(self.path)
        #self.DetectrononVideo(self.path)


##**** MOBILENET-SSD***        
    
    def MobileNetSSDonVideo(self, videoPath):
        
        with open('C:\\Users\\casper\\Desktop\\MobileNetSSD\\input\\object_detection_classes_coco.txt', 'r') as f:
            class_names = f.read().split('\n')

        COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

       
        model = cv2.dnn.readNet(model='.\\input\\frozen_inference_graph.pb',
                                config='.\\input\\ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', 
                                framework='TensorFlow')


        cap = cv2.VideoCapture(videoPath)
    
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                image = frame
                image_height, image_width, _ = image.shape
               
                blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), 
                                            swapRB=True)
                
                model.setInput(blob)
                output = model.forward()        
               
                for detection in output[0, 0, :, :]:
                    
                    confidence = detection[2]
                   
                    if confidence > .4:
                       
                        class_id = detection[1]
                        
                        class_name = "%s:%.2f " % (class_names[int(class_id)-1], confidence*100)
                        color = COLORS[int(class_id)]
                        
                        box_x = detection[3] * image_width
                        box_y = detection[4] * image_height
                        
                        box_width = detection[5] * image_width
                        box_height = detection[6] * image_height
                       
                        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=3)
                        
                        cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
                        
                        image = cv2.resize(image, (560, 580))
                    
                        self.change_pixmap_signal.emit(image)
                        time.sleep(0.040)
                      
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
   

    #***DETECTRON2****

    # def DetectrononVideo(self,VideoPath):

    #     t0= time.time()
    #     self.cfg =get_cfg()
    
    #     self.cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml"))
    #     self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml")
    
    #     self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST=0.6
    #     self.cfg.MODEL.DEVICE= "cuda"
    #     self.predictor =DefaultPredictor(self.cfg)
    #     t1= time.time()

        
    #     print("elepsed : ", t1-t0)

    #     cap = cv2.VideoCapture(VideoPath)
        
    #     if (cap.isOpened() == False):
    #         print("Error is opening the file..")

    #     (success, image) = cap.read()
        
    #     while success:

    #         outputs=self.predictor(image)   

    #         viz = Visualizer(image[:,:,::-1],metadata= MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]),
    #          instance_mode = ColorMode.IMAGE)
           
    #         output=viz.draw_instance_predictions(outputs["instances"].to("cpu"))
    #         result = output.get_image()[:,:,::-1]
    #         result = cv2.resize(result, (600,600))
    #         self.change_pixmap_signal.emit(result)
    #         time.sleep(0.040)
    #         cv2.waitKey(1) 

    #         (success, image) = cap.read()
                

    def stop(self):

        self.Flag=False
        return self.Flag




