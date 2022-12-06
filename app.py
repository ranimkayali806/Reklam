import pygame
from led import mlcdinit,mlcddraw

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


import random
from datetime import datetime

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/reklam'
db = SQLAlchemy(app)

class Annons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kundid = db.Column(db.Integer, nullable=False)
    del1 = db.Column(db.String(30), unique=False, nullable=False)
    del2 = db.Column(db.String(30), unique=False, nullable=False)
    del3 = db.Column(db.String(30), unique=False, nullable=False)

class Kund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(50),unique=False,nullable=False)
    betalt = db.Column(db.Integer,unique=False,nullable=False)



today_time = datetime.now()
current_minute = today_time.strftime("%M")
current_minute_format = datetime.strptime(current_minute, "%M")
current_hour = today_time.strftime("%H")
current_hour_format = datetime.strptime(current_hour, "%H")

start_hour = "17"
stop_hour = "6"
start_hour_format = datetime.strptime(start_hour, "%H")
stop_hour_format = datetime.strptime(stop_hour, "%H")

Hederlige_Harrys_Bilar = []
Farmor_Ankas_Pajer_AB = []
Svarte_Petters_Svartbyggen = []
Långbens_detektivbyrå = []
Yrrol_AB =[]

if __name__  == "__main__":
    with app.app_context():

        annons= Annons.query.filter_by(kundid = 1).all()
        for a in annons:
            Hederlige_Harrys_Bilar.append([a.del1, a.del2, a.del3])

        annons= Annons.query.filter_by(kundid = 2).all()
        for a in annons:
            Farmor_Ankas_Pajer_AB.append([a.del1, a.del2, a.del3])

        annons= Annons.query.filter_by(kundid = 3).all()
        for a in annons:
            Svarte_Petters_Svartbyggen.append([a.del1, a.del2, a.del3])

        annons= Annons.query.filter_by(kundid = 4).all()
        for a in annons:
            Långbens_detektivbyrå.append([a.del1, a.del2, a.del3])

        annons= Annons.query.filter_by(kundid = 5).all()
        for a in annons:
            Yrrol_AB.append([a.del1, a.del2, a.del3])

        totalsumma = 0
        kundsumma =[]
        slot = []
        kund = Kund.query.all()

        for k in kund :
            totalsumma += k.betalt
            kundsumma.append(k.betalt)
            slot.append(totalsumma)

        totalsumma += 1000


    # Farmor_Ankas_Pajer_AB = [["Köp paj", "hos", "Farmor Anka"], ["Skynda innan Mårten", "ätit", "alla pajer"]]

    # Svarte_Petters_Svartbyggen = [["Låt Petter", "bygga", "åt dig"], ["Bygga svart?", "Ring", "Petter"]]

    # Långbens_detektivbyrå = [["Mysterier?", "Ring", "Långben"], ["Långben", "fixar", "biffen"]]

    egen_reklam_text = ["Synas här?", "Python22:s", "Reklambyrå"]
    larm_text = ["BRANDLARM", "UTRYM", "SNARAST"]

    def ReklamTid():
        
        reklam_tid = random.randint(1,totalsumma)
        if reklam_tid >= 1 and reklam_tid <= slot[0]:
            reklam_text = random.choice(Hederlige_Harrys_Bilar)
        elif reklam_tid >= (slot[0] + 1) and reklam_tid <= slot[1]:
            reklam_text = random.choice(Farmor_Ankas_Pajer_AB)
        elif reklam_tid >= (slot[1] + 1) and reklam_tid <= slot[2]:
            if ((current_minute_format).minute % 2) == 0:
                reklam_text = Svarte_Petters_Svartbyggen[0]
            else:
                reklam_text = Svarte_Petters_Svartbyggen[1]
        elif reklam_tid >= (slot[2] + 1) and reklam_tid <= slot[3]: 
            if current_hour_format >= start_hour_format and current_hour_format <= stop_hour_format:
                reklam_text = Långbens_detektivbyrå[0]
            else:
                reklam_text = Långbens_detektivbyrå[1]
        elif reklam_tid >= (slot[3] + 1) and reklam_tid <= slot[4]:
            reklam_text = random.choice(Yrrol_AB)
        else:
            reklam_text = egen_reklam_text
        
        return reklam_text

    # if __name__  == "__main__":
    #     with app.app_context():

    #         db.create_all()
    #         db.session.commit()

    mlcdinit(16,3,3) # initialize a 16x3 display scaled 3x  

    #draw the three lines passed as a list
    mlcddraw(["Synas här?",         
                "Python22:s",
                "Reklambyrå"])

    running = True
    larm = False

    pygame.time.set_timer(pygame.USEREVENT, 5000)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if larm == False:
                    mlcddraw(ReklamTid())
                else :
                    mlcddraw(larm_text)
            elif event.type == KEYDOWN:
                if larm == False:
                    larm = True
                else :
                    larm = False
            elif event.type == QUIT:
                running = False