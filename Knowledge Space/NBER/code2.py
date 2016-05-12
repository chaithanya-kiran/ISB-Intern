import pandas as pd
data = pd.read_csv("DYNASS.csv")

#print data.shape
#print data.head()
#print data.columns.tolist()

gvkey1 = data["gvkey1"].tolist()
gvkey2 = data["gvkey2"].tolist()
gvkey3 = data["gvkey3"].tolist()
gvkey4 = data["gvkey4"].tolist()
gvkey5 = data["gvkey5"].tolist()

pdpass=data["pdpass"].tolist()

df = pd.DataFrame(pdpass,columns=['pdpassgn'])
df["gvkey1"] = gvkey1
df["gvkey2"] = gvkey2
df["gvkey3"] = gvkey3
df["gvkey4"] = gvkey4
df["gvkey5"] = gvkey5

#print df.head()


#comparing with data816
#comparing not only with final gvkey checking dor all from gvkey5-gvkey1
data816 = pd.read_csv("816_target_gvkeys.csv")
data816gvkey = data816["gvkey"].tolist()


def generate_816_assignee(row):
	if row["gvkey"] in gvkey5:
		return data["pdpass"][data["gvkey5"]==row["gvkey"]]
	elif row["gvkey"] in gvkey4:
		return data["pdpass"][data["gvkey4"]==row["gvkey"]]
	elif row["gvkey"] in gvkey3:
		return data["pdpass"][data["gvkey3"]==row["gvkey"]]
	elif row["gvkey"] in gvkey2:
		return data["pdpass"][data["gvkey2"]==row["gvkey"]]
	elif row["gvkey"] in gvkey1:
		return data["pdpass"][data["gvkey1"]==row["gvkey"]]

final = data816.apply(generate_816_assignee, axis =1)
print final	

#final assignee considering all gvkeys
data816["final_pdpassgn_allgvkey"]=final
#print data816.head()

final_null=pd.isnull(data816["final_pdpassgn_allgvkey"])
#print final_null
final_null_false=final_null[final_null==False]
print len(final_null_false)

#data816.to_csv('816_target_gvkeys_assgn_525.csv')

#print final.loc[1]
#print final[3].tolist()[0]
#print final[3][0]


#This function is for removing duplicate assignee values
final1=[]
for ck in final:
	if not (ck is None):
		final1.append(list(set(ck.tolist()))) #for removing duplicates
	else:
		final1.append(None)
#print final1.head()

print len(final)
print len(final1)

#data816["pdpassgn_rm_dup"]=final1

data816=data816.drop('final_pdpassgn_allgvkey',1)
data816["pdpassgn_525"]=final1

#def generate_single(row):
#	assigngvkeylist=row["final_assgn_allgvkey"].tolist()
#	return list(set(assigngvkeylist))

#singlegvkey=data816.apply(generate_single, axis=1)
#print singlegvkey

#print data816
data816.to_csv('816_target_gvkeys_assgn_525.csv')

#generated 525 pdpassgn out of 816 targetted using gvkeys(1-5)