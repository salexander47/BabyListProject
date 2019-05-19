import pandas as pd

# read in the table containing all items ordered within the last 30 days
# and their shipping times (if shipped).

tdf = pd.read_csv("F:/BabyListProject/TurnaroundTimeTbl.csv")

#find number of records where turnaround time is 12 hrs or less,
#12-24 hrs, 24-48 hrs, and >48 hrs
num12Hr = len(tdf[tdf['turnaround_time']<= 12.0])
num24Hr = len(tdf[(tdf['turnaround_time']<= 24.0) & (tdf['turnaround_time']>12.0)])
num48Hr = len(tdf[(tdf['turnaround_time']<= 48.0) & (tdf['turnaround_time']>24.0)])
numAbove48Hr = len(tdf[tdf['turnaround_time']>48.0])
#find total number of records in this table
totalShipped = len(tdf[tdf['turnaround_time']>0.0])

#calculate percentage of orders shipped within 12 hours of order completion
pct12Hr = round(num12Hr/totalShipped, 3)
pct24Hr = round(num24Hr/totalShipped, 5)#used 5 to eliminate rounding error
pct48Hr = round(num48Hr/totalShipped, 3)
pctAbove48Hr = round(numAbove48Hr/totalShipped, 3)

#print('totalShipped: '+ str(totalShipped))
print('<=12 hrs: '+ str(pct12Hr*100)+'%')
print('12-24 hrs: '+ str(pct24Hr*100)+'%')
print('24-48 hrs: '+ str(pct48Hr*100)+'%')
print('>48 hrs: '+ str(pctAbove48Hr*100)+'%')
