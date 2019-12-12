class Team:

    teamCnt = 0

    def __init__(self, id, name, numOfTeamsInPool):
        self.teamID = int(id)
        self.teamName = name
        self.wins = 0
        self.losses = 0
        self.pointDiff = 0
        self.headToHead = [None] * numOfTeamsInPool
        self.headToHead[self.teamID] = 0
        Team.teamCnt += 1

    def displayTeamInfo(self):
        print(self.toString())

    def toString(self):
        return "\nTEAM ID: " + str(self.teamID) + "\nTEAM NAME: " + self.teamName + "\nWINS: " + str(self.wins) + \
               "\nLOSSES: " + str(self.losses) + "\nPOINT DIFF: " +str(self.pointDiff)

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def updateHeadToHeadWin(self, teamIdWonAgainst):
        self.headToHead[teamIdWonAgainst] = 1

    def updateHeadToHeadLoss(self, teamIdLossAgainst):
        self.headToHead[teamIdLossAgainst] = -1

    def addToPointDiff(self, wonBy):
        self.pointDiff = self.pointDiff + wonBy

    def subtractFromPointDiff(self, lostBy):
        self.pointDiff = self.pointDiff - lostBy

    # Getter and Setter functions
    def getTeamId(self):
        return self.teamID

    def setTeamId(self, id):
        self.teamID = id

    def getTeamName(self):
        return self.teamName

    def setTeamName(self, name):
        self.teamName = name

    def getWins(self):
        return self.wins

    def setWins(self, wins):
        self.wins = wins

    def getLosses(self):
        return self.losses

    def setLosses(self, losses):
        self.losses = losses

    def getPointDiff(self):
        return self.pointDiff

    def setPointDiff(self, pd):
        self.pointDiff = pd

    def getHeadToHead(self):
        return self.headToHead

    def setHeadToHead(self, hth):
        self.headToHead = hth
