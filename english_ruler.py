#!/usr/bin/python3
"""
   This modules contains functions to draw an english
   ruler recursively
"""


def draw_line(tick_length, tick_label=""):
    """
      Draw one line with a given followed by optional label

    Parameters
    ----------
    tick_length: int
           Number of ticks to draw
    tick_label: string (optional)
           Label to add to the tick

    Returns
    -------
    None

    """

    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """
       Draw the interval based on the central tick lenght.

    Parameters
    ----------
    center_length : int
       central tick length

    """

    if center_length > 0:
        draw_interval(center_length - 1) # recursively draw top ticks
        draw_interval(center_length) # draw center tick
        draw_interval(center_length - 1) # recursively draw bottom ticks


def draw_ruler(num_inches, major_length):
    """
       Draw English ruler with given number of inches, major tick length

    Parameters
    ----------
    num_inches : int
        Number of inches
    major_length : int
        number of ticks for inches
    """

    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == "__main__":
    # runs tests
    draw_ruler(10, 5);
