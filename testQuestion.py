import urllib.request, json

def getQuestion():
    q = urllib.request.urlopen('http://jservice.io/api/random').read().decode('utf-8')
    x = json.loads(q)
    getQuestion.question = x[0]['question']
    getQuestion.answer = x[0]['answer']
    print(getQuestion.question + ' ===== ' + getQuestion.answer)
