from View import View
from Vector import Vector


if __name__ == "__main__":
    view = View()
    while True:
        a = view.waitForClick()
        print("Done with click in controller.")
        if(a == 1):
            drawUnitVector(view)

def drawUnitVector(view):
    vec = Vector(vector1 = (70,70), vector2=(100,50))
    view.drawVector(vec)
