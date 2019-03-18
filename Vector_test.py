from Vector import Vector
import math

def test_coordinate_system():
    vec = Vector(vector=(1,1))
    guiCoord = vec.getGUIVector1()
    assert guiCoord[0] == 261
    assert guiCoord[1] == 259
