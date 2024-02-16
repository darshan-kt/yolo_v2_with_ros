# Create and Compiling the package

    mkdir -p assignment_ws/src
    cd assignment_ws/src
    git clone https://github.com/darshan-kt/yolo_v2_with_ros
    catkin_make


## Enabling webcam using ros script
### Terminal 1: Launching webcam & Visualizing webcam images
    cd assignment_ws
    source devel/setup.bash
    roslaunch webcam_pkg webcam.launch


### Launch YOLO V2 model
    cd assignment_ws
    souce devel/setup.bash
    roslaunch yolo_v2_ros assignment.launch



