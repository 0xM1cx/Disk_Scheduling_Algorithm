import customtkinter
'''
* The width of the RequestTable must be lesser than the width of the ScatterLineChart
'''
### TODO ###
# Place the two frames next to each other
# Add a entry to input the number of requests
# Add a table input to pass in those requests

class ScatterLineChart(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

#### The widgets in the frames must be in a grid
class RequestTable(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
class OptionMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ### Entry for the highest DISK ###        
        label_innerDisk = customtkinter.CTkLabel(self, text="What is the highest number of DISK?")
        label_innerDisk.grid(row=0, column=0, padx=10, pady=10)
        self.inner_Disk = customtkinter.CTkEntry(self, placeholder_text="Input here")
        self.inner_Disk.grid(row=1, column=0, padx=10, pady=10)

        ### Entry box for the start head disk ###
        label_headDisk = customtkinter.CTkLabel(self, text="What is the starting disk?")
        label_headDisk.grid(row=0, column=1, padx=10, pady=10)
        self.headDisk = customtkinter.CTkEntry(self, placeholder_text="Head Disk Number")
        self.headDisk.grid(row=1, column=1, padx=10, pady=10)

        ### The number of request ###
        label_NumRequets = customtkinter.CTkLabel(self, text="Hoe many request do you want?") 
        label_NumRequets.grid(row=0, column=2, padx=10, pady=10)
        self.NumRequest = customtkinter.CTkEntry(self, placeholder_text="No. of Requests")
        self.NumRequest.grid(row=1, column=2, padx=10, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("900x600")

        self.optionMenu = OptionMenu(self)
        self.optionMenu.pack(side="bottom")

if __name__ == "__main__":
    app = App()
    app.mainloop()