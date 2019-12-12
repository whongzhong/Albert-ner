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
for lines in ids:
	aspflag = False
	asp = ''
	for item in lines:
		if(aspflag):
			if item[0] == 'ASP':
				ans.append((i, asp, '_'))
				#o.write(str(i)+','+ asp + ',' + '_\n')
				asp = item[1]
			else:
				ans.append((i, asp, item[1]))
				#o.write(str(i)+','+ asp + ',' + item[1] +'\n')
				aspflag = False
		else:
			if item[0] == 'ASP':
				asp = item[1]
				aspflag = True
			else:
				ans.append((i, '_', item[1]))
				#o.write(str(i)+','+ '_' + ',' + item[1] +'\n')
	if(aspflag):
		#o.write(str(i)+','+ asp + ',' + '_\n')
		ans.append((i, asp, '_'))
	i+=1
with open('task1_answer.csv', 'w', encoding='utf-8', newline='') as f:  
    writer = csv.writer(f)  
    for row in ans:  
        writer.writerow(row)  
#out=pd.DataFrame(data=ans)
#out.to_csv('task1_answer.csv', encoding='utf-8', index=False, header=False)