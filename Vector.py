import numpy as np
import math

"""
Helper function for normalizing a vector vector in tuple form
"""
def normalizeVector(vector):
    magReciprocal = 1.0 / getMagnitude(vector)
    vector = (vector[0] * magReciprocal, vector[1] * magReciprocal)
    return vector
        
"""
Helper function for getting the magnitude of a vector in tuple form
"""
def getMagnitude(vector):
    return math.sqrt((vector[0] ** 2) + (vector[1] ** 2))


""""
Container for vectors. Can be used to paint vectors
onto a given GUI canvas.
"""
class Vector:

    """
    Default construtor takes in coordinates in regular space
    and then keeps the regular coordinates and finds the corresponding
    ordered pair set in GUI coordinaate space.
    vector: A tuple containing the x and y component of a given vector
            given in regular cartesian coordinates
    """
    def __init__(self, vector=()):
        self.cartesianVector1 = vector #by definition cartesian vectors
                                      #always start at origin
        self.transformToGUICoordinates()
        self.cartesianMagnitude = getMagnitude(vector)

    """
    Helper method for transforming the coordinates inputted through the
    constructor from cartesian coordinates to GUI coordinates. This works
    by using instance variables so no parameters are needed.
    """
    def transformToGUICoordinates(self):
        self.startGUICoordinates = (260,260)
        self.endGUICoordinates1 = (self.cartesianVector1[0] + 260,\
                                  260 - self.cartesianVector1[1])
    """
    Returns the contained/stored vector in cartesian coordiantes
    """
    def getCartesianVector(self):
        return (self.cartesianVector1)

    """
    Returns BOTH the coordinates of the tail and head of the stored
    vector in GUI coordinates
    """
    def getGUICoordinates(self):
        return (self.startGUICoordinates, self.endGUICoordinates1)

    """
    Returns only the head coordinates of the stored vector in GUI
    coordinates
    """
    def getGUIVector1(self):
        return self.endGUICoordinates1

    """
    Rotates the stored vector counter-clockwise by the amount of passed in
    degrees
    """
    def rotateBy(self, degrees):
        #Convert degrees to radians
        rads = (math.pi/180) * (degrees)
        #Converting vectors to matrix form
        obj = np.asmatrix((self.cartesianVector1[0],self.cartesianVector1[1]))
        obj = obj.transpose()
        print(obj)
        #Creating the rotation matrix
        rotationMatrix = np.asmatrix(((math.cos(rads),-1*math.sin(rads)),\
                                     (math.sin(rads),math.cos(rads))))
        print(rotationMatrix)

        #Calculate the linear transformation
        transformedVectors = rotationMatrix * obj
        print(transformedVectors)
        asListVectors = transformedVectors.tolist()
        normalizedVector = normalizeVector((asListVectors[0][0], asListVectors[1][0]))
        self.cartesianVector1 = (normalizedVector[0] * self.cartesianMagnitude,\
                                 normalizedVector[1] * self.cartesianMagnitude)
        self.transformToGUICoordinates()

