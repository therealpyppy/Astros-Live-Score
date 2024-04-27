import tkinter as tk
import customtkinter as CTk
import statsapi
import datetime
import time
#   Gets the current date
date = datetime.datetime.now().strftime("%m/%d/%Y")
#   Gets the astros schedule for the current date
astros_schedule = statsapi.schedule(date=date, team="117", sportId=1)
class Window:
    def __init__(self, parent):
    #   Creats the Textbox
        self.parent = parent
        self.label = CTk.CTkTextbox(parent,state="disabled",border_width=10,corner_radius=20, font=("Courier",14))
        self.label.pack(expand=True, fill='both')
    #   Calls Update
        self.update()
 
    def update(self):
    #   If the astros schedule contains game_id sets gamepk = to it and sets astros_linescore to the current linescore
    #   If the astros schedule doesn't contain game_id sets astros_linescore to "No game today check back later"
        astros_schedule = statsapi.schedule(date=date, team="117", sportId=1)
        if str(range(len(astros_schedule))).find("0"):
            gamepk = astros_schedule[0]['game_id']
            astros_linescore = statsapi.linescore(gamePk=gamepk)
        else:
            astros_linescore = "no game today"
    #   Sets the text = to astros_linescore
        self.label.configure(state="normal")
        self.label.delete("0.0", "end")
        self.label.insert("0.0", astros_linescore)
        self.label.configure(state="disabled")
        self.parent.after(10000, self.update)
        
 
if __name__ == '__main__':


    root = CTk.CTk()
    root.geometry('650x300')
    Window(root)




    root.mainloop()
