#trying to optimise code2.py in the double for loop instead of searching entire data(appended by dataframes) again create required 
#dataframe of particular key1 and search in that one.

import time
start_time = time.time()


#trying to optimize
import pandas as pd
import sys 
data=pd.read_csv('tnic_all years_data.csv')
data816=pd.read_csv('816_target_gvkeys.csv')

dealyear=1999


df1=data[data["gvkey_1"]==2598]
df2=data[data["gvkey_2"]==2598]
collist=list(df2)
collist[1],collist[2]=collist[2],collist[1]
df2.columns=collist
df=df1.append(df2,ignore_index=True)
df.drop_duplicates()

uniquelist=[2598]
uniquelist.extend(df['gvkey_2'].tolist())
uniquelist=list(set(uniquelist))
uniqlength=len(uniquelist)
print "uniquelist length : ",
print uniqlength
uniquelist.sort()
print uniquelist


#joining multiple dataframes
for item in uniquelist:
#	print item
	df1=data[data["gvkey_1"]==item]
	df2=data[data["gvkey_2"]==item]
	collist=list(df2)
	collist[1],collist[2]=collist[2],collist[1]
	df2.columns=collist
	df=df.append(df1,ignore_index=True)
	df=df.append(df2,ignore_index=True)
#	df.drop_duplicates()

df.drop_duplicates()
print df.shape

temp=1
fnlsum=0
for key1 in uniquelist[0:]:	
	print key1

	data=df[df["gvkey_1"]==key1]

	for key2 in uniquelist[temp:]:
		avg_count=3
		val1=data["score"][data["gvkey_2"]==key2][data["eyear"]==dealyear-1].tolist()
		if not val1:
			val1=0
			avg_count=avg_count-1
		else:
			val1=val1[0]

		val2=data["score"][data["gvkey_2"]==key2][data["eyear"]==dealyear-2].tolist()
		if not val2:
			val2=0
			avg_count=avg_count-1
		else:
			val2=val2[0]

		val3=data["score"][data["gvkey_2"]==key2][data["eyear"]==dealyear-3].tolist()
		if not val3:
			val3=0
			avg_count=avg_count-1
		else:
			val3=val3[0]
		

		val=(val1+val2+val3)/avg_count if avg_count>0 else 0
		fnlsum=fnlsum+val

	temp=temp+1

print fnlsum
density=(fnlsum*2)/(uniqlength*uniqlength-1)
print density


print(" %s seconds" % (time.time()-start_time))
