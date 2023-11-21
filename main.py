import customtkinter
'''
* The width of the RequestTable must be lesser than the width of the ScatterLineChart
'''
### TODO ###
# Add inner disk number entry 
# Place the two frames next to each other
# Add a entry box for the starting head disk
# Add a entry to input the number of requests
# Add a table input to pass in those requests

class ScatterLineChart(customtkinter.CTkFrame):
    pass

#### The widgets in the frames must be in a grid
class RequestTable(customtkinter.CTkFrame):
    def __init__(self):
       pass 

class OptionMenu(customtkinter.CTkFrame):
    def __init__(self):
        self.inner_Disk = customtkinter.CTkEntry(self, placeholder_text="What is the highest number of the Disk")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("900x600")



if __name__ == "__main__":
    app = App()
    app.mainloop()