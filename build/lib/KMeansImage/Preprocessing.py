from skimage import io

class Preprocessing:
    def __init__(self, img_path):
        self.img = io.imread(img_path)
       

    def reshape_rgb(self):
        return (self.img / 255.0).reshape(-1, 3)
        

        
