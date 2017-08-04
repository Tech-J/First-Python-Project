import sys
# sys.path.insert(0, './site-packages')
import GetQuestions
import string
import random
import math

class DisplayQuestions(object):
    def __init__(self, arg):
        super(DisplayQuestions, self).__init__()
        self.arg = arg
        self.random=0
        self.answerBank = None
        self.answer = None
        self.score = 0

    def answerEachQuestion(self):
        for x in self.arg:
            print(x['question'])
            self.random = random.randint(0,len(x['incorrect_answers']))
            x['incorrect_answers'].insert(self.random,x['correct_answer'])
            self.answerBank = x['incorrect_answers']
            for newX in self.answerBank:
                print(newX)
            self.answer = input("Enter Answer")
            self.checkAnswer(self.answer,x['correct_answer'])
        self.displayScore()


    def checkAnswer(self,input_answer, correct_answer):
        print(input_answer, correct_answer)
        if input_answer == correct_answer:
            print("you got it right")
            self.score+=self.score+1
        else:
            print("Sorry Your wrong")


    def displayScore(self):
        print("Your Score Is")
        print(self.score)
