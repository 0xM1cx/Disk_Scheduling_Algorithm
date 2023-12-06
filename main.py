import customtkinter
import tkinter as tk
from tkinter import ttk
from time import sleep
import numpy as np

## Plotting Stuff
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


'''
# TODO 
1. Add animation to the line plot
2. Add a feature when picking UP and DOWN
3. Make the graph stright not gay
'''

## Algorithms
from FCFS import FCFS
from SSTF import SSTF
from SCAN__CSCAN import SCAN, CSCAN

'''
* The width of the RequestTable must be lesser than the width of the ScatterLineChart
'''
entries = []

class ErrorMessage(customtkinter.CTkToplevel):
    def __init__(self, *args):
        super().__init__(*args)
        self.geometry("500x500")
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=20)
        self.label = customtkinter.CTkLabel(self, font=font, width = 100, height=100, text_color="#b5e853", text="The Requests must be within the outermost and innermost disk range")

class ScatterLineChart(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

    def start(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data

        self.fig, self.ax = plt.subplots(figsize=(10, 9), dpi=100)
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, marker="o", linestyle='', color='orange')
        
        self.ax.set_yticks(self.y_data)
        self.ax.set_xticks(self.x_data)


        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack() 

        self.animation = FuncAnimation(self.fig, self.update_plot, frames=len(self.x_data), interval=200, blit=False)

    def update_plot(self, x_data, y_data, calc_label, total_head_movements):
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=14)

        # Update or recreate labels/widgets as needed
        for widget in self.winfo_children():
            widget.destroy()
        
        self.start(x_data, y_data)
        self.calcu_Label = customtkinter.CTkLabel(self, font=font, width = 50, height=50, text_color="#b5e853", text=f" = {calc_label}")
        self.calcu_Label.pack()
        self.total_calcu = customtkinter.CTkLabel(self, font=font, width=50, height=50, text_color="#b5e853", text=f"= {total_head_movements} Tracks")
        self.total_calcu.pack()
        self.canvas.draw()

#### The widgets in the frames must be in a grid
class RequestTable(customtkinter.CTkScrollableFrame):
    rowCounter = 0
    flag = True
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure((0), weight=1)

    def displayEntries(self, target_frame, noOfRequests):
        global entries

        if len(entries) != 0:
            for entry in entries:
                entry.destroy()
            entries = []

        for i in range(noOfRequests):
                entry = customtkinter.CTkEntry(target_frame)
                entry.grid(row=self.rowCounter, column=0, pady=5, padx=80, sticky="ew")
                entries.append(entry)
                self.rowCounter += 1

class OptionMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=14)
        ### Entry for the highest DISK ###        
        label_innerDisk = customtkinter.CTkLabel(self, font=font, text_color="#b5e853", text="What is the Innermost Track?")
        label_innerDisk.grid(row=0, column=0, padx=10, pady=10)
        self.inner_Disk = customtkinter.CTkEntry(self, font=font, text_color="#b5e853", placeholder_text="Number")
        self.inner_Disk.grid(row=1, column=0, padx=10, pady=10)

        ### Entry box for the start head disk ###
        label_headDisk = customtkinter.CTkLabel(self, font=font, text_color="#b5e853", text="What is the disk head?")
        label_headDisk.grid(row=0, column=1, padx=10, pady=10)
        self.headDisk = customtkinter.CTkEntry(self, font=font, text_color="#b5e853", placeholder_text="Disk Number")
        self.headDisk.grid(row=1, column=1, padx=10, pady=10)

        ### The number of request ###
        label_NumRequets = customtkinter.CTkLabel(self, font=font, text_color="#b5e853", text="How many request do you want?") 
        label_NumRequets.grid(row=0, column=2, padx=10, pady=10)
        self.NumRequest = customtkinter.CTkEntry(self, font=font, text_color="#b5e853", placeholder_text="No. of Requests")
        self.NumRequest.grid(row=1, column=2)

        ### Algorithm Picker ###
        self.pickAlgo = customtkinter.CTkComboBox(self, values=["FCFS", "SSTF", "SCAN", "LOOK", "C-SCAN", "C-LOOK"], command=self.getInput)
        self.pickAlgo.set("Pick A Algorithm")
        self.pickAlgo.grid(row=0, column=3, padx=10, pady=10)

        ### Start Button ###
        self.startBtn = customtkinter.CTkButton(self, text_color="#b6e853", font=font, fg_color="#1a1a1a", text="Execute", command=self.startExecution)
        self.startBtn.grid(row=1, column=3, padx=10, pady=10)
        
    def startExecution(self):
        DISK_ALGORITHMS = {
            "FCFS": FCFS(), 
            "SSTF": SSTF()
        }
        global entries
        requests = [int(entry.get()) for entry in entries]
        
        # check if the request are within the number of disks
        for value in requests:
            if value < 0 or value > int(self.inner_Disk.get()):
                error = ErrorMessage()
                self.removeAllInput()

        requests.insert(0, int(self.headDisk.get())) 

        if (self.pickAlgo.get() == "FCFS"):
            res_floats, total_head_movements, head_movement_calculation_str, req = DISK_ALGORITHMS[self.pickAlgo.get()].executeAlgorithm(requests)
        elif (self.pickAlgo.get() == "SSTF"):
            res_floats, total_head_movements, head_movement_calculation_str, req = DISK_ALGORITHMS[self.pickAlgo.get()].executeAlgorithm(requests)
        elif (self.pickAlgo.get() == "SCAN"):
            res_floats, total_head_movements, head_movement_calculation_str, req = SCAN(int(self.inner_Disk.get()), int(self.headDisk.get()), "U", requests)
        elif (self.pickAlgo.get() == "C-SCAN"):
            res_floats, total_head_movements, head_movement_calculation_str, req = CSCAN(int(self.inner_Disk.get()), int(self.headDisk.get()), "U", requests)
       
        chart = self.master.scatterLineChart
        chart.update_plot(res_floats, req, head_movement_calculation_str, total_head_movements)

    def getInput(self, value):
        self.test = RequestTable(self)
        self.test.displayEntries(target_frame=self.master.requestFrame, noOfRequests=int(self.NumRequest.get()))

    def removeAllInput(self):
        self.inner_Disk.delete("0.0", "end")
        self.headDisk.delete("0.0", "end")
        self.NumRequest.delete("0.0", "end")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("900x600")
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.optionMenu = OptionMenu(self)
        self.optionMenu.grid(row=1, column=0, sticky="ew", columnspan=2, padx=20, pady=20)
        
        self.requestFrame = RequestTable(self)
        self.requestFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
 
        self.scatterLineChart = ScatterLineChart(self)
        self.scatterLineChart.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()