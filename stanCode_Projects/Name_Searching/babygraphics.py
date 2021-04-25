"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
    fix_width = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)
    x_coordinate = year_index * fix_width + GRAPH_MARGIN_SIZE
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
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


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
    # draw the fixed background grid
    draw_fixed_lines(canvas)
    # Write your code below this line
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            for j in range(len(YEARS)):
                if j+2 <= len(YEARS):
                    x1 = get_x_coordinate(CANVAS_WIDTH, j)
                    x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
                    fix_y = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000
                    year1 = str(YEARS[j])
                    year2 = str(YEARS[j+1])
                    if year1 in name_data[lookup_names[i]]:
                        y1 = int(name_data[lookup_names[i]][year1])*fix_y + GRAPH_MARGIN_SIZE
                        canvas.create_text(x1, y1, text=(lookup_names[i], name_data[lookup_names[i]][year1]), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                    else:
                        y1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                        canvas.create_text(x1, y1, text=(lookup_names[i], "*"), anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                    if year2 in name_data[lookup_names[i]]:
                        y2 = int(name_data[lookup_names[i]][year2])*fix_y + GRAPH_MARGIN_SIZE
                        if j+2 == len(YEARS):
                            canvas.create_text(x2, y2, text=(lookup_names[i], name_data[lookup_names[i]][year2]),
                                               anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                    else:
                        y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                        if j + 2 == len(YEARS):
                            canvas.create_text(x2, y2, text=(lookup_names[i], "*"), anchor=tkinter.SW,
                                               fill=COLORS[i % 4])
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])


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
