'''
pandas notes 1/26/24
alena hemminger CSC-103 spring 2024
doc site: https://pandas.pydata.org/docs/
'''
import pandas as pd

csvString="""ID,First Name,Last Name,E-Mail,Confirmed,Premium
1,Ray,Naruto,naruto@gmail.com,true,true
2,Cindy, Johns,cjohns@outlook.com,true,true
3,John,Smith,jsmith@yahoo.com,true,false
4,Pelé,,p@soccer.net,true,false
5,Mando,Lorian,thisistheway@gmail.com,,false"""

from io import StringIO

# bring csvString, use StringIO to make it the type of string pandas expects
csvIO = StringIO(csvString)
df = pd.read_csv(csvIO)

'''
in the console, you can 
    put df to call the new file 
    
    df.info() 
        to get into on it
    
    df.decribe() 
        get distribution info
    
    df.shape 
        get rows and columns of data
    
    df.value_counts() 
        get count of each full data point
    
            df.value_counts() 
                for piece of data where other data is (not) another data point
        
        
    f["First Name"] 
        pull all first names
    
        for i in df["First Name"]:
            print(i)
            
            
    df[df.index == 2] 
        gives that index's data set
    
    df[df.index.isin(range(1,3))] 
        gives the indexes between 1 and 3, exclusive of bigger number
        
    df.loc[0:2,[‘identifier’]]
        take series of indexes and brings just the info from your requested identifier
'''
    
# this is a full directory search
df = pd.read_csv('/Users/alenahemminger/Library/CloudStorage/OneDrive-CarlowUniversity/Spring24/CSC-103/ex1_pokemon/locations.csv')
 
# for a relative directory do something similar to this (this one didn't work)
# df = pd.read_csv('./ex1_pokemon/locations.csv')

'''
in console:
    df['region_id']==2
        comes out as true or false because pandas is best at booleans
    
    df[df['region_id']==2]
        runs previous data and gives the data we want: the identifiers and ids that line up w a region_id of 2
        
        first call queries the data, returns t/f
        second one passes the query through the dataframe and shows where it is true
        
    .tail(##)
          added to something like last 2, provides last ## lines of that dataset
                    
'''

