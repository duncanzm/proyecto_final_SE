from enum import Enum
import random


class AmplitudeModifier(Enum):
    quiet = lambda: str(random.randint(-10, -6))
    normal = lambda: str(random.randint(-5, 5))
    loud = lambda: str(random.randint(6, 10))
