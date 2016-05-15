import urllib.request, json

#from pylatex import Document, Section, Package
def randQuest(n, filename):
    #f = ur.urlopen('http://jservice.io/api/random').read().decode('utf-8')
    file = open(filename, "w+")
    '''c = 0
    while c < n:
        q = urllib.request.urlopen('http://jservice.io/api/random').read().decode('utf-8')
        x = json.loads(q)
        print('question: ' + x[0]['question'] + ' ---- answer: ' + x[0]['answer'])
        c += 1'''
    print('Name: ', file.name)

