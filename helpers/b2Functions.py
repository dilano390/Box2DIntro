import Box2D
import pygame

from helpers.b2PyHelper import B2PyHelper


def drawGame(b2pyh: B2PyHelper, gameInstance, screen: pygame.surface,
             world: Box2D.b2World) -> None:
    for body in world.bodies:
        for fixture in body.fixtures:
            shape = fixture.shape
            if isinstance(shape, Box2D.b2CircleShape):
                pos = b2pyh.flipYaxis(b2pyh.convertB2Vec2toTuple(body.position))
                pygame.draw.circle(screen, (255, 0, 100), pos,
                                   shape.radius * gameInstance.PPM)
            else:
                vertices = [(body.transform * v) * gameInstance.PPM for v in shape.vertices]
                vertices = [(v[0], gameInstance.WINDOW_HEIGHT - v[1]) for v in vertices]

                if isinstance(shape, Box2D.b2EdgeShape):
                    pygame.draw.line(screen, (0, 155, 255), vertices[0], vertices[1], 3)
                elif isinstance(shape, Box2D.b2PolygonShape):
                    color = (255, 0, 0)
                    if body.userData is not None:
                        if 'color' in body.userData:
                            color = body.userData['color']

                    pygame.draw.polygon(screen, color, vertices)
