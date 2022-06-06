from input import lapota,cut


names = ["диоды.txt","конструктивные особенности дискретных элементов.txt",
"лр-5(те,схем).txt","розрахунки в схемах з кодненсаторами.txt","транзистор.txt"] 



for name in names:
    qa=lapota(name)    
    dir='answers/complete_'+name
    test=open(dir,'w',encoding='utf-8')
    for i in range(len(qa)):
        qa[i]=dict(qa[i])
        helpstr=str(i+1)+" "+str(qa[i]['question']['question'])+'\n'
        test.write(helpstr)
        try:
            test.write(str(qa[i]['question']['dir']+'\n'))
        except:
            pass
        for q in range(len(qa[i]['answers'])):
            test.write(str(qa[i]['answers'][q]['answer']+'\n'))
            helpstr2="Приоритет: "+str(qa[i]['answers'][q]['priority']+'\n')
            test.write(helpstr2) 

