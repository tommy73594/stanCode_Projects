"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the click circle
SIZE = 10
# Global variables
window = GWindow(title='draw_line')
position = None  # This constant saves the prior position


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(click)


def click(event):
    global position
    circle = GOval(SIZE, SIZE)

    # if there is a prior position, then it needs to draw a line base on the prior click position
    # and the current click position, if not, then it means to add a circle,
    # and save the position to wait next click in order to create a line
    if not position:  # if no prior position
        window.add(circle, event.x-SIZE/2, event.y-SIZE/2)
        position = [event.x, event.y]
    else:  # there is a prior position, draw the line and delete the prior circle
        obj1 = window.get_object_at(position[0], position[1])
        window.remove(obj1)
        window.add(GLine(position[0], position[1], event.x, event.y))
        position = None  # reset to None for the next line


if __name__ == "__main__":
    main()
