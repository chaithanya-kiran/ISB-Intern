#optimized version
#Instead of checking for every element of upper triangular 2-d matrix in the entire data, created a dataframe with data of all 
#	elements of uniquelist -> iterating the for loop over this dataframe.

import pandas as pd
import sys 
data=pd.read_csv('tnic_all years_data.csv')
data816=pd.read_csv('816_target_gvkeys.csv')

dataorig=data

print data.shape

data816gvkeylist=data816["gvkey"].tolist()

uniqlength816=[]
density816=[]
finalsum816=[]

count816=1
for gvkeys in data816gvkeylist:

	data=dataorig
	print "\n\ncompany",
	print count816
	count816=count816+1

	print gvkeys

	dealyear=data816["deal year"][data816["gvkey"]==gvkeys].tolist()[0]
#	print dealyear

	df1=data[data["gvkey_1"]==gvkeys]
	df2=data[data["gvkey_2"]==gvkeys]
	collist=list(df2)
	collist[1],collist[2]=collist[2],collist[1]
	df2.columns=collist
	df=df1.append(df2,ignore_index=True)
	df.drop_duplicates()
	uniquelist=[gvkeys]
	uniquelist.extend(df['gvkey_2'].tolist())
	uniquelist=list(set(uniquelist))
	uniqlength=len(uniquelist)
	print uniqlength
	uniquelist.sort()
	print uniquelist


	for item in uniquelist:
#		print item
		df1=data[data["gvkey_1"]==item]
		df2=data[data["gvkey_2"]==item]
		collist=list(df2)
		collist[1],collist[2]=collist[2],collist[1]
		df2.columns=collist
		df=df.append(df1,ignore_index=True)
		df=df.append(df2,ignore_index=True)
	#	df.drop_duplicates()

	df.drop_duplicates()

	data=df
	print data.shape

	temp=1
	fnlsum=0
	count=0
	for key1 in uniquelist[0:]:	
#		print key1,
#		print count
		count=count+1
		key1list=[]
	#	print uniquelist
		for key2 in uniquelist[temp:]:
			avg_count=3
			val1=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-1]
			if not val1.tolist():
				val1=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]
			val1=val1.tolist()
			if not val1:
				val1=0
				avg_count=avg_count-1
			else:
				val1=val1[0]
		
			val2=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-2]
			if not val2.tolist():
				val2=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]		
			val2=val2.tolist()
			if not val2:
				val2=0
				avg_count=avg_count-1
			else:
				val2=val2[0]

			val3=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-3]		
			if not val3.tolist():
					val3=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]
			val3=val3.tolist()
			if not val3:
				val3=0
				avg_count=avg_count-1
			else:
				val3=val3[0]
			

			val=(val1+val2+val3)/avg_count if avg_count>0 else 0
			print key2,
			print val
			key1list.append(val)
		temp=temp+1
	#	print key1list
	#	print len(key1list)
		fnlsum=fnlsum+sum(key1list)
	#	print "key1rowsum: "
		print fnlsum	
	print fnlsum,
	density=(fnlsum*2)/(uniqlength*uniqlength-1)
	print density

	finalsum816.append(fnlsum)
	density816.append(density)


data816["uniqlength816"]=uniqlength816
data816["finalsum816"]=finalsum816
data816["density816"]=density816

data816.to_csv("816_target_gvkeys_density.csv")






'''


uniquelist=[2598]
list1=data["gvkey_2"][data["gvkey_1"]==2598].tolist()
list2=data["gvkey_1"][data["gvkey_2"]==2598].tolist()
uniquelist.extend(list1)
uniquelist.extend(list2)
uniquelist=list(set(uniquelist))
uniqlength=len(uniquelist)
print uniqlength
uniquelist.sort()
print uniquelist

'''

'''

Product Space :
---------------
TNIC -> Universal Data which contains the density between any two companies for all companies.
Assuming a company as node which is connected to other nodes(other companies) which are again interlinked in the network.
Now the overall density_index(proximity val) of a particular company has been calculated by taking the ratio of upper triangle in this    2-d matrix(n*n matrix denpting densities between companies) to the overall possible.


Now we are finding how the same varies in the knowledge space assuming a company looks at the other companies past 3 years 
data(here we are assuming it to be the patent data, how they are related) before merging or acquiring other 

'''