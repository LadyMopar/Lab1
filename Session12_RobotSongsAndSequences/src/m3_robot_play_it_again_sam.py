"""
This module lets you integrate:
  -- SEQUENCES, and
  -- ROBOT METHODS.

Authors: David Mutchler, Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Lexi Harris and Emily Richardson.  September 2013.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

#-----------------------------------------------------------------------
# TODO: 2. Implement a program that accomplishes the specification
#   that is sketched in the attached    PlayItAgainSam_picture.pdf.
#
#   IMPORTANT:
#     1. Implement using ITERATIVE ENHANCEMENT:
#          -- Implement a bit and test that bit, getting it to work.
#          -- Implement a bit more and test it, getting it to work.
#          -- Etc until the entire program works corectly.
#
#     2. Put meaningful chunks of work into FUNCTIONS.
#        Do NOT put the entire program (i.e., all the code) in main!
#
#     3. Write and use TEST FUNCTIONS as needed (but only as needed).
#
#     4. Include BRIEF but MEANINGFUL comments AS YOU WRITE THE CODE.
#-----------------------------------------------------------------------

import new_create
import time
import zellegraphics as zg


def main():
    """ Calls the other functions in this module, as needed. """
    port = 'sim'
    robot = new_create.Create(port)
    robot.toSafeMode()

    window = zg.GraphWin('notes', 485, 200)
    rect1 = zg.Rectangle(zg.Point(0, 0), zg.Point(485, 100))
    rect2 = zg.Rectangle(zg.Point(0, 100), zg.Point(485, 200))
    rect1.setFill('black')
    rect2.setFill('yellow')
    rect1.draw(window)
    rect2.draw(window)
    song = []
    while True:
        point = window.getMouse()
        if point.y < window.height / 2:
            circle = zg.Circle(point, 5)
            circle.setFill('white')
            circle.draw(window)
            pitch = round((point.x / 485) * 96) + 31
            robot.playNote(pitch, 1)
            song.append(pitch)
        else:
            for k in range(len(song)):
                robot.playNote(song[k], 1)
                time.sleep(1.001)
            break

    mary = [64, 62, 60, 62, 64, 64, 64, 62, 62, 62, 60, 67, 67, 64, 62, 60, 62, 64, 64, 64, 62, 62, 64, 62, 60]
    for k in range(len(mary)):
        robot.playNote(mary[k], 1)
        time.sleep(1.001)


    window.close()
    robot.shutdown()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
