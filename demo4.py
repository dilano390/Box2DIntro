import Box2D
import pygame

# Importing necessary functions and classes from helper modules
from helpers.b2Functions import drawGame
from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper
from helpers.gameInstance import GameInstance

# Function to determine the velocity based on pressed keys
def determineVelocity(sensitivity: float) -> Box2D.b2Vec2:
    velY = 0
    velX = 0
    keys = pygame.key.get_pressed()

    # Checking pressed keys to determine velocity in X and Y directions
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        velY += sensitivity
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        velY -= sensitivity
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        velX += sensitivity
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        velX -= sensitivity

    return Box2D.b2Vec2(velX, velY)

# Main function where the game logic resides
def main():
    # Initializing Pygame
    pygame.init()

    # Creating a GameInstance object
    game = GameInstance([0, -9.8])

    # Creating instances of B2Helper and B2PyHelper classes
    b2pyh = B2PyHelper(game.PPM, game.WINDOW_HEIGHT)
    b2h = B2Helper(game.world, game.PPM)

    # Creating a grid of circles
    dx = 0
    dy = 0
    w = 30
    h = 20
    radius = 5
    for i in range(w):
        for j in range(h):
            # Adding circles in a grid pattern
            b2h.addCircleToWorld(b2h.createCircle(0, 0, radius),
                                 b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2 + dx, 3 + dy), 1, 1, 0)
            dx += 5
        dx = 0
        dy += 5

    # Adding a larger box with specific properties
    box = b2h.addBoxToWorld(b2h.createPolygon(0, 0, 30, 30),
                            b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2 + 300, 10), 300, 1, 0)
    # Adding user data to the larger box for color representation
    box.userData = {'color': (255, 0, 255)}

    # Adding edges to the Box2D world for collision boundaries
    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, game.WINDOW_HEIGHT))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH, 0))


    # Game loop
    while game.gameActive:
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameActive = False

        # Filling the screen with a gray color
        game.screen.fill((80, 80, 80))

        # Drawing game objects on the screen
        drawGame(b2pyh, game, game.screen, game.world)

        # Setting linear velocity based on key inputs
        box.linearVelocity = determineVelocity(game.INPUT_SENSITIVITY)

        # Updating the display
        pygame.display.flip()

        # Stepping the Box2D world forward in time
        game.world.Step(game.TIME_STEP, 10, 10)
        game.clock.tick(game.FPS)

# Entry point of the script
if __name__ == '__main__':
    main()
