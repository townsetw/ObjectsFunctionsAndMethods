"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and TYLER TOWNSEND.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    circle_and_rectangle()
    two_circles()


def two_circles():
    """
    -- Constructs an rg.RoseWindow. DONE
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible. DONE
           -- They have different radii. DONE
           -- One is filled with some color and one is not filled. DONE
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(1000,1000)

    point1 = rg.Point(500,500)
    circle1 = rg.Circle(point1, 25)
    point2 = rg.Point(200,200)
    circle2 = rg.Circle(point2, 100)



    circle1.attach_to(window)
    circle2.attach_to(window)

    circle1.fill_color = 'red'


    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow. DONE
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible. DONE
          -- The rg.Circle is filled with 'blue' DONE
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness. DONE
          -- Its fill color. DONE
          -- Its center. DONE
          -- Its center's x coordinate.DONE
          -- Its center's y coordinate.DONE
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle. DONE
    -- Waits for the user to press the mouse, then closes the window. DONE

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window = rg.RoseWindow(1000,1000)
    x1 = 400
    y1 = 400
    x2 = (700+600)/2
    y2 = (600+500)/2
    point1 = rg.Point(x1,y1)
    center1 = x1,y1
    center2 = x2,y2


    circle1 = rg.Circle(point1, 50)
    circle1.fill_color = 'blue'
    circle1.outline_thickness = 10
    circle1.attach_to(window)


    corner1 = rg.Point(700,600)
    corner2 = rg.Point(600,500)

    rectangle1 = rg.Rectangle(corner1,corner2)
    rectangle1.outline_thickness = 20
    rectangle1.attach_to(window)

    print(circle1.outline_thickness)
    print(circle1.fill_color)
    print(center1)
    print(x1)
    print(y1)

    print(rectangle1.outline_thickness)
    print('no fill color')
    print(center2)
    print(x2)
    print(y2)

    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
