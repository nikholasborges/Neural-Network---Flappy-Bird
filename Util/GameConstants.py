import os
import pygame


class Global:
    WIDTH = 600
    HEIGHT = 1000
    BACKGROUND_SPRITE = os.path.join('.\\Resources\\img', 'background.png')


class Bird:
    BIRD_SPRITE = [os.path.join('.\\Resources\\img', 'bird-0.png'),
                   os.path.join('.\\Resources\\img', 'bird-1.png'),
                   os.path.join('.\\Resources\\img', 'bird-2.png'),
                   os.path.join('.\\Resources\\img', 'bird-3.png')]

    MAX_ROTATION = 20
    ROTATION_VELOCITY = 20
    JUMP_HEIGHT = -8
    DISPLACEMENT_LIMIT = 10
    DEFAULT_DRAW_X_AXIS = 250
    DEFAULT_DRAW_Y_AXIS = 250

class Pipe:
    PIPE_SPRITE = os.path.join('.\\Resources\\img', 'pipe.png')
    GAP = 180
    VELOCITY = 5
    DRAW_SPEED = 800


class Floor:
    FLOOR_SPRITE = os.path.join('.\\Resources\\img', 'floor.png')
    VELOCITY = 5
    DEFAULT_HEIGHT = 870
