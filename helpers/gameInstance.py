import Box2D
import pygame

from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper


class GameInstance:
    def __init__(self, gravity):
        self.PPM = 20
        self.FPS = 60
        self.TIME_STEP = 1.0 / self.FPS
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 400
        self.INPUT_SENSITIVITY = 10

        self.gameActive = True

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.world = Box2D.b2World(gravity, doSleep=True)
        self.clock = pygame.time.Clock()

        self.b2PyHelper = B2PyHelper(self.PPM, self.WINDOW_HEIGHT)
        self.b2Helper = B2Helper(self.world, self.PPM)
