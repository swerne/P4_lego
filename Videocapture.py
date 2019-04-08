"""
To do:
Læs farve billed
læs dybde billed (done)

modtag inputs (semi done)
bekræft inputs

Gem inputs i ordenligt format.

"""

import os
import numpy as np
import cv2
from openni import openni2
from primesense import _openni2 as c_api
import matplotlib.pyplot as plt

openni2.initialize("C:\Program Files\OpenNI2\Redist")     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()

#depth_stream = dev.create_depth_stream() dev.create_color_stream()
#depth_stream = dev.create_depth_stream()
#depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))

color_stream = dev.create_color_stream()
color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_COLOR_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))

depth_stream.start()

while(True):
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    img = np.frombuffer(frame_data, dtype=np.uint16)
    img.shape = (1, 480, 640)
    img = np.concatenate((img, img, img), axis=0)
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 0, 1)

    cv2.imshow("image", img)
    cv2.waitKey(25)

depth_stream.stop()
openni2.unload()