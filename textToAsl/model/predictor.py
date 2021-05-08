import torch
import torchvision
import torch.nn as nn
from .pytorch_i3d import InceptionI3d
from torchvision import transforms
from .videotransforms import *
import cv2
import numpy as np
import torch.nn.functional as F

class Predictor():
    def __init__(self,model_path,label_path):
        self.model_path=model_path
        self.label_path = label_path
        self.i3d = i3d = InceptionI3d(400,in_channels=3)
        self.i3d.replace_logits(100)
        self.i3d.load_state_dict(torch.load(self.model_path,map_location=torch.device('cpu')))
        self.i3d.eval()

    def predict(self,vid_path):
        test_transforms = transforms.Compose([CenterCrop(224)])
        # i3d.load_state_dict(torch.load('weights/rgb_imagenet.pt'))
        vidcap=cv2.VideoCapture(vid_path)
        frames = []    
        num=-1
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if num == -1:
            num = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        for offset in range(num):
            success, img = vidcap.read()
            try:
                w,h,c=img.shape
            except AttributeError:
                continue
            sc = 224 / w
            img = cv2.resize(img, dsize=(0, 0), fx=sc, fy=sc)
            img = (img / 255.) * 2 - 1
            frames.append(img)
        frames=np.asarray(frames,dtype=np.float32)
        frames = test_transforms(frames)
        ip_tensor=torch.Tensor(frames)
        ip_tensor=torch.unsqueeze(ip_tensor,3)
        t = ip_tensor.shape[2]
        ip_tensor = torch.transpose(ip_tensor,1,4)
        ip_tensor = torch.transpose(ip_tensor,0,3)
        ip_tensor = torch.transpose(ip_tensor,2,3)
        ip_tensor = torch.transpose(ip_tensor,3,4)
        with torch.no_grad():
            per_frame_logits = self.i3d(ip_tensor)
            predictions = torch.max(per_frame_logits, dim=2)[0]
    
        file = open(self.label_path,'r')
        line = file.readline()
        while(line):
            if int(line.split()[0])==torch.argmax(predictions).item():
                return line.split()[1]
            else:
                line = file.readline()