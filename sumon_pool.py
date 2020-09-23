from tkinter import *
from enum import IntEnum
import random


class servant:

    class rarity (IntEnum):
        SSR = 1
        SR = 2
        R = 3

    R = rarity.R
    SR = rarity.SR
    SSR = rarity.SSR

    names = ["Odessyeus" , "Mashu" , "Artoria Pendragon" , "Salter" , "Lily" , "Nero"]
    rarity = [SSR,R,SSR,SR,SR,SR]

    def __init__(self, name, rarity, num):
        self.name = name
        self.rarity = rarity
        self.num = num
        print(num)
        if num < 10:
            self.str_num = "00"+str(num)
        elif num < 100:
            self.str_num = "0"+str(num)
        else:
            self.str_num = str(num)
        self.file = "servant_" + self.str_num + ".png"

    def __repr__(self):
        return self.name

    ssr_pool = []
    sr_pool = []
    r_pool = []

servants = []
for i in range (6):
    servants.append(servant(servant.names[i], servant.rarity[i], i))
    print(servants[i].file)
print(servants)

for servant in servants:
    if servant.rarity == servant.rarity.SSR:
        servant.ssr_pool.append(servant)
    elif servant.rarity == servant.rarity.SR:
        servant.sr_pool.append(servant)
    elif servant.rarity == servant.rarity.R:
        servant.r_pool.append(servant)
    else:
        print("ErrOr")


ssr = [
    "Artoria Pendragon" , "Altera" , "Okita Sōji" , "Mordred" , "Nero (Bride)" , "Ryogi Shiki (Saber)" , "Miyamoto Musashi" , "Arthur Pendragon (Prototype)" , "Sigurd" , "Beni-enma" , "Dioscuri"
    ]

sr = [
    "Artoria Pendragon (Alter)" , "Nero" , "Siegfried","Chevalier d'Eon","Rama","Lancelot (Saber)","Gawain","Suzuka Gozen","Frankenstein (Saber)","Yagyu Munenori","Medb (Saber)","Diarmuid Ua Duibhne (Saber)","Lanling Wang","Lakshmibai"
    ]

r = [
    "Gaius Julius Caesar","Gilles de Rais (Saber)","Fergus mac Róich","Bedivere"
    ]

ssrce = ["ssrce crin ge","ssrce sad","ssrce josh","ssrce jett"]

srce = ["srcebroDee","srcearniie","srcechirisu","srcebob",]

rce = ["black keys", "white keys", "yorokobe", "shounen", "rejoice"]

