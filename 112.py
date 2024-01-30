import random
import keyboard
import time
from tkinter import *

root = Tk()
root.title('RandomHOI4')
root.geometry('350x350')
root.iconbitmap(default="HOI4_icon.ico")
root.configure(bg = 'green')

years_list=[' 1936',' 1939']
country_list=[' USSR',' Nazi Germany',' USA',' The Great England',' France',' Communist China',' China',' Manchukuo',' Italia',' Japan',' Austalia',' Bulgaria',' Britan India',' Hungary',' Greece',' Guangxi clique',' Spain',' Dominion Canada',' Mexico',' Netherlands',' New Zealand',' Poland',' Portugal',' Romania',' Sibei San Ma',' Turkey',' xinjiang',' Czechoslovakia',' Shanxi',' Yugoslavia',' South Africa',' Yunnan',' Latvia',' Lithuania',' Estonia',' Austria',' Albania',' Argentina',' Afghanistan',' Belgium',' Bolivia',' Venezuela',' Haiti',' Guatemala',' Dutch East Indies',' Honduras',' Denmark',' Dominican Republic',' Iraq',' Iran',' Ireland',' Yemen',' Costa Rica',' Cuba',' Liberia',' Luxembourg',' Mongolia',' Nicaragua',' Norway',' Oman',' Panama',' Paraguay',' Peru',' Salvador',' Saudi Arabia',' Siam',' Tannu-tuva',' Uruguay',' Philippines',' Finland',' Chile',' Switzerland',' Sweden',' Ecuador',' Ethiopia']
idelogy_list=[' communism',' fasism',' neutral',' democracy']

def wa():
    time.sleep(1)
    lbl_2.configure(text=random.choice(years_list))
    lbl_3.configure(text=random.choice(country_list))
    lbl_4.configure(text=random.choice(idelogy_list))

lbl = Label(root, text='touch grass(alt+f4 to exit)', font=('Comic Sans', 20), bg = 'green')
lbl_2 = Label(root, text='', font=('Comic Sans', 10), bg = 'green' )
lbl_3 = Label(root, text='', font=('Comic Sans', 10), bg = 'green')
lbl_4 = Label(root, text='', font=('Comic Sans', 10), bg = 'green')
lbl.pack()
lbl_2.pack()
lbl_3.pack()
lbl_4.pack()

btn = Button(root, text='touch me :)', command=wa)
btn.pack()

root.mainloop()
    
