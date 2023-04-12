import random
from drunk import Drunk

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0, -1), (1,0), (-1, 0)]
        return random.choice(stepChoices)
