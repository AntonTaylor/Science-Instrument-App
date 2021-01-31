import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

import matplotlib

#creates main window object called root


class MainWindow:

    

    def __init__(self, root):
        
        root.geometry('800x650+560+150')
        root.resizable(FALSE, FALSE)
        root.title("Capacitance Measurment")

        ########### Below defines all frames and their grid stuff ###############

            #creates main frame which is child to root
        mainframe = ttk.Frame(root)
        mainframe.grid(column = 0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        ##### Below defines frames tied to main frame ########
            #top frame
        topframe = ttk.Frame(mainframe, borderwidth=1, width=600, height=400)
        topframe.grid(column=0, row=0, rowspan=1, columnspan = 2, sticky=(N))
            #middle top frame
        midtopframe = ttk.Frame(mainframe, borderwidth=1, width=400, height=200)
        midtopframe.grid(column=0, row=1, rowspan=1, columnspan = 2)
            #middle bottom frame
        midbotframe = ttk.Frame(mainframe, borderwidth=1, relief="ridge", width=400, height=200)
        midbotframe.grid(column=0, row=2, rowspan=1, columnspan = 2, pady=40)
            #bottom frame
        botframe = ttk.Frame(mainframe, borderwidth=1, relief="ridge", width=400, height=200)
        botframe.grid(column=0, row=3, rowspan=1, columnspan = 2)
        ###### Ends define frames tied to main frame ########

        ##### Below defines frames tied to top frame ######
            #frame containing title:
        titleframe = ttk.Frame(topframe, borderwidth=3, relief="solid", width=400, height=200, padding=10)
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

        ###### Below Defines all Widgets on screen ########

        #TITLE label (implement)
        self.title = tk.StringVar(value="Capacitance Measurment")
        title_label = ttk.Label(titleframe, textvariable=self.title)
        #self.title.set("Capacitance Measurment") #title var holds string for title
        title_label.config(font=("TkDefaultFont", 32))
        title_label.grid()
        
        #title_label.grid(column = 1, row = 1, sticky = (N)) #WORK IN PROGRESS

        # "CURRENT VALUE" static label (implement)
        currCap_label = ttk.Label(capframe, text = "CURRENT CAPACITANCE VALUE")
        currCap_label.config(font=("TkDefaultFont", 20), relief='solid', padding=10, borderwidth=2)
        currCap_label.grid(column = 0, row = 0, rowspan = 1, columnspan = 1)

        #updating value dynamic label (implement)
        self.Cap_val = tk.StringVar() #this is the string var that will be updated
        Cap_val_label = ttk.Label(capframe, textvariable=self.Cap_val)
        Cap_val_label.config(font=("TkDefaultFont", 20), padding=10, relief='solid', borderwidth=2)
        Cap_val_label.grid(column = 1, row = 0, rowspan = 1, columnspan = 1)
        self.Cap_val.set("0")

        # "pf" label (implement)
        pf_label1 = ttk.Label(capframe, text = "pf")
        pf_label1.config(font=("TkDefaultFont", 20), padding=10, relief='solid', borderwidth=2)
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
        time_entry = tk.Entry(inputframe, width=4, textvariable=self.time)
        time_entry.grid(column = 1, row = 0, rowspan = 1, columnspan = 1)

        # max cap entry (implement)
        self.max_cap_var = StringVar()
        max_cap_entry = tk.Entry(inputframe, width=4, textvariable=self.max_cap_var)
        max_cap_entry.grid(column = 1, row = 1, rowspan = 1, columnspan = 1)

        # num points entry (implement)
        self.num_points_var = StringVar()
        num_points_entry = tk.Entry(inputframe, width=4, textvariable=self.num_points_var)
        num_points_entry.grid(column = 1, row = 2, rowspan = 1, columnspan = 1)

        # "sec" label (implement)
        sec_label = ttk.Label(inputframe, text = "sec")
        sec_label.grid(column = 2, row = 0, rowspan = 1, columnspan = 1, sticky=(W))

        # second "pf" label (implement)
        pf_label2 = ttk.Label(inputframe, text = "pf")
        pf_label2.grid(column = 2, row = 1, rowspan = 1, columnspan = 1, sticky=(W))

        # Start button (implement)
        start_btn = ttk.Button(midtopframe, text="START")
        start_btn.grid(column = 1, row = 0, rowspan = 1, columnspan = 1, padx=100, sticky=(E))

        # Cancel button (implement)
        cancel_btn = ttk.Button(midtopframe, text="CANCEL")
        cancel_btn.grid(column = 1, row = 1, rowspan = 1, columnspan = 1)

        # Plot Figure (implement)

        # Save Button (implement)
        save_btn = ttk.Button(botframe, text="SAVE")
        save_btn.grid()

        ####### END defines Widgets ########

    

root = Tk()

mainObject = MainWindow(root)
#MainWindow(root)


root.mainloop()