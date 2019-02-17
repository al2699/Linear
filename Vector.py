import numpy as np
import math

"""
Container for vectors. Can be used to paint vectors
onto a given GUI canvas.
"""
class Vector:

    """
    Default construtor takes in coordinates in regular space
    and then keeps the regular coordinates and finds the corresponding
    ordered pair set in GUI coordinaate space.
    x: x coordinate in regular cartesian coordinates
    y: y coordinates in regular cartesian coordinates
    """
    def __init__(self, vector1=(), vector2 = ()):
        self.cartesianVector1 = vector1 #by definition cartesian vectors
                                      #always start at origin
        self.cartesianVector2 = vector2
        self.transformToGUICoordinates()

    def transformToGUICoordinates(self):
        self.startGUICoordinates = (260,260)
        self.endGUICoordinates1 = (self.cartesianVector1[0] + 260,\
                                  260 - self.cartesianVector1[1])
        self.endGUICoordinates2 = (self.cartesianVector2[0] + 260,\
                                   260 - self.cartesianVector2[1])

    def getCartesianVectors(self):
        return (self.cartesianVector1, self.cartesianVector2)

    def getGUICoordinates(self):
        return (self.startGUICoordinates, self.endGUICoordinates1,\
                self.endGUICoordinates2)
    
    def getGUIVector1(self):
        return self.endGUICoordinates1

    def getGUIVector2(self):
        return self.endGUICoordinates2

    def rotateBy(self, degrees):
        #Convert degrees to radians
        rads = (math.pi/180) * (degrees)
        #Converting vectors to matrix form
        obj = np.asarray((self.cartesianVector1,self.cartesianVector2))
        print(obj)
        #Creating the rotation matrix
        rotationMatrix = np.asmatrix(((math.cos(rads),math.sin(rads)),\
                                     (-1*math.sin(rads),math.cos(rads))))
        print(rotationMatrix)

        #Calculate the linear transformation
        transformedVectors = obj * rotationMatrix
        print(transformedVectors)
        asListVectors = transformedVectors.tolist()
        self.cartesianVector1 = (asListVectors[0][0], asListVectors[0][1])
        self.cartesianVector2 = (asListVectors[1][0], asListVectors[1][1])
        self.transformToGUICoordinates()
