import pymysql
from entities import Question, Answer

def queryToDatabase(sql):
    connection=pymysql.connect(host="45.129.97.37", port=3306, user="aumann", password="aumann_game", database="pp_aumann", cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

def getQuestions():
    rawData = queryToDatabase("""SELECT
        Q.Id,
        Q.Text AS QuestionText,
        Q.IsTest,
        Q.HasBeenPlayed,
        Q.AuthorId,
        Q.CorrectAnswerId,
        A.Id AS AnswerId,
        A.Text AS AnswerText,
        A.IsCorrect
        FROM Question Q JOIN Answer A ON A.QuestionId = Q.Id""")
    items = {}
    for item in rawData:
        id = item['Id']
        if id in items.keys():
            q = items[id]
        else:
            q = Question(item['Id'], item['QuestionText'], bool(item['IsTest']), bool(item['HasBeenPlayed']), item['AuthorId'], None, item['CorrectAnswerId'], None)
            items[id] = q
        answer = Answer(item['AnswerId'], item['Id'], q, item['AnswerText'], bool(item['IsCorrect']))
        q.answers.append(answer)
        if (answer.isCorrect):
            q.correctAnswer = answer
    return items
