import pyglet


class Overlay:
    def __init__(self, size, position):
        self.width, self.height = size
        self.x, self.y = position

        self.batch = pyglet.graphics.Batch()

        self.area = pyglet.shapes.Rectangle(
            x=self.x, y=self.y, width=self.width, height=self.height,
            color=(255, 255, 255), batch=self.batch
        )