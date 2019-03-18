from Vector import Vector
import math

"""
Tests for the mapping from cartesian to GUI-space coordinates
"""
def test_coodinate_conversion():
    #Testing quadrant 1 coordinate conversion
    vec = Vector(vector=(1,1))
    guiCoord = vec.getGUIVector1()
    assert guiCoord[0] == 261
    assert guiCoord[1] == 259

    #Testing quadrant 2 coordinate conversion
    vec = Vector(vector=(-3,10))
    guiCoord = vec.getGUIVector1()
    assert guiCoord[0] == 257
    assert guiCoord[1] == 250

    #Testing quadrant 3 coordinate conversion
    vec = Vector(vector=(-5,-10))
    guiCoord = vec.getGUIVector1()
    assert guiCoord[0] == 255
    assert guiCoord[1] == 270

    #Testing quadrant 4 coordinate conversion
    vec = Vector(vector=(5, -10))
    guiCoord = vec.getGUIVector1()
    assert guiCoord[0] == 265
    assert guiCoord[1] == 270

"""
Tests for vector rotation
"""
def test_rotation():
    #Testing rotation by 45 degrees; using rounding since rotated vectors
    #return 0 as a approximation
    vec = Vector(vector=(1,1))
    vec.rotateBy(45)
    rotatedVector = vec.getCartesianVector()
    assert round(rotatedVector[0]) == 0
    assert round(rotatedVector[1]) == 1

    #Testing rotation by 30 degrees; Rounding because rotation matrix
    #returns rotated vector with truncated sig figs
    vec.rotateBy(30)
    rotatedVector = vec.getCartesianVector()
    print(rotatedVector)
    assert round(rotatedVector[0]) == round(-0.5)
    assert round(rotatedVector[1]) == round(math.sqrt(3)/2.0)
    
