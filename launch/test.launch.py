import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    fetch_position = launch_ros.actions.Node(
        package = 'satellite_position',
        executable = 'fetch_position',
    )

    receive_position = launch_ros.actions.Node(
        package = 'satellite_position',
        executable = 'receive_position',
        output = 'screen',
    )

    return launch.LaunchDescription([fetch_position,receive_position])
