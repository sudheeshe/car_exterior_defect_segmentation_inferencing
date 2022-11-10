
# Car Exterior Defect Detection

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/1_.jpg?raw=true)

### Artificial Intelligence in Vehicle Inspection.

- Inspections are critical throughout a vehicle’s lifespan. Nonetheless, vehicle inspections can be time-consuming. 
- By combining AI in the car inspection business, we can automate inspections in vehicles on various stages – manufacturing, shipping, bought/sold, renting, and repair – and determinate the vehicle condition at a specific point in time. So, Artificial intelligence is changing the entire car inspection process, with an immediate return on your investment
- Automatic Vehicle Inspection saves time, reduce costs, and improve reliability of car inspection businesses.
- With artificial intelligence, it’s possible to identifies and classifies damages in vehicles, and estimation of repair costs according to damage location and characteristics.
- The best… the process can be done in real time on site, or the images can be collected and be processed afterwards. This makes the process of vehicle inspection cost-efficient an improve the business reliability.


## Business Scenario

- The Client is looking for an Effective Car Exterior Defect Detection System which detect the following defects.

        1. Paint Scratches
        2. Dents
      

## Data Understanding

- The available dataset have total 459 images for Training and 61 images for Validation 


Let's see some sample from training data

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/2_.jpg?raw=true)


## Data Labeling

- Labeling was done with `Labelme` tool and labels are saved on `.json` format

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/3_.jpg?raw=true)


## Model Building and Evaluation

- Used `mask_rcnn_inception_v2_coco` model for segmentation from TFOD 1.X.
- `mask_rcnn_inception_v2_coco` trained from scratch to 30000 epochs on Paperspace P4000 GPU.
- The loss for `8000 epochs` reached to `1.982` from `5.5`.

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/5_.jpg?raw=true)


- I've tried to run the model for total `30k` epochs and the loss reduced to `1.134`.

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/6_.jpg?raw=true)



## Prediction Images

- UI is used for individual predictions by uploading the image

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/7_.jpg?raw=true)

- Let's see some prediction done by the model through UI

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/8_.jpg?raw=true)


## Video Demo

[click here](https://www.youtube.com/watch?v=JV4_exl785M&ab_channel=SudheeshE)


## References:

#### TFOD 1.X custom training helper repo
[click here](https://github.com/sudheeshe/TFOD_1_Custom_Instance_Segmenation_Template)


## Improvements needed 

- Need more images for better performance of the model. And we can also do Image Augmentations for better generalized model
- Some of `False Positives (Ability of model not to give false predictions)` and `False Negatives (Ability of the model to detect all the ground truth)` by the model are given below
- `False Positives` are given in `Red` marks and `False Negatives` are given in `Yellow`.

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/9_.jpg?raw=true)

### Note:

- I'm currently unable to do find the performance metrics for the model which I have developed. Due to the issue related to TFOD 1.x.
- We can find the mAP(Mean Average Precision) and mAR (Mean Average Recall) of the model by running `models/research/object_detection/legacy/eval.py` or `models/research/object_detection/model_main.py` file.
- But in TFOD 1.X we have a problem of `excess memory usage` issue. Due to this the programs crashes.

![alt text](https://github.com/sudheeshe/car_exterior_defect_segmentation_inferencing/blob/main/readme_imgs/10_.jpg?raw=true)

[click here detailed demo](https://youtu.be/q7W9b4X4ymg)

