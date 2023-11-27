import Box2D

class B2PyHelper:
    def __init__(self, PPM: int, WINDOW_HEIGHT: int):
        # Initialize the PPM (pixels per meter) scaling factor and the window height
        self.PPM = PPM
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

    # Converts a tuple (x, y) to a Box2D vector (x, y)
    def convertTupleToB2Vec2(self, loc: tuple) -> Box2D.b2Vec2:
        # Convert the x and y coordinates to meters using the PPM scaling factor
        x = loc[0] / self.PPM
        y = loc[1] / self.PPM
        return Box2D.b2Vec2(x, y)

    # Converts separate x and y coordinates to a Box2D vector (x, y)
    def convertCordsToB2Vec2(self, x: int, y: int) -> Box2D.b2Vec2:
        # Convert the x and y coordinates to meters using the PPM scaling factor
        x = x / self.PPM
        y = y / self.PPM
        return Box2D.b2Vec2(x, y)

    # Converts a Box2D vector (x, y) to a tuple (x, y)
    def convertB2Vec2toTuple(self, loc: Box2D.b2Vec2) -> tuple:
        # Convert the x and y coordinates from meters to pixels using the PPM scaling factor
        x = loc.x * self.PPM
        y = loc.y * self.PPM
        return tuple([x, y])

    # Flips the y-axis of a tuple (x, y)
    def flipYaxis(self, cords: tuple) -> tuple:
        # Subtract the y-coordinate from the window height to flip the y-axis
        y = self.WINDOW_HEIGHT - cords[1]
        return tuple((cords[0], y))