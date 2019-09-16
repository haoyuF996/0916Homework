names = [
        ['Daniel','Chu',0,0,0],
        ['Julian','Ye',0,0,0],
        ['Lisa','Xu',0,0,0],
        ['Shirley','Zeng',0,0,0],
        ['Nico','Jiang',0,0,0],
        ['Tim','Xing',0,0,0],
        ['James','Liu',0,0,0],
        ['Andy','Zhang',0,0,0],
        ['Cathy','Yang',0,0,0],
        ['Brian','Dan',0,0,0],
        ['Harry','Fang',0,0,0],
        ['Jack','Jin',0,0,0]]
import random
def RandomGradeA(NumberOfGrades,Average):
    Grade = [random.randint(0,60) for i in range(NumberOfGrades)]
    while sum(Grade)/len(Grade) < Average:
        rand = random.randint(0,len(Grade)-1)
        if Grade[rand]<100:
            Grade[rand]+=1
    return Grade
AverageDict = {'1':90,'2':95,'3':88}
for k in range(3):
    Grades =  RandomGradeA(12,AverageDict[f'{k+1}'])
    for i,v in enumerate(Grades):
        names[i][k+2] = v
for i in range(3):
    names[-2][i+2] = random.randint(97,100)
f = open("AS_CS_opt2_gradebook.txt",'w')
for k,g in enumerate(names):
    for i,v in enumerate(g):
        names[k][i]=str(v)
for i in names:
    f.write(' '.join(i)+'\n')
f.close()