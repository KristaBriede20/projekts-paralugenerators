from tkinter import *
from random import randint
import yaml
import logging
import logging.config

from configparser import ConfigParser

with open('./config.yaml', 'r') as stream:  
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

logger = logging.getLogger('root')

logger.info('Paroļu ģenerātors')


base = Tk()
base.title('Paroļu Ģenerātors')
base.geometry("500x300")

#Ģenerē jaunu paroli
def paroles() :
    par_ievade.delete(0, END)
    par_garums = int(ievade.get())

    parole = ''


    for p in range(par_garums) :
        parole += chr(randint(33,126))

    
    par_ievade.insert(0, parole)

#Izveido label frame
label = LabelFrame(base,background="red", text="Number of characters?")
label.pack(pady=20)

#Izveido lodziņu, kur ievadīt vēlamo paroles garumu
ievade = Entry(label, background="white", font=("Helvetica", 24))
ievade.pack(pady=20, padx=20)

#Izveido logu priekš random izveidotās paroles
par_ievade = Entry(base, text='hiiiii', font=("Helvetica",24), bd=0, bg="white")
par_ievade.pack(pady=20)

#Izveido logu priekš paroļu ģenerēšanas palaišanas pogas
frame = Frame(base, background="black")
frame.pack(pady=20)

#Izveido paroļu ģenerēšanas palaišanas pogu
button = Button(frame, text="Ģenerēt jaunu paroli", command=paroles)
button.grid(row=0, column=0, padx=10)

#Palaiž
base.mainloop()



