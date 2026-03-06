"""
WRITE YOUR PROGRAM HEADER HERE
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze


class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze                  # The maze to solve
        self.ss = searchStructure()        # Stack or Queue instance

    # ----------------------------
    # Helper methods (robust access)
    # ----------------------------
    def _is_wall(self, tile):
        # Try common method names first
        if hasattr(tile, "isWall") and callable(tile.isWall):
            return tile.isWall()
        if hasattr(tile, "getIsWall") and callable(tile.getIsWall):
            return tile.getIsWall()
        if hasattr(tile, "is_wall") and callable(tile.is_wall):
            return tile.is_wall()
        if hasattr(tile, "getWall") and callable(tile.getWall):
            return tile.getWall()

        # Try common attribute names
        if hasattr(tile, "isWall"):
            return bool(tile.isWall)
        if hasattr(tile, "is_wall"):
            return bool(tile.is_wall)

        # Last resort: private name-mangled attribute from "__isWall"
        if hasattr(tile, "_Tile__isWall"):
            return bool(getattr(tile, "_Tile__isWall"))

        # If we can't find it, assume not a wall (so tests show a clearer failure elsewhere)
        return False

    def _is_visited(self, tile):
        # Method names
        if hasattr(tile, "isVisited") and callable(tile.isVisited):
            return tile.isVisited()
        if hasattr(tile, "getVisited") and callable(tile.getVisited):
            return tile.getVisited()

        # Attribute names (your PDF shows "visited" exists)
        if hasattr(tile, "visited"):
            return bool(tile.visited)

        # Last resort: private name-mangled attribute from "__visited" (if used)
        if hasattr(tile, "_Tile__visited"):
            return bool(getattr(tile, "_Tile__visited"))

        return False

    def _set_visited(self, tile, value=True):
        if hasattr(tile, "visited"):
            tile.visited = value
            return
        if hasattr(tile, "_Tile__visited"):
            setattr(tile, "_Tile__visited", value)
            return
        # If Tile uses a setter method (rare), try it
        if hasattr(tile, "setVisited") and callable(tile.setVisited):
            tile.setVisited(value)

    def _set_previous(self, tile, prev_tile):
        # PDF shows "previous" exists
        if hasattr(tile, "previous"):
            tile.previous = prev_tile
            return
        if hasattr(tile, "_Tile__previous"):
            setattr(tile, "_Tile__previous", prev_tile)
            return
        if hasattr(tile, "setPrevious") and callable(tile.setPrevious):
            tile.setPrevious(prev_tile)

    # ----------------------------
    # Required methods
    # ----------------------------
    def tileIsVisitable(self, row, col):
        # 1) bounds
        if row < 0 or row >= self.maze.num_rows:
            return False
        if col < 0 or col >= self.maze.num_cols:
            return False

        tile = self.maze.contents[row][col]

        # 2) not a wall
        if self._is_wall(tile):
            return False

        # 3) not already visited
        if self._is_visited(tile):
            return False

        return True

    def solve(self):
        # Add the starting tile to ss
        self.ss.add(self.maze.start)

        while not self.ss.isEmpty():
            current = self.ss.remove()

            # Mark current as visited
            self._set_visited(current, True)

            # If current is the goal tile, return it
            if current == self.maze.goal:
                return current

            r = current.getRow()
            c = current.getCol()

            # REQUIRED neighbor order: North, South, East, West
            directions = [
                (r - 1, c),  # North
                (r + 1, c),  # South
                (r, c + 1),  # East
                (r, c - 1),  # West
            ]

            for nr, nc in directions:
                if self.tileIsVisitable(nr, nc):
                    neighbor = self.maze.contents[nr][nc]
                    self._set_previous(neighbor, current)
                    self.ss.add(neighbor)

        # No path found
        return None

    def getPath(self):
        # If goal was never reached, it won't have a previous pointer
        # (also handles "no solution" cleanly)
        goal = self.maze.goal
        start = self.maze.start

        # If start == goal, path is just [start]
        if start == goal:
            return [start]

        # If goal has no previous pointer, no solution
        if getattr(goal, "previous", None) is None and not hasattr(goal, "_Tile__previous"):
            return []

        path = []
        current = goal

        # Walk backward using previous pointers
        while current is not None:
            path.append(current)
            if current == start:
                break

            if hasattr(current, "previous"):
                current = current.previous
            elif hasattr(current, "_Tile__previous"):
                current = getattr(current, "_Tile__previous")
            else:
                # can't follow chain -> treat as no path
                return []

        path.reverse()
        return path

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        solution = self.getPath() or []   # never None
        output_string = self.maze.makeMazeBase()

        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'

        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        for row in output_string:
            print(row)


if __name__ == "__main__":
    maze = Maze([
        "____",
        "S##G",
        "__#_",
        "____"
    ])

    solver = MazeSolver(maze, Stack)  # change Stack -> Queue to test BFS
    solver.solve()
    solver.printSolution()