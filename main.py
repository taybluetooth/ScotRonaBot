# import Pandas and PrettyTable for csv parsing
import pandas as pd
from prettytable import PrettyTable
# initalise url for covid data
url = 'https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/7fad90e5-6f19-455b-bc07-694a22f8d5dc/download/total_cases_by_hb_20201223.csv'
# initialise data for twitter parsing
data = pd.read_csv(url, usecols=["HBName", "NewPositive", "TotalCases", "NewDeaths", "TotalDeaths"])
# assign data to seperate lists for ease of access
areas = data.HBName.to_list()
newCases = data.NewPositive.to_list()
totalCases = data.TotalCases.to_list()
newDeaths = data.NewDeaths.to_list()
totalDeaths = data.TotalDeaths.to_list()

table = PrettyTable()
table.field_names = ['Area', 'New Cases', 'Total Cases', 'New Deaths', 'Total Deaths']

for i in range(0, len(areas)):
    table.add_row([areas[i], newCases[i], totalCases[i], newDeaths[i], totalDeaths[i]])

print("\nCOVID 19 Statistics for Scotland (23/12/2020)\n")
print(table)
