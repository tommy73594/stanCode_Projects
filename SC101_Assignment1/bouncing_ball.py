"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)  # bouncing ball
count = 0  # count the times that the bouncing already run


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)

    onmouseclicked(bounce)  # once click, then bounce


def bounce(e):
    global ball, count
    if ball.x == START_X and ball.y == START_Y and count < 3:  # check if bouncing running to avoid duplicate run
        vy = 0  # initial y velocity
        while True:
            ball.move(VX, vy)
            vy += GRAVITY  # effect of the gravity
            if ball.y >= window.height:  # once touch the ground, bounce and add the effect of the friction
                vy = -(vy * REDUCE)
            if ball.x >= window.width:  # once bounce to the end then restart to the origin point and count
                window.add(ball, START_X, START_Y)
                count += 1
                break

            pause(DELAY)



if __name__ == "__main__":
    main()
