import pandas as pd
data = pd.read_csv("DYNASS.csv")

#print data.shape
#print data.head()
#print data.columns.tolist()


#print data.head().isnull()


#print data['gvkey1'].iloc[1]
#print data['gvkey1'].iloc[0]


#for ck in data.columns.tolist():
	#print ck
	#print data[ck]
#	print data[ck].iloc[0]
	#if (data[ck].iloc[0].isnull().values.any()):
	#	print ("yes")



#print data['gvkey5']
#gvkey5_null=pd.isnull(data["gvkey5"])
#print gvkey5_null
#print "ck"
#print gvkey5_null.iloc[162]
#print data['gvkey5'].iloc[162]
#gvkey5_null_false=gvkey5_null[gvkey5_null == False]
#print gvkey5_null_false
#print len(gvkey5_null_false)

#print "pk"
#print gvkey5_null_false

#generating final gvkey(last present one)

def generate_finalkey(row):
	if (pd.isnull(row['gvkey5']) == False):
		return row['gvkey5']
	elif (pd.isnull(row["gvkey4"]) == False):
		return row["gvkey4"]
	elif (pd.isnull(row["gvkey3"]) == False):
		return row["gvkey3"]
	elif (pd.isnull(row["gvkey2"]) == False):
		return row["gvkey2"]
	else:
		return row["gvkey1"]

final=data.apply(generate_finalkey, axis=1) #applying on each row to get final key
#print final
#print final.dtypes
#print final.shape

data["final_gvkey_val"]=final  #adding inal gvkey column to data
#print data.shape
#print data.head()
#print data.columns.tolist()

#print data["pdpass"]
#print len(data["pdpass"])


#sorting based on pdpass and taking only negative pdpass
pdpass_sort=data.sort(["pdpass"])
#print pdpass_sort["pdpass"].head(60)

negative_assgn=pdpass_sort["pdpass"][0:58]
#print negative_assgn

neg_ass_gvkey=[]
neg_ass_gvkey=negative_assgn.tolist()	#converting column to list


#corresponding gvkeys for negative assg
final_neg_gvkey=[]
final_neg_gvkey=pdpass_sort["final_gvkey_val"][0:58].tolist()
print neg_ass_gvkey
print final_neg_gvkey


#creating a dataframe and writing to a file
df=pd.DataFrame(neg_ass_gvkey,columns=['neg_pdpass'])
df["final_gvkey_val"]=final
print df

#writer=pd.ExcelWriter('negDYNASS.xlsx',engine='xlsxwriter') # Create a Pandas Excel writer using XlsxWriter as the engine.
#df.to_excel(writer,'Sheet1',merge_cells=False) # Convert the dataframe to an XlsxWriter Excel object.
#writer.save() # Close the Pandas Excel writer and output the Excel file. 

df.to_csv('negDYNASS.csv')



#taking only assgn columns and their corresponding final gvkeys into df1 and creating file
final_pdpass=[]
final_pdpass=pdpass_sort["pdpass"].tolist()
#print final_pdpass
print len(final_pdpass)

final_gvkey=[]
final_gvkey=pdpass_sort["final_gvkey_val"].tolist()
#print final_gvkey
print len(final_gvkey)

df1=pd.DataFrame(final_pdpass,columns=['assgn_final'])
df1["gvkey_final"]=final_gvkey
print df1

df1.to_csv('fnlDYNASS.csv')