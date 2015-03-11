"""
This module lets you see the Create ROBOT in a SIMULATOR.

Authors: David Mutchler, Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, Katie Dion & their colleagues. September 2013.
"""
#-----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
#     *** GET YOUR INSTRUCTOR TO SHOW YOU HOW TO USE THE SIMULATOR. ***
#     *** You must RUN THE SIMULATOR   BEFORE   starting this program!
#-----------------------------------------------------------------------

import new_create
import time


def main():
    """ Demonstrates the use of the Create Robot's SIMULATOR. """
    port = 'sim'  # Note the quotes.
    wall_E = new_create.Create(port)

    go_until_bumped(wall_E, 10)

    wall_E.go(0, 90)
    time.sleep(2.0)
    wall_E.stop()

    go_until_bumped(wall_E, 30)

    time.sleep(3)  # To see the final state briefly in the simulator.
    wall_E.shutdown()


def go_until_bumped(robot, centimeters_per_second):
    """
    Makes the given robot go forward at the given speed
    until the robot bumps into something, at which point it stops.

    Preconditions: The first argument is a Create (connected to a
        Create robot).  The second argument is a reasonable speed.
    """
    sensor_name = new_create.Sensors.bumps_and_wheel_drops

    robot.go(centimeters_per_second, 0)
    while True:
        sensor_values = robot.getSensor(sensor_name)

        # The  bumps_and_wheel_drops  sensor returns a LIST of 5 items.
        # The last two are the states of the left and right bumpers:
        #   1 for "pressed"   or 0 for "not pressed"
        left_bumper_state = sensor_values[3]
        right_bumper_state = sensor_values[4]

        if left_bumper_state == 1 or right_bumper_state == 1:
            robot.stop()
            break

        time.sleep(0.05)  # To be sure not to flood the robot with msgs.

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
