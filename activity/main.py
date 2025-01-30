'''
You are given a 2D array of size rows x columns, where heights[row][column] represents the height of cell (row, column).

You are situated in the top-left cell (0, 0) and are travelling to the bottom-right cell, (rows - 1, columns - 1). 
You can move up, down, left or right (not diagonal) and wish to find the route that requires the minimum effort to traverse.

For this problem, a route's effort is defined as the maximum absolute difference in heights between two consecutive cells of that route.

For instance, imagine you are riding a bike from one part of your city to another. If there's a route with an elevation change of 
maximum of 3 feet and a route with a maximum elevation change of 30 feet, the minimum effort path would be the route with a maximum 
elevation change of 3 feet. In this case, we would eturn the int 3 as our result for the minimum 
effort path.

Check out the README for your task instructions and examples.
'''

def min_effort_path(heights):
    """ Given a 2D array of heights, write a function to return
        the path with minimum effort.
        A route's effort is the maximum absolute difference in heights 
        between two consecutive cells of the route.
        Parameters
        ----------
        heights : list[list[]] (2D array)
            2D array containing the heights of the available paths
        Returns
        -------
        int
            minimum effort required to navigate the path from (0, 0) to heights[rows - 1][columns - 1]
    """
    pass