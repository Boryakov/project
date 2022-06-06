

def cut(cur_list:list() ) -> dict():
    if (len(cur_list)==1):
        return []
    quest=dict()
    answer=list()
    for i in range(len(cur_list)):
        
        
        if cur_list[i].startswith("Вопрос: "):
            
            quest['question']=cur_list[i]
            if cur_list[i+4].startswith("Прикрепленный файл:"):
                quest['dir']="Директория вопроса: "+str(cur_list[i+4].split()[2])

        elif cur_list[i].startswith("Ответ:"):
            temp=cur_list[i+1].split()
            if int(temp[1]) > 0:
                a=dict()
                if cur_list[i+2].startswith("Прикрепленный файл:"):
                    a['answer']="Директория ответа: "+str(cur_list[i+2].split()[2])
                else:
                    a['answer'] = cur_list[i]
                
                a['priority'] = temp[1]
                answer.append(a)
    cur_list = dict()
    cur_list["question"] = quest
    cur_list["answers"] = answer

    return cur_list 


names = ["диоды.txt","конструктивные особенности дискретных элементов.txt",
"лр-5(те,схем).txt","розрахунки в схемах з кодненсаторами.txt","транзистор.txt"]
def lapota(name:str) -> list:
    file = open(name,encoding="utf-8")
    qa = list()
    cur = list()




    for num,line in enumerate(file):
        if num<27:
            continue  
        line = line.strip()
        if line == '':
            continue
        cur.append(line)
        if line.startswith("[НОВЫЙ ВОПРОС]"):
            cur = cut(cur)
            
            if type(cur)==list:
                cur=list()
                
            else:
                qa.append(cur)
                cur=list()
                
    cur=cut(cur)
    qa.append(cur)

    return qa

""" qa=lapota(names[0])
#print(qa)
      
test=open('test.txt','w',encoding='utf-8')
test.write('huesos')
for i in range(len(qa)):
    qa[i]=dict(qa[i])
    helpstr=str(i+1)+" "+str(qa[i]['question']['question'])
    test.write(helpstr)
    try:
        test.write(qa[i]['question']['dir'])
    except:
        pass
    for q in range(len(qa[i]['answers'])):
        test.write(qa[i]['answers'][q]['answer'])
        helpstr2="Приоритет: "+str(qa[i]['answers'][q]['priority'])
        test.write(helpstr2)
 """