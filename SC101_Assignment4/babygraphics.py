"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

Name: 黃元品
File: babygraphics.py
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_unit = (width - GRAPH_MARGIN_SIZE*2)/len(YEARS)  # count the width between two year
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * x_unit
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for year in YEARS:  # draw the line of each year
        x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_count = 0  # to decide the color of the line
    height_unit = (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) / 1000  # count the position of the rank
    for name in lookup_names:
        if name in name_data:
            first_dot = True  # check if it is first year, only one year can't draw the line
            x_temp = []  # store the x position
            y_temp = []  # store the y position
            for year in YEARS:
                x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))
                x_temp.append(x)
                year = str(year)
                if year not in name_data[name]:  # rank over 1000
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    y_temp.append(y)
                    canvas.create_text(x+TEXT_DX, y, text=name+' *', anchor=tkinter.SW, fill=COLORS[color_count])
                else:
                    y = int(height_unit * int(name_data[name][year])) + GRAPH_MARGIN_SIZE
                    y_temp.append(y)
                    canvas.create_text(x + TEXT_DX, y, text=name + ' ' + name_data[name][year],
                                       anchor=tkinter.SW, fill=COLORS[color_count])
                if not first_dot:  # only draw the line when it has two position
                    canvas.create_line(x_temp[0], y_temp[0], x_temp[1], y_temp[1], width=LINE_WIDTH, fill=COLORS[color_count])
                    x_temp.pop(0)
                    y_temp.pop(0)
                else:
                    first_dot = False  # already store one position then set it to False
            color_count += 1
            if color_count == len(COLORS):  # the color loop
                color_count = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
