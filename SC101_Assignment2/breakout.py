"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: 黃元品
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    dx = graphics.get_dx()
    dy = graphics.get_dy()
    life = NUM_LIVES

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.is_start:  # check if the mouse already clicked to start the game
            graphics.ball.move(dx, dy)
            if graphics.ball.x + graphics.ball_diameter >= graphics.window.width or graphics.ball.x <= 0:
                graphics.prior_collide_obj = 'wall'
                dx = -dx
            elif graphics.ball.y <= 0:
                graphics.prior_collide_obj = 'wall'
                dy = -dy
            elif graphics.ball.y >= graphics.window.height:
                graphics.prior_collide_obj = 'wall'
                life -= 1
                graphics.reset_ball()

        if graphics.check_remove():  # if collide sth. then bounce and decide remove or not
            dy = -dy

        if graphics.get_brick_count() == 0:  # win condition
            graphics.win()
            break

        if life == 0:  # lose condition
            graphics.gameover()
            break


if __name__ == '__main__':
    main()
