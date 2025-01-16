from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text ="type", src ="English",dest ="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg, src = s, dest = d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END,textget)






root = Tk()
root.title("Translator by Ashraf")
root.geometry("800x650")
root.config(bg='orange')

lab_txt = Label(root, text= "Translator", font =("Time new Roman", 35, "bold"))
lab_txt.place(x=230,y=50, height=60, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text= "Source text", font =("Time new Roman", 20, "bold"),fg="Black", bg="orange")
lab_txt.place(x=230,y=125, height=30, width=300)

Sor_txt = Text(frame,font =("Time new Roman", 20, "bold"),wrap=WORD)
Sor_txt.place(x=15,y=180, height=120, width=770)

list_text = list(LANGUAGES.values())

comb_sor  = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=15,y=320, height=40, width=170)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief = RAISED, command=data)
button_change.place(x=300,y=320, height=40, width=180)

comb_dest  = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=580,y=320, height=40, width=170)
comb_dest.set("English")

lab_txt = Label(root, text= "Destination text", font =("Time new Roman", 20, "bold"),fg="Black", bg="orange")
lab_txt.place(x=230,y=400, height=30, width=300)

dest_txt = Text(frame,font =("Time new Roman", 20, "bold"),wrap=WORD)
dest_txt.place(x=15,y=450, height=120, width=770)



root.mainloop()