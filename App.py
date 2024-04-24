import customtkinter
import statsapi
import datetime
import time
    
date = datetime.datetime.now().strftime("%m/%d/%Y")
astros_schedule = statsapi.schedule(team=117,start_date=date,end_date=date)
gamepk = astros_schedule[0]['game_id']
astros_linescore = statsapi.linescore(gamePk=gamepk)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()
app.title("Astros Score Manual")
app.grid_columnconfigure(0, weight=1)
app.geometry("675x325")
switch_var = customtkinter.StringVar(value="off")

def switch_event():
    onoff = switch_var.get()
    if onoff == "off":
        Textbox.configure(state="normal")
        Textbox.delete("0.0","end")
        Textbox.configure(state="disabled")
    if onoff == "on":
        Textbox.configure(state="normal")
        Textbox.delete("0.0","end")
        Textbox.insert("0.0",astros_linescore)
        Textbox.configure(state="disabled")
        print("1")
        app.after(10000, switch_event)

Switch = customtkinter.CTkSwitch(master=app, text="Check the astros score (live)", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off")
Switch.pack(padx=20, pady=10)

Textbox = customtkinter.CTkTextbox(master=app,width=650,height=300, corner_radius=20, border_width=5, activate_scrollbars = False, state="disabled",font=("Courier",14), wrap="none")
Textbox.pack(padx=20, pady=10)




app.after(10000, switch_event)
app.mainloop()