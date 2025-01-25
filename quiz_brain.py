class Quiz():
    
    def __init__(self,list1):
        self.question=0
        self.list1=list1
        self.score=0
        self.question_list1=[]
        self.answer_list1=[]
        self.true_false_list1=[]
        self.sr_list1=[]
        self.real_ans_list1=[]
        
    def next_question(self):
        return self.question<len(self.list1)
    
    def print1(self):
        self.curr=self.list1[self.question]
        self.question += 1
        self.answer=input(f"Q.{self.question} : {self.curr.question}: (T/F) : ")
        self.question_list1.append(self.curr.question)
        self.answer_list1.append(self.answer)
        self.sr_list1.append(self.question)
        self.real_ans_list1.append(self.curr.answer)
        
    def check_answer(self):
        if self.answer.lower() == self.curr.answer.lower():
            self.score += 1
            print("Correct Answer!!! Hurray!!!")
            self.true_false_list1.append("✔️")
        else:
            print("Wrong Answer Better luck Next time")
            self.true_false_list1.append("❌")
        print(f"Your current score is print {self.score}/{self.question}")
        print()
        
