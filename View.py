import Tkinter as tk
from Tkinter import *
from Vector import Vector

class View:

    def __init__(self):
        self.createGUI()

    def create_grid(self, event=None):
        w = self.c.winfo_width()
        h = self.c.winfo_height()
        self.c.delete('grid_line')

        #Creates all vericle lines at intervals of 100
        for i in range(0,w,20):
            self.c.create_line([(i,0),(i,h)],tag='grid_line')

        #Creates all horizontal lines at intervals of 100
        for i in range(0,h,20):
           self.c.create_line([(0,i),(w,i)], tag='grid_line')

        #Create the x-axis
        self.c.create_line([(260,0),(260,500)],tag='x-axis',fill='blue')
        #Create the y-axis
        self.c.create_line([(0,260),(500,260)],tag='y-axis',fill='blue')

    def drawVector(self, vec):
        self.vector1 = self.c.create_line([260,260], vec.getGUIVector1(), tag='first')
        self.vector2 = self.c.create_line([260,260], vec.getGUIVector2(), tag='second')
        self.root.update_idletasks()
        self.root.update()

    def unDrawVector(self):
        if(self.hasBeenDrawnOn):
            self.c.delete(self.vector1)
            self.c.delete(self.vector2)
        
    def waitForClick(self):
        self.root.update_idletasks()
        self.root.update()

    def graphVector(self):
        self.unDrawVector()
        x = int(self.e1.get()) * 20
        y = int(self.e2.get()) * 20
        self.vec = Vector(vector1=(x,y),vector2=(0,0))
        self.drawVector(self.vec)
        #Set to true to let other methods know the canvas has been
        #drawn on
        self.hasBeenDrawnOn = True

    def rotateVector(self):
        self.unDrawVector()
        degrees = int(self.e3.get())
        self.vec.rotateBy(degrees)
        self.drawVector(self.vec)
    
    def createGUI(self):
        self.root = tk.Tk()

        self.c = tk.Canvas(self.root, height=520, width=520, bg='white')
        self.c.pack(fill=tk.BOTH, expand=True)
        #Frame creation for buttons and input
        f = Frame(self.root, height = 50, width = 50)
        inputFrame = Frame(self.root, height=50, width=50)
        f.pack_propagate(0)
        f.pack()
        inputFrame.pack_propagate(0)
        inputFrame.pack()

        #Button Creation
        self.graphButton = Button(f, text='Graph', command=self.graphVector)
        self.graphButton.grid(row=0, column=0)
        self.rotateButton = Button(f, text='Rotate', command=self.rotateVector)
        #self.rotateButton.pack(fill=BOTH, expand=1)
        self.rotateButton.grid(row=0, column=5)

        #Input labels and textfields
        Label(inputFrame, text="X coordinate").grid(row=0)
        Label(inputFrame, text="Y coordinate").grid(row=1)
        Label(inputFrame, text="Rotate by").grid(row=0, column=2)
        self.e1 = Entry(inputFrame)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(inputFrame)
        self.e2.grid(row=1, column=1)
        self.e3 = Entry(inputFrame)
        self.e3.grid(row=0, column=3)

        #For letting class methods know that this is a fresh canvas
        self.hasBeenDrawnOn = False

        self.c.bind('<Configure>', self.create_grid)
        #Can be replaced with the lines
if __name__ == "__main__":
    view = View()
    while True:
        view.waitForClick()
        
