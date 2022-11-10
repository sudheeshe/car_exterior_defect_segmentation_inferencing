
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

- Labeling was done with `LabelImg` tool and labels are saved on `.txt` format

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/5.jpg?raw=true)


## Model Building and Evaluation

- Used YoloV5 model for detection.
- YoloV5 trained from scratch to 1500 epochs on Paperspace P4000 GPU.
- YoloV5 does image augmentation internally on training images which helps in better predictions and reduce overfitting.

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/6.jpg?raw=true)

Let's visualize some of our `training image batch` and `validation image batch`

#### Training image batch with Mosaic augmentation applied

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/train_tile_batch.jpg?raw=true)

#### Validation image batch

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/val_tile_batch.jpg?raw=true)


- Let's see the `mAP` for first `100 epochs`. The mAP was `0.0086`

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/Reports/100_epoch_eport.png?raw=true)


- The mAP for `1500 epochs` reached to `0.811` at mAP@0.5 (means mAP at threshold of 0.5). 
- I've tried to run the model for another 200 epochs but the model didn't show any improvement in mAP beyond 1500 epochs.

#### Precision-Recall Curve

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/YoloV5_Training/yolov5/runs/train/yolov5s_results8/PR_curve.png?raw=true)

#### F1 Curve

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/YoloV5_Training/yolov5/runs/train/yolov5s_results8/F1_curve.png?raw=true)

- The F1 curve shows that any threshold (confidence) value between 0.2 to almost 0.6 gives better results from the model

#### Confusion Matrix

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/YoloV5_Training/yolov5/runs/train/yolov5s_results8/confusion_matrix.png?raw=true)

- The model has less prediction power on `spurious_copper` class and very high confidence on `missing_hole` and other classes have decent prediction capability.

## Prediction Images

- In order to do prediction on new images please find my another repository

[Github link](https://github.com/sudheeshe/PCB_Defect_Detection)

- The UI is used for individual predictions by uploading the image

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/UI.jpg?raw=true)

- Let's see some prediction done by the model through UI

![alt text](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/imgs_readme/pred_collage.jpg?raw=true)


## Video Demo

[click here](https://www.youtube.com/watch?v=oRXxbZ7rxrI&ab_channel=SudheeshE)


## References:
#### How to do training and inferencing 
[click here](https://github.com/sudheeshe/PCB_Defect_Detection_Training/blob/main/How_to_run.txt)

#### YoloV5 custom training helper repo
[click here](https://github.com/sudheeshe/YoloV5_Custom_training_template)
