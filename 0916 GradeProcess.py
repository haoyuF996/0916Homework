f = open('AS_CS_opt2_gradebook.txt','r')
temp=[]
for i in f:
    temp.append(i.split())
    #temp.reverse().append(f'{i+1:<2}').reverse()
f.close()
f = open('new-gradebook.txt','w')
PhyScoreList = []
for i,v in enumerate(temp):
    zeros = '0'*(2-len(str(i+1)))
    temp[i].reverse()
    temp[i].append(zeros+str(i+1))
    temp[i].reverse()
    temp[i].append(str(int((int(v[3])+int(v[4])+int(v[5]))/3)))
    if v[2] == 'Daniel':
        temp[i][3] = int(v[3]*1.1)
    PhyScoreList.append(v[-2])
PhyScoreList.sort()
for i in temp:
    if i[-2]>PhyScoreList[0]:
        f.write(' '.join(i)+'\n')
f.close()

