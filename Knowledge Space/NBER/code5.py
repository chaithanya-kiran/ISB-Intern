import pandas as pd 
import numpy as np
import json
'''
df=pd.DataFrame(columns=('a','b','c'))
for i in range(5):
	df.loc[i] = [n for n in range(3)]
print df

print df.loc[0]['b']

df1=pd.DataFrame(columns=('a','b','c'))
df1.append(df.iloc[0])
print df1
'''

data=pd.read_csv('816_target_gvkeys_assgn_525.csv')
#print data
#print data.index.values
#print data.dtypes
#print type(json.loads(data.iloc[3]["pdpassgn_525"])) 
#print len(json.loads(data.iloc[3]["pdpassgn_525"]))

def generate_assignee_count(row):
	var=row["pdpassgn_525"]
	if pd.isnull(var):
		return 0
	ck= json.loads(var)
	return len(ck)

assignee_count=data.apply(generate_assignee_count, axis=1)
#print assignee_count
data['assignee_count']=assignee_count
#print data.head()

df=pd.DataFrame(columns=data.columns)
#print data.loc[0].tolist()
#print pd.Series(data.iloc[0].tolist())
#df.loc[0]=data.loc[0].tolist()
#df.loc[1]=data.loc[1].tolist()
#df=data.loc[np.repeat(df.index.values,df.assignee_count)]

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
df=df.drop('pdpassgn_525',1)
print df
print temp


#print type(data['pdpassgn_525'].tolist())
pdpassgn_525list= data['pdpassgn_525'].tolist()
#print type(pdpassgn_525list[1])


#import itertools
#singlelist=list(itertools.chain.from_iterable(pdpassgn_525list))
#singlelist=[item for sublist in pdpassgn_525list for item in sublist]

notnull=0
import math
singlelist=[]
for ck in pdpassgn_525list:
	if pd.isnull(ck):
		singlelist.append(None)
	else:
		ck = json.loads(ck)
		for pk in ck:
			singlelist.append(pk)	
			notnull=notnull+1

print notnull
print len(singlelist)
df['pdpassgn']=singlelist 
print df

df=df.drop('Unnamed: 0',1)
df.to_csv('816_target_gvkeys_assgn__expand_525.csv')