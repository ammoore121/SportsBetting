import requests
import pandas as pd

Privilege_content = "https://content.unabated.com/markets/game-odds/b_gameodds.json"

url = Privilege_content
#returns isPrivileged: true for premium sportsbooks

payload = ""
headers = {
    "authority": "content.unabated.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "dnt": "1",
    "origin": "https://unabated.com",
    "referer": "https://unabated.com/",
    "sec-ch-ua": "^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-amz-cf-v-id": "dNSob7rQOiJFE_59NDSm7tuZ6ed5MA_8w8CHVqr8tGSFYpgzEUqBuQ=="
}
#We can customize the headers we include ^ I left as it came
r = requests.request("GET", url, data=payload, headers=headers)


data = r.json()

marketSources = (data["marketSources"])
teams = (data["teams"])
gameOddsEvents = (data["gameOddsEvents"])



df_sportsbooks = pd.DataFrame(marketSources)
df_teams = pd.DataFrame(teams)
df_ScoreId = pd.DataFrame.from_dict(gameOddsEvents, orient='index')




df1 = pd.DataFrame().assign(Name=df_sportsbooks['name'],bookId=df_sportsbooks['id'],isActive=df_sportsbooks['isActive'],
isPrivileged=df_sportsbooks['isPrivileged'],statusId=df_sportsbooks['statusId'],modifiedDate=df_sportsbooks['modifiedOn'])

df1['nyBook']= 0
df1['sharpBook']=0


df_nyBooks= pd.DataFrame(
    {"Name" : ["Caesars", "DraftKings", "FanDuel", "FanDuel - Delayed", "BetMGM", "PointsBet", "BetRivers", "WynnBet", "Resorts", "BallyBet"],
    'nyBook': [1,1,1,1,1,1,1,1,1,1]
    }
)
df_sharpBooks = pd.DataFrame(
    {"Name" :['Unabated','Pinnacle','Pinnacle - Delayed','Bookmaker','Prophet Exchange'],
    'sharpBook': [1,1,1,1,1]
    }
)




df1=df1.set_index('Name')
df2 = df_nyBooks.set_index('Name')
df1.update(df2)
df3=df_sharpBooks.set_index('Name')
df1.update(df3)



print(df1)
