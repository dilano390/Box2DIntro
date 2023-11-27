import Box2D

# This class provides helper methods for creating and adding Box2D bodies to a world
class B2Helper:
    def __init__(self, world: Box2D.b2World, PPM: int):
        # Initialize the PPM (pixels per meter) scaling factor and the Box2D world
        self.PPM = PPM
        self.world = world

    def createEdge(self, w: int, h: int, x: int, y: int) -> Box2D.b2EdgeShape:
        # Create an edge shape with the given width, height, and position
        # Convert the dimensions to meters using the PPM scaling factor
        x = x / self.PPM
        y = y / self.PPM
        w = w / self.PPM
        h = h / self.PPM

        # Create an edge shape with the specified vertices
        edge = Box2D.b2EdgeShape(vertices=[(x, y), (w + x, h + y)])
        return edge

    def createPolygon(self, x: float, y: float, w: float, h: float) -> Box2D.b2PolygonShape:
        # Create a polygon shape with the given width, height, and position
        # Convert the dimensions to meters using the PPM scaling factor
        x = x / self.PPM
        y = y / self.PPM
        w = w / self.PPM
        h = h / self.PPM

        # Create a polygon shape with the specified vertices
        return Box2D.b2PolygonShape(vertices=[
            (x, y), (x + w, y), (x + w, y + h), (x, y + h)])

    def createCircle(self, x, y, radius: float):
        # Create a circle shape with the given position and radius
        # Convert the radius to meters using the PPM scaling factor
        radius /= self.PPM

        # Create a circle shape with the specified radius
        return Box2D.b2CircleShape(radius=radius)

    def addCircleToWorld(self, circle: Box2D.b2CircleShape, position: Box2D.b2Vec2, mass: float, linearDamping: float,
                         friction: float) -> Box2D.b2Body:
        # Create a dynamic body with the given circle shape, position, mass, linear damping, and friction
        circle = self.world.CreateDynamicBody(position=position, shapes=circle)
        circle.mass = mass
        circle.linearDamping = linearDamping
        circle.fixtures[0].friction = friction
        return circle

    def addBoxToWorld(self, polygon: Box2D.b2PolygonShape, position: Box2D.b2Vec2, mass: float, linearDamping: float,
                      friction: float) -> Box2D.b2Body:
        # Create a dynamic body with the given polygon shape, position, mass, linear damping, and friction
        box = self.world.CreateDynamicBody(position=position, shapes=polygon)
        box.mass = mass
        box.linearDamping = linearDamping
        box.fixtures[0].friction = friction
        return box

    def addEdgeToWorld(self, edge: Box2D.b2EdgeShape, position: Box2D.b2Vec2):
        # Create a static body with the given edge shape and position
        self.world.CreateStaticBody(position=position, shapes=edge)