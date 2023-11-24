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
    def __init__(self, master):
        super().__init__(master)

# The widgets in the frames must be in a grid


class RequestTable(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class OptionMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ### Entry for the highest DISK ###
        label_innerDisk = customtkinter.CTkLabel(
            self, text="What is the highest number of DISK")
        label_innerDisk.grid(row=0, column=0)
        self.inner_Disk = customtkinter.CTkEntry(
            self, placeholder_text="Input here")
        self.inner_Disk.grid(row=1, column=0)

        ### Entry box for the start head disk ###
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("900x600")

        self.optionMenu = OptionMenu(self)
        self.optionMenu.pack()
if __name__ == "__main__":
    app = App()
    app.mainloop()
