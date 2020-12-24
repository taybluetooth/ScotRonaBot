# import Pandas and PrettyTable for csv parsing
import pandas as pd
from prettytable import PrettyTable, ORGMODE
# import date time for dynamic date changing
import datetime
import tweepy
from PIL import Image, ImageDraw, ImageFont
# initialise date
d = datetime.datetime.now()
year = str(d.year)
month = str(d.month)
day = str(d.day)
# initalise url for covid data
url = 'https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/7fad90e5-6f19-455b-bc07-694a22f8d5dc/download/total_cases_by_hb_'+year+month+day+'.csv'
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
table.set_style(ORGMODE)

for i in range(0, len(areas)):
    table.add_row([areas[i], newCases[i], totalCases[i], newDeaths[i], totalDeaths[i]])

print("COVID 19 Statistics for Scotland ("+day+"/"+month+"/"+year+")")
print("Data Gathered from @NHS and @ScotGov")
print(table)

data = table.get_string()

with open('test.txt', 'w') as f:
    f.write(data)

blank_image = Image.new('L', (900, 350), 'white')
img_draw = ImageDraw.Draw(blank_image)
font = ImageFont.truetype("consola.ttf", 18)
img_draw.text((0,0), data, fill='black', font=font)
blank_image.save('drawn_image.png')

auth = tweepy.OAuthHandler("wnbmWZRxAFeZe2Ckaszxvr76Q",
    "Lp6M69hrAAVxXS8wkQ6RoWx6GtxySs8m8WUr7dvp5gF0v5Ymnl")
auth.set_access_token("1341891940665716737-Yok4xnPegKTcy3aBzCIlSTylXryJYW",
    "6h4Q7mpyGHMoc69C9uUyMMVWoGYObyqQCmormROEMstX9")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def tweet_image(message):
    filename = 'drawn_image.png'
    api.update_with_media(filename, status=message)

message = "COVID 19 Statistics for Scotland ("+day+"/"+month+"/"+year+"). Data from @NHS and @ScotGov."
tweet_image(message)
