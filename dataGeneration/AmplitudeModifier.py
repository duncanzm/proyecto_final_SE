from enum import Enum
import random


class AmplitudeModifier(Enum):
    quiet = lambda: random.randint(-6, 10)
    normal = lambda: random.randint(-5, 5)
    loud = lambda: random.randint(6, 10)