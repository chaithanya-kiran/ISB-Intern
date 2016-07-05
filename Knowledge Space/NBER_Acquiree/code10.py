import pandas as pd
import json

data = pd.read_csv("Connected_gvkeys_Assignees_Expand.csv")

data76_06 = pd.read_csv("PAT76_06_assg.csv", low_memory=False)
data76_06assgnlist=data76_06["pdpass"].tolist()

row_number = 1
def generate_patent(row):
	global row_number
	assignee = row["assignee"]
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
	if not pat_extend:
		return None
	else:
		return pat_extend
	
	#print len(pat_extend)
	#return pat_extend

patent = data.apply(generate_patent, axis=1)
print patent

def generate_patent_count(row):
	assignee=row["assignee"]
	if pd.isnull(assignee):
		return None
	pat_extend=[]
	if assignee in data76_06assgnlist:
		pat_extend.extend(data76_06["patent"][data76_06["pdpass"]==assignee])
	return len(pat_extend)

patent_count = data.apply(generate_patent_count, axis=1)

data["patent_count"]=patent_count
data['patents']=patent

data.to_csv('Connected_gvkeys_Assignees_Patent_Expand.csv')