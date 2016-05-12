import pandas as pd
data816 = pd.read_csv("816_target_gvkeys.csv")
dataneg = pd.read_csv("negDYNASS.csv")

dataneggvkey = dataneg["final_gvkey_val"].tolist()
#print dataneggvkey
data816gvkey = data816["gvkey"].tolist()
#print data816gvkey

count=0
for key in dataneggvkey:
	if key in data816gvkey:
		count=count+1
		print key
		print data816["Target name"][data816["gvkey"]==key]

print count


datafnlassn = pd.read_csv("fnlDYNASS.csv")
datafnlassnlist = datafnlassn["gvkey_final"].tolist()


def generate_816_assgn(row):
	if row["gvkey"] in datafnlassnlist:
		return datafnlassn["assgn_final"][datafnlassn["gvkey_final"]==row["gvkey"]]

final=data816.apply(generate_816_assgn, axis=1)
#print final

data816["final_assgn"]=final
print data816

data816.to_csv('816_target_gvkeys_assgn_270.csv')

final_assgn_null=pd.isnull(data816["final_assgn"])
#print final_assgn_null
final_assgn_null_False=final_assgn_null[final_assgn_null == False]
print len(final_assgn_null_False)