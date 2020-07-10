
import os
import ipywidgets as widgets
import matplotlib.pyplot as plt
from skimage import io
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider
from .Save import save_pic
from .Preprocessing import Preprocessing

class kmeans_image_ui:
    def __init__(self, img_dir):
        
        @interact
        def color_compression(image=os.listdir(img_dir), k=IntSlider(min=1,max=256,step=1,value=16,
                                                                     continuous_update=False,
                                                                     layout=dict(width='100%'))):

        
            # input_img = io.imread(img_dir + image)
            self.img_path = img_dir + image
            img_object = Preprocessing(self.img_path)
            
            input_img = img_object.img
            img_data = img_object.reshape_rgb()

            kmeans = MiniBatchKMeans(k).fit(img_data)
            k_colors = kmeans.cluster_centers_[kmeans.predict(img_data)]
            #After K-means has converged, load the large image into your program and 
            #replace each of its pixels with the nearest of the centroid colors you found
            #from the small image. 
            k_img = np.reshape(k_colors, (input_img.shape))

            fig, (ax1, ax2) = plt.subplots(1, 2)
            fig.suptitle('K-means Image Compression', fontsize=20)
            plt.imsave("temp.jpg",k_img)    
            ax1.set_title('Compressed: '+str(os.stat('temp.jpg').st_size/1000)+" KB")
            os.remove('temp.jpg')
            ax1.set_xticks([])
            ax1.set_yticks([])
            ax1.imshow(k_img)   
            self.k_img = k_img
            
            ax2.set_title('Original :'+str(os.stat(img_dir+image).st_size/1000)+"KB")
            ax2.set_xticks([])
            ax2.set_yticks([])
            ax2.imshow(input_img)

            plt.subplots_adjust(top=0.85)
            plt.show()

    def save(self):
        save_pic(self.img_path, self.k_img)

            
        
                    
            
            	
            
         
