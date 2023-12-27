import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_desription():

        talker = launch_ros.actions.Node(
                package='mypkg',
                executable='talker'
                )
        listener = launch_ros2.actions.Node(
                package='mypkg',
                executable='listener'
                output='screen'
                )

        return launch.LaunchDescription([talker, listener[)
