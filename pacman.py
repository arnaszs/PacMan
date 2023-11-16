import pygame
from vector import myVector
import numpy as np


class Node(object):
    def __init__(self, x, y, isGhostHome=False):
        self.position = myVector(x, y)
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None, PORTAL:None}
        self.isGhostHome = isGhostHome


class Maze(object):
    def __init__(self, level):
        self.level = level
        self.nodes = {} # the games nodes
        self.nodeSymbols = ['+', 'P', 'n', 'G']
        self.pathSymbols = ['.', '-', '|', 'p']
        self.homekey = None
        self.buildMaze()


class buildMaze(self):
    ''' Generating a maze from a link '''