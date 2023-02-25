class Question():
    def __init__(self,soru,suklar,cevap):
        self.soru=soru
        self.suklar=suklar
        self.cevap=cevap

    def cevapKontrol(self,cevap):
        return self.cevap==cevap

class Quiz():
    def __init__(self,sorular):
        self.sorular=sorular
        self.score=0
        self.soruindex=0

    def soruyuyazdir(self):
        return self.sorular[self.soruindex]

    def soruyugoster(self):
        question=self.soruyuyazdir()
        print(f'Soru {self.soruindex+1}: {question.soru}')

        for q in question.suklar:
            print('-'+q)
        cevap=input('Cevap: ')
        self.tahmin(cevap)
        self.indexkontrol()

    def tahmin(self,cevap):
        question=self.soruyuyazdir()

        if question.cevapKontrol(cevap):
            self.score+=1
        self.soruindex+=1

    def indexkontrol(self):
        if len(self.sorular)==self.soruindex:
            self.skor()
        else:
            self.soruilerlemesi()
            self.soruyugoster()

    def skor(self):
        print('Skor: ',self.score)
        
    def soruilerlemesi(self):
        toplamsoru=len(self.sorular)
        sorusayisi=self.soruindex+1

        if sorusayisi>toplamsoru:
            print('Quiz Bitti.')

        else:
            print(f'{toplamsoru} sorudan {sorusayisi}. sorudasiniz.')

q1=Question('En iyi programlama dili hangisidir?',['C#','python','javascript','java'],'python')
q2=Question('En populer programlama dili hangisidir?',['C#','python','javascript','java'],'python')
q3=Question('En cok kullanilan programlama dili hangisidir?',['C#','python','javascript','java'],'python')

sorular=[q1,q2,q3]

quiz=Quiz(sorular)
quiz.indexkontrol()