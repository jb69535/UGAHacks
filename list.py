from tkinter import*

win = Tk()
win.title("CafeName")
win.geometry("200x200+100+100")

frame=Frame(win)
frame.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox=Listbox(frame, yscrollcommand = scrollbar.set)
for i in range(0, len(df['Name'])):
    listbox.insert(i,df.iloc[i,0])
    listbox.pack()

scrollbar["command"]=listbox.yview

def command_return_loc():
        for i in listbox.curselection():
            lon=df.iloc[i, 3]
            lat=df.iloc[i, 4]
            loc = lon, lat
            m = folium.Map(location=loc, zoom_start=15)

            Tokyomap = 'Tokyomap.html'

            m.save('Tokyomap.html')

            webbrowser.open(Tokyomap)


button = Button(frame, text="Find", command = command_return_loc)
button.pack()


mainloop()
