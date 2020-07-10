from matplotlib import pyplot 

class save_pic:
	def __init__(self, img_path, k_img):
		img_path = img_path.split('.')[0]+"_KMeans_."+img_path.split('.')[1]
		pyplot.imsave(img_path,k_img)
		print("Image saved: "+ img_path)