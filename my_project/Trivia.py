from GetQuestions import GetQuestions
from DisplayQuestions import DisplayQuestions

#here we ceate a new instance of the GetQuestions clsss
triviaQuestions = GetQuestions().getitem()
#there we crete a new instance of the Display Questions and use the
#instance of the GetQuestions class to get the game started
startGame = DisplayQuestions(triviaQuestions)
#here we call the method answerEachQuestion which begins the game
startGame.answerEachQuestion()

