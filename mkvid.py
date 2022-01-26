# importing libraries
import os
import cv2
from PIL import Image


# Video Generating function
def generate_video():
	image_folder = '/home/aniket/NEU_Courses/PRCV/Project/gradient_lidar'
	video_name = 'lidar_gradient.avi'
	os.chdir("/home/aniket/NEU_Courses/PRCV/Project/")
	
	images = [img for img in os.listdir(image_folder)
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	
	# Array images should only consider
	# the image files ignoring others if any
	print(sorted(images))

	frame = cv2.imread(os.path.join(image_folder, images[0]))

	# setting the frame width, height width
	# the width, height of first image
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 10, (width, height))

	# Appending the images to the video one by one
	for image in sorted(images):
		video.write(cv2.imread(os.path.join(image_folder, image)))
	
	# Deallocating memories taken for window creation
	cv2.destroyAllWindows()
	video.release() # releasing the video generated


# Calling the generate_video function
generate_video()
