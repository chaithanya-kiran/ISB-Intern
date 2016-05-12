import pandas as pd
import json

data=pd.read_csv('Acquirer_Assignees_Patent_Expand.csv')
df=pd.DataFrame(columns=data.columns)

print data.shape
'''
temp=0
row_count=0
pat_count=[]
for index,row in data.iterrows():
	print row_count
	row_count=row_count+1
	#print temp
	#print type(row["patents"])
	var=row["patents"]
	if pd.isnull(var):
		#print None
		pat_count.append(None)
		df.loc[temp]=row.tolist()
		temp=temp+1
	else:
		#var=json.loads(var)
		#print type(var)
		pat_count.append(len(var))
		for i in range(len(var)):
			df.loc[temp]=row.tolist()
			temp=temp+1
'''

data["patent_count"].fillna(0, inplace=True)
row_count=0
temp=0
#print data["patent_count"]
for index,row in data.iterrows():
	#print row_count
	row_count=row_count+1	
	var=int(row["patent_count"])
#	print type(int(var))
	if var==0:
		df.loc[temp]=row.tolist()
		temp=temp+1
	else:
		for i in range(var):
			df.loc[temp]=row.tolist()
			temp=temp+1

			
#print pat_count
#print len(pat_count)

print df.shape
df=df.drop('patents',1)

patent_list=data['patents'].tolist()
print len(patent_list)


import math
notnull=0
singlelist=[]
temp=0
for ck in patent_list:
	
	#print temp
	#temp=temp+1
	if pd.isnull(ck):
		singlelist.append(None)
	else:
		ck = json.loads(ck)
		for pk in ck:
			singlelist.append(pk)	
			notnull=notnull+1

print singlelist
print notnull
print len(singlelist)

df['patents']=singlelist

df.drop('Unnamed: 0',1)
df.drop('patent_count',1)

print df.shape
print df.head(20)
df.to_csv("Acquirer_Assignees_Patent_Expand_Final.csv")	