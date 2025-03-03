import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Task4a_data_November 22.csv")
extract_flight_route = df.loc[(df['From'] == "LHR") & (df['To'] == "DUB")]

am_extract = extract_flight_route.loc[(extract_flight_route["Time"]=="AM")]
pm_extract = extract_flight_route.loc[(extract_flight_route["Time"]=="PM")]
extract_dates_am = am_extract.loc[: , "01/04/22":"05/04/22"]
extract_dates_pm = pm_extract.loc[: , "01/04/22":"05/04/22"]


print(f"Flights in AM from LHR to DUB {extract_dates_am.sum()}")
print(f"Flights in PM from LHR to DUB {extract_dates_pm.sum()}")
plt.figure(figsize=(10, 6))
# Assuming the index of extracted_data represents the date labels,
# or you could map the data to appropriate dates if available.
extract_dates_am.sum().plot(kind='bar', color='skyblue')
plt.xlabel("Dates")
plt.ylabel("Passengers")
plt.title(f"Flights in AM from LHR to DUB")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
# groupedAMDates = am_extract.groupby(am_extract.loc[am_extract["Time"]=="AM"])["01/04/22":"05/04/22"].sum()

# print(f"We have found these flights that match your criteria: {am_extract}")
