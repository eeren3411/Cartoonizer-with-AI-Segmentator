from Interfaces.ISegmenter import ISegmenter
import cv2
import mediapipe as mp
import numpy as np

class Segmenter(ISegmenter):
    def __init__(self):
        self.selfieSegmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=0)

    def run(self, image):
        RGBimage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = self.selfieSegmentation.process(RGBimage)

        condition = np.stack((result.segmentation_mask,) * 3, axis=-1) > 0.1
        background = np.zeros(image.shape, dtype=np.uint8)
        output = np.where(condition, image, background)
        return output