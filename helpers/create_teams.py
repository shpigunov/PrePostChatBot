import random 
def createTeams(users):
    random.shuffle(users)
    empty_list = []
    if len(users) < 3:
        return empty_list
    if len(users) == 6:
        return [users[0:3], users[3:6]]
    remaining_users = len(users)%4
    teams = [users[x:x+4] for x in range(0, len(users), 4)]
    if remaining_users == 0:
        return teams
    teams.pop()   
    if remaining_users == 1:
        teams[-1].append(users[-1])
    if remaining_users == 2:
        teams[-2].append(users[-2])
        teams[-1].append(users[-1])
    if remaining_users == 3:
        teams = [*teams, [users[-3:len(users)]]]
    return teams
