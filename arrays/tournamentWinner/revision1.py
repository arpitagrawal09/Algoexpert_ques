#Revision attempt 1
def tournamentWinner(competitions, results):
    leaderboard = {}
    for i in range(len(competitions)):
        pair = competitions[i]
        team1 = pair[0]
        team2 = pair[1]
        score1 = 0
        score2 = 0
        result = results[i]
        if result == 1: score1 = 3
        else: score2 = 3
        if team1 in leaderboard:
            leaderboard[team1]+=score1
        else: leaderboard[team1]=0
        if team2 in leaderboard:
            leaderboard[team2]+=score2
        else: leaderboard[team2]=0
    max = 0
    winner = "unknown"
    for team in leaderboard:
        score = leaderboard[team]
        if score > max:
            winner = team
            max = score
    return winner 

competitions = [["Bulls", "Eagles"]]
results = [1]
winner = tournamentWinner(competitions, results)