"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

File: breakoutgraphics.py
Name: 黃元品
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
import functools


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        paddle_x_position = (window_width - paddle_width) / 2
        paddle_y_position = window_height - paddle_offset
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height, x=paddle_x_position, y=paddle_y_position)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_x_position = window_width / 2 - ball_radius
        self.ball_y_position = window_height / 2 - ball_radius
        self.ball_diameter = ball_radius * 2
        self.ball = GOval(self.ball_diameter, self.ball_diameter, x=self.ball_x_position, y=self.ball_y_position)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx

        # Initialize our mouse listeners
        self.is_start = False
        onmouseclicked(self.start_ball)
        onmousemoved(self.paddle_move)

        # Draw bricks
        brick_init_row_position = 0
        self.__brick_count = brick_rows * brick_cols  # count the total brick
        for row in range(brick_rows):
            brick_init_col_position = brick_offset
            for col in range(brick_cols):
                rect = GRect(brick_width, brick_height,
                             x=brick_init_row_position,
                             y=brick_init_col_position)
                rect.filled = True
                # decide color
                if col % 11 == 0 or col % 11 == 1:
                    rect.fill_color = 'red'
                elif col % 11 == 2 or col % 11 == 3:
                    rect.fill_color = 'orange'
                elif col % 11 == 4 or col % 11 == 5:
                    rect.fill_color = 'yellow'
                elif col % 11 == 6 or col % 11 == 7:
                    rect.fill_color = 'green'
                elif col % 11 == 8 or col % 11 == 9:
                    rect.fill_color = 'blue'

                self.window.add(rect)
                brick_init_col_position += (brick_height + brick_spacing)

            brick_init_row_position += (brick_width + brick_spacing)
        # initial condition
        self.score = 0
        self.label_score = GLabel('Score: ' + str(self.score))
        self.label_score.font = "SansSerif-18"
        self.window.add(self.label_score, 0, self.window.height)
        self.prior_collide_obj = None

    # make sure the paddle is in the window, and move with the mouse
    def paddle_move(self, event):
        if event.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x == self.window.width - self.paddle.width
        elif event.x - self.paddle.width/2 <= 0:
            self.paddle.x == 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2

        self.paddle.y = self.window.height - self.paddle_offset
        self.window.add(self.paddle)

    def start_ball(self, event):
            self.is_start = True

    # getter
    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy

    def get_brick_count(self):
        return self.__brick_count

    # if ball drop, reset it to the middle of the window
    def reset_ball(self):
        self.is_start = False
        self.ball.x = self.ball_x_position
        self.ball.y = self.ball_y_position

    # check if the ball collide anything
    def is_collision(func):
        @functools.wraps(func)
        def check_collision(self):
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
            if self.obj is not None:
                return func(self)
            self.obj = self.window.get_object_at(self.ball.x + self.ball_diameter, self.ball.y)
            if self.obj is not None:
                return func(self)
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_diameter)
            if self.obj is not None:
                return func(self)
            self.obj = self.window.get_object_at(self.ball.x + self.ball_diameter, self.ball.y + self.ball_diameter)
            if self.obj is not None:
                return func(self)
            return False

        return check_collision

    # remove the brick if collide
    @is_collision
    def check_remove(self):
        if self.obj == self.paddle:
            if self.prior_collide_obj != 'paddle':  # prevent bounce twice on the paddle
                self.prior_collide_obj = 'paddle'
                return True
            else:
                return False
        elif self.obj == self.label_score:
            return False
        else:
            self.window.remove(self.obj)
            self.score += 1
            self.__brick_count -= 1
            self.label_score.text = 'Score: ' + str(self.score)
            self.prior_collide_obj = 'brick'
            return True

    # gameover label
    def gameover(self):
        self.window.remove(self.ball)
        label_gameover = GLabel("Game Over!")
        label_gameover.font = "SansSerif-18"
        x = (self.window.width - label_gameover.width) / 2
        y = (self.window.height + label_gameover.ascent) / 2
        self.window.add(label_gameover, x, y)

    # win label
    def win(self):
        self.window.remove(self.ball)
        label_win = GLabel("Win!")
        label_win.font = "SansSerif-18"
        x = (self.window.width - label_win.width) / 2
        y = (self.window.height + label_win.ascent) / 2
        self.window.add(label_win, x, y)

