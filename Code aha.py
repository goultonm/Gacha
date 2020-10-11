from tkinter import *
from sumon_pool import *
import random
from PIL import ImageTk, Image
from FGOArt import *




root = Tk()
root.title ("Gacha Simulator") #the title things
root.iconbitmap('cringe.ico') #makes Astolfo-kun the icon
root.geometry('1600x900')
canvas = Canvas(root, width = 1600, height = 900)
background_file = PhotoImage(file = 'summon_background.png')
background_cool = Label(image=background_file)
background_cool.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()
root.resizable(0, 0)



single_butt = ImageTk.PhotoImage(Image.open('summon_tile.png'))
ten_butt = ImageTk.PhotoImage(Image.open('ten_summon_tile.png'))
exit_butt = ImageTk.PhotoImage(Image.open('Close.png'))


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
    load = Image.open(summoned.file)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER)

sr_pool_size=len(servant.sr_pool)


def summon_sr():
    summoned_val = random.randint(0, sr_pool_size-1)
    summoned =  servant.sr_pool[summoned_val]
    print(summoned)
    print(summoned.file)
    load = Image.open(summoned.file)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER)

r_pool_size=len(servant.r_pool)


def summon_r():
    summoned_val = random.randint(0, r_pool_size-1)
    summoned =  servant.r_pool[summoned_val]
    print(summoned)
    print(summoned.file)
    load = Image.open(summoned.file)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER)

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
def nothing():
    print("nothing")


close = Button(root, bd = '0', anchor = "ne", image = exit_butt, command = kys) # this is an exit button
close.place(x = 1525, y =25)

one_summon = Button(root, bd = '0', image = single_butt, command = roll, text = "1x Summon")  # made a button that rolls the gacha
one_summon.place(x = 380, y =750)

ten_summon = Button(root, bd = '0', anchor = 's', image = ten_butt, command = nothing, )  # made a button that does nothing
ten_summon.place(x = 900, y =750)



root.mainloop()
