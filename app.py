import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

import matplotlib
from matplotlib import figure
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation

import pyvisa
import time

import numpy.core._dtype_ctypes #need so that pyinstaller doesn't freak out

#sets up figure in main scope
plot = Figure(figsize=(5,3),dpi=100, tight_layout=True)
subPlot = plot.add_subplot(111)
subPlot.set_xlabel("time (s)")
subPlot.set_ylabel("capacitance (pf)")



#creates main window object called root


class MainWindow:

    def __init__(self, root):
        
        root.geometry('900x750+560+150')
        root.resizable(FALSE, FALSE)
        root.title("Capacitance Measurment")

        self.timePeriod = 0
        self.maxCap = 0
        self.numPoints = 0

        Interrupt = False

        ########### Below defines all frames and their grid stuff ###############

            #creates main frame which is child to root
        mainframe = ttk.Frame(root, padding='3 3 12 12')
        mainframe.pack()
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ##### Below defines frames tied to main frame ########
            #top frame
        topframe = ttk.Frame(mainframe, borderwidth=2, width=600, height=400)
        topframe.grid(column=0, row=0, rowspan=1, columnspan = 2, sticky=(N))
            #middle top frame
        midtopframe = ttk.Frame(mainframe, borderwidth=2, width=400, height=200)
        midtopframe.grid(column=0, row=1, rowspan=1, columnspan = 2)
            #middle bottom frame
        midbotframe = ttk.Frame(mainframe, borderwidth=2, relief="solid", width=1000, height= 1000)
        midbotframe.grid(column=0, row=2, rowspan=1, columnspan = 2, pady=20)
            #bottom frame
        botframe = ttk.Frame(mainframe, borderwidth=2, width=400, height=200)
        botframe.grid(column=0, row=3, rowspan=1, columnspan = 2)
        ###### Ends define frames tied to main frame ########

        ##### Below defines frames tied to top frame ######
            #frame containing title:
        titleframe = ttk.Frame(topframe, borderwidth=3, padding=10)
        titleframe.grid(column = 0, row = 0, rowspan = 1, columnspan = 1)
            #frame containing current capacitance and static labels
        capframe = ttk.Frame(topframe, borderwidth=3, width=200, height=100, padding=10)
        capframe.grid(column = 0, row = 1, rowspan = 1, columnspan = 1)
        ###### Ends defining frames tied to top frame #######

        ###### Bellow defines frames tied to middle top frame #######
        inputframe = ttk.Frame(midtopframe, borderwidth=2, relief="solid")
        inputframe.grid(column = 0, row = 0, rowspan = 2, columnspan = 1)
        ###### Ends defining frames ties to middle top frame #######

        ############ Ends defining all frames  ##################


        ###### Below Defines all Styles for Widgets ########
        style = ttk.Style()
        style.configure('.', font=('TkDefaultFont', 15), padding=5)
       


        ###### Ends Defining all Styles for Widgets ########

        ###### Below Defines all Widgets on screen ########

        #TITLE label (implement)
        self.title = tk.StringVar(value="Capacitance Measurment")
        title_label = tk.Label(titleframe, textvariable=self.title, borderwidth=3, width =25, bg='white')
        #self.title.set("Capacitance Measurment") #title var holds string for title
        title_label.config(font=("TkDefaultFont", 30), relief="solid", highlightbackground='red')
        title_label.grid()

        #title_label.grid(column = 1, row = 1, sticky = (N)) #WORK IN PROGRESS

        # "CURRENT VALUE" static label (implement)
        currCap_label = ttk.Label(capframe, text = "CURRENT CAPACITANCE VALUE")
        currCap_label.config(font=("TkDefaultFont", 15), relief='solid', padding=10, borderwidth=2)
        currCap_label.grid(column = 0, row = 0, rowspan = 1, columnspan = 1)

        #updating value dynamic label (implement)
        self.Cap_val = tk.StringVar() #this is the string var that will be updated
        #Cap_val_label = ttk.Label(capframe, textvariable=self.Cap_val)
        Cap_val_label = tk.Label(capframe, textvariable=self.Cap_val, background='white', font=("TkDefaultFont", 15), padx=10, pady=10, relief='solid', borderwidth=1, width=3)
        #Cap_val_label.config(font=("TkDefaultFont", 20), padding=10, relief='solid', borderwidth=2)
        Cap_val_label.grid(column = 1, row = 0, rowspan = 1, columnspan = 1, sticky=(W))
        self.Cap_val.set("0")

        # "pf" label (implement)
        pf_label1 = ttk.Label(capframe, text = "pf")
        pf_label1.config(font=("TkDefaultFont", 15), padding=10, relief='solid', borderwidth=3)
        pf_label1.grid(column = 2, row = 0, rowspan = 1, columnspan = 1)

        # "TIME" label (implement)
        time_label = ttk.Label(inputframe, text = "TIME")
        time_label.grid(column = 0, row = 0, rowspan = 1, columnspan = 1, sticky= (W))

        # "MAX CAPACITANCE" label (implement)
        max_cap_label = ttk.Label(inputframe, text = "MAX CAPACITANCE")
        max_cap_label.grid(column = 0, row = 1, rowspan = 1, columnspan = 1, sticky= (W))

        # "NUMBER OF POINTS" label (implement)
        num_points_label = ttk.Label(inputframe, text = "NUMBER OF POINTS")
        num_points_label.grid(column = 0, row = 2, rowspan = 1, columnspan = 1, sticky= (W))

        # Time entry (implement)
        self.time = StringVar()
        time_entry = ttk.Entry(inputframe, width=4, textvariable=self.time, font=("TkDefaultFont", 15))
        time_entry.grid(column = 1, row = 0, rowspan = 1, columnspan = 1)

        # max cap entry (implement)
        self.max_cap_var = StringVar()
        max_cap_entry = ttk.Entry(inputframe, width=4, textvariable=self.max_cap_var, font=("TkDefaultFont", 15))
        max_cap_entry.grid(column = 1, row = 1, rowspan = 1, columnspan = 1)

        # num points entry (implement)
        self.num_points_var = StringVar()
        num_points_entry = ttk.Entry(inputframe, width=4, textvariable=self.num_points_var, font=("TkDefaultFont", 15))
        num_points_entry.grid(column = 1, row = 2, rowspan = 1, columnspan = 1)

        # "sec" label (implement)
        sec_label = ttk.Label(inputframe, text = "sec")
        sec_label.grid(column = 2, row = 0, rowspan = 1, columnspan = 1, sticky=(W))

        # second "pf" label (implement)
        pf_label2 = ttk.Label(inputframe, text = "pf")
        pf_label2.grid(column = 2, row = 1, rowspan = 1, columnspan = 1, sticky=(W))

        # Start button (implement)

        start_btn = tk.Button(midtopframe, text = "START", bg='green', fg='white', relief='solid', height = 2, width=20, command=self.startTest)
        start_btn.grid(column = 1, row = 0, rowspan = 1, columnspan = 1, padx=100, sticky=(E))
        # Cancel button (implement)
        cancel_btn = tk.Button(midtopframe, text="CANCEL", bg='red', fg='white', relief='solid', height = 2, width=20, command = self.cancelTest)
        cancel_btn.grid(column = 1, row = 1, rowspan = 1, columnspan = 1)

        # Plot Figure (implement)
        
        
        
        canvas = FigureCanvasTkAgg(plot, master=midbotframe)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand= False)
        # Save Button (implement)
        save_btn = tk.Button(botframe, text="SAVE", bg='green', fg='white', relief='solid', height = 1, width= 10)
        save_btn.grid()

        ####### END defines Widgets ########


    ######### Functions ############

    #start button command:
    def startTest(self):
        #checks if any entries are empty
        if len(self.time.get()) == 0 or len(self.max_cap_var.get()) == 0 or len(self.num_points_var.get()) == 0:
            return
        self.Interrupt = True 
        self.timePeriod=int(self.time.get())
        self.maxCap = int(self.max_cap_var.get())
        self.numPoints = int(self.num_points_var.get())
        self.numPointsPerm = self.numPoints 
        self.sec_per_point = float(self.timePeriod)/float(self.numPoints)
        subPlot.clear()
        subPlot.set_aspect('auto')
        subPlot.set_xlim([0, self.numPoints])
        subPlot.set_xbound(lower=0.0, upper=self.numPoints)
        subPlot.set_ylim([0, self.maxCap])
        subPlot.set_ybound(lower=0.0, upper=self.maxCap)
        subPlot.set_xlabel("time (s)")
        subPlot.set_ylabel("capacitance (pf)")
        xList.clear()
        yList.clear()
        self.Interrupt = False
        self.mili_per_point = int(self.sec_per_point*1000)
        self.increment = 0
        global startTime 
        startTime = time.monotonic()
        global nextTime
        nextTime = startTime*1000 #in milliseconds
        self.queryLoop()

    def cancelTest(self):
        self.Interrupt = True
        subPlot.clear()
        xList.clear()
        yList.clear()

    #loop to query data  
    def queryLoop(self): 
        
        if self.numPoints == 0 or self.Interrupt == True:
            return 
        #if self.numPoints == self.numPointsPerm:
        #   global startTime
        #   global nextTime
        #   startTime = time.monotonic()
        #   nextTime = startTime*1000  #in milliseconds
        global nextTime             
        nextTime += self.mili_per_point 
        #print(nextTime)
        root.after(int(nextTime - (time.monotonic()*1000)), self.queryLoop)
        endTime = time.monotonic()
        queryList = hanteck.query("FETC?").split(',')
        finalTime = endTime - startTime       
        print(finalTime)       
        #print(queryList)
        xList.append(finalTime)
        capacitance = float(queryList[0])
        picoFarads = capacitance*10**12 #brings return from farads to pico farads for display
        self.Cap_val.set(round(picoFarads, 2))
        yList.append(picoFarads)
        self.numPoints -=1
        self.increment += 1
        #root.after(int(self.sec_per_point*1000), self.queryLoop)
       
    
    


def animate(self):
   
    subPlot.clear()
    subPlot.set_aspect('auto')
    subPlot.set_xlim([0, mainObject.timePeriod])
    subPlot.set_xbound(lower=0.0, upper=mainObject.timePeriod)
    subPlot.set_xlabel("time (s)")
    subPlot.set_ylabel("capacitance (pf)")
    if yList:
        subPlot.set_ylim([0, yList[0]])
        subPlot.set_ybound(lower=0.0, upper=yList[0])
    subPlot.plot(xList, yList, 'o')


   

xList = []
yList = []
startTime = time.monotonic()
endTime = time.monotonic()
nextTime = 0.0

timeSeconds = 0
rm = pyvisa.ResourceManager()
rm.list_resources()
hanteck = rm.open_resource('ASRL3::INSTR')


root = Tk()

mainObject = MainWindow(root)
#MainWindow(root)
ani = animation.FuncAnimation(plot, animate, interval=1000)

root.mainloop()
