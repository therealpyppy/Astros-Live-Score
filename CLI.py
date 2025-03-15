import statsapi
import datetime
import time
import os

date = datetime.datetime.now().strftime("%m/%d/%Y")

astros_schedule = statsapi.schedule(team=117,start_date=date,end_date=date)
gamepk = astros_schedule[0]['game_id']

while True:
    os.system('cls || clear')
    print(statsapi.linescore(gamePk=gamepk))
    time.sleep(10)