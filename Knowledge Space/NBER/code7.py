import pandas as pd
import json

data=pd.read_csv('816_assign_patent_expand.csv')
df=pd.DataFrame(columns=data.columns)


temp=0
for index,row in data.iterrows():
	#print type(row["patents"])
	var=row["patents"]
	if pd.isnull(var):
		#print None
		df.loc[temp]=row.tolist()
		temp=temp+1
	else:
		var=json.loads(var)
		#print type(var)
		for i in range(len(var)):
			df.loc[temp]=row.tolist()
			temp=temp+1

#print df.head(20)
df=df.drop('patents',1)
patent_list=data['patents'].tolist()
#print patent_list
print len(patent_list)


import math
notnull=0
singlelist=[]
for ck in patent_list:
	if pd.isnull(ck):
		singlelist.append(None)
	else:
		ck = json.loads(ck)
		for pk in ck:
			singlelist.append(pk)	
			notnull=notnull+1

print notnull
print len(singlelist)

df['patents']=singlelist

#df['patents'][patent_null_false]='0'+df['patents'].astype(str)

df.drop('Unnamed: 0',1)
df.drop('Unnamed: 0.1',1)

print df.head(20)
df.to_csv("816_assign_patent_expand_final.csv")	