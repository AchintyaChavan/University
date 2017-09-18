'''
Created on 9 Sep. 2017

@author: AC
'''

import numpy as np
# from shapely import geometry

class ASVConfig:
    """
        Represents a configuration of the ASVs, in python. This class doesn't do
        validity checking, so see the code in tester for this...

        TODO: translate tester?
        TODO: iterator, generator, or access function

        @author Loreith
    """
    def __init__(self, coords):
        """
            Implements either constructor from the java 'cause you don't need lend

            @param coords either a list of tuples (x,y)
                or a space-separated string containing x y coords
                doing it with a list of [x,y,x,y] seems silly, if you need it just use the string method except check if the list contains tuples or floats
                I don't understand what the cfg thing is, some Java object? If you need it, use the same method!
        """
        if isinstance(coords, str):
            coordsList = coords.split(' ')
            coords = []
            for i in range(len(coordsList)/2):
                coords.append(( coordsList[i*2], coordsList[(i*2)+1] ))

        #Now that input is homogenised, we can continue

        self.asvPositions = coords

    def __str__(self):
        """
            Enables using str(asvConfig) to return the space-separated string

            @return a space-separated string x y x y for all asv units
        """
        string = ""
        for i in self.asvPositions:
            string += str(i[0]) + " " + str(i[1]) + " "
        return(string)

    def __add__(self, coord):
        """
            Enables using += point to add a point to the asvConfig

            @param coord a tuple coordinate (x,y)
        """
        self.asvPositions.append(coord)

    def __len__(self):
        """
            Enables the use of len(asvConfig) to get the number of asvs

            @return the length of the asvPositions list
        """
        return(len(self.asvPositions))

    def getASVCount(self):
        return(len(self.asvPositions))

    def getPosition(self, asvNo):
        """
            Returns the position of the ASV with the given index

            @param asvNo the index of the asv to return

            @return the position of the asv with the given index
        """
        return(self.asvPositions[asvNo])

    def getASVPositions(self):
        """
            Returns the positions of all of the ASVs. Analogous to printing.

            @return the list of (x,y) tuples representing ASVs
        """
        return(self.asvPositions[:]) #Slice to actually copy the list as opposed to unsafe access

    def maxDistance(self, otherState):
        """
            Returns the maximum straight-line distance between this state
            and another state, or -1 if the asv counts don't match

            @param otherState The other state to compare with. Type = ASVConfig

            @return the maximum straight-line distance for any ASV
        """
        if len(self.asvPositions) != len(otherState):
            return(-1)

        maxDistance = 0
        for i in range(len(self.asvPositions)):
            p1 = self.asvPositions[i]
            p2 = otherState.getPos(i)
            distance = np.sqrt( abs(p2[0] - p1[0])**2 + abs(p2[1] - p1[1])**2 )

            maxDistance = max([distance, maxDistance])

        return(maxDistance)

    def totalDistance(self, otherState):
        """
            Returns the total straight-line distance over all the ASVs between this
              state and the other state, or -1 if the ASV counts don't match.

            @param otherState The other state to compare with. Type = ASVConfig

            @return the total straight-line distance over all ASVs.
        """
        if len(self.asvPositions) != len(otherState):
            return(-1)

        totalDistance = 0
        for i in range(len(self.asvPositions)):
            p1 = self.asvPositions[i]
            p2 = otherState.getPos(i)
            distance = np.sqrt( abs(p2[0] - p1[0])**2 + abs(p2[1] - p1[1])**2 )
            #TODO: remove unnecesary variable when tested
            totalDistance += distance

        return(totalDistance)
    
        

class Obstacle:
    """
        This class attempts to clone a Rectangle2D class from Java, but in Python.

        Basically the obstacle class but with a different name for clarity and possible
        extensions later.

        It constructs a rectangle with the given coordinates (x,y) at the bottom-left hand corner,
        to the size of a given width and height.

        @param x = the x coordinate of the bottom left corner
        @param y = the y coordinate of the bottom left corner
        @param w = the width of the rectangle
        @param h = the height of the rectangle

        @Methods:
            getCoords

            __contains__(coord)
                enables coord in obstacle

            __equals__
                enables rectangle == obstacle

            constructor(string)
                re-constructs the rectangle from a string.

            distance(coord) where coord = (x,y)
                How far away the given point is from the closest point of the obstacle

            outcode(coord) where coord = (x,y)
                Vector (x,y,dx,dy) of mag (dx,dy) from closest point (x,y) of the obstacle

        @Author Loreith
    """
    
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        
        self.rect = [x, y, w, h]
