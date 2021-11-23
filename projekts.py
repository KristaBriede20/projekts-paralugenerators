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

with open(r"./conf.yaml") as stream:  
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)
logger = logging.getLogger('root')

connection = sqlite3.connect(r"database/database.db")
cursor = connection.cursor()

try:
    config = ConfigParser()
    config.read('config.ini')

    default_password_length = int(config.get('generator', 'default_password_length'))
    min_ascii = int(config.get('generator', 'min_ascii'))
    max_ascii = int(config.get('generator', 'max_ascii'))
except:
    logger.error(logging.error)

logger.info("DATA")

logger.info('Programma tiek palaista')

if __name__ == "__main__":
    base = Tk()
    base.title('Paroļu Ģenerātors')
    base.geometry("500x300")

#Ģenerē jaunu paroli
    def paroles() :
        par_ievade.delete(0, END)
        try:
            par_garums = int(ievade.get())
        except:
            par_garums = default_password_length
        logger.info('Izvēlēts paroles garums: ' + str(par_garums))
        garums.append(par_garums)
        
        parole = ''
        
        if par_garums == '':
            par_garums = default_password_length

        for p in range(par_garums) :
            parole += chr(randint(min_ascii,max_ascii))

    
        par_ievade.insert(0, parole)
        gen_par.append(parole)
        print(parole)

        cursor.execute('INSERT INTO paroles(garums, parole) VALUES(?, ?)', (par_garums, parole,))
        connection.commit()
        logger.info('Parole ievietota datubāzē')
        return 0
        
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
    
#connection.commit()
logger.info('Commited')
#cursor.close()

#Palaiž
base.mainloop()
logger.info('Programma aizvērta')
