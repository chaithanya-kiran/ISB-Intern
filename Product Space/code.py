import pandas as pd
import sys 
data=pd.read_csv('tnic_all years_data.csv')
data816=pd.read_csv('816_target_gvkeys.csv')

print data.shape

data816gvkeylist=data816["gvkey"].tolist()

'''
df1=data[data["gvkey_1"]==2598]
df2=data[data["gvkey_2"]==2598]
collist=list(df2)
collist[1],collist[2]=collist[2],collist[1]
df2.columns=collist
df=df1.append(df2,ignore_index=True)
#print df
df.drop_duplicates()
df.to_csv('check.csv')
'''
'''
uniquelist=['2598']
uniquelist.extend(df['gvkey_2'].tolist())
uniquelist=list(set(uniquelist))
print len(uniquelist)
'''



dealyear=1999

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

temp=1
fnlsum=0
count=0
for key1 in uniquelist[0:]:	
	print key1,
	print count
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
		print val1,
		print val2,
		print val3,
		print val
		key1list.append(val)
	temp=temp+1
#	print key1list
#	print len(key1list)
	fnlsum=fnlsum+sum(key1list)
	print "key1rowsum: "
	print fnlsum	
print fnlsum
density=(fnlsum*2)/(uniqlength*uniqlength-1)
print density






'''
fnlsum=0
for key1 in uniquelist:
	print key1
	key1list=[]
	for key2 in uniquelist:
#		print "key2",
#		print key2
		avg_count=0
		val1=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-1]
		if not val1.tolist():
			val1=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]
#		print val1.tolist()
		val2=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-2]
		if not val2.tolist():
			val2=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]		
#		print val2.tolist()
		val3=data["score"][data["gvkey_1"]==key1][data["gvkey_2"]==key2][data["eyear"]==dealyear-3]		
		if not val3.tolist():
			val3=data["score"][data["gvkey_1"]==key2][data["gvkey_2"]==key1][data["eyear"]==dealyear-1]
#		print val3.tolist()

		if not val1.tolist():			
			val1=0
			avg_count=avg_count-1
		if not val2.tolist():
			val2=0
			avg_count=avg_count-1
		if not val3.tolist():
			val3=0
			avg_count=avg_count-1
		val=(val1+val2+val3)/avg_count
#		print "avg",
#		print val
		key1list.append(val)
	print key1list
	print len(key1list)
	fnlsum=fnlsum+sum(key1list)
	print fnlsum
	uniquelist.remove(key1)
	print len(uniquelist)
'''