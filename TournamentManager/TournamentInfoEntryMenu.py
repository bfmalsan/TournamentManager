import tkinter as tk


class TournamentInfoEntryMenu(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.infoSubmitted = False

        labelName = tk.Label(self, text="Name").grid(row=0, column=0, sticky=tk.E)
        self.entryName = tk.Entry(self)
        self.entryName.grid(row=0, column=1)
        labelPlace = tk.Label(self, text="Place").grid(row=1, column=0, sticky=tk.E)
        self.entryPlace = tk.Entry(self)
        self.entryPlace.grid(row=1, column=1)
        labelTime = tk.Label(self, text="Start Time").grid(row=2, column=0, sticky=tk.E)
        self.entryTime = tk.Entry(self)
        self.entryTime.grid(row=2, column=1)
        labelTeams = tk.Label(self, text="Number of Teams").grid(row=3, column=0, sticky=tk.E)
        self.entryTeams = tk.Entry(self)
        self.entryTeams.grid(row=3, column=1)
        labelPlayers = tk.Label(self, text="Number of Players").grid(row=4, column=0, sticky=tk.E)
        self.entryPlayers = tk.Entry(self)
        self.entryPlayers.grid(row=4, column=1)
        labelNets = tk.Label(self, text="Number of Nets").grid(row=5, column=0, sticky=tk.E)
        self.entryNets = tk.Entry(self)
        self.entryNets.grid(row=5, column=1)

        submitButton = tk.Button(self, text="Submit", command=lambda: self.submitInfo(controller))
        submitButton.grid(columnspan=2)

    def submitInfo(self, controller):
        print("info submitted")
        controller.t.getInfoFromMenu(self.getName(), self.getPlace(), self.getTime(), self.getTeams(), self.getPlayers(), self.getNets())
        controller.show_frame("StartPage")
        self.infoSubmitted = True

    def hasBeenSubmitted(self):
        return self.infoSubmitted

    def getName(self):
        return self.entryName.get()

    def getPlace(self):
        return self.entryPlace.get()

    def getTime(self):
        return self.entryTime.get()

    def getTeams(self):
        return self.entryTeams.get()

    def getPlayers(self):
        return self.entryPlayers.get()

    def getNets(self):
        return self.entryNets.get()
