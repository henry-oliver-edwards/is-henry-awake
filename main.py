import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd
import datetime
from time import sleep
import csv

OAuthCID = "22C425"
ClientSecret = "c0d66e697d269ad02c2b90d38033c1ec"

server = Oauth2.OAuth2Server(OAuthCID, ClientSecret)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token["access_token"])
REFRESH_TOKEN = str(server.fitbit.client.session.token["refresh_token"])

Henry = fitbit.Fitbit(OAuthCID, ClientSecret, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

startTime = pd.datetime(year=2021, month=2, day=16)

csv_heads = ["ID", "Time", "Steps"]

with open("steps-data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow(csv_heads)

ID = 0

# print(data)
# print(data["summary"])
# print(data["summary"]["steps"])

while True:
    data = Henry.activities()
    steps = data["summary"]["steps"]
    time = datetime.datetime.now()
    print(f"Adding log at ID={ID}, Time={time}, Steps={steps}")
    sleep(30)