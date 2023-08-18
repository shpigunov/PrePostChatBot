from dbconnection import queryToDatabase

def getLatestGame():
    latestGame = queryToDatabase(f"""SELECT
    Time,
    GameState
    FROM Game ORDER BY Time DESC LIMIT(1)""")
    return latestGame[0]["GameState"]

