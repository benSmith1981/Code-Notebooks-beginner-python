import pandas as pd

# OR we can just read in the CSV file
df = pd.read_csv("Task3_data_spending.csv")
# See the head of the data to understand it
df.head() 

item = "Tickets"

print(df.groupby("Day"))
#We are grouping by the day (all the days fo the week not repeating them) for the entered expense
groupedDays = df.groupby("Day")[item].sum()

print(groupedDays)

