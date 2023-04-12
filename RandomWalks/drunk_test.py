import random
from usual_drunk import UsualDrunk
from walk_simulator import WalkSimulator as wm

class DrunkTest:

    def __init__(self):
        random.seed(0)
        self.test((10, 100, 1000, 10000), 100, UsualDrunk)
    
    def test(self, walkLengths, numTrials, dClass):
        """
        Assumes walkLengths a sequence of ints >= 0
        numTrials an int > 0, dClass a subclass of Drunk
        for each number of steps in walkLengths, runs simwalks with
        numTrials walks and prints results
        """
        for numSteps in walkLengths:
            distances = wm.simWalks(numSteps, numTrials, dClass)
            print(dClass.__name__, 'random walks of numSteps', 'steps')
            print(' Mean =', round(sum(distances)/len(distances), 4))
            print(' max =', max(distances), 'Min =', min(distances))

if __name__ == '__main__':
    DrunkTest()
