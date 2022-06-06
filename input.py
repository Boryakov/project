

def cut(cur_list:list() ) -> dict():
    if (len(cur_list)==1):
        return []
    quest=dict()
    answer=list()
    for i in range(len(cur_list)):
        
        
        if cur_list[i].startswith("Вопрос: "):
            
            quest['question']=cur_list[i]
            try:
                if cur_list[i+4].startswith("Прикрепленный файл:"):
                    quest['dir']="Директория вопроса: "+str(cur_list[i+4].split()[2])
            except:
                pass
        elif cur_list[i].startswith("Ответ:"):
            index=i
            while not cur_list[index].startswith("Приоритет:"):
                if cur_list[i]!=cur_list[index]:
                    cur_list[i]+=cur_list[index]
                index+=1
            temp=cur_list[index].split()
            if int(temp[1]) > 0:
                a=dict()
                try:
                    if cur_list[i+2].startswith("Прикрепленный файл:"):
                        a['answer']="Директория ответа: "+str(cur_list[i+2].split()[2])
                    else:
                        a['answer'] = cur_list[i]
                except:
                    a['answer'] = cur_list[i]
                
                a['priority'] = temp[1]
                answer.append(a)
    cur_list = dict()
    cur_list["question"] = quest
    cur_list["answers"] = answer

    return cur_list 


def lapota(name:str) -> list and str:
    file = open(name,encoding="ANSI")
    qa = list()
    cur = list()
    title=''



    for num,line in enumerate(file):
        if num==23:
            title=line.strip()
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

    return qa , title+'\n'

