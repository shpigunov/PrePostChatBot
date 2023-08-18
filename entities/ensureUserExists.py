from dbconnection import queryToDatabase
def ensureUserExists(name, telegramUserId):
    rawData = queryToDatabase(f"""SELECT
        Id,
        TelegramUserId
        FROM User WHERE TelegramUserId = {telegramUserId}""")
    

    if len(rawData) > 0:
        return rawData[0]["Id"]
    userId = queryToDatabase(f"""INSERT INTO User(TelegramUserId, Name) 
    VALUES ({telegramUserId}, {repr(name)})""")

    return userId
