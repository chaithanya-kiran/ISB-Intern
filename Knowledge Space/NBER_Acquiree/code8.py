import pandas as pd
data = pd.read_csv("DYNASS.csv")

gvkey1 = data["gvkey1"].tolist()
gvkey2 = data["gvkey2"].tolist()
gvkey3 = data["gvkey3"].tolist()
gvkey4 = data["gvkey4"].tolist()
gvkey5 = data["gvkey5"].tolist()

dataacq=pd.read_csv('Acquirer companies.csv')
dataacqgvkey=dataacq["gvkey_a"]
#print dataacqgvkey

final=[]
row_number=0
for index,row in dataacq.iterrows():
#	print row_number
	row_number=row_number+1
	if row["gvkey_a"] in gvkey5:
		final.append(data["pdpass"][data["gvkey5"]==row["gvkey_a"]].tolist())
	elif row["gvkey_a"] in gvkey4:
		final.append(data["pdpass"][data["gvkey4"]==row["gvkey_a"]].tolist())
	elif row["gvkey_a"] in gvkey3:
		final.append(data["pdpass"][data["gvkey3"]==row["gvkey_a"]].tolist())
	elif row["gvkey_a"] in gvkey2:
		final.append(data["pdpass"][data["gvkey2"]==row["gvkey_a"]].tolist())
	elif row["gvkey_a"] in gvkey1:
		final.append(data["pdpass"][data["gvkey1"]==row["gvkey_a"]].tolist())
	else:
		final.append(None)

print final
#print len(final)
#print type(final)
#print final[0]

dataacq["assignee"]=final

final_null=pd.isnull(dataacq["assignee"])
final_null_false=final_null[final_null==False]
print len(final_null_false)

dataacq.to_csv('Acquirer_Assignees.csv')