# print("Hello, World")
import random
from tkinter import *
from PIL import Image

window = Tk()
window.title("my practice program")

keys = ["a", "b", "c", "d", "e", "f", "g"]

random_keyselected = random.choice(keys)


def randomkey():
    keys = ["a", "b", "c", "d", "e", "f", "g"]
    key_selected = random.choice(keys)
    return key_selected

# # key_pressed = input("press the key shown:" + key_selected)
# # if key_pressed == key_selected :
# #  print("good")


mytoplabel = Label(window, text=random_keyselected)
mytoplabel.grid(row=0, column = 1)

def check_keypressed(buttonpressed):
    key_button = buttonpressed
    print(f"You tried to click: {buttonpressed}")
    if buttonpressed == random_keyselected:
        mylable = Label(window, text="Good!")

        mylable.grid(row = 5, column =1)

def buttonclick():
    mylabel = Label(window, text="Hello World!")
    mylabel.pack()
# switch()

ff_add = lambda a,b : a+ b

result = ff_add(3, 4)

# (a, b) => a+b

myButton1 = Button(window, text= keys[0], command = lambda : check_keypressed(keys[0]))
myButton2 = Button(window, text= keys[1], command = lambda : check_keypressed(keys[1]))
myButton3 = Button(window, text= keys[2], command =lambda : check_keypressed(keys[2]))
myButton4 = Button(window, text= keys[3], command = lambda : check_keypressed(keys[3]))
myButton5 = Button(window, text= keys[4], command = lambda : check_keypressed(keys[4]))
myButton6 = Button(window, text= keys[5], command = lambda : check_keypressed(keys[5]))
myButton7 = Button(window, text= keys[6], command = lambda : check_keypressed(keys[6]))
myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=2)
myButton3.grid(row=2, column=0)
myButton4.grid(row=2, column=2)
myButton5.grid(row=3, column=0)
myButton6.grid(row=3, column=2)
myButton7.grid(row=4, column=0)


# mylabel1 = Label(window, text="Hello World!")
# mylabel2 = Label(window, text="My name is prosun")
#
# mylabel1.grid(row=0, column= 0)
# mylabel2.grid(row=1, column=0)

# mylabel.pack()
window.mainloop()

