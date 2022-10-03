import pygame
import random
import math
from Wall import Wall


class Map:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.seed = None
        self.map_squares = None
        self.start_positions = None
        self.columns = None
        self.rows = None
        self.walls = []
        self.walls_listed = []
        self.end_points = []

        self.spacing_x = 0
        self.spacing_y = 0
        self.top_y = 0
        self.left_x = 0
        self.width = 0
        self.height = 0

    def generate_map(self, seed):
        self.seed = seed
        self.map_squares, self.start_positions = self.decode_seed(self.seed)
        self.columns = len(self.map_squares)
        self.rows = len(self.map_squares[0])
        self.definitions()
        self.walls = []
        self.walls_listed = []
        self.end_points = []
        for i in range(len(self.map_squares)):
            col = []
            for j in range(len(self.map_squares[i])):
                row = [None, None, None, None]
                if self.map_squares[i][j][0] == 1:
                    wall = Wall(self.screen, (self.get_xy_position(i + 1, j)), (self.get_xy_position(i + 1, j + 1)), 0)
                    self.walls.append(wall)
                    row[0] = wall
                    self.end_points.append((self.get_xy_position(i + 1, j)))
                    self.end_points.append((self.get_xy_position(i + 1, j + 1)))
                if self.map_squares[i][j][1] == 1:
                    wall = Wall(self.screen, (self.get_xy_position(i, j)), (self.get_xy_position(i + 1, j)), 1)
                    self.walls.append(wall)
                    row[1] = wall
                    self.end_points.append((self.get_xy_position(i, j)))
                    self.end_points.append((self.get_xy_position(i + 1, j)))
                if self.map_squares[i][j][2] == 1:
                    wall = Wall(self.screen, (self.get_xy_position(i, j + 1)), (self.get_xy_position(i, j)), 2)
                    self.walls.append(wall)
                    row[2] = wall
                    self.end_points.append((self.get_xy_position(i, j + 1)))
                    self.end_points.append((self.get_xy_position(i, j)))
                if self.map_squares[i][j][3] == 1:
                    wall = Wall(self.screen, (self.get_xy_position(i + 1, j + 1)), (self.get_xy_position(i, j + 1)), 3)
                    self.walls.append(wall)
                    row[3] = wall
                    self.end_points.append((self.get_xy_position(i + 1, j + 1)))
                    self.end_points.append((self.get_xy_position(i, j + 1)))
                col.append(row)
            self.walls_listed.append(col)

        self.width = self.spacing_x * self.columns
        self.height = self.spacing_y * self.rows


    def definitions(self):
        self.spacing_x = 90
        self.spacing_y = 90
        self.top_y = (self.screen.get_height() / 2) - ((self.rows * self.spacing_y) / 2)
        self.left_x = (self.screen.get_width() / 2) - ((self.columns * self.spacing_x) / 2)

    def generate_seed(self):
        """return a string where the first set of values are the columns and rows,
        the next 8 values represent starting positions,
         and the rest represent barrier locations
         form : 'col;row s1x;s1y s2x;s2y s3x;s3y s4x;s4y 0;1;0;0|0;0;1;0|1;0;0;1 ...'"""
        map_squares = []
        columns = random.randint(10, 14)
        rows = random.randint(5, 7)
        self.rows = rows
        self.columns = columns
        self.definitions()
        for i in range(columns):
            col = []
            for j in range(rows):
                if i == 0 and j == 0:
                    row = [0, 1, 1, 0]
                elif i == 0 and j == rows - 1:
                    row = [0, 0, 1, 1]
                elif i == columns - 1 and j == 0:
                    row = [1, 1, 0, 0]
                elif i == columns - 1 and j == rows - 1:
                    row = [1, 0, 0, 1]
                elif i == 0:
                    row = [0, 0, 1, 0]
                elif j == 0:
                    row = [0, 1, 0, 0]
                elif i == columns - 1:
                    row = [1, 0, 0, 0]
                elif j == rows - 1:
                    row = [0, 0, 0, 1]
                else:
                    row = [0, 0, 0, 0]
                col.append(row)
            map_squares.append(col)

        for i in range(1, columns - 1):
            for j in range(1, rows - 1):
                spot = random.randint(0, 3)
                if spot == 0:
                    map_squares[i][j][0] = 1
                    map_squares[i + 1][j][2] = 1
                elif spot == 1:
                    map_squares[i][j][1] = 1
                    map_squares[i][j - 1][3] = 1
                elif spot == 2:
                    map_squares[i][j][2] = 1
                    map_squares[i - 1][j][0] = 1
                elif spot == 3:
                    map_squares[i][j][3] = 1
                    map_squares[i][j + 1][1] = 1


        start1 = [0, 0]
        start2 = [columns - 1, rows - 1]
        start3 = [columns-1, 0]
        start4 = [0, rows - 1]

        seed = "{};{} {};{};{} {};{};{} {};{};{} {};{};{} ".format(columns, rows,
                                                                   self.get_xy_position(start1[0], start1[1])[0] + (self.spacing_x / 2) - 20,
                                                                   self.get_xy_position(start1[0], start1[1])[1] + (self.spacing_y / 2) - 25,
                                                                   -math.pi / 4,
                                                                   self.get_xy_position(start2[0], start2[1])[0] + (self.spacing_x / 2) - 20,
                                                                   self.get_xy_position(start2[0], start2[1])[1] + (self.spacing_y / 2) - 25,
                                                                   (3 * math.pi) / 4,
                                                                   self.get_xy_position(start3[0], start3[1])[0] + (self.spacing_x / 2) - 20,
                                                                   self.get_xy_position(start3[0], start3[1])[1] + (self.spacing_y / 2) - 25,
                                                                   -(3 * math.pi) / 4,
                                                                   self.get_xy_position(start4[0], start4[1])[0] + (self.spacing_x / 2) - 20,
                                                                   self.get_xy_position(start4[0], start4[1])[1] + (self.spacing_y / 2) - 25,
                                                                   math.pi / 4)
        string_cols = ""

        for i in range(len(map_squares)):
            row = ""
            for j in range(len(map_squares[i])):
                box = ""
                for x in map_squares[i][j]:
                    box += str(x) + ";"
                box = box[0:-1]
                row += box + "|"
            row = row[0:-1]
            string_cols += row + " "
        string_cols = string_cols[0:-1]
        seed += string_cols

        self.seed = seed
        self.map_squares = map_squares
        return seed, map_squares

    def decode_seed(self, seed):
        """decodes seed based on the generation above"""
        components = seed.split()
        col_and_row = components[0].split(";")
        map_squares = []
        for i in range(int(col_and_row[0])):
            roww = []
            col = components[5 + i].split("|")
            for j in range(int(col_and_row[1])):
                box = []
                row = col[j].split(";")
                for k in range(4):
                    box.append(int(row[k]))
                roww.append(box)
            map_squares.append(roww)

        start_positions = []
        for i in range(4):
            start_positions.append(components[i + 1].split(";"))

        self.map_squares = map_squares
        self.start_positions = start_positions
        return map_squares, start_positions

    def get_xy_position(self, col, row):
        """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
        return self.left_x + col * self.spacing_x, self.top_y + row * self.spacing_y

    def get_col_row(self, x, y):
        """ Converts an x, y screen position into a col, row value. """
        # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
        return int((x - self.left_x) // self.spacing_x), int((y - self.top_y) // self.spacing_y)

    def draw(self):
        for wall in self.walls:
            wall.draw()
