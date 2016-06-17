import time
start_time_total=time.time()
import pandas as pd
import sys 
data=pd.read_csv('tnic_all years_data.csv')
data525=pd.read_csv('Acquirer companies.csv')

dataorig=data

data525gvkeylist=data525["gvkey"].tolist()

uniqlength525=[]
density525=[]
finalsum525=[]

count525=1
for gvkeys in data525gvkeylist:

	start_time = time.time()

	data=dataorig
	print "\n\ncompany",
	print count525,
	count525=count525+1

	print gvkeys,			

	dealyear=data525["deal year"][data525["gvkey"]==gvkeys].tolist()[0]
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
	print "uniqlength : ",
	print uniqlength
	uniqlength525.append(uniqlength)
	uniquelist.sort()
#	print uniquelist


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

	temp=1
	fnlsum=0
	count=0
	print "processing upper triangle ..."
	for key1 in uniquelist[0:]:	

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

	print fnlsum,
	if uniqlength==1:
		density=1
	else:
		density=(fnlsum*2)/(uniqlength*uniqlength-1) 

	uniqlength525.append(uniqlength)
	finalsum525.append(fnlsum)
	density525.append(density)
	print("%s seconds for this company\n" % (time.time()-start_time))


data525["uniqlength525"]=uniqlength525
data525["finalsum525"]=finalsum525
data525["density525"]=density525

data525.to_csv("525_target_gvkeys_density.csv")
print(" %s seconds" % (time.time()-start_time_total))

#uniqlength ave 397