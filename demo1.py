import pygame

from helpers.b2Functions import drawGame
from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper
from helpers.gameInstance import GameInstance


def main():
    pygame.init()
    game = GameInstance([0, -9.8])
    b2pyh = B2PyHelper(game.PPM, game.WINDOW_HEIGHT)
    b2h = B2Helper(game.world, game.PPM)
    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2), 100, 1, 4)

    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2 - 40), 30, 5, 4)

    b2h.addBoxToWorld(b2h.createPolygon(0, 0, 10, 10),
                      b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2, game.WINDOW_HEIGHT / 2 - 100), 300, 5, 4)

    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))

    while game.gameActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameActive = False
        game.screen.fill((80, 80, 80))
        drawGame(b2pyh, game, game.screen, game.world)

        pygame.display.flip()

        game.world.Step(game.TIME_STEP, 10, 10)
        game.clock.tick(game.FPS)


if __name__ == '__main__':
    main()