#         self.polygon = geometry.Polygon([list((x, y)), 
#                                          list((x + w, y)), 
#                                          list((x + w, y + h)), 
#                                          list((x, y + h))])
        
        
#         self.polygon = geometry.Polygon([list(v1),
#                                          list(v2),
#                                          list(v3),
#                                          list(v4)])
                
    def __repr__(self):
        
        return "%s, %s, %s, %s\n %s\n" % (self.v1, self.v2, self.v3, self.v4, self.polygon)
    
    
    def __equals__(self,rect):
        """
            Returns true if the rectangle is equal to self

            @param rect = [x,y,w,h]

            @return true if rect == self.rect. False if otherwise
        """
        for i in range(len(rect)):
            if rect[i] != self.rect[i]:
                return(False)
        return(True)

    
    def __contains__(self, coord):
        """
            Returns true if coordinate is in the obstacle

            @param coord = (x,y)

            @return true if coord is in rectangle, false if not
        """     
        ownX = self.rect[0]
        ownY = self.rect[1]
    
        x = coord[0]
        y = coord[1]
        if (x > ownX and x < ownX + self.rect[2]):
            
            if (y > ownY and y < ownY + self.rect[3]):
                
                return(True)
            
        return(False)
    
    def construct(self, string):
        """
            Second constructor method:
                Constructs an obstacle from the representation used in the input file:
                  that is, the x- and y- coordinates of all of the corners of the
                  rectangle.

            @param string the string describing the obstacle
        """
        #xs = []
        #yx = []

        xMin = 0
        xMax = 0
        yMin = 0
        yMax = 0

        stringList = string.split(' ')
        stringList = [float(s) for s in stringList]
#         print(stringList)

        for i in range(4):
            #xs.append(stringList[i*2])
            #ys.append(stringList[(i*2) + 1])

            xMin = stringList[i*2] if stringList[i*2] < xMin else xMin
            xMax = stringList[i*2] if stringList[i*2] > xMax else xMax
            yMin = stringList[(i*2) + 1] if stringList[(i*2) + 1] < yMin else yMin
            yMax = stringList[(i*2) + 1] if stringList[(i*2) + 1] > yMax else yMax

        

        self.rect = [xMin, yMin, xMax - xMin, yMax - yMin]

    def getRect(self):
        """
         Returns the rectangle as a list of x,y,w,h
        """
        return(self.rect)

    def getCorners(self):
        """
            Returns the corners of the rectangles as a list of (x,y) tuples
        """
        l = [None]*4
        l[0] = (self.rect[0],self.rect[1])
        l[1] = (self.rect[0],self.rect[1]+self.rect[3])
        l[2] = (self.rect[0]+self.rect[2],self.rect[1])
        l[3] = (self.rect[0]+self.rect[2],self.rect[1]+self.rect[3])
        return (l)

    def distance(self, coord):
        """
            How far away the given point is from the closest point of the rectangle

            @param coord = (x,y)

            @return the minimum distance from the coordinates to the obstacle
        """
        # Circles, all 4
        x = coord[0]
        y = coord[1]

        ownX = self.rect[0]
        ownY = self.rect[1]
        ownW = self.rect[2]
        ownH = self.rect[3]


        if coord in self:
            return(0)

        if (x > ownX and x < ownX + ownW):
            #If a perpendicular line is possible it is the shortest something something dot product
            return( min([ abs(y-ownY), abs(y-(ownY + ownH)) ]) )
        elif (y > ownY and y < ownY + ownH):
            return( min([ abs(x-ownX), abs(x-(ownX + ownW)) ]) )

        else:
            #If we are past a corner, return the pythagorean distance from said corner
            cornerX = min([ abs(x-ownX), abs(x-(ownX + ownW)) ])
            cornerY = min([ abs(y-ownY), abs(y-(ownY + ownH)) ])

            dx = abs(x-cornerX)
            dy = abs(y-cornerY)

            return( np.sqrt(dx**2 + dy**2) )

    def outcode(self, coord):
        """
            Gives the shortests vector from the obstacle to the coord

            @param coord = (x,y)

            @return the vector [x,y,dx,dy] from the closest point on the rectangle to the point coord
        """
        # Circles, all 4
        x = coord[0]
        y = coord[1]

        ownX = self.rect[0]
        ownY = self.rect[1]
        ownW = self.rect[2]
        ownH = self.rect[3]


        if coord in self:
            return(0)

        if (x > ownX and x < ownX + ownW):
            #If a perpendicular line is possible it is the shortest something something dot product

            sideY   = ownY if abs(y-ownY) < abs(y-(ownY + ownH)) else ownY + ownH
            dy      = min( [ abs(y-ownY), abs(y-(ownY + ownH)) ] )

            return( [x, sideY, 0, dy ] )

        elif (y > ownY and y < ownY + ownH):

            sideX   = ownX if abs(x-ownX) < abs(x-(ownX + ownW)) else ownX + ownW
            dx      = min( [ abs(x-ownX), abs(x-(ownX + ownW)) ] )

            return( [sideX, y, dx, 0] )

        else:
            #If we are past a corner, return the pythagorean distance from said corner
            cornerX = min([ abs(x-ownX), abs(x-(ownX + ownW)) ])
            cornerY = min([ abs(y-ownY), abs(y-(ownY + ownH)) ])

            dx = abs(x-cornerX)
            dy = abs(y-cornerY)

            return( [cornerX, cornerY, dx, dy] )   