import customtkinter
import tkinter as tk
from tkinter import ttk
'''
* The width of the RequestTable must be lesser than the width of the ScatterLineChart
'''
### TODO ###
# When the displayEntries function is called, it must 1st destroy any entries to prevent overlap
# Make the entries responsive

class ScatterLineChart(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

#### The widgets in the frames must be in a grid
class RequestTable(customtkinter.CTkScrollableFrame):
    entries = []
    columnCounter = 0
    rowCounter = 0
    flag = True
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure((0, 1), weight=1)

    def displayEntries(self, target_frame, noOfRequests):
        print(self.winfo_children())
        

        for i in range(noOfRequests):
            if(i >= 11):
                self.columnCounter = 1
                if self.flag:
                    self.rowCounter = 0
                    self.flag = False
                self.entry = customtkinter.CTkEntry(target_frame)
                self.entry.grid(row=self.rowCounter, column=self.columnCounter, pady=5, padx=5, sticky="ew")
                self.entries.append((self.rowCounter, self.columnCounter))
                self.rowCounter += 1
            elif(i < 11):
                self.entry = customtkinter.CTkEntry(target_frame)
                self.entry.grid(row=i, column=0, pady=2, padx=5, sticky="ew", columnspan=2)
                self.entries.append((i, 0))
            elif(i > 22):
                self.entry = customtkinter.CTkEntry(target_frame)
                self.entry.grid(row=self.rowCounter, column=self.columnCounter, pady=5, padx=5, sticky="ew")
                self.entries.append((self.rowCounter, self.columnCounter))
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
        label_NumRequets = customtkinter.CTkLabel(self, font=font, text_color="#b5e853", text="Hoe many request do you want?") 
        label_NumRequets.grid(row=0, column=2, padx=10, pady=10)
        self.NumRequest = customtkinter.CTkEntry(self, font=font, text_color="#b5e853", placeholder_text="No. of Requests")
        self.NumRequest.grid(row=1, column=2)


        ### Algorithm Picker ###
        self.pickAlgo = customtkinter.CTkComboBox(self, values=["FCFS", "SSTF", "SCAN", "LOOK", "C-SCAN", "C-LOOK"], command=self.getInput)
        self.pickAlgo.set("Pick A Algorithm")
        self.pickAlgo.grid(row=0, column=3, padx=10, pady=10)
        ### Start Button ###
        self.startBtn = customtkinter.CTkButton(self, text_color="#b5e853", font=font, fg_color="#1a1a1a", text="Execute", command=self.startExecution)
        self.startBtn.grid(row=1, column=3, padx=10, pady=10)

    def startExecution(self):
        pass

    def getInput(self, value):
        self.test = RequestTable(self)
        self.test.displayEntries(target_frame=self.master.requestFrame, noOfRequests=int(self.NumRequest.get()))


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