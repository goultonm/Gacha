from tkinter import *
from sumon_pool import *
import random
from PIL import *





root = Tk()
root.title ("I did work Mr Craig, I swear.") #the title things
root.iconbitmap('cringe.ico') #makes astolfo-kun the icon
root.geometry('1000x600')


one_sum = PhotoImage(file = 'Summon.gif')
ten_sum = PhotoImage(file = '10Summon.gif')

def roll():
    percentage = random.randint(0,5)
    print(percentage)
    if percentage ==0:
        summon_ssr()
    elif percentage <=3:
        summon_sr()
    elif percentage <=43:
        summon_r()
    elif percentage <=47:
        summon_ssrce()
    elif percentage <=59:
        summon_srce()
    else:
        summon_rce()



ssr_pool_size=len(servant.ssr_pool)
def summon_ssr():
    summoned_val = random.randint(0, ssr_pool_size-1)
    summoned =  servant.ssr_pool[summoned_val]
    print(summoned)
    print(summoned.file)
sr_pool_size=len(servant.sr_pool)

def summon_sr():
    summoned_val = random.randint(0, sr_pool_size-1)
    summoned =  servant.sr_pool[summoned_val]
    print(summoned)
    print(summoned.file)

r_pool_size=len(servant.r_pool)
def summon_r():
    summoned_val = random.randint(0, r_pool_size-1)
    summoned =  servant.r_pool[summoned_val]
    print(summoned)

ssrce_pool_size=len(ssrce)
def summon_ssrce():
    summoned_val = random.randint(0, ssrce_pool_size-1)
    summoned =  ssrce[summoned_val]
    print(summoned)
srce_pool_size=len(srce)
def summon_srce():
    summoned_val = random.randint(0, srce_pool_size-1)
    summoned =  srce[summoned_val]
    print(summoned)
rce_pool_size=len(srce)
def summon_rce():
    summoned_val = random.randint(0, rce_pool_size-1)
    summoned =  rce[summoned_val]
    print(summoned)


def kys():
    root.destroy()
one_summon = Button(root, text = 'End me !', bd = '0', image = (one_sum), command = roll) #made a button that does something
one_summon.place(x=150, y=400)

ten_summon = Button(root, text = 'End me !', bd = '0', image = (ten_sum), command = kys) #made a button that does something
ten_summon.place(x=600, y=400)


root.mainloop()
