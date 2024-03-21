# ROBOLIFT

this project use ros2 distro is humble.

# Getting started
1.Clone the repo:
```
git clone https://github.com/Mosseir/ROBOLIFT
```
2.Navigate to your workspace:
```
cd ~/robotics_lab_ws
```
3.Update dependencies:
```
rosdep update
```
4.Install dependencies:
```
rosdep install --ignore-src --from-paths src -y -r
```
5.Compile
```
colcon build
```
# Operating Instructions
After you build, remember to source the proper install folder...
```
source ~/robotics_lab_ws_ws/install/local_setup.bash
```
And then run the launch file...
```
ros2 launch articubot_one rsp.launch.py
```
After that run the this file to control robot
```
ros2 run articubot_one Controller.py
```
