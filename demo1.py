import pygame

from helpers.b2Functions import drawGame
from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper
from helpers.gameInstance import GameInstance


def main():
    # Initialize pygame
    pygame.init()

    # Create an instance of the GameInstance class
    game = GameInstance([0, -9.8])

    # Create instances of the B2PyHelper and B2Helper classes
    b2pyh = B2PyHelper(game.PPM, game.WINDOW_HEIGHT)
    b2h = B2Helper(game.world, game.PPM)

    # Create and add static boxes to the world
    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2), 100, 1, 4)
    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2 - 40), 30, 5, 4)
    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2 - 100), 300, 5, 4)

    # Adding edges to the Box2D world for collision boundaries
    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, game.WINDOW_HEIGHT))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH, 0))

    # Set the game loop to run
    game.gameActive = True

    # Main game loop
    while game.gameActive:
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameActive = False

        # Fill the screen with a gray background
        game.screen.fill((80, 80, 80))

        # Draw the game objects using the drawGame function
        drawGame(b2pyh, game, game.screen, game.world)

        # Update the display
        pygame.display.flip()

        # Step the physics simulation (Simulate for time step amount of time)
        game.world.Step(game.TIME_STEP, 10, 10)

        # Advance the clock
        game.clock.tick(game.FPS)


if __name__ == '__main__':
    main()