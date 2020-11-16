# # import sys

# # src_path = sys.argv[1] if len(sys.argv) > 1 else '.'

# import os 
# #dir_path = os.path.dirname(os.path.realpath(__file__))

# path2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'FTP1')
# # print (src_path)
# print (path2)


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import glob
import tensorflow as tf
from PIL import Image, ImageDraw, ImageFont
from six import BytesIO
#import io

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.
    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.
    Args:
        path: a file path (this can be local or on colossus)
    Returns:
        uint8 numpy array with shape (img_height, img_width, 3)
    """
    img_data = tf.io.gfile.GFile(path, 'rb').read()
    image = Image.open(BytesIO(img_data))
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)



for image_path in glob.glob('C:/Users/Anders Ormstrup/Dropbox/Anders - UNI/Pre-Thesis VELUX/DEEPLEARNINGSTUFF/TestImg1/*.jpeg'):
    image_np = load_image_into_numpy_array(image_path)
    plt.imshow(image_np)
    plt.show()
    print(image_np)

