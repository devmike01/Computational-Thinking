import random

class masochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9),
        (1.0, 0.0), (-1.0, 0.0)]
    return random.choice(stepChoices)
