import statsapi
import datetime
import time
import os
# Gets the current date for the schedule
date = datetime.datetime.now().strftime("%m/%d/%Y")
 
# Finds astros current gamepk
astros_schedule = statsapi.schedule(team=117,start_date=date,end_date=date)
gamepk = astros_schedule[0]['game_id']

# Loops so you dont have to restart the program every time
i = 10
while i > 0:
    # Gets the linescore for the current astros game
    astros_gameinfo = statsapi.linescore(gamePk=gamepk)
    # Prints the linescore
    os.system('cls')
    print(astros_gameinfo)
    time.sleep(10)
else: 
    print("The program has been stopped")
