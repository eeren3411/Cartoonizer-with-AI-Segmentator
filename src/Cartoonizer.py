from Interfaces.ISegmenter import ISegmenter
import cv2
import numpy as np

class Cartoonizer:
    def __init__(self, segmenter: str | ISegmenter = None):
        if(segmenter == "Human" or segmenter == "Default" or segmenter == "Mediapipe"):
            from Segmenter import Segmenter
            self.segmenter = Segmenter()
        else:
            self.segmenter = segmenter

    def run(self, image: str | np.ndarray, show: bool = False) -> np.ndarray:
        #If provided path instead of image
        if(type(image) == type("string")):
            image = cv2.imread(image)
        
        #If segmenter
        if(self.segmenter != None):
            image = self.segmenter.run(image)
        
        #It was a lot easier than I thought. I'm sad
        image = cv2.stylization(image, sigma_r=0.5)

        #Should I show it or not?
        if(show):
            cv2.imshow("style", image)
            cv2.waitKey(0)
        return image

def main():
    cartoonizer = Cartoonizer(segmenter=None)
    cartoonizer.run("./tests/robert.jpg", show=True)

if __name__ == "__main__":
    main()