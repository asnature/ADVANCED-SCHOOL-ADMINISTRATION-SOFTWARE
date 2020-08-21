from tkinter import *
from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode

root = Tk()
root.title("ID Card Generator")
root.geometry("1530x830")
f1 = Frame(root, height=830, width=1530, bg='red').pack()

n1_id = StringVar()


def Card_Generator():
    t1_id = n1_id.get()
    filename = t1_id + '.txt'
    fileopen = open(filename, 'r')

    (x, y) = (50, 50)
    message = "XYZ School"
    company = message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), message, fill=color, font=font)

    # ADMISSION NUMBER
    x_value = fileopen.readline()
    (x, y) = (550, 115)
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y), x_value, fill=color, font=font)

    # FIRST NAME
    x_value = fileopen.readline()
    (x, y) = (50, 250)
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), x_value, fill=color, font=font)

    # LAST NAME
    x_value = fileopen.readline()
    (x, y) = (530, 250)
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=45)  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # MOBILE NUMBER
    (x, y) = (50, 350)
    x_value = fileopen.readline()
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # EMAIL ID
    x_value = fileopen.readline()
    (x, y) = (50, 450)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # DOB
    (x, y) = (50, 550)
    x_value = fileopen.readline()
    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # GENDER
    x_value = fileopen.readline()
    (x, y) = (50, 650)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # ADDRESS
    x_value = fileopen.readline()
    (x, y) = (50, 750)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), x_value, fill=color, font=font)

    # save the edited image

    image.save('admission.png')

    img = qrcode.make(t1_id)  # this info. is added in QR code, also add other things
    img.save('qrcode.bmp')

    til = Image.open('admission.png')
    im = Image.open('qrcode.bmp')  # 25x25
    til.paste(im, (600, 550))
    til.save('admission.png')


l1 = Label(f1, text='Enter Admission Number', font='25', bg='yellow').place(x=300, y=300)
e1 = Entry(f1, textvariable=n1_id, font='20', width=3, bd=5).place(x=550, y=300)
b1 = Button(f1, text="Generate", bg='green', padx=5, pady=5, command=Card_Generator).place(x=600, y=350)

root.propagate(0)
root.mainloop()