import Box2D
import pygame

from helpers.b2Functions import drawGame
from helpers.b2Helper import B2Helper
from helpers.b2PyHelper import B2PyHelper
from helpers.gameInstance import GameInstance


def determineVelocity(sensitivity: float) -> Box2D.b2Vec2:
    velY = 0
    velX = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        velY += sensitivity
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        velY -= sensitivity
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        velX += sensitivity
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        velX -= sensitivity
    return Box2D.b2Vec2(velX, velY)


def main():
    pygame.init()
    game = GameInstance([0, -9.8])
    b2pyh = B2PyHelper(game.PPM, game.WINDOW_HEIGHT)
    b2h = B2Helper(game.world, game.PPM)

    dx = 0
    dy = 0
    w = 30
    h = 30
    for i in range(w):
        for j in range(h):
            b2h.addBoxToWorld(b2h.createPolygon(0, 0, 5, 5),
                              b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2 + dx, 3 + dy), 1, 1, 0)
            dx += 5
        dx = 0
        dy += 5

    box = b2h.addBoxToWorld(b2h.createPolygon(0, 0, 30, 30),
                            b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH / 2 + 300, 10), 300, 1, 0)
    box.userData = {'color': (255, 0, 255)}

    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(game.WINDOW_WIDTH, 0, 0, 0), b2pyh.convertCordsToB2Vec2(0, game.WINDOW_HEIGHT))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(0, 0))
    b2h.addEdgeToWorld(b2h.createEdge(0, game.WINDOW_HEIGHT, 0, 0), b2pyh.convertCordsToB2Vec2(game.WINDOW_WIDTH, 0))

    while game.gameActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameActive = False

        game.screen.fill((80, 80, 80))

        drawGame(b2pyh, game, game.screen, game.world)

        box.linearVelocity = determineVelocity(game.INPUT_SENSITIVITY)

        pygame.display.flip()

        game.world.Step(game.TIME_STEP, 10, 10)
        game.clock.tick(game.FPS)


if __name__ == '__main__':
    main()