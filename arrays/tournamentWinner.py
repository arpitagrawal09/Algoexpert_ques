def tournamentWinner(competitions, results):
    # Write your code here.
    winner = "pls hang tight! our systems will return the result soon"
    leaderboard = []
    teams = []
    noOfComp = len(competitions)
    for i in range(noOfComp):
        teamPair = competitions[i]
        homeTeam = teamPair[0]
        awayTeam = teamPair[1]
        registerTeam = ""
        
        if(homeTeam not in teams):
            registerTeam = homeTeam
            teams.append(registerTeam)
            leaderboard.append([registerTeam, 0])
        if(awayTeam not in teams):
            registerTeam = awayTeam                
            teams.append(registerTeam)            
            leaderboard.append([registerTeam, 0])
                
        if(results[i]==1):
            matchWinner = homeTeam
        else:
            matchWinner = awayTeam
        teamIndex = teams.index(matchWinner)
        leaderboard[teamIndex][1]+=1                
    
    maxWins = 0
    noOfTeams = len(leaderboard)
    for i in range(noOfTeams):
        if(leaderboard[i][1]>maxWins):
            maxWins = leaderboard[i][1]
            winner = leaderboard[i][0]
    
    return winner
