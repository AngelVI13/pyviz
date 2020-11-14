import pyglet


class Overlay:
    def __init__(self, size, position):
        self.width, self.height = size
        self.x, self.y = position

        self.background_group = pyglet.graphics.OrderedGroup(0)
        self.foreground_group = pyglet.graphics.OrderedGroup(1)
        self.batch = pyglet.graphics.Batch()

        self.padding = 5

        self.area = pyglet.shapes.Rectangle(
            x=self.x, y=self.y, width=self.width, height=self.height,
            color=(255, 255, 255), batch=self.batch, group=self.background_group
        )

        self.title = pyglet.text.Label(
            text="Visualization Training",
            font_size=26,
            font_name="comicsans",
            color=(0, 0, 0, 255),
            x=self.x + self.width // 2, y=self.y + self.height * 0.85, 
            anchor_x='center',
            # anchor_y='top',
            batch=self.batch,
            group=self.foreground_group
        )

        self.description = pyglet.text.Label(
            text=(
                "The aim of the game: Say which piece can "
                "reach a given square. You start with 2 pieces "
                "and get 1 more for every 10 right answers.\n\n"
                "The catch: you cannot see where your pieces are!\n"
            ),
            font_size=16,
            font_name="comicsans",
            color=(0, 0, 0, 255),
            x=self.x + self.width // 2 + self.padding, 
            y=self.y + self.height * 0.70, 
            anchor_x='center',
            # anchor_y='top',
            width=self.width - 2 * self.padding,
            multiline=True,
            batch=self.batch,
            group=self.foreground_group
        )

        # self.button = pyglet.shapes.Rectangle(
        #     x=
        # )