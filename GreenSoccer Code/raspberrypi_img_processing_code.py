Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
from picamera import PiCamera
import numpy as np

# picamera setup
h = 640 # change this to anything < 2592 (anything over 2000 will likely get a memory error when plotting
cam_res = (int(h),int(0.75*h)) # keeping the natural 3/4 resolution of the camera
cam_res = (int(16*np.floor(cam_res[1]/16)),int(32*np.floor(cam_res[0]/32)))
cam = PiCamera()
## making sure the picamera doesn't change white balance or exposure
## this will help create consistent images
cam.resolution = (cam_res[1],cam_res[0])
cam.framerate = 30
time.sleep(2) #let the camera settle
cam.iso = 100
cam.shutter_speed = cam.exposure_speed
cam.exposure_mode = 'off'
gain_set = cam.awb_gains
cam.awb_mode = 'off'
cam.awb_gains = gain_set
# prepping for analysis and recording background noise
# the objects should be removed while background noise is calibrated
data = np.empty((cam_res[0],cam_res[1],3),dtype=np.uint8)
noise = np.empty((cam_res[0],cam_res[1],3),dtype=np.uint8)
x,y = np.meshgrid(np.arange(np.shape(data)[1]),np.arange(0,np.shape(data)[0]))
rgb_text = ['Red','Green','Blue'] # array for naming color
input("press enter to capture background noise (remove colors)")
cam.capture(noise,'rgb')
noise = noise-np.mean(noise) # background 'noise'
# looping with different images to determine instantaneous colors
while True:
    try:
        print('===========================')
        input("press enter to capture image")
        cam.capture(data,'rgb')
        mean_array,std_array = [],[]
        for ii in range(0,3):
            # calculate mean and STDev and print out for each color
            mean_array.append(np.mean(data[:,:,ii]-np.mean(data)-np.mean(noise[:,:,ii])))
            std_array.append(np.std(data[:,:,ii]-np.mean(data)-np.mean(noise[:,:,ii])))
            print('-------------------------')
            print(rgb_text[ii]+'---mean: {0:2.1f}, stdev: {1:2.1f}'.format(mean_array[ii],std_array[ii]))
        # guess the color of the object
        print('--------------------------')
        print('The Object is: {}'.format(rgb_text[np.argmax(mean_array)]))
        print('--------------------------')
    except KeyboardInterrupt:
        break