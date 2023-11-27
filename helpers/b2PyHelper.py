import Box2D


class B2PyHelper:
    def __init__(self, PPM: int, WINDOW_HEIGHT: int):
        self.PPM = PPM
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

    def convertTupleToB2Vec2(self, loc: tuple) -> Box2D.b2Vec2:
        return Box2D.b2Vec2(loc[0] / self.PPM, loc[1] / self.PPM)

    def convertCordsToB2Vec2(self, x: int, y: int) -> Box2D.b2Vec2:
        return Box2D.b2Vec2(x / self.PPM, y / self.PPM)

    def convertB2Vec2toTuple(self, loc: Box2D.b2Vec2) -> tuple:
        return tuple([loc.x * self.PPM, loc.y * self.PPM])

    def flipYaxis(self, cords: tuple) -> tuple:
        return tuple((cords[0], self.WINDOW_HEIGHT - cords[1]))
