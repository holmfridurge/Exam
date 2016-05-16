import urllib.request, json

def randQuest():
    print("Please insert the following information.")
    filename = input('Filename: ')
    dateOfTest = input('Date of the test: ')
    n = input('How many questions do you want to generate? ')
    n = int(n)

    return questions(filename, n, dateOfTest)
    
def questions(filename, n, dateOfTest):
    file1 = open((filename+'.txt'), 'w+')
    file2 = open((filename+'Answers.txt'), 'w+')
    
    file1.write('Test ' + '\n' + 'Date: ' + dateOfTest + (('\n')*3))
    c = 0
    while c < n:
        q = urllib.request.urlopen('http://jservice.io/api/random').read().decode('utf-8')
        x = json.loads(q)
        if x[0]['question'] != '' and x[0]['answer'] != '':
            file1.write('Question ' + str(c+1) + ': ' + '\n' + x[0]['question']
                       + ('\n')*6)
            file2.write('Question ' + str(c+1) + ': ' + '\n' + x[0]['question']
                       + '\n' + '---- answer: ' + x[0]['answer'] + (('\n')*6))
        c += 1

def getQuestion():
    q = urllib.request.urlopen('http://jservice.io/api/random').read().decode('utf-8')
    x = json.loads(q)
    getQuestion.question = x[0]['question']
    getQuestion.answer = x[0]['answer']
    print(getQuestion.question + ' ===== ' + getQuestion.answer)
    return getQuestion.question

def getAnswer():
    return getQuestion.answer

def getResult(answer, givenAns):
    if answer.lower() == givenAns.lower():
        return "True"
    else:
        return "False"
