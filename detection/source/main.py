import sys,cv2,time,json
from unittest.mock import patch

sys.path.insert(1, './user_interface')

from MultiCam import Ui_MainWindow




from VideoThreding import VideoCapture

from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSlot
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore,QtGui,QtWidgets
import time


  

class MultiCam(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    
        self.CamId=0
       

        self.ui.toolButton_exit.clicked.connect(self.close)
      
        #Window restore

        self.ui.toolButton_restore.clicked.connect(self.Restore)
        self.count=0

        # # Button Status

        self.Play_Pause_B1=None
        self.Play_Pause_B2=None

        self.Play_Pause_ButtonStatus=[self.Play_Pause_B1,self.Play_Pause_B2]

        # # Video MultiThread

        self.VideoThread_1=None
        self.VideoThread_2=None
       
        self.VideoPaths=[".\\input\\video.mp4"] 
        

        self.VideoThread =[self.VideoThread_1,self.VideoThread_2]
        
        # Video Screens
        self.Screens = [self.ui.Screen_1,self.ui.Screen_2]
     
        #Cam 1

        self.ui.Button_Play_Pause_1.toggled['bool'].connect(self.Play_Pause_Screen_1)
        

        #Cam 2

        self.ui.Button_Play_Pause_2.toggled['bool'].connect(self.Play_Pause_Screen_2)
        self.butID=None

    
    @pyqtSlot(np.ndarray)  
    def Screen_1(self,Frame):
        
        rgb_Frame=Frame
        h, w ,ch = rgb_Frame.shape
        img = QImage(rgb_Frame, w, h, rgb_Frame.strides[0], QImage.Format_BGR888)
        self.ui.Screen_1.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.Screen_1.setPixmap(QPixmap.fromImage(img)) 
        
        if self.Play_Pause_B1==False:
            time.sleep(0.01)
            self.ui.Screen_1.setPixmap(QtGui.QPixmap(":/icons/icons8-no-camera-48.png"))
         

    @pyqtSlot(np.ndarray)  
    def Screen_2(self,Frame):

        rgb_Frame=Frame
        h, w ,ch = rgb_Frame.shape
        img = QImage(rgb_Frame, w, h, rgb_Frame.strides[0], QImage.Format_BGR888)
        self.ui.Screen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.Screen_2.setPixmap(QPixmap.fromImage(img)) 
        

        if self.Play_Pause_B2==False:
            time.sleep(0.01)
            self.ui.Screen_2.setPixmap(QtGui.QPixmap(":/icons/icons8-no-camera-48.png"))

        
           
    
    def Play_Pause_Screen_1(self,State):
        self.CamId=0
        self.runThread(State)
    
    def Play_Pause_Screen_2(self,State):
        self.CamId=1
        self.runThread(State)
    
   
    def runThread(self,st):
        Screens=[self.Screen_1,self.Screen_2]
        if st==True:  

            self.Play_Pause_ButtonStatus[self.CamId]=True
          
            Path = self.VideoPaths[self.CamId]
            self.LogPrint("CamID :",self.CamId,"Path :",Path)
           

            self.VideoThread[self.CamId] = VideoCapture(self.CamId,Path) 
            self.VideoThread[self.CamId].change_pixmap_signal.connect(Screens[self.CamId])
            self.VideoThread[self.CamId].start()

        elif st==False:

            self.Play_Pause_ButtonStatus[self.CamId]=False
            self.VideoThread[self.CamId].stop()
       
        

    def Restore(self):

        if (self.count==0):
            self.showNormal()
            self.count+=1

        elif (self.count==1):
            self.showFullScreen()
            self.count=0

    def LogPrint(*argv):
        pass
        print(argv[1:])        

app = QApplication([])
window = MultiCam()
window.showMinimized()
app.exec_()
