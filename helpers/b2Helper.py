import Box2D


class B2Helper:
    def __init__(self, world: Box2D.b2World, PPM: int):
        self.PPM = PPM
        self.world = world

    def createEdge(self, w: int, h: int, x: int, y: int) -> Box2D.b2EdgeShape:
        x = x / self.PPM
        y = y / self.PPM
        w = w / self.PPM
        h = h / self.PPM
        edge = Box2D.b2EdgeShape(vertices=[(x, y), (w + x, h + y)])
        return edge

    def createPolygon(self, x: float, y: float, w: float, h: float) -> Box2D.b2PolygonShape:
        x = x / self.PPM
        y = y / self.PPM
        w = w / self.PPM
        h = h / self.PPM
        return Box2D.b2PolygonShape(vertices=[
            (x, y), (x + w, y), (x + w, y + h), (x, y + h)])

    def createCircle(self, x, y, radius: float):
        radius /= self.PPM
        return Box2D.b2CircleShape(radius=radius)

    def addCircleToWorld(self, circle: Box2D.b2CircleShape, position: Box2D.b2Vec2, mass: float, linearDamping: float,
                         friction: float) -> Box2D.b2Body:
        circle = self.world.CreateDynamicBody(position=position, shapes=circle)
        circle.mass = mass
        circle.linearDamping = linearDamping
        circle.fixtures[0].friction = friction
        return circle

    def addBoxToWorld(self, polygon: Box2D.b2PolygonShape, position: Box2D.b2Vec2, mass: float, linearDamping: float,
                      friction: float) -> Box2D.b2Body:
        box = self.world.CreateDynamicBody(position=position, shapes=polygon)
        box.mass = mass
        box.linearDamping = linearDamping
        box.fixtures[0].friction = friction
        return box

    def addEdgeToWorld(self, edge: Box2D.b2EdgeShape, position: Box2D.b2Vec2):
        self.world.CreateStaticBody(position=position, shapes=edge)
