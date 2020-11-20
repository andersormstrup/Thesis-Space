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



# basepath1 = os.path.dirname(os.path.realpath(__file__))
# path1 = os.path.join(basepath, 'FTP1')
# path2 = os.path.join(basepath, 'FTP2')
# path3 = os.path.join(basepath, 'FTP3')

class DLObjectDetector():
    """
    docstring
    """
    def __init__(self):
        basepath1 = os.path.dirname(os.path.realpath(__file__))
        path1 = os.path.join(basepath1, 'label_map1.pbtxt')
        path11 = os.path.join(basepath1, 'object_detection/inference_graph1/saved_model')
        path2 = os.path.join(basepath1, 'label_map2.pbtxt')
        path22 = os.path.join(basepath1, 'object_detection/inference_graph2/saved_model')
        self.labelmap_path1 = path1   #'C:/Users/Ander/Documents/GitHub/Thesis-Space/label_map.pbtxt'
        self.category_index = label_map_util.create_category_index_from_labelmap(self.labelmap_path1, use_display_name=True)
        self.labelmap_path2 = path2
        self.category_index2 = label_map_util.create_category_index_from_labelmap(self.labelmap_path2, use_display_name=True)
        #self.output_directory = 'C:/Users/Ander/Documents/GitHub/Thesis-Space'
        tf.keras.backend.clear_session()
        # start_time4 = time.time()
        # end_time4 = time.time() 
        # print(end_time4 - start_time4)
        self.model = tf.saved_model.load(path11)#'C:/Users/Ander/Documents/GitHub/Thesis-Space/object_detection/inference_graph/saved_model')
        self.model2 = tf.saved_model.load(path22)


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
        
        #start_time2 = time.time()
        img_data = tf.io.gfile.GFile(path, 'rb').read()
        image = Image.open(BytesIO(img_data))
        #= (image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8) - RESHAPING - NOT NEEDED
        Np_array = np.array(image)
        #end_time2 = time.time() 
        #print(end_time2 - start_time2)
        return Np_array


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

    #for image_path in glob.glob('C:/Users/Anders Ormstrup/Dropbox/Anders - UNI/Pre-Thesis VELUX/DEEPLEARNINGSTUFF/TestImg1/*.jpeg'):
    def DetectOnImage(self, image_path):
        image_np = self.load_image_into_numpy_array(image_path)
        
        start_time1 = time.time()
        
        output_dict = self.run_inference_for_single_image(image_np)
        
        end_time1 = time.time() 
        print(end_time1 - start_time1)

        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=12)
        #display(Image.fromarray(image_np))
        #plt.imshow(image_np)
        #plt.show()
        imgt = Image.fromarray(image_np, 'RGB')

        classes = output_dict['detection_classes']
        indexes = np.where(output_dict['detection_scores']>0.5)
        for i in indexes:
            detClas = classes[i]  
        detClasses = []
        for k in detClas:
            detClasses.append(self.category_index2[k]['name'])
        print(detClasses)
        #print(class_names)
        #imgt.save('test.png')
        return imgt, detClasses



    def run_inference_for_single_image2(self, image):
        image = np.asarray(image)
        # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.

        input_tensor = tf.convert_to_tensor(image)

        # The model expects a batch of images, so add an axis with `tf.newaxis`.
        input_tensor = input_tensor[tf.newaxis,...]

        # Run inference
        model_fn = self.model2.signatures['serving_default']
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

    #for image_path in glob.glob('C:/Users/Anders Ormstrup/Dropbox/Anders - UNI/Pre-Thesis VELUX/DEEPLEARNINGSTUFF/TestImg1/*.jpeg'):
    def DetectOnImage2(self, image_path):
        image_np = self.load_image_into_numpy_array(image_path)
        
        start_time1 = time.time()
        
        output_dict = self.run_inference_for_single_image2(image_np)
        
        end_time1 = time.time() 
        print(end_time1 - start_time1)

        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.category_index2,
            instance_masks=output_dict.get('detection_masks_reframed', None),
            use_normalized_coordinates=True,
            line_thickness=12)
        #display(Image.fromarray(image_np))
        #plt.imshow(image_np)
        #plt.show()
        imgt = Image.fromarray(image_np, 'RGB') #To show in GUI canvas.
    
        classes = output_dict['detection_classes']
        indexes = np.where(output_dict['detection_scores']>0.5)
        for i in indexes:
            detClas = classes[i]  
        detClasses = []
        for k in detClas:
            detClasses.append(self.category_index2[k]['name'])
        print(detClasses)
        #print(class_names)
        #imgt.save('test.png')
        return imgt, detClasses




