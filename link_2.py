import pandas as pd
import csv
def get_string(self, x):
        now = x.split('\n')
        o = now[1].split(' ')
        while '' in o:
            o.remove('')
        return o[1]
ids = [[] for i in range(2235)]
tests = pd.read_csv('output.txt')
name = ['id', 'asp', 'opi']
with open('output.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        idd, asp, opi = line.split(',')
        ids[int(idd)-1].append((asp, opi.strip('\n')))
i = 1
ans = []
ans1 = []
ans2 = []
aspDict = {'PAC':'包装', 'COM':'成分', 'SIZ':'尺寸', 'SER':'服务', 'EFF':'功效', 'PRI':'价格', 'SME':'气味', 'EXP':'使用体验', 'TRA':'物流', 'FRE':'新鲜度', 'TOF':'真伪', 'TOT':'整体', 'EXT':'其他', '_':'整体'}
opiDict = {'POS':'正面', 'NEU':'中性', 'NEG':'负面', '_':'中性'}
for lines in ids:
    aspflag = False
    asp_tag = ''
    asp = ''
    for item in lines:
        tag_1, tag_2 = item[0].split('-')
        if(aspflag):
            if tag_1 == 'A':
                ans.append((i, asp, '_'))
                ans1.append((i, asp, '_', aspDict[asp_tag]))
                ans2.append((i, asp, '_', aspDict[asp_tag], opiDict['_']))
                #o.write(str(i)+','+ asp + ',' + '_\n')
                asp = item[1]
                asp_tag = tag_2
            else:
                ans.append((i, asp, item[1]))
                ans1.append((i, asp, item[1], aspDict[asp_tag]))
                ans2.append((i, asp, item[1], aspDict[asp_tag], opiDict[tag_2]))
                #o.write(str(i)+','+ asp + ',' + item[1] +'\n')
                aspflag = False
        else:
            if tag_1 == 'A':
                asp = item[1]
                asp_tag = tag_2
                aspflag = True
            else:
                ans.append((i, '_', item[1]))
                ans1.append((i, '_', item[1], aspDict['_']))
                ans2.append((i, '_', item[1], aspDict['_'], opiDict[tag_2]))
                #o.write(str(i)+','+ '_' + ',' + item[1] +'\n')
    if(aspflag):
        #o.write(str(i)+','+ asp + ',' + '_\n')
        ans.append((i, asp, '_'))
        ans1.append((i, asp, '_', aspDict[tag_2]))
        ans2.append((i, asp, '_', aspDict[tag_2], opiDict['_']))
    i+=1
with open('task1_answer.csv', 'w', encoding='utf-8', newline='') as f:  
    writer = csv.writer(f)  
    for row in ans:  
        writer.writerow(row)  
#out=pd.DataFrame(data=ans)
#out.to_csv('task1_answer.csv', encoding='utf-8', index=False, header=False)