import io
import os
import scipy.misc
import numpy as np
import six
import time
import glob
from IPython.display import display

from six import BytesIO

import matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

import tensorflow as tf

from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

class DLObjectDetector():
    """
    docstring
    """
    def __init__(self):
        self.labelmap_path = 'C:/Users/Anders Ormstrup/Documents/GitHub/Thesis-Space/label_map.pbtxt'

        self.category_index = label_map_util.create_category_index_from_labelmap(self.labelmap_path, use_display_name=True)

        self.output_directory = 'C:/Users/Anders Ormstrup/Documents/GitHub/Thesis-Space'
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load('C:/Users/Anders Ormstrup/Documents/GitHub/Thesis-Space/object_detection/inference_graph/saved_model')

    def load_image_into_numpy_array(self, path):
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

    def run_inference_for_single_image(self, image):
        image = np.asarray(image)
        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis,...]

        # Run inference
        model_fn = self.model.signatures['serving_default']
        output_dict = model_fn(input_tensor)

        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(output_dict.pop('num_detections'))
        output_dict = {key:value[0, :num_detections].numpy() 
                        for key,value in output_dict.items()}
        output_dict['num_detections'] = num_detections

        # detection_classes should be ints.
        output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    
        # Handle models with masks:
        if 'detection_masks' in output_dict:
            # Reframe the the bbox mask to the image size.
            detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                    output_dict['detection_masks'], output_dict['detection_boxes'],
                    image.shape[0], image.shape[1])      
            detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                            tf.uint8)
            output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
        
        return output_dict


    #for image_path in glob.glob('C:/Users/Anders Ormstrup/Dropbox/Anders - UNI/Pre-Thesis VELUX/DEEPLEARNINGSTUFF/TestImg1/*.jpeg'):
    def DetectOnImage(self, image_path):
        image_np = self.load_image_into_numpy_array(image_path)
        output_dict = self.run_inference_for_single_image(image_np)
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=8)
        display(Image.fromarray(image_np))
        plt.imshow(image_np)
        plt.show()


