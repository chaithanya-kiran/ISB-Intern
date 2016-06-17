import time
start_time_total=time.time()
import pandas as pd
import sys 
data=pd.read_csv('tnic_all years_data.csv')
data816=pd.read_csv('816_target_gvkeys.csv')
data816=data816[0:5]

dataorig=data

data816gvkeylist=data816["gvkey"].tolist()

uniqlength816=[]
density816=[]
finalsum816=[]

count816=1
for gvkeys in data816gvkeylist:
	start_time = time.time()

	with open('Target Density Files/{}_ps.txt'.format(gvkeys), 'w') as output:
#		output.write("%d %s\n\n"%(data816.loc[count816-1]["gvkey"],data816.loc[count816-1]["Target name"]))

		data=dataorig
	#	print "\n\ncompany",
	#	print count816,
		count816=count816+1

	#	print gvkeys,

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
	#	print "uniqlength : ",
	#	print uniqlength
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

		output.write("DL n=%d\n"%(uniqlength))
		output.write("Format=edgelist1\n")
		output.write("Labels embedded\n")
		output.write("Data:\n")

		temp=1
		fnlsum=0
		count=0
	#	print "processing upper triangle ..."
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
				print key2,
				print key1,
				print val 
				if val!=0:
					output.write("%d %d %.10f\n"%(key2,key1,val))
			temp=temp+1

	#	print fnlsum,
		density=(fnlsum*2)/(uniqlength*uniqlength-1)
	#	print density

#		uniqlength816.append(uniqlength)
#		finalsum816.append(fnlsum)
#		density816.append(density)
		print("%s seconds for this company\n" % (time.time()-start_time))

	with open('densityfile.txt','a') as file:
		file.write("%d %d %.10f %.10f\n"%(gvkeys,uniqlength,fnlsum,density))
#	data816["uniqlength816"]=uniqlength816
#	data816["finalsum816"]=finalsum816	
#	data816["density816"]=density816

#	data816.to_csv("816_target_gvkeys_density.csv")
	#print(" %s seconds" % (time.time()-start_time_total))