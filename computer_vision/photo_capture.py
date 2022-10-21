import requests
from PIL import Image
from io import BytesIO
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def PullFrameFromStream():
    print("Requesting a frame from the stream...")
    resp = requests.get(url, stream=True)
    print("got response", resp.status_code)
    if (resp.status_code == 200):
        jpeg_chunk = bytearray()
        for chunk in resp.iter_content(chunk_size=1024): 
            jpeg_chunk += chunk 
            a = jpeg_chunk.find(b'\xff\xd8')
            b = jpeg_chunk.find(b'\xff\xd9')
            if a != -1 and b != -1: 
                jpg = jpeg_chunk[a:b+2]
                break
            
        img = Image.open(BytesIO(jpg))
        print("img is open")
        img_crop_map = img.crop(crop_area)
        print("image is cropped")
        img_crop_map.save(os.path.dirname(__file__) + '/LastFrame_map.jpg', 'jpeg') # saves in same directory as this script
        return img_crop_map
    else: # Other http responses will return None. 500 is common.
        print(resp)
