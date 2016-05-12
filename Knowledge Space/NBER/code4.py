#map pdpassgn to pat76-06 file

import pandas as pd
import math
import json

data = pd.read_csv("816_target_gvkeys_assgn_525.csv")
data76_06 = pd.read_csv("PAT76_06_assg.csv", low_memory=False)

#print data.head()
#print data76_06.head()

data816assgnlist=data["pdpassgn_525"].tolist()
#print data816assgnlist
#print len(data816assgnlist)
data76_06assgnlist=data76_06["pdpass"].tolist()
#print data76_06assgnlist 
print len(data76_06assgnlist)

#print data76_06["pdpass"]



#data76_06assgnlist.sort()
#print data76_06assgnlist[0:10]

'''

temp = json.loads(data816assgnlist[1])
print temp
if temp[0] in data76_06assgnlist:
	print "Yes"
else:
	print "Not Found"
'''

#patent=[]
#for asgnlist in data816assgnlist:
#	if (math.isnan(asgnlist)):
#		patent.append(None)
#	else:
#		for key in asgnlist:
#			if key in data76_06assgnlist:
#				patent.append(data76_06assgnlist["patent"][data76_06assgnlist["patent"]==key])
#print patent
#print len(patent)
row_number = 1
def generate_patent(row):
	global row_number
	var = row["pdpassgn_525"]
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

'''for l in data816assgnlist:
	if not pd.isnull(l):
		print "Entered"
		print generate_patent(l)
	else:
		pass 
'''

patent = data.apply(generate_patent, axis=1)
#print patent 

def generate_patent_count(row):
	var=row["pdpassgn_525"]
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
data.to_csv('816_assgn_patent.csv')