from datetime import datetime
from enum import Enum

class GameState(Enum):
    PENDING = 1
    TEAMS_FORMING = 2
    ROUND_STARTED = 3
    ROUND_FINISHED = 4
    GAME_FINISHED = 5

# Запитання в грі
class Question:
    def __init__(self, id: int, text: str, isTest: bool, hasBeenPlayed: bool, authorId: int, author: User, correctAnswerId: int, correctAnswer: Answer):
        self.id = id
        self.text = text
        self.isTest = isTest
        self.hasBeenPlayed = hasBeenPlayed
        self.authorId = authorId
        self.author = author
        self.correctAnswerId = correctAnswerId
        self.correctAnswer = correctAnswer

# варіант відповіді на запитання
class Answer:
    def __init__(self, id: int, questionId: int, question: Question, text: str, isCorrect: bool):
        self.id = id
        self.questionId = questionId
        self.question = question
        self.text = text
        self.isCorrect = isCorrect

# користувач бота (гравець)
class User:    
    def __init__(self, id: int, telegramUserId: int, name: str):
        self.id = id
        self.telegramUserId = telegramUserId
        self.name = name

# раунд гри (одне запитання, зігране в певний момент часу)
class Round:
    def __init__(self, id: int, questionId: int, question: Question, gameId: int, game: Game, time: datetime):
        self.id = id
        self.questionId = questionId
        self.question = question
        self.gameId = gameId
        self.game = game
        self.time = time

# гра (серія раундів)
class Game:
    def __init__(self, id: int, time: datetime, initiatingUserId: int, initiatingUser: User, gameState: GameState, numberOfRounds: int, isTest: bool):
        self.id = id
        self.time = time
        self.initiatingUserId = initiatingUserId
        self.initiatingUser = initiatingUser
        self.gameState = gameState
        self.numberOfRounds = numberOfRounds
        self.isTest = isTest

# команда гравців
class Team:
    def __init__(self, id: int, gameId: int, game: Game, playersCount: int):
        self.id = id
        self.gameId = gameId
        self.game = game
        self.playersCount = playersCount

# користувач-запитання - запис, який показує, що цей користувач уже зіграв це запитання (щоб не показувати йому те саме запитання знову)
# необов’язково
class UserToQuestion:
    def __init__(self, userId: int, user: User, questionId: int, question: Question, gameId: int, game: Game):
        self.userId = userId
        self.user = user
        self.questionId = questionId
        self.question = question
        self.gameId = gameId 
        self.game = game

# користувач-раунд - інформація про ставку, яку зробив цей користувач у цьому раунді, і про виграні бали
class UserToRound:
    def __init__(self, userId: int, user: User, roundId: int, round: Round, answerId: int, answer: Answer, bet: int, score: int):
        self.userId = userId
        self.user = user
        self.roundId = roundId
        self.round = round
        self.answerId = answerId
        self.answer = answer
        self.bet = bet
        self.score = score
    
# користувач-гра - інформація про те, скільки балів заробив цей гравець у цій грі і яке місце посів
class UserToGame:
    def __init__(self, userId: int, user: User, gameId: int, game: Game, score: int, place: int):
        self.userId = userId
        self.user = user
        self.gameId = gameId 
        self.game = game
        self.score = score
        self.place = place

# користувач-команда - хто до якої команди належить у кожній грі
class UserToTeam:
    def __init__(self, userId: int, user: User, teamId: int, team: Team):
        self.userId = userId
        self.user = user
        self.teamId = teamId
        self.team = team