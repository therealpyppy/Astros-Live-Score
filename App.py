import tkinter as tk
import customtkinter as CTk
import statsapi
import datetime
import time
gamepk=None
date = datetime.datetime.now().strftime("%m/%d/%Y")
astros_schedule = statsapi.schedule(date=date, team="117", sportId=1)
for i in range(len(astros_schedule)):
    gamepk = astros_schedule[i]['game_id']
    astros_linescore = statsapi.linescore(gamePk=gamepk)
else:
    astros_linescore = "No game today check back later"

class Window:
    def __init__(self, parent):
       self.parent = parent
       self.label = CTk.CTkTextbox(parent,state="disabled",border_width=10,corner_radius=20, font=("Courier",14))
       self.label.pack(expand=True, fill='both')
       self.update()
 
    def update(self):
        self.label.configure(state="normal")
        self.label.delete("0.0", "end")
        self.label.insert("0.0", astros_linescore)
        self.label.configure(state="disabled")
        self.parent.after(1000, self.update)
 
if __name__ == '__main__':



    root = CTk.CTk()
    root.geometry('650x300')
    Window(root)




    root.mainloop()
