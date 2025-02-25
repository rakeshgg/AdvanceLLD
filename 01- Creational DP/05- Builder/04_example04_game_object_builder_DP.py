"""
GameBuilder
GameEngine have several components such as Transformer
Renderer, collider, scripts
The GameObject Builder class allows it to add incremently
making the construction process more managable

"""


class GameObject:
    def __init__(self):
        self.transform: Transform = None
        self.renderer: Renderer = None
        self.collider: Collider = None
        self.script: str = None

    def __str__(self):
        return f"Tranforms: {self.transform}\nRenderer: {self.renderer}\nCollider: {self.collider}\nScript: {self.script}\n"


class Transform:
    def __init__(self, position: tuple, rotation: tuple, scale: tuple):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def __str__(self):
        return (
            f"Position: {self.position}, Rotation: {self.rotation}, Scale: {self.scale}"
        )


class Renderer:
    def __init__(self, mesh: str, material: str):
        self.mesh = mesh
        self.material = material

    def __str__(self):
        return f"Mesh: {self.mesh}, Material: {self.material}"


class Collider:
    def __init__(self, shape: str, is_trigger: bool):
        self.shape = shape
        self.is_trigger = is_trigger

    def __str__(self):
        return f"Shape: {self.shape}, Trigger: {self.is_trigger}"


# Game builder
class GameBuilder:
    def __init__(self):
        self._game = GameObject()

    def add_transform(self, position: tuple, rotation: tuple, scale: tuple):
        self._game.transform = Transform(position, rotation, scale)

    def add_renderer(self, mesh: str, material: str):
        self._game.renderer = Renderer(mesh, material)

    def add_collider(self, shape, is_trigger):
        self._game.collider = Collider(shape, is_trigger)

    def add_script(self, script):
        self._game.script = script

    def get_game(self):
        return self._game


# Building a Game
print("=======ENGINE 1============")
builder = GameBuilder()
builder.add_transform((1, 2, 3), (4, 6, 2), (5, 6, 2))
builder.add_renderer("CubeMesh", "DefaultBlackShine")
builder.add_collider("Box", False)
builder.add_script("TurnScript.js")

game = builder.get_game()
print(game)


print("=======ENGINE 2============")
builder2 = GameBuilder()
builder2.add_transform((10, 12, 23), (5, 22, 15), (14, 9, 7))
builder2.add_renderer("Cylinder", "DarkCloud")
builder2.add_collider("Circlic", True)
builder2.add_script("ManualTurner")
game = builder2.get_game()
print(game)

"""
create objects step by steps and allow to
seperate building objects from actual objs

"""
