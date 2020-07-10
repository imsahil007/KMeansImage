from skimage import io
import matplotlib.pyplot as plt


class display:
    def __init__(self, img):
        
        #ax = plt.axes(xticks=[], yticks=[])
        plt.imshow(img)
        
