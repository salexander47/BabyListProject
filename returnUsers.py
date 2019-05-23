import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

odf = pd.read_csv('bl_fulfillment_orders.csv')

#get dataframe where all rows are user orders
udf = odf.dropna(subset=['user_id'])

#get dataframe with the count of orders for each user
ucdf = udf.groupby('user_id').count()

#get summary statistics for count of orders per user
ucdf.describe()

#print number of users that made only one order
print(len(ucdf[ucdf['id']== 1]))

#eliminate rows where there is only one order per user
hdf = ucdf[ucdf['id'] != 1]

#print number of users that made only two orders
print(len(hdf[hdf['id'] == 2]))

#eliminate rows where there are only two orders per user
hdf2 = hdf[hdf['id'] != 2]

#now print a histogram with log y-axis
hdf2.hist(column='id', bins = 50, log = True)
plt.show()
