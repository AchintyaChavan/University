import config

class ProblemSpec:
    """
        This class represents the specifications of a given problem and solution; in python.
        that is, it provides a structured representation of the contents of a problem
        text file and associated solution text file, as described in the assignment
        specifications.

        This class doesn't do validity checking - need to translate tester TODO

        @author Loreith
    """

    def __init__(self):
        """
            No explicit constructor in the java class, but there are instance
            variables to declare.
        """
        self.problemLoaded = False
        self.solutionLoaded = False

        self.asvCount = 0
        self.initialState = None
        self.goalState = None
        self.obstacles = []

        self.path = []
        self.solutionCost = 0

    def loadProblem(self, filename):
        """
            Loads a problem from a text file

            @param filename the path of the file to load

            @throws IOError if the text file doesn't exist or meet specifications
        """
        self.problemLoaded = False
        self.solutionLoaded = False
        inputData = open(filename, 'r').read().split('\n')
        
#         print(inputData)

        i = 0

        try:
            self.asvCount = inputData[i]
            i += 1

            self.initialState = config.ASVConfig(inputData[i])
            i += 1

            self.goalState = config.ASVConfig(inputData[i])
            i += 1

            numObstacles = int(inputData[i])
            i += 1

            
#             self.obstacles = [None] * numObstacles
            for j in range(numObstacles):
                o = config.Obstacle()
                o.construct(inputData[i])
                self.obstacles.append(o)
                i += 1

            self.problemLoaded = True
        except IndexError:
            print("Index out of range in input " + i )
            raise IOError("Index out of range in input " + i)
        except IOError:
            print("Input file not found")
            raise IOError("Input file not found")
        #TODO: Input varification error

    def loadSolution(self, filename):
        """
            Loads a solution from a solution text file.

            @param filename the path of the text file to loadSolution

            @throws IOError if the text file doesn't exist or doesn't meet the expectations
        """
        if (not self.problemLoaded):
            return(None)

        self.solutionLoaded = False
        inputData = open(filename, 'r').read().split('\n')

        i = 0
        line = ""

        try:
            line = inputData[i].split(' ')
            i += 1
            pathLength = line[0]
            self.solutionCost = line[1]

            self.path = [None]*pathLength
            for it in range(pathLength):
                self.path[it] = ASVconfig.ASVConfig(inputData[i])
                i += 1

            self.solutionLoaded = True

        except IndexError:
            print("Index out of range in solution loading")
            raise IOError("Index out of range in solution loading")
        except FileNotFoundError:
            print("Solution file not found")
            raise IOError("Solution file not found")
        #TODO: Input varificaiton error.

    def saveSolution(self, filename):
        """
            Saves the current solution to a text file

            @param filename the path of the text file to save to

            No need for Exception here, we should overwrite if there exists a text file
        """
        if (not self.problemLoaded or not self.solutionLoaded):
            return(None)

        outputFile = open(filename, 'w+')

        outputFile.write(str(len(self.path)) + " " + "{:.1f}".format(self.solutionCost) + '\n') #If you are on windows this will need to be \r\n but moss and unix will need \n only. \r\n will display as two line breaks
        for cfg in self.path:
            outputFile.write(cfg.__str__() + '\n')
        outputFile.close()

    def calculateTotalCost(self):
        """
            Returns the total cost of the currently loaded solutionCost

            @return The true total cost of the currently loaded solution
        """
        cost = 0
        
#         c0 = config.ASVConfig(self.path[0])
        c0 = self.path[0]
        for i in range(1, len(self.path)):
#             c1 = config.ASVConfig(self.path[i])
            c1 = self.path[i]
            cost += c0.totalDistance(c1)
            c0 = c1

        return cost

    def assumeDirectSolution(self):
        """
            Assumes that a path can be taken directly from the intial condition
            to the goal
        """
        if (not self.problemLoaded):
            return(None)

        self.path = [self.initialState, self.goalState]
        self.solutionCost = self.calculateTotalCost()
        self.solutionLoaded = True

    def getASVCount(self):
        return(self.asvCount)

    def getInitialState(self):
        return(self.initialState) #object reference preferred

    def getGoalState(self):
        return(self.goalState) #object reference preferred

    def getObstacles(self):
        return(self.obstacles[:]) #New object

    def setPath(self, path):
        if (not self.problemLoaded):
            return(None)
        self.path = path       
        self.solutionCost = self.calculateTotalCost()
        self.solutionLoaded = True

    def getPath(self):
        return(self.path[:]) #New object

    def getSolutionCost(self):
        return(self.solutionCost)

    def hasProblem(self):
        return(self.problemLoaded)

    def hasSolution(self):
        return(self.solutionLoaded)
