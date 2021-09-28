from tkinter import *
from random import randint

base = Tk()
base.title('Paroļu Ģenerātors')
base.geometry("500x300")

def paroles() :
    par_ievade.delete(0, END)
    par_garums = int(ievade.get())

    parole = ''


    for p in range(par_garums) :
        parole += chr(randint(33,126))

    
    par_ievade.insert(0, parole)

label = LabelFrame(base,background="red", text="Number of characters?")
label.pack(pady=20)

ievade = Entry(label, background="white", font=("Helvetica", 24))
ievade.pack(pady=20, padx=20)

par_ievade = Entry(base, text='', font=("Helvetica",24), bd=0, bg="black")
par_ievade.pack(pady=20)

frame = Frame(base, background="black")
frame.pack(pady=20)

button = Button(frame, text="Ģenerēt jaunu paroli", command=paroles)
button.grid(row=0, column=0, padx=10)

base.mainloop()
