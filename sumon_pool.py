from tkinter import *
from enum import IntEnum
import random


class servant:  #creates class called servants for summoning

    class rarity (IntEnum):
        SSR = 1
        SR = 2
        R = 3

    R = rarity.R
    SR = rarity.SR
    SSR = rarity.SSR
    #names and rarity of the servants to create the objects
    names = ["Mafia Kajita" , "Mashu" , "Artoria Pendragon" , "Salter" , "Lily" , "Nero" , "Siegfried", "Julius", "Altera", "Gilles", "Deon","Emiya", "Gilgamesh", "Robin Hood", "Nyarcher", "Euryle", "Arash", "Cuu", "Liz", "Benki","Proto Cu", "Leonidas", "Romulas", "Medusa", "George"]
    rarity = [SSR,R,SSR,SR,SR,SR,SR,R,SSR,R,SR,SR,SSR,R,SR,R,R,R,SR,R,R,R,R,R,R]

    def __init__(self, name, rarity, num):
        self.name = name
        self.rarity = rarity
        self.num = num
        if num < 10: #creates file path so that the appropriate image can be found
            self.str_num = "00"+str(num)
        elif num < 100:
            self.str_num = "0"+str(num)
        else:
            self.str_num = str(num)
        self.file = "FGOArt\servant_" + self.str_num + ".png" #filename for the images

    def __repr__(self):  #unscrambles the jargon numbers
        return self.name

    ssr_pool = []
    sr_pool = []
    r_pool = []

servants = []
for i in range (25): #turns the first 25 entries in the class into objects
    servants.append(servant(servant.names[i], servant.rarity[i], i))


for servant in servants:
    if servant.rarity == servant.rarity.SSR:
        servant.ssr_pool.append(servant)
    elif servant.rarity == servant.rarity.SR:
        servant.sr_pool.append(servant)
    elif servant.rarity == servant.rarity.R:
        servant.r_pool.append(servant)
    else:
        print("ErrOr")

ssrce = ["ssrce crin ge","ssrce sad","ssrce josh","ssrce jett"]     #place holder variables to leave room for possible expansion

srce = ["srcebroDee","srcearniie","srcechirisu","srcebob",]

rce = ["black keys", "white keys", "yorokobe", "shounen", "rejoice"]

