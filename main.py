from tkinter import Tk, Entry, Button, StringVar, Label
import math as m
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('911x420+0+0')
        master.config(bg='black')
        # master.resiable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(width=43, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90,
                                                                                                              y=50)
        Button(width=11, height=4, text='mod', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180,
                                                                                                                y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='#ccddff', command=lambda: self.show(1)).place(x=0,
                                                                                                              y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='#ccddff', command=lambda: self.show(2)).place(x=90,
                                                                                                              y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='#ccddff', command=lambda: self.show(3)).place(x=180,
                                                                                                              y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='#ccddff', command=lambda: self.show(4)).place(x=0,
                                                                                                              y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='#ccddff', command=lambda: self.show(5)).place(x=90,
                                                                                                              y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='#ccddff', command=lambda: self.show(6)).place(x=180,
                                                                                                              y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='#ccddff', command=lambda: self.show(7)).place(x=0,
                                                                                                              y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='#ccddff', command=lambda: self.show(8)).place(x=180,
                                                                                                              y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='#ccddff', command=lambda: self.show(9)).place(x=90,
                                                                                                              y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text=',', relief='flat', bg='white', command=lambda: self.show(',')).place(x=180,
                                                                                                              y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270,
                                                                                                              y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270,
                                                                                                              y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270,
                                                                                                              y=50)
        Button(width=11, height=4, text='X', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270,
                                                                                                              y=125)
        Button(width=11, height=4, text='sqrt()', relief='flat', bg='white', command=lambda: self.show('m.sqrt(')).place(x=360,
                                                                                                              y=50)
        Button(width=11, height=4, text='X^Y', relief='flat', bg='white', command=lambda: self.show('**')).place(x=360,
                                                                                                              y=125)
        Button(width=11, height=4, text='e^X', relief='flat', bg='white', command=lambda: self.show('m.exp(')).place(x=360,
                                                                                                              y=200)
        Button(width=11, height=4, text='e', relief='flat', bg='white', command=lambda: self.show('m.e')).place(x=360,
                                                                                                              y=275)
        Button(width=11, height=4, text='pi', relief='flat', bg='white', command=lambda: self.show('m.pi')).place(x=360, y=350)
        Button(width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)
        Button(width=11, height=4, text='plot', relief='flat', bg='white', command=self.plot).place(x=450, y=350)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('x')).place(x=450,
                                                                                                                y=50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

    def plot(self):
        plot_equation = self.entry_value

        fig, ax = plt.subplots()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        canvas.get_tk_widget().place(x=540, y=50, height=370, width=370)

        x=np.arange(-2,2,0.001)
        plt.plot(x,plot_equation)
        plt.grid()
        plt.show()

root = Tk()
calculator = Calculator(root)

root.mainloop()