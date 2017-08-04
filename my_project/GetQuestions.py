import requests
import json
class GetQuestions(object):
    def __init__(self):
        super(GetQuestions, self).__init__()
        self.arg = None
    #this method gets
    def getitem(self):
        r=requests.get('https://opentdb.com/api.php?amount=10')
        new1= r.json()
        self.arg=new1['results']
        return self.arg


