import os


class TestReader():

    def __init__(self, directory: str):

        self.directory = directory
        self.list = list()
        self.title = str()
        TestReader.__create_list(self)
        """
        Parameters
        ----------
        directory : str
            The text file directory
        list : list
            The list of qustion in test and answers
            on them . List item is dictionary
            with question dictionary which contain
            question and if exist question image
            directory and 
            answer which contains every correct answer
            and if exist answer image directory
        title : str
            Contains the name of a test

        """

    def __list_transformer(cur_list: list) -> dict():
        """Takes list of all strings from quest to next quest 
        and transform it to dictionary which contains filtered
        question and answers

        Parameters
        ----------
        cur_list : list
            list of all strings from quest to next quest

        Return
        ------
        None
            if list size is 1
        dictionary 
            dictionary which contains question and answers
            format:
                quest:
                    dictionary["quest"]["quest"] = test quest
                    dictionary["quest"]["dir"] = test image directory if exist
                answers: list of dictionaries
                    dictionary["answers"][index]["answer"] = correct answer 
                    dictionary["answers"][index]["priority"] = priority of answer
        """

        if (len(cur_list) == 1):
            return
        quest = dict()
        answer = list()

        for i in range(len(cur_list)):
            if cur_list[i].startswith("Вопрос: "):

                quest['question'] = cur_list[i]
                try:

                    for index in range(i, i+6, 1):  # TODO maybe rework
                        if cur_list[index].startswith("Прикрепленный файл:"):
                            quest['dir'] = "Директория вопроса: " + \
                                str(cur_list[index].split()[2])
                            break
                except:
                    pass

            elif cur_list[i].startswith("Ответ:"):

                index = i
                while not cur_list[index].startswith("Приоритет:"):
                    if cur_list[i] != cur_list[index]:
                        cur_list[i] += cur_list[index]
                    index += 1
                answer_priority = cur_list[index].split()[1]

                if int(answer_priority) > 0:
                    right_answer = dict()
                    try:
                        if cur_list[i+2].startswith("Прикрепленный файл:"):
                            right_answer['answer'] = "Директория ответа: " + \
                                str(cur_list[i+2].split()[2])
                        else:
                            right_answer['answer'] = cur_list[i]
                    except:
                        right_answer['answer'] = cur_list[i]

                    right_answer['priority'] = answer_priority
                    answer.append(right_answer)

        cur_list = dict()
        cur_list["question"] = quest
        cur_list["answers"] = answer

        return cur_list

    def __create_list(self):
        """
        read text file , put lines from question to question in
        list , put it in __list_transformer add recived dictionary to list
        and change self.list on recived list  
        """
        file = open(self.directory, encoding="ANSI")
        quest_ask_list = list()
        from_quest_to_next_quest_holder = list()
        cur_quest_ask = dict()

        for num, line in enumerate(file):

            if num == 23:

                self.title = line+'\n'
            if num < 27:

                continue
            line = line.strip()

            if line == '':
                continue

            from_quest_to_next_quest_holder.append(line)

            if line.startswith("[НОВЫЙ ВОПРОС]"):

                cur_quest_ask = TestReader.__list_transformer(
                    from_quest_to_next_quest_holder)

                if cur_quest_ask == None:
                    from_quest_to_next_quest_holder = []

                else:
                    quest_ask_list.append(cur_quest_ask)
                    from_quest_to_next_quest_holder = []

        cur_quest_ask = TestReader.__list_transformer(
            from_quest_to_next_quest_holder)
        quest_ask_list.append(cur_quest_ask)

        self.list = quest_ask_list

    def write(self):
        """Takes information from list, creating directory "answers" 
           in folder and put infromation to new text file

        """
        dir = 'answers/complete_'+self.directory

        try:
            test = open(dir, 'w', encoding='utf-8')

        except:
            os.mkdir("answers")
            test = open(dir, 'w', encoding='utf-8')

        test.write(self.title)

        for i in range(len(self.list)):

            self.list[i] = dict(self.list[i])
            helpstr = str(i+1)+" " + \
                str(self.list[i]['question']['question'])+'\n'
            test.write(helpstr)

            try:

                test.write(str(self.list[i]['question']['dir']+'\n'))

            except:

                pass

            for q in range(len(self.list[i]['answers'])):

                test.write(str(self.list[i]['answers'][q]['answer'] +
                               "   (приоритет " + str(self.list[i]['answers'][q]['priority']) + ')\n'))

            test.write('\n')
