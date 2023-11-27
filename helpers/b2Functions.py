import Box2D
import pygame

from helpers.b2PyHelper import B2PyHelper


def drawGame(b2pyh: B2PyHelper, gameInstance, screen: pygame.surface,
             world: Box2D.b2World) -> None:

    # Iterate through all the bodies in the physics world
    for body in world.bodies:

        # Iterate through all the fixtures attached to the current body
        for fixture in body.fixtures:

            # Get the shape of the current fixture
            shape = fixture.shape

            # Check if the shape is a circle
            if isinstance(shape, Box2D.b2CircleShape):
                # Flip the Y-coordinates to match the pygame's coordinate system
                pos = b2pyh.flipYaxis(b2pyh.convertB2Vec2toTuple(body.position))

                # Draw a circle on the screen using the converted position and radius
                pygame.draw.circle(screen, (255, 0, 100), pos,
                                   shape.radius * gameInstance.PPM)

            # Handle other shapes, such as edges and polygons
            else:
                # Convert the shape's vertices from Box2D coordinates to screen coordinates
                vertices = [(body.transform * v) * gameInstance.PPM for v in shape.vertices]

                # Flip the Y-coordinates to match pygame's coordinate system
                vertices = [(v[0], gameInstance.WINDOW_HEIGHT - v[1]) for v in vertices]

                # Draw a line for edge shapes
                if isinstance(shape, Box2D.b2EdgeShape):
                    pygame.draw.line(screen, (0, 155, 255), vertices[0], vertices[1], 3)

                # Draw a polygon for polygon shapes
                elif isinstance(shape, Box2D.b2PolygonShape):
                    color = (255, 0, 0)

                    # Check if the body has user data and if it contains a 'color' property
                    if body.userData is not None:
                        if 'color' in body.userData:
                            color = body.userData['color']

                    # Draw a polygon using the determined color and vertices
                    pygame.draw.polygon(screen, color, vertices)