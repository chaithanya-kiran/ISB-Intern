import pandas as pd
data = pd.read_csv("DYNASS.csv")

gvkey1 = data["gvkey1"].tolist()
gvkey2 = data["gvkey2"].tolist()
gvkey3 = data["gvkey3"].tolist()
gvkey4 = data["gvkey4"].tolist()
gvkey5 = data["gvkey5"].tolist()

dataacq=pd.read_csv('connected_gvkeys.csv')
dataacqgvkey=dataacq["Unique gvkeys"]
#print dataacqgvkey

final=[]
row_number=0
for index,row in dataacq.iterrows():
#	print row_number
	temp=[]
	row_number=row_number+1
	if row["Unique gvkeys"] in gvkey5:
		temp.extend(data["pdpass"][data["gvkey5"]==row["Unique gvkeys"]].tolist())
	if row["Unique gvkeys"] in gvkey4:
		temp.extend(data["pdpass"][data["gvkey4"]==row["Unique gvkeys"]].tolist())	
	if row["Unique gvkeys"] in gvkey3:
		temp.extend(data["pdpass"][data["gvkey3"]==row["Unique gvkeys"]].tolist())
	if row["Unique gvkeys"] in gvkey2:
		temp.extend(data["pdpass"][data["gvkey2"]==row["Unique gvkeys"]].tolist())
	if row["Unique gvkeys"] in gvkey1:
		temp.extend(data["pdpass"][data["gvkey1"]==row["Unique gvkeys"]].tolist())
	if not temp:
		final.append(None)
	else:
		final.append(temp)
print final
#print len(final)
#print type(final)
#print final[0]

dataacq["assignee"]=final

final_null=pd.isnull(dataacq["assignee"])
final_null_false=final_null[final_null==False]
print len(final_null_false)

dataacq.to_csv('Connected_gvkeys_Assignees.csv')