from helper import lapota, cut
import os


names = ["1.txt"]


def complete(name):
    qa, title = lapota(name)
    dir = 'answers/complete_'+name
    try:
        test = open(dir, 'w', encoding='utf-8')
    except:
        os.mkdir("answers")
        test = open(dir, 'w', encoding='utf-8')
    test.write(title)
    for i in range(len(qa)):
        qa[i] = dict(qa[i])
        helpstr = str(i+1)+" "+str(qa[i]['question']['question'])+'\n'
        test.write(helpstr)
        try:
            test.write(str(qa[i]['question']['dir']+'\n'))
        except:
            pass
        for q in range(len(qa[i]['answers'])):
            test.write(str(qa[i]['answers'][q]['answer'] +
                       "   (приоритет " + str(qa[i]['answers'][q]['priority']) + ')\n'))
        test.write('\n')
