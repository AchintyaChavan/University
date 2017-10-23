'''
Created on 23 Oct. 2017

@author: AC
'''

import numpy as np

stateSpace = {}
stateSpace['bronze'] = [(0,0),
                        (0,1),
                        (0,2),
                        (0,3),
                        (1,0),
                        (1,1),
                        (1,2),
                        (2,0),
                        (2,1),             
                        (3,0)]

stateSpace['silver'] = [(0,0),
                        (0,1),
                        (0,2),
                        (0,3),
                        (1,0),
                        (1,1),
                        (1,2),
                        (2,0),
                        (2,1),             
                        (3,0)]


class ProblemSpec:    
    
    def __init__(self):
                
        self.modelLoaded = False            #True iff user stochastic model is currently loaded 
        self.fortnights = 0                 #The number of fortnights the venture manager will be evaluated
        self.discount = 0                   #Discount Factor
        self.venture = VentureManager()     #Venture Manager Type
        self.probabilities = {}             #Probability Matrices
        self.salePrices = {}                #Price of products manufactured by ventures
        self.initialFunds = {}              #Manufacturing cost of ventures
        self.stateSpace = None              #Possible states of funding

    """
     * Loads the stochastic model from file
     * @param filename the path of the text file to load.
     * @throws IOException
     *      if the text file doesn't exist or doesn't meet the assignment specs
     """
    def loadInputFile(self, filename):
        
        lineNo = 0
        
        try:
            array = []    
        
            with open(filename, "r") as f:
                
                array = f.read().split("\n")
            
    #         print(array)
            
            self.venture.constructor(array[0])
            self.discount = float(array[1])
            self.fortnights = int(array[2])
            self.stateSpace = stateSpace[self.venture.getName()]
            
            arr3 = array[3].split(' ')
            arr4 = array[4].split(' ')
        
            for i in range(len(arr3)):
    
                self.salePrices[i + 1] = int(arr3[i])
                self.initialFunds[i + 1] = int(arr4[i])
    
            lineNo = 5
            
            for j in range(self.venture.getNumVentures()):
                
                mat = []
                
                for k in range(self.venture.getManufacturingFunds() + 1):
                    
                    row = [float(r) for r in array[lineNo + k].split(' ')]
                    mat.append(row)
            
                self.probabilities[j + 1] = np.array(mat)
                
                lineNo = lineNo + k
    
            self.modelLoaded = True
            
        except IndexError:
            
            print("Index out of range in input " + lineNo )
            raise IOError("Index out of range in input " + lineNo)
        
        except IOError:
            
            print("Input file not found")
            raise IOError("Input file not found")

    def __str__(self):
        
        string = ""        
        string += str(self.fortnights) + str(self.discount)
        
        return string
        
    def isModelLoaded(self):
        
        return self.modelLoaded
    
    def getNumFortnights(self):
        
        return self.fortnights
    
    def getDiscountFactor(self):
        
        return self.discount
    
    def getVentureManager(self):
        
        return self.getVentureManager()
    
    def getSalePrices(self):
        
        return self.salePrices
    
    def getInitialFunds(self):
        
        return self.initialFunds

    def getProbabilities(self):
        
        return self.probabilities
    
    def getStateSpace(self):
        
        return self.stateSpace
    
    

class VentureManager:
    
    def __init__(self):
                
        self.name = 0                       #Name of customer level for this Venture Manager 
        self.maxManufacturingFunds = 0      #Maximum amount of manufacturing funding across all ventures (x$10 000)
        self.maxAdditionalFunding = 0       #Maximum amount of funding which can be added to a venture in 1 fortnight (x$10 000)
        self.numVentures = 0                #Number of ventures to be managed
    
    """
     * Constructor
     * @param ventureType Takes values bronze, silver, gold or platinum
    """    
    def constructor(self, ventureType):
        
        self.name = ventureType
        
        if self.name == 'bronze':
        
            self.maxManufacturingFunds = 3
            self.maxAdditionalFunding = 3
            self.numVentures = 2
            
        elif self.name == 'silver':
            
            self.maxManufacturingFunds = 5
            self.maxAdditionalFunding = 4
            self.numVentures = 2

        elif self.name == 'gold':
            
            self.maxManufacturingFunds = 6
            self.maxAdditionalFunding = 4
            self.numVentures = 3
            
        elif self.name == 'platinum':
            
            self.maxManufacturingFunds = 8
            self.maxAdditionalFunding = 5
            self.numVentures = 3
            
        else:
            
            raise Exception("Invalid customer level.")
    
    """
     * Enables using str() to return the space-separated string
     *  @return a space-separated string of venture name, funding and venture num
    """    
    def __str__(self):
        
        string = ""        
        string += str(self.name) + " " + str(self.maxManufacturingFunds) + " " \
                    + str(self.maxAdditionalFunding) + " " + str(self.numVentures)
        
        return string
               
    def getName(self):
        
        return self.name
    
    def getManufacturingFunds(self):
        
        return self.maxManufacturingFunds
    
    def getAdditionalFunds(self):
        
        return self.maxAdditionalFunding
    
    def getNumVentures(self):
        
        return self.numVentures
    
    