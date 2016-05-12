print ("816 Target GVKeys")

import pandas as pd 
data = pd.read_csv("816_target_gvkeys.csv")

dimensions = data.shape
#print (type(data))
#print data.dtypes
#print dimensions
#print data.head()

#print data.index
print data.columns.tolist()
#print data.loc[0]
#print data.loc[0:5]
#print data.iloc[0:2]

#print data[["Target name","gvkey"]].head()
#sorting based on gvkeys
datasort=data.sort(['gvkey'])


print datasort.head()
print datasort.reset_index(drop=True).head()
#print dimensions[0]





#print ("\nPAT76_06_assg")
data1=pd.read_csv("PAT76_06_assg.csv")
#print data1.shape
#print data1.head()
#print data1.columns.tolist()

#print ("\nDYNASS")
data2=pd.read_csv("DYNASS.csv")
#print data2.shape
#print data2.columns.tolist()




key=data.iloc[0]["gvkey"]
#print key
