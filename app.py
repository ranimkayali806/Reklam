

import pygame
from led import mlcdinit,mlcddraw

import random
from datetime import datetime

today_time = datetime.now()
current_minute = today_time.strftime("%M")
current_minute_format = datetime.strptime(current_minute, "%M")
current_hour = today_time.strftime("%H")
current_hour_format = datetime.strptime(current_hour, "%H")

start_hour = "17"
stop_hour = "6"
start_hour_format = datetime.strptime(start_hour, "%H")
stop_hour_format = datetime.strptime(stop_hour, "%H")


Hederlige_Harrys_Bilar = [["Köp bil", "hos", "Harry"],
["En god", "bilaffär", "(för Harry!)"], ["Hederlige", "Harrys", "Bilar"]]


Farmor_Ankas_Pajer_AB = [["Köp paj", "hos", "Farmor Anka"], ["Skynda innan Mårten", "ätit", "alla pajer"]]

Svarte_Petters_Svartbyggen = [["Låt Petter", "bygga", "åt dig"], ["Bygga svart?", "Ring", "Petter"]]

Långbens_detektivbyrå = [["Mysterier?", "Ring", "Långben"], ["Långben", "fixar", "biffen"]]

egen_reklam_text = ["Synas här?", "Python21:s", "Reklambyrå"]

def ReklamTid():
    
    reklam_tid = random.randint(1,14500)
    if reklam_tid >= 1 and reklam_tid <= 5000:
        reklam_text = random.choice(Hederlige_Harrys_Bilar)
    elif reklam_tid >= 5001 and reklam_tid <= 8000:
        reklam_text = random.choice(Farmor_Ankas_Pajer_AB)
    elif reklam_tid >= 8001 and reklam_tid <= 9500:
        if ((current_minute_format).minute % 2) == 0:
            reklam_text = Svarte_Petters_Svartbyggen[0]
        else:
            reklam_text = Svarte_Petters_Svartbyggen[1]
    elif reklam_tid >= 9501 and reklam_tid <= 13500: 
        if current_hour_format >= start_hour_format and current_hour_format <= stop_hour_format:
            reklam_text = Långbens_detektivbyrå[0]
        else:
            reklam_text = Långbens_detektivbyrå[1]
    else:
        reklam_text = egen_reklam_text
    
    return reklam_text


mlcdinit(16,3,3) # initialize a 16x3 display scaled 3x  

#draw the three lines passed as a list
mlcddraw(["Hello",         
               "     world",
               "What"])

pygame.time.set_timer(pygame.USEREVENT, 5000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            mlcddraw(ReklamTid())