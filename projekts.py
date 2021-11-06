from sqlite3.dbapi2 import Cursor
from tkinter import *
from random import randint
import logging
import yaml
import logging.config
import sqlite3
from sqlite3 import Error
from configparser import ConfigParser

garums = []
gen_par = []

with open(r"C:\Users\Default.DESKTOP-NKF7PFE\Desktop\projekts-paroles\conf.yaml", 'r') as stream:  
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)
logger = logging.getLogger('root')

connection = sqlite3.connect(r"C:\Users\Default.DESKTOP-NKF7PFE\Desktop\projekts-paroles\database.db")
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS "paroles"("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "garums" INTEGER NOT NULL, "parole" TEXT NOT NULL UNIQUE)')
logger.info("DATA")

logger.info('Programma tiek palaista')

if __name__ == "__main__":
    base = Tk()
    base.title('Paroļu Ģenerātors')
    base.geometry("500x300")

#Ģenerē jaunu paroli
    def paroles() :
        par_ievade.delete(0, END)
        par_garums = int(ievade.get())
        logger.info('Izvēlēts paroles garums: ' + str(par_garums))
        garums.append(par_garums)
        
        parole = ''
        

        for p in range(par_garums) :
            parole += chr(randint(1,555))

    
        par_ievade.insert(0, parole)
        gen_par.append(parole)
        
        
        
    for dataID in enumerate(garums):
        lastID = cursor.lastrowid
        cursor.execute('INSERT INTO paroles(garums, parole) VALUES(?, ?)', (dataID + 1, gen_par[dataID],))

        cursor.execute('SELECT * FROM paroles')
    for x in cursor:
        print(x)
        
        
#Izveido label frame
    label = LabelFrame(base,background="red", text="Number of characters?")
    label.pack(pady=20)

#Izveido lodziņu, kur ievadīt vēlamo paroles garumu
    ievade = Entry(label, background="white", font=("Helvetica", 24))
    ievade.pack(pady=20, padx=20)

#Izveido logu priekš random izveidotās paroles
    par_ievade = Entry(base, text='', font=("Helvetica",24), bd=0, bg="white")
    par_ievade.pack(pady=20)

#Izveido logu priekš paroļu ģenerēšanas palaišanas pogas
    frame = Frame(base, background="black")
    frame.pack(pady=20)

#Izveido paroļu ģenerēšanas palaišanas pogu
    button = Button(frame, text="Ģenerēt jaunu paroli", command=paroles)
    button.grid(row=0, column=0, padx=10)
    
connection.commit()
cursor.close()

#Palaiž
base.mainloop()
logger.info('Programma aizvērta')


