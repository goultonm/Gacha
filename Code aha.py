from tkinter import *
from sumon_pool import *
import random
from PIL import ImageTk, Image

#########################################################
#Imports the all librarys I need and my other code file
#########################################################

root = Tk()  # The first step for the GUI #
root.title ("Gacha Simulator")  #Sets the title of the top bar
root.iconbitmap('cringe.ico')  #Sets the Image on the top bar
root.geometry('1600x900')  #sets the size of the window
canvas = Canvas(root, width = 1600, height = 900) #makes the UI background the same size as the window
background_file = PhotoImage(file = 'summon_background.png') #sets background image
background_cool = Label(image=background_file)
background_cool.place(x=0, y=0, relwidth=1, relheight=1) #Finishes setting the background
canvas.pack()
root.resizable(0, 0) #makes the window not resizable



single_butt = ImageTk.PhotoImage(Image.open('summon_tile.png'))  #makes the summon button
exit_butt = ImageTk.PhotoImage(Image.open('Close.png'))     #makes the exit button


def roll(): #uses a random number to generate what comes out of the gacha
    percentage = random.randint(0,43) #number in range of 0 to 43
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



ssr_pool_size=len(servant.ssr_pool)  #allows for the code to accept changing numbers of objects for future proofing
def summon_ssr():
    summoned_val = random.randint(0, ssr_pool_size-1)   #picks object from class in sumon_pool
    summoned =  servant.ssr_pool[summoned_val]
    load = Image.open(summoned.file)    #loads image stored in the object
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER)    #displays the image in the center of the GUI

sr_pool_size=len(servant.sr_pool)   #allows for the code to accept changing numbers of objects for future proofing
def summon_sr():
    summoned_val = random.randint(0, sr_pool_size-1)  #picks object from class in sumon_pool
    summoned =  servant.sr_pool[summoned_val]
    load = Image.open(summoned.file)    #loads image stored in the object
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER)    #displays the image in the center of the GUI

r_pool_size=len(servant.r_pool)     #allows for the code to accept changing numbers of objects for future proofing
def summon_r():
    summoned_val = random.randint(0, r_pool_size-1) #picks object from class in sumon_pool
    summoned =  servant.r_pool[summoned_val]
    load = Image.open(summoned.file)    #loads image stored in the object
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render, bd=0)
    img.image = render
    img.place(x=800, y=350, anchor = CENTER) #displays the image in the center of the GUI

ssrce_pool_size=len(ssrce)      #allows for the code to accept changing numbers of objects for future proofing
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
    root.destroy() #program ends itself

close = Button(root, bd = '0', anchor = "ne", image = exit_butt, command = kys) # this is an exit button
close.place(x = 1525, y =25)

one_summon = Button(root, bd = '0', image = single_butt, command = roll, text = "1x Summon")  #button that rolls the gacha
one_summon.place(x = 640, y =750 )


root.mainloop()