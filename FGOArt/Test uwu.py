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

    names = ["Odessyeus" , "Mashu" , "Artoria Pendragon" , "Salter" , "Lily" ]
    rarity = [SSR,R,SSR,SR,SR]

    def __init__(self, name, rarity, id):
        self.name = name
        self.rarity = rarity
        self.id = id
        self.file = "servant_"+str(id)+".png"

    def __repr__(self):
        return self.name

    ssr_pool = []
    sr_pool = []
    r_pool = []

servants = []
for i in range (5):
    servants.append(servant(servant.names[i], servant.rarity[i], i))

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
