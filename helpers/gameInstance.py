import Box2D
import pygame

from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper


class GameInstance:
    def __init__(self, gravity):
        # Set up game parameters
        self.PPM = 20  # Pixels per meter scaling factor
        self.FPS = 60  # Frames per second
        self.TIME_STEP = 1.0 / self.FPS  # Time step for physics simulation
        self.WINDOW_WIDTH = 1200  # Window width in pixels
        self.WINDOW_HEIGHT = 400  # Window height in pixels
        self.INPUT_SENSITIVITY = 10  # Sensitivity for player input

        self.gameActive = True  # Flag to keep the game loop running

        # Initialize pygame display and Box2D world
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.world = Box2D.b2World(gravity, doSleep=True)  # Create a Box2D world with the given gravity
        self.clock = pygame.time.Clock()

        # Create helpers for converting between Box2D vectors and pygame coordinates
        self.b2PyHelper = B2PyHelper(self.PPM, self.WINDOW_HEIGHT)
        self.b2Helper = B2Helper(self.world, self.PPM)