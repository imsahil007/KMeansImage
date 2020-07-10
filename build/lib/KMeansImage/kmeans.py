from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
from .Preprocessing import Preprocessing
import numpy as np
from .Display import display
import os
from .Save import save_pic

class kmeans_image:
    def __init__(self, image_path, output_colors):
        self.image_path = image_path
        img_object = Preprocessing(image_path)
        input_img = img_object.img
        img_data = img_object.reshape_rgb()

        kmeans = MiniBatchKMeans(output_colors).fit(img_data)
        k_colors = kmeans.cluster_centers_[kmeans.predict(img_data)]
        k_img = np.reshape(k_colors, (input_img.shape))
        plt.imsave("temp.jpg",k_img)
        print("Original Image size: "+str(os.stat(image_path).st_size/1000)+"KB")
        print("Compressed Image: "+ str(os.stat('temp.jpg').st_size/1000)+"KB")
        os.remove('temp.jpg')
        
        display(k_img)
        self.k_img = k_img
        
    def save(self):
        save_pic(self.image_path, self.k_img)

        

