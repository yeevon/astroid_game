from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0