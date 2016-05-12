import pandas as pd
import json

data = pd.read_csv("816_target_gvkeys_assgn__expand_525.csv")
data1 = pd.read_csv("816_assgn_patent.csv", low_memory=False)


data76_06 = pd.read_csv("PAT76_06_assg.csv", low_memory=False)
data76_06assgnlist=data76_06["pdpass"].tolist()

'''
notnull=0
singleassignee_patcount=[] 
for index,row in data1.iterrows():
	var=row["patents"]
	#print type(var)
	if pd.isnull(var):
		singleassignee_patcount.append(None)
	else:
		var=json.loads(var)
		for ck in var:
			singleassignee_patcount.append(len(ck))
			notnull=notnull+1
#print singleassignee_patcount
print notnull
print len(singleassignee_patcount)

print data.shape

#data["patent_count"]=singleassignee_patcount

cnt=0
notnull2=0
for index,row in data1.iterrows():
	var=row["pdpassgn_525"]
	if pd.isnull(var):
		cnt=cnt+1
	else:
		var=json.loads(var)
		cnt=cnt+len(var)
		notnull2=notnull2+len(var)
print notnull2
print cnt


data1pdp525list=data1["pdpassgn_525"].tolist()
notnull1=0
singlelist=[]
for ck in data1pdp525list:
	if pd.isnull(ck):
		singlelist.append(None)
	else:
		ck = json.loads(ck)
		for pk in ck:
			singlelist.append(pk)	
			notnull1=notnull1+1

print notnull1
print len(singlelist)

'''
row_number = 1
def generate_patent(row):
	global row_number
	assignee = row["pdpassgn"]
	if pd.isnull(assignee):
		return None
	pat=[]
	pat_extend=[]
	print "Number: ",
	print row_number
	row_number = row_number + 1
	if assignee in data76_06assgnlist:
	#	pat.append(data76_06["patent"][data76_06["pdpass"]==assignee].tolist())
		pat_extend.extend(data76_06["patent"][data76_06["pdpass"]==assignee])
	#print len(pat_extend)
	return pat_extend

patent = data.apply(generate_patent, axis=1)
print patent
data['patents']=patent
data.to_csv('816_assign_patent_expand.csv')