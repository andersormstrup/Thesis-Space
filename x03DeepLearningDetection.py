## - Imports for Machine Learning Detection --
import io                       # System information handling.
import os                       # Paths handling.
import scipy.misc               # Image handling as array.
import numpy as np              # Math.
import six                      # Utilities for Python 2 and 3.
import time                     # Time handling.
import glob                     # Filename globbing.
from IPython.display import display # Paralel computing for display.
from six import BytesIO         # In memomry bytes buffer.
import matplotlib               # Plotting.
import matplotlib.pyplot as plt # Plotting.
from PIL import Image, ImageDraw, ImageFont # Image handling in python.
import tensorflow as tf         # Tensorflow Root.
# - Function Imports from Tensorflow object detection.
from object_detection.utils import ops as utils_ops 
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# Object detection Class for all Cameras.
class DLObjectDetector():
    # Initilization - Running ONCE.
    def __init__(self):
        basepath1 = os.path.dirname(os.path.realpath(__file__)) # Getting Paths for models.
        path1 = os.path.join(basepath1, 'label_map1.pbtxt') 
        path11 = os.path.join(basepath1, 'object_detection/inference_graph1/saved_model')
        path2 = os.path.join(basepath1, 'label_map2.pbtxt')
        path22 = os.path.join(basepath1, 'object_detection/inference_graph2/saved_model')
        path3 = os.path.join(basepath1, 'label_map3.pbtxt')
        path33 = os.path.join(basepath1, 'object_detection/inference_graph3/saved_model')
        self.labelmap_path1 = path1  
        self.category_index = label_map_util.create_category_index_from_labelmap(self.labelmap_path1, use_display_name=True)
        self.labelmap_path2 = path2
        self.category_index2 = label_map_util.create_category_index_from_labelmap(self.labelmap_path2, use_display_name=True)
        self.labelmap_path3 = path3
        self.category_index3 = label_map_util.create_category_index_from_labelmap(self.labelmap_path3, use_display_name=True)
        tf.keras.backend.clear_session()                # Clear other TF sessions.
        # LOAD MODELS.
        self.model = tf.saved_model.load(path11)
        self.model2 = tf.saved_model.load(path22)
        self.model3 = tf.saved_model.load(path33)

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
        Np_array = np.array(image)
        return Np_array

    # Detect Function on image for MODEL 1.
    def run_inference_for_single_image(self, image):
        image = np.asarray(image)
        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
        input_tensor = tf.convert_to_tensor(image)
        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis,...]
        # Run inference
        model_fn = self.model.signatures['serving_default']
        output_dict = model_fn(input_tensor) # - DETECT ON IMAGE!!! - 1,3 SEC CPU
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

    # Run detection function on images for CAMERA 1.
    def DetectOnImage(self, image_path):
        # Convert image to math array.
        image_np = self.load_image_into_numpy_array(image_path)
        # Run model on image
        output_dict = self.run_inference_for_single_image(image_np)
        # Print boxes on image for display.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=12)
        imgt = Image.fromarray(image_np, 'RGB')
        # Get detected classes as strings FOR UI display.
        classes = output_dict['detection_classes']
        indexes = np.where(output_dict['detection_scores']>0.5) 
        for i in indexes:
            detClas = classes[i]  
        detClasses = []
        for k in detClas:
            detClasses.append(self.category_index[k]['name'])
        print(detClasses)
        return imgt, detClasses

    # Detect Function on image for MODEL 2.
    def run_inference_for_single_image2(self, image):
        image = np.asarray(image)
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis,...]
        model_fn = self.model2.signatures['serving_default']
        output_dict = model_fn(input_tensor) # - DETECT ON IMAGE!!! - 1,3 SEC CPU
        num_detections = int(output_dict.pop('num_detections'))
        output_dict = {key:value[0, :num_detections].numpy() 
                        for key,value in output_dict.items()}
        output_dict['num_detections'] = num_detections
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

    # Run detection function on images for CAMERA 2.
    def DetectOnImage2(self, image_path):
        # Convert image to math array.
        image_np = self.load_image_into_numpy_array(image_path)
        # Run model on image
        output_dict = self.run_inference_for_single_image2(image_np)
        # Print boxes on image for display.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index2,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=12)
        imgt = Image.fromarray(image_np, 'RGB') #To show in GUI canvas.
        # Get detected classes as strings FOR UI display.    
        classes = output_dict['detection_classes']
        indexes = np.where(output_dict['detection_scores']>0.5)
        for i in indexes:
            detClas = classes[i]  
        detClasses = []
        for k in detClas:
            detClasses.append(self.category_index2[k]['name'])
        print(detClasses)
        return imgt, detClasses

    # Detect Function on image for MODEL 3.
    def run_inference_for_single_image3(self, image):
        image = np.asarray(image)
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis,...]
        # Run inference
        model_fn = self.model3.signatures['serving_default']
        output_dict = model_fn(input_tensor) # - DETECT ON IMAGE!!! - 1,3 SEC CPU
        num_detections = int(output_dict.pop('num_detections'))
        output_dict = {key:value[0, :num_detections].numpy() 
                        for key,value in output_dict.items()}
        output_dict['num_detections'] = num_detections
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

    # Run detection function on images for CAMERA 3.
    def DetectOnImage3(self, image_path):
        # Convert image to math array.
        image_np = self.load_image_into_numpy_array(image_path)
        # Run model on image
        output_dict = self.run_inference_for_single_image3(image_np)
        # Print boxes on image for display.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index3,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=12)
        imgt = Image.fromarray(image_np, 'RGB') #To show in GUI canvas.
        # Get detected classes as strings FOR UI display.    
        classes = output_dict['detection_classes']
        indexes = np.where(output_dict['detection_scores']>0.5)
        for i in indexes:
            detClas = classes[i]  
        detClasses = []
        for k in detClas:
            detClasses.append(self.category_index3[k]['name'])
        print(detClasses)
        return imgt, detClasses




