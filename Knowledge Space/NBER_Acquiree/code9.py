import pandas as pd 
import json

data = pd.read_csv("Acquirer_Assignees.csv")
data76_06 = pd.read_csv("PAT76_06_assg.csv", low_memory=False)

dataassgnlist=data["assignee"].tolist()
data76_06assgnlist=data76_06["pdpass"].tolist()

'''
row_number=0
def generate_patent(row):
	global row_number
	var = row["assignee"]
	if pd.isnull(var):
		return None
	li = json.loads(var)
	pat=[]
	pat_extend=[]
	print "Number: ",
	print row_number
	row_number = row_number + 1
	for assignee in li:
		if assignee in data76_06assgnlist:
			pat.append(data76_06["patent"][data76_06["pdpass"]==assignee].tolist())
	#		pat_extend.extend(data76_06["patent"][data76_06["pdpass"]==assignee])
	#print len(pat_extend)
	return pat

patent = data.apply(generate_patent, axis=1)
print patent

def generate_patent_count(row):
	var=row["assignee"]
	if pd.isnull(var):
		return None
	li = json.loads(var)
	pat_extend=[]
	for assignee in li:
		if assignee in data76_06assgnlist:
			pat_extend.extend(data76_06["patent"][data76_06["pdpass"]==assignee])
	return len(pat_extend)

patent_count = data.apply(generate_patent_count, axis=1)

data["patent_count"]=patent_count
data["patents"]=patent
print data.head()
data.to_csv('Acquirer_Assignees_Patents.csv')
'''

def generate_assignee_count(row):
	var=row["assignee"]
	if pd.isnull(var):
		return 0
	ck= json.loads(var)
	return len(ck)

assignee_count=data.apply(generate_assignee_count, axis=1)
data['assignee_count']=assignee_count
#print data.head()

df=pd.DataFrame(columns=data.columns)

temp=0
for index,row in data.iterrows():
	if (row["assignee_count"]==0):
		df.loc[temp]=row.tolist()
		temp=temp+1
	else:	
		for i in range(row["assignee_count"]):
			df.loc[temp]=row.tolist()
			temp=temp+1
df=df.drop('assignee_count',1)
df=df.drop('assignee',1)
print df
print temp
assignee_list= data['assignee'].tolist()


notnull=0
import math
singlelist=[]
for ck in assignee_list:
	if pd.isnull(ck):
		singlelist.append(None)
	else:
		ck = json.loads(ck)
		for pk in ck:
			singlelist.append(pk)	
			notnull=notnull+1

print notnull
print len(singlelist)
df['assignee']=singlelist 
print df

df=df.drop('Unnamed: 0',1)
df.to_csv('Acquirer_Assignees_Expand.csv')