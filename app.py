
## Importing necessary libraries
import numpy as np
import os
import sys
import tensorflow as tf
from PIL import Image
sys.path.append("..")

from models.research.object_detection.utils import label_map_util
from models.research.object_detection.utils import visualization_utils as vis_util
from inference_help import load_image_into_numpy_array
from inference_help import run_inference_for_single_image
from flask import Flask,request, render_template,redirect,url_for
from werkzeug.utils import secure_filename
import shutil


## Setting the necessary paths
PATH_TO_FROZEN_GRAPH = 'models/research/saved_model_30000/frozen_inference_graph.pb'

PATH_TO_LABELS = 'models/research/saved_model_30000/labelmap.pbtxt'
PATH_TO_TEST_IMAGES_DIR = 'test_images'




app = Flask(__name__)

# The image which gets through UI wille get saved at this location
app.config["IMAGE_UPLOADS"] = "static/Images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

@app.route('/',methods = ["GET","POST"])
def upload_image():
    ## Loading the trained model
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    ## Loading the labels
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
    save_img = r'runs/detect'



    if request.method == "POST":
        shutil.rmtree('static/Images')
        os.mkdir('static/Images')
        os.mkdir('static/Images/pred_img')

        image = request.files['file']

        filename = secure_filename(image.filename)

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))

        TEST_IMAGE_PATHS = os.path.join(basedir, app.config["IMAGE_UPLOADS"], filename)
        #TEST_IMAGE_PATHS = os.listdir(PATH_TO_TEST_IMAGES_DIR)


        #image = Image.open(os.path.join(PATH_TO_TEST_IMAGES_DIR, image_path))
        image = Image.open(TEST_IMAGE_PATHS)
        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        image_np = load_image_into_numpy_array(image)
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        # Actual detection.
        output_dict = run_inference_for_single_image(image_np, detection_graph)
        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            category_index,
            instance_masks=output_dict.get('detection_masks'),
            use_normalized_coordinates=True,
            line_thickness=8)

        im = Image.fromarray(image_np)
        im.save(f'static/Images/pred_img/{filename}')

        return render_template("index.html", filename=filename)



    return render_template('index.html')


@app.route('/display/<filename>')
def display_image(filename):

    a= "/Images/pred_img/" + filename

    return redirect(url_for('static', filename="/Images/pred_img/" + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True,port=2000)







