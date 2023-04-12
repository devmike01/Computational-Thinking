from location import Location
from field import Field

class WalkSimulator():
    
    def __init__(self):
        print()
    
    def walk(self, f, d, numSteps):
        """Assumes: f a Field, d a Drunk in f, and numsteps an int >= 0.
        Move d numSteps times; returns the distance
        between the final location and the location
        at the start of the walk"""
        start = f.getLoc(d)
        for s in range(numSteps):
            f.moveDrunk(d)
        return start.distFrom(f.getLoc(d))

    def simWalks(self, numsteps, numTrials, dClass):
        """Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subclass of Drunk Simulates numTrials walks of numSteps steps
        each. Returns a list of the final distance for each trial"""
        Homer = dClass()
        origin = Location(0,0)
        distance = []
        for t in range(numTrials):
            f = Field()
            f.addDrunk(Homer, origin)
            distance.append(round(self.walk(f, Homer, numTrials), 1))
        
        return distance
