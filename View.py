import Tkinter as tk
from Tkinter import *
from Vector import Vector
import numpy as np

class View:

    def __init__(self):
        self.createGUI()

    def create_grid(self, event=None):
        w = self.c.winfo_width()
        h = self.c.winfo_height()

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
        vector1 = self.c.create_line([260,260], vec.getGUIVector1(), tag='first')
        self.root.update_idletasks()
        self.root.update()

    def unDrawVector(self):
        if(self.hasBeenDrawnOn):
            self.c.delete('first')
            self.c.delete('second')
        
    def waitForClick(self):
        self.root.update_idletasks()
        self.root.update()

    def graphVector(self):
        self.unDrawVector()
        x = int(self.e1.get()) * 20
        y = int(self.e2.get()) * 20
        self.vec = Vector(vector1=(x,y))
        self.drawVector(self.vec)
        #Set to true to let other methods know the canvas has been
        #drawn on
        self.hasBeenDrawnOn = True

    def rotateVector(self):
        self.unDrawVector()
        degrees = int(self.e3.get())
        self.vec.rotateBy(degrees)
        self.drawVector(self.vec)

    def transformGrid(self):
        x1 = int(self.e4.get())
        y1 = int(self.e5.get())
        x2 = int(self.e6.get())
        y2 = int(self.e7.get())
        transformMat = np.asarray((x1,y1),(x2,y2))
        base1 = np.asarray((0,1))
        base2 = np.asarray((1,0))
        base1 = transformMat * base1
        base2 = transformMat * base2

        #To list
        base1 = base1.tolist()
        base2 = base2.tolist()
        
        self.drawVector(Vector(vector1=(base1[0],base1[1])))
        self.drawVector(Vector(vector1=(base2[0],base2[1])))
    
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
        self.transformButton = Button(f, text='Transform', command=self.transformGrid)
        self.transformButton.grid(row=0,column=1)
        #self.rotateButton.pack(fill=BOTH, expand=1)
        self.rotateButton = Button(f, text='Rotate', command=self.rotateVector)
        self.rotateButton.grid(row=0, column=2)

        #Input labels and textfields
        Label(inputFrame, text="X coordinate").grid(row=0)
        Label(inputFrame, text="Y coordinate").grid(row=1)
        Label(inputFrame, text="Rotate by").grid(row=0, column=6)
        Label(inputFrame, text="X1|-").grid(row=0,column=2)
        Label(inputFrame, text="Y1|_").grid(row=1,column=2)
        Label(inputFrame, text="-|X2").grid(row=0,column=5)
        Label(inputFrame, text="_|Y2").grid(row=1,column=5)
        self.e1 = Entry(inputFrame, width=1)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(inputFrame, width=1)
        self.e2.grid(row=1, column=1)
        self.e3 = Entry(inputFrame, width=3)
        self.e3.grid(row=0, column=7)
        #Matrix input entries
        self.e4 = Entry(inputFrame, width=1)
        self.e4.grid(row=0,column=3)
        self.e5 = Entry(inputFrame, width=1)
        self.e5.grid(row=1,column=3)
        self.e6 = Entry(inputFrame, width=1)
        self.e6.grid(row=0,column=4)
        self.e7 = Entry(inputFrame, width=1)
        self.e7.grid(row=1,column=4)

        #For letting class methods know that this is a fresh canvas
        self.hasBeenDrawnOn = False

        self.c.bind('<Configure>', self.create_grid)
        #Can be replaced with the lines
if __name__ == "__main__":
    view = View()
    while True:
        view.waitForClick()
        
