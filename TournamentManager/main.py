# Main file for application

# Using tkinter library for GUI
import tkinter as tk
from Tournament import Tournament
from TournamentInfoEntryMenu import TournamentInfoEntryMenu


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.t = Tournament("Test", "Collins Park", "9:00 am", 20, 4, 15)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (StartPage, TournamentInfoEntryMenu):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        #self.t.displayInfo()


class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        label = tk.Label(self, text="Create New Tournament")
        label.pack()

        button = tk.Button(self, text="Start", command=lambda: controller.show_frame("TournamentInfoEntryMenu"))
        button.pack()



# Start button callback, will ask user to give information about tournament
def createCallBack():
    print("Creating Tournament...")

    #t.getTeamsFromUser()
    #t.displayAllTeams()
    #t.getResultsFromUser()
    #t.displayAllTeams()
    #t.calculatePlayoffSeeding(0)
    #t.getPlayoffResultsFromUser()

app = App()
app.mainloop()

