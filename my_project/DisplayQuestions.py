import GetQuestions
import string
import random
import math

class DisplayQuestions(object):
    #class constructor which initializes class variables to start the game
    def __init__(self, arg):
        super(DisplayQuestions, self).__init__()
        #this variable is set to the questions poll json object
        self.arg = arg
        self.random=0
        self.answerBank = None
        self.answer = None
        self.score = 0

    #this loop display each question and answer choices and ask for an input for the answer
    def answerEachQuestion(self):
        #loop over each item in the list and display the question
        for x in self.arg:
            print(x['question'])
            #get a random number between zero and the length of the incorrect answer list and use that number
            #to  insert the correct answer into the incorrect answer list and store those answers into the class
            #variable self.answerBank
            self.random = random.randint(0,len(x['incorrect_answers']))
            x['incorrect_answers'].insert(self.random,x['correct_answer'])
            self.answerBank = x['incorrect_answers']
            #print out all the answer selections from the answerbank list and get a user input
            #and call the method checkAnswer
            for newX in self.answerBank:
                print(newX)
            self.answer = input("Enter Answer")
            self.checkAnswer(self.answer,x['correct_answer'])
        #at the end of the loop we call this method to display the score at the end of the game
        self.displayScore()

    #this methods check to see if the answer entered is the correct answer
    def checkAnswer(self,input_answer, correct_answer):
        #conditional statement that checks if your answer is right. If the answer is correct display "you got it right"
        # and add 1 to the score,  if not display a message you got it wrong and don't earn a point
        if input_answer == correct_answer:
            print("you got it right")
            self.score+=self.score+1
        else:
            print("Sorry Your wrong")

    #this method displays the score at the end of the game
    def displayScore(self):
        print("Your Score Is")
        print(self.score)
