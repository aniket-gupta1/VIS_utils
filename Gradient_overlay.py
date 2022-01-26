import os
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
image_folder = '/home/aniket/NEU_Courses/PRCV/Project/output'
output_folder = '/home/aniket/NEU_Courses/PRCV/Project/depth_gradient'


images = [img for img in os.listdir(image_folder)
        if img.endswith(".jpg") or
            img.endswith(".jpeg") or
            img.endswith("png")]

# Appending the images to the video one by one
for image in sorted(images):
    img = plt.imread(os.path.join(image_folder, image))
    plt.imsave(os.path.join(output_folder, image), img, cmap="plasma")