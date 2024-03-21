import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
)
from launch_ros.actions import Node
import time

from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='articubot_one' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    #gazebo = IncludeLaunchDescription(
    #            PythonLaunchDescriptionSource([os.path.join(
    #               get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    #        )
    world_path = PathJoinSubstitution(
        [FindPackageShare("articubot_one"), "worlds", "map2.world"]
    )
    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            "-s",
            "libgazebo_ros_factory.so",
            "-s",
            "libgazebo_ros_init.so",
            world_path,
        ],
        output="screen",
    )
        

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')

    node_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "gripper_controller",
        ],
    )
    
    node_controller1 = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
        ],
    )

    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        node_controller,
        node_controller1,
    ])