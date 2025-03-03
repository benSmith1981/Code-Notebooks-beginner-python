import pandas as pd

# OR we can just read in the CSV file
df = pd.read_csv("Task3_data.csv")
# See the head of the data to understand it
df.head() 

menuItem = "Nachos"

# while answer != "n":
#     meunitemsList = print(df["MenuItems"].unique())
#     answer = input(f"Enter menu item {meunitemsList} n to quit")
#     if answer == "n":
#         break
#     else:
#         menuItems.append(answer)


filterMenuItems = df.loc[df["Menu Item"] == menuItem]
print(filterMenuItems)

filteredSalesDates = filterMenuItems.loc[:,"03/03/2023": "08/03/2023"]

print(filteredSalesDates)

# Sum the sales across the date range for this item
#Nachos
total_sales = filteredSalesDates
print(total_sales)
#Soup
# total_sales = filteredSalesDates.sum(axis=1).values[1]
# print(total_sales)
