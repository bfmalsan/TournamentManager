from Team import Team


class Tournament:

    # Variables to hold the main information about the tournament
    def __init__(self, title, place, startTime, numTeamsMax, numPlayersPerTeam, numNets):
        self.title = title
        self.place = place
        self.startTime = startTime
        self.numTeamsMax = numTeamsMax
        self.numPlayersPerTeam = numPlayersPerTeam
        self.numNets = numNets  # Will help decide the number of pools
        self.teams = []  # Will hold all the teams in the tournament
        self.finalSeeding = []  # Team id is index of the list, will hold value for what position the team is in

    def displayInfo(self):
        print(self.toString())

    def toString(self):
        return "TITLE: " + self.title + "\nPLACE: " + self.place + "\nSTART TIME: " + self.startTime + \
               "\n# MAX TEAMS: " + str(self.numTeamsMax) + "\n# PLAYERS/TEAM: " + str(self.numPlayersPerTeam) + \
               "\n# NETS: " + str(self.numNets)

    # Eventually will save and load tournament info from a file
    # def saveTournament(self):

    # def loadTournament(self):

    def getInfoFromUser(self):
        print("Input Title: ")
        self.setTitle(input())
        print("Input Place: ")
        self.setPlace(input())
        print("Input Start Time: ")
        self.setStartTime(input())
        print("Input Max Number of Teams: ")
        self.setMaxNumTeams(int(input()))
        print("Input Number of Players Per Team: ")
        self.setNumPlayersPerTeam(int(input()))
        print("Input Number of Nets: ")
        self.setNumNets(int(input()))

    def getInfoFromMenu(self, name, place, time, teams, players, nets):
        self.setTitle(name)
        self.setPlace(place)
        self.setStartTime(time)
        self.setMaxNumTeams(int(teams))
        self.setNumPlayersPerTeam(int(players))
        self.setNumNets(int(nets))

    def getTeamsFromUser(self):
        print("Insert the teams:")
        for x in range(self.numTeamsMax):

            print("Team " + str(x) + ":")
            team = Team(x, input(), self.numTeamsMax)
            self.teams.append(team)
            self.finalSeeding.append(1)

    def getResultsFromUser(self):
        print("Please input the scores of each game:")
        for team1 in self.teams:
            for nextTeamIndex in range(team1.getTeamId() + 1, self.numTeamsMax):
                team2 = self.teams[nextTeamIndex]
                print("Team " + str(team1.getTeamId()) + " VS. Team " + str(team2.getTeamId()))
                print("Team " + str(team1.getTeamId()) + " Score: ")
                team1Score = int(input())
                print("Team " + str(team2.getTeamId()) + " Score: ")
                team2Score = int(input())

                if team1Score > team2Score:
                    team1.addWin()
                    team2.addLoss()
                    team1.updateHeadToHeadWin(team2.getTeamId())
                    team2.updateHeadToHeadLoss(team1.getTeamId())
                    scoreDiff = team1Score - team2Score
                    team1.addToPointDiff(scoreDiff)
                    team2.subtractFromPointDiff(scoreDiff)
                else:
                    team1.addLoss()
                    team2.addWin()
                    team1.updateHeadToHeadLoss(team2.getTeamId())
                    team2.updateHeadToHeadWin(team1.getTeamId())
                    scoreDiff = team2Score - team1Score
                    team1.subtractFromPointDiff(scoreDiff)
                    team2.addToPointDiff(scoreDiff)

    # recursive function to calculate final seeding for playoffs
    def calculatePlayoffSeeding(self, startIndex):
        # print("\nCalculating Playoff Seeding...")

        if startIndex == self.numTeamsMax:
            return

        testTeam = self.teams[startIndex]

        for team in self.teams:
            if team.getWins() > testTeam.getWins():
                self.finalSeeding[testTeam.getTeamId()] += 1
            elif team.getWins() == testTeam.getWins():
                # whoever has the highest point diff becomes the new higher seed.
                if team.getPointDiff() > testTeam.getPointDiff():
                    self.finalSeeding[testTeam.getTeamId()] += 1
                elif team.getPointDiff() == testTeam.getPointDiff():
                    # whoever won the head to head becomes the the higher seed.
                    print("We need a head to head tie breaker")
                    testingHTH = testTeam.getHeadToHead()
                    if testingHTH[team.getTeamId()] == -1:
                        self.finalSeeding[testTeam.getTeamId()] += 1

        print("FINAL SEEDING: \n")
        print(self.finalSeeding)

        self.calculatePlayoffSeeding(startIndex + 1)

    def getPlayoffResultsFromUser(self):
        # semifinals 1v4, 2v3
        for teamNum in range(self.numTeamsMax):
            if self.finalSeeding[teamNum] == 1:
                team1 = self.teams[teamNum]
            elif self.finalSeeding[teamNum] == 2:
                team2 = self.teams[teamNum]
            elif self.finalSeeding[teamNum] == 3:
                team3 = self.teams[teamNum]
            elif self.finalSeeding[teamNum] == 4:
                team4 = self.teams[teamNum]

        print("Semifinal #1: Team " + str(team1.getTeamId()) + " VS. Team " + str(team4.getTeamId()))
        print("Team " + str(team1.getTeamId()) + " Score: ")
        team1Score = int(input())
        print("Team " + str(team4.getTeamId()) + " Score: ")
        team4Score = int(input())

        if team1Score > team4Score:
            semiTeam1 = team1
        else:
            semiTeam1 = team4

        print("Semifinal #2: Team " + str(team2.getTeamId()) + " VS. Team " + str(team3.getTeamId()))
        print("Team " + str(team2.getTeamId()) + " Score: ")
        team2Score = int(input())
        print("Team " + str(team3.getTeamId()) + " Score: ")
        team3Score = int(input())

        if team2Score > team3Score:
            semiTeam2 = team2
        else:
            semiTeam2 = team3

    # Finals
        print("Finals: Team " + str(semiTeam1.getTeamId()) + " VS. Team " + str(semiTeam2.getTeamId()))
        print("Team " + str(semiTeam1.getTeamId()) + " Score: ")
        semiTeam1Score = int(input())
        print("Team " + str(semiTeam2.getTeamId()) + " Score: ")
        semiTeam2Score = int(input())

        if semiTeam1Score > semiTeam2Score:
            print("Team " + str(semiTeam1.getTeamId()) + ": " + semiTeam1.getTeamName() + " is the winner!")
        else:
            print("Team " + str(semiTeam2.getTeamId()) + ": " + semiTeam2.getTeamName() + " is the winner!")

    def displayAllTeams(self):
        for team in self.teams:
            team.displayTeamInfo()
            print(team.getHeadToHead())

    # Getter and Setter functions for variables
    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getMaxNumTeams(self):
        return self.numTeamsMax

    def setMaxNumTeams(self, numTeamsMax):
        self.numTeamsMax = numTeamsMax

    def getNumPlayersPerTeam(self):
        return self.numPlayersPerTeam

    def setNumPlayersPerTeam(self, numPlayersPerTeam):
        self.numPlayersPerTeam = numPlayersPerTeam

    def getNumNets(self):
        return self.numNets

    def setNumNets(self, numNets):
        self.numNets = numNets

    def getTeams(self):
        return self.teams
