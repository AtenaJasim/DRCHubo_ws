# Description
Simulate the humanoid robot DRC Hubo in Rviz using moveit. Includes all of his body meshes and his custom grippers.

## Prerequisites
```
Ros2 Humble
Moveit2
Rviz2
```
## How to Launch
```
Command to launch moveit demo with Hubo's full body and grippers : ros2 launch hubo_gripper_moveit_config demo.launch.py
Command to move DRC Hubo's arms programmatically: ros2 launch moveit2_scripts test_trajectory.launch.py
```

