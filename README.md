# KMeansImage
# Pip package(Python >= 3.0)

This is a python package to compress images in python using KMeans-Clustering technique.

[![N|Solid](https://pypi.org/static/images/logo-small.6eef541e.svg)](https://pypi.org/project/KMeansImage/)

![png](https://github.com/imsahil007/KMeansImage/blob/master/res/kmeans.png)
Download the package using:
```
pip3 install KMeansImage
```

# How to use:
```
from KMeansImage import kmeans_image
k_img = kmeans_image( $image_path_with_image_name ,  $output_colors )
k_img.save( $save_path_with_file_name )
```
In case you are using Jupyter notebook, you can also use:
```
from KMeansImage import kmeans_image_ui
k_img = kmeans_image_ui( $image_directory_path )
k_img.save( $save_path_with_file_name )
```
# Example: [Pdf](https://github.com/imsahil007/KMeansImage/blob/master/res/tutorial.pdf)

Import Library


```python
from KMeansImage import kmeans_image
```

First parameter = path<br>
Second parameter = No. of colors i.e. Clusters


```python
k_img = kmeans_image('/home/sahil/Downloads/KMeansImage/res/batman.jpg', 20)
```

    Original Image size: 419.291KB
    Compressed Image: 253.235KB



![png](https://github.com/imsahil007/KMeansImage/blob/master/res/batman_KMeans_.jpg)


See the difference between size of both pics<br>
For saving the file use -


```python
k_img.save()
```

    Image saved: /home/sahil/Downloads/KMeansImage/res/batman_KMeans_.jpg


# Interactive For Jupyter Notebook


```python
from KMeansImage import kmeans_image_ui
```

Parameter = Image directory path


```python
k_img = kmeans_image_ui('/home/sahil/Downloads/KMeansImage/res/')
```


![png](https://github.com/imsahil007/KMeansImage/blob/master/res/example.png)



```python
k_img.save()
```

    Image saved: /home/sahil/Downloads/KMeansImage/res/sherlock_KMeans_.jpg

# Jupyter Notebook Dependency:
```
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

You can also download using Github:
  - Download and extract this repo
  - Move the terminal to the directory of setup.py
  ```
  pip install .
  ```

# Packages Required:
- numpy
- scikit-learn
- matplotlib
- ipywidgets





#### Contact Me:

[Sahil](https://github.com/imsahil007)


### Todos

 - Add a button for saving images instead of save() in interactive notebook
 - Add some boundary conditions
 - Add Test cases

License
----

MIT


**Free Software, Hell Yeah!**

