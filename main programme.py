from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode

root=Tk()
root.title("Check")
root.geometry("1530x830+0+0")
root.configure(bg="lime")
root.propagate(0)
root.state('zoomed')
nb = ttk.Notebook(root)

l1 = Label(root, text="Welcome To the School Management System Online Portal",bg="yellow",font="comicsans 15 italic",fg="red").pack(fill = X)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
page5 = ttk.Frame(nb)
nb.add(page1, text='       STUDENT AND TEACHER REGISTRATION      ')
nb.add(page2, text= '      TIME TABLE MANAGEMENT       ')
nb.add(page3, text= '            GENERATE IDCARD         ')
nb.add(page4, text= '            FEES MANAGEMENT         ')
nb.add(page5, text= '            ATTANDANCE         ')
nb.pack(expand=True, fill = 'both')



#-----------------frame for the status bar and website info----------------

statusbar = StringVar()
statusbar.set("This portal is designed using python only")
sbar = Label(root, textvariable=statusbar, relief=SUNKEN, bg="purple",fg="white").pack(side=BOTTOM,fill=X)



# ---------------Background frame------------------
Background_Frame = Frame(page1,bg='sky blue',relief=GROOVE,bd=10)
Background_Frame.place(x=0,y=0,width=1530,height=800)
'''canvas = Canvas(Background_Frame,width=1530,height=800)
image = ImageTk.PhotoImage(Image.open("G:\\photos\\hd wallpaper\\TECH\\bbb.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
'''
# ---------------Registration Frame-----------------------
Left_frame = Frame(page1, bd=5, relief=GROOVE, bg="green")
Left_frame.place(x=35, y=205, width=700, height=600)
'''canvas1 = Canvas(Left_frame,width=700, height=600)
image1 = ImageTk.PhotoImage(Image.open("G:\\photos\\hd wallpaper\\TECH\\aa.jpg"))
canvas1.create_image(0,0,anchor=NW,image=image1)
canvas1.place(x=0,y=0)
'''
# ----------------Check detail frame______________________
Right_frame = Frame(page1, bd=5, relief=SUNKEN, bg="green")
Right_frame.place(x=810, y=205, width=700, height=607)
'''canvas2 = Canvas(Right_frame,width=700, height=600)
image2 = ImageTk.PhotoImage(Image.open("G:\\photos\\hd wallpaper\\TECH\\bbb.png"))
canvas2.create_image(0,0,anchor=NW,image=image2)
canvas2.place(x=0,y=0)
'''
# -------------left Frame for title in registration frame---------------
Left_Registration_frame_title = Frame(page1, bd=1, relief=RIDGE, bg="red")
Left_Registration_frame_title.place(x=85, y=155, width=600, height=50)

# -------------right Frame for title in check detais frame---------------
Right_Registration_frame_title = Frame(page1, bd=1, relief=RIDGE, bg="red")
Right_Registration_frame_title.place(x=870, y=145, width=600, height=57)

##----------Frame for the dialog box-----------

Left_Diag_frame = Frame(Left_frame,bd=3,relief=RIDGE,bg="yellow")
Left_Diag_frame.place(x=50,y=380, width=600, height=57)
##--------------Frame---------------------------------
Right_Diag_frame = Frame(Right_frame,bd=3,relief=RIDGE,bg="yellow")
Right_Diag_frame.place(x=50,y=380, width=600, height=57)

#-------------------PAGE3 FRAME-----------------
Page3_frame = Frame(page3,bg='red',relief=GROOVE,bd=10)
Page3_frame.place(x=0,y=0,width=1530,height=800)

#---------------Id frame-------------------
id_frame1 = Frame(Page3_frame,bg='lime',bd=10,relief=RIDGE)
id_frame1.place(x=20,y=140,height=600,width=400)

id_frame2 = Frame(Page3_frame,bg='lime',bd=10,relief=RIDGE)
id_frame2.place(x=500,y=140,height=600,width=750)
l1_id = Label(Page3_frame, text="Generate Your e-Identification Card here",bg="blue",font="comicsans 30 bold",fg="white",bd=3,relief=RIDGE).pack(fill = X)


#----------------------------FEES MANAGEMENT---------------

fees_frame = Frame(page4,bg="blue",height=800,width=1550)
fees_frame.place(x=0,y=0)

frame1 = Frame(fees_frame,bg="red",bd=5,relief=SUNKEN,height=500,width=500)
frame1.place(x=20,y=330)

label_fees = Label(frame1, text= "Enter The Details",bg= "white",fg="red",bd=3,relief=RIDGE,padx=10,pady=5).place(x=180,y=10)

Admission_no_fees = Label(frame1, text="Admission no  :",fg="white",bg="red",
font="comicsans 17 bold").place(x=10,y=50)
e1_id_fees = Entry(frame1, font='20', width=10, bd=5).place(x=230, y=50)
b1_id_fees = Button(frame1, text="View Details", fg='red',bg='yellow', padx=50, pady=7).place(x=120, y=100)


frame2 = Frame(fees_frame,bg="red",bd=5,relief=SUNKEN,height=750,width=900)
frame2.place(x=600,y=20)
frame3 = Frame(frame2,bg="white",bd=2,relief=SUNKEN,height=300,width=850)
frame3.place(x=20,y=10)

First_name_fees = Label(frame3, text="First name  :",fg="red",font="comicsans 17 bold").place(x=10,y=10)
Last_name_fees = Label(frame3, text="Last name  :",fg="red",font="comicsans 17 bold").place(x=10,y=60)
dateofbirth_fees = Label(frame3, text="D-O-B   :",fg="red",font="comicsans 17 bold").place(x=10,y=110)
class_fees = Label(frame3, text="Class name  :",fg="red",font="comicsans 17 bold").place(x=10,y=160)
faathers_fees = Label(frame3, text="Fathers  name  :",fg="red",font="comicsans 17 bold").place(x=10,y=210)
fees_paid_fees = Label(frame3, text="Month paid  :",fg="red",font="comicsans 17 bold").place(x=10,y=260)






###----------Page2 background image------------
canvas = Canvas(page2,width=1530,height=800)
image = ImageTk.PhotoImage(Image.open("G:\\photos\\hd wallpaper\\TECH\\NVIDIA-GEFRCEWallpaper-3840x2160.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

title1 = Label(Left_Registration_frame_title, text="TEACHER REGISTRATION", bg="red", fg="white",font="comicsans 30 bold", padx=50).grid(row=0, column=0)

title2 = Label(Right_Registration_frame_title, text="STUDENT REGISTRATION", bg="red", fg="white",font="comicsans 30 bold", padx=50).grid(row=0, column=0)

#------------------MAIN PROGRAMME--------------------------------

n1=StringVar()
n2=StringVar()
n3=StringVar()
n4=StringVar()
n5=StringVar()
n6=StringVar()
n11=StringVar()
n12=StringVar()
n13=StringVar()

def Teacher_button():
    t1=n1.get()
    t2=n2.get()
    t3=n3.get()
    t4=n4.get()
    t5=n5.get()
    t6=n6.get()
    t11=n11.get()
    t12=n12.get()
    t13=n13.get()

    temp_value2=open("admission_number.txt","r")
    temp_value4=temp_value2.read(20)
    temp_value2.close()
    temp_value2=open("admission_number.txt","w")
    temp_value4=int(temp_value4)
    temp_value3=temp_value4
    temp_value4=temp_value4+1
    temp_value4=str(temp_value4)
    temp_value2.write(temp_value4)
    temp_value2.close()



    temp_value1=str(temp_value3)
    full_file_name=temp_value1+".txt"
    student_record=open(full_file_name,"x")
    student_record.close()
    student_record=open(full_file_name,"a")
    student_record.write("First Name: "+t1)
    student_record.write("\nLast Name: "+t2)
    student_record.write("\nMobile Name: "+t3)
    student_record.write("\n /EmailId: "+t4)
    student_record.write("\nDateofBirth: "+t5)
    student_record.write("\nSpecialisation: "+t6)
    student_record.write("\nGender: "+t11)
    student_record.write("\nAddress: "+t12)
    student_record.write("\nQualification: "+t13)
    student_record.close()
    print("Admission Number is",(temp_value3))
    admission_number = Label(Left_Diag_frame, text="Unique Id Generated Is :"+str(temp_value3),fg='red',bg="yellow",font="comicsans 20 bold").grid(padx =25,pady=5)


Firstname = Label(Left_frame, text="First Name  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=0, column=0, pady=5, sticky="w")
txtfirstname = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n1).grid(row=0,column=1, padx=20,sticky="w")

Lastname = Label(Left_frame, text="Last Name  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1, column=0, sticky="w")
txtlastname = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n2).grid(row=1,column=1, padx=20,pady=5,sticky="w")

Mobileno = Label(Left_frame, text="Mbile No.  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=2, column=0, sticky="w")
txtmobile = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n3).grid(row=2, column=1, padx=20,pady=5,sticky="w")

Email = Label(Left_frame, text="Email Id.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=3,column=0, sticky="w")
txtemail = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n4).grid(row=3, column=1, padx=20,pady=5,sticky="w")

Dateofbirth = Label(Left_frame, text="D. O. B.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=4, column=0, sticky="w")
txtdateofbirth = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n5).grid(row=4, column=1,padx=20,pady=5,sticky="w")

Specialisation = Label(Left_frame, text="Specialisation  :", bg="green", fg="white",font="comicsans 15 bold").grid(row=5, column=0, sticky="w")
txtspecialisation = Entry(Left_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n6).grid(row=5, column=1,padx=20, pady=5,sticky="w")

Gender = Label(Left_frame, text="Gender  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Left_frame, font="comicsans 14 bold", state="readonly",textvariable=n11)
Dropdown_gender['values'] = ("male", "female", "other")
Dropdown_gender.grid(row=6, column=1, pady=5)

adress = Label(Left_frame, text="Address  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1,column=2, sticky="w")
txtadress = Entry(Left_frame,textvariable=n12,relief=SUNKEN,bd=5).grid(row=2, column=2, sticky="w")

qualification = Label(Left_frame, text="Qualifications:", bg="green", fg="white",font="comicsans 17 bold bold").grid(row=4, column=2, sticky="w")
txtqualification1 = Entry(Left_frame,textvariable=n13,relief=SUNKEN,bd=5).grid(row=5, column=2, sticky="w")




n7= StringVar()
admission = Label(page1, text="uniqueID  :", bg="green", fg="white",
font="comicsans 17 bold").place(x=10,y=100)
txtadmissiion = Entry(page1, font="comicsans 15 bold", bd=5, relief=GROOVE,textvariable=n7).place(x=150,y=100)



global t8




b11=Button(Left_frame,text="Click",bg='blue',command=Teacher_button,padx = 100,pady=20)
b11.place(x=150,y=450)

###############################################################








def button1():
        root1=Tk()
        root1.geometry('1200x800')
        frame12=Frame(root1,height=800,width=1200,bg='green').pack()
        t7 = n7.get()
        t8=t7+".txt"
        #t9=t8+".txt"
        t10 = open(t8,'r')
        t20 = t10.read()
        #t20.close()
        label1 = Label(root1,text=t20).place(x=800,y=50)
        root1.mainloop()
b12=Button(page1,text="Click",bg='blue',command=button1,padx = 30,pady=5)
b12.place(x=400,y=100)

#################################
############################
###########################################################
#######################################################################3
##################################################################################3
#####################################################################################3



#------------------MAIN PROGRAMME--------------------------------

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()

def Student_button():
    b1=a1.get()
    b2=a2.get()
    b3=a3.get()
    b4=a4.get()
    b5=a5.get()
    b6=a6.get()

    temp_value2=open("regg_number.txt","r")
    temp_value4=temp_value2.read(20)
    temp_value2.close()
    temp_value2=open("regg_number.txt","w")
    temp_value4=int(temp_value4)
    temp_value3=temp_value4
    temp_value4=temp_value4+1
    temp_value4=str(temp_value4)
    temp_value2.write(temp_value4)
    temp_value2.close()



    temp_value1=str(temp_value3)
    full_file_name=temp_value1+".txt"
    student_record=open(full_file_name,"x")
    student_record.close()
    student_record=open(full_file_name,"a")
    student_record.write("First Name: "+b1)
    student_record.write("\nSecond Name: "+b2)
    student_record.write("\nSecond Name: "+b3)
    student_record.write("\nSecond Name: "+b4)
    student_record.write("\nSecond Name: "+b5)
    student_record.write("\nSecond Name: "+b6)
    student_record.close()
    print("Admission Number is",(temp_value3))
    admission_number = Label(Right_Diag_frame, text="Unique Id Generated Is :"+str(temp_value3),fg='red',bg="yellow",font="comicsans 20 bold").grid(padx =25,pady=5)



First_name = Label(Right_frame, text="First Name  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=0, column=0, pady=5, sticky="w")
txtfirstname = Entry(Right_frame, font="comicsans 15 bold", bd=5,width=13, relief=GROOVE,textvariable=a1).grid(row=0,column=1, padx=20,sticky="w")

Last_name = Label(Right_frame, text="Last Name  :", bg="green", fg="white",
font="comicsans 17 bold").place(x=370,y=2)
txtfirstname = Entry(Right_frame, font="comicsans 15 bold", bd=5,width=13, relief=GROOVE,textvariable=a1).place(x=520,y=2)

Fathername = Label(Right_frame, text="Father's Name  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=1, column=0, sticky="w")
txtlastname = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,width =13,textvariable=a2).grid(row=1,column=1, padx=20,pady=5,sticky="w")

Mothername = Label(Right_frame, text="Mother Name:", bg="green", fg="white",font="comicsans 17 bold").place(x=370,y=50)
txtlastname = Entry(Right_frame, font="comicsans 15 bold", bd=5, relief=GROOVE,width =10,textvariable=a2).place(x=550,y=50)

Mobileno = Label(Right_frame, text="Mobile No.  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=2, column=0, sticky="w")
txtmobile = Entry(Right_frame, font="comicsans 15 bold",width=13, bd=5, relief=GROOVE,textvariable=a3).grid(row=2, column=1, padx=20,pady=5,sticky="w")

Email = Label(Right_frame, text="Email Id.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=3,column=0, sticky="w")
txtemail = Entry(Right_frame, font="comicsans 15 bold", bd=5,width=13, relief=GROOVE,textvariable=a4).grid(row=3, column=1, padx=20,pady=5,sticky="w")

Dateofbirth = Label(Right_frame, text="D. O. B.  :", bg="green", fg="white",font="comicsans 17 bold").grid(row=4, column=0, sticky="w")
txtdateofbirth = Entry(Right_frame, font="comicsans 15 bold", bd=5,width=13, relief=GROOVE,textvariable=a5).grid(row=4, column=1,padx=20,pady=5,sticky="w")

Class = Label(Right_frame, text="Class  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=5, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Right_frame, font="comicsans 14 bold",width=12, state="readonly")
Dropdown_gender['values'] = ("Play Way","L K G","U K G","Class - 1","Class - 2","Class - 3","Class - 4","Class - 5","Class - 6","Class - 7","Class - 8","Class - 9","Class - 10","Class - 12","Class - 12")
Dropdown_gender.grid(row=5, column=1, pady=5)


Gender = Label(Right_frame, text="Gender  :", bg="green", fg="white",
font="comicsans 17 bold").grid(row=6, column=0, sticky="w")
Dropdown_gender = ttk.Combobox(Right_frame, font="comicsans 14 bold",width=12, state="readonly")
Dropdown_gender['values'] = ("male", "female", "other")
Dropdown_gender.grid(row=6, column=1, pady=5)


Adress = Label(Right_frame, text="Adress  :", bg="green", fg="white",font="comicsans 15 bold").place(x=370,y=100)
txtqualification = Entry(Right_frame,width=13, font="comicsans 15 bold", bd=5, relief=GROOVE,).place(x=520,y=100)

Section = Label(Right_frame, text="Section  :", bg="green", fg="white",
font="comicsans 17 bold").place(x=370,y=150)
Dropdown_Section = ttk.Combobox(Right_frame, font="comicsans 14 bold",width=12, state="readonly")
Dropdown_Section['values'] = ("Sec.- A", "Sec.- B", "Sec.- C","Sec.- D")
Dropdown_Section.place(x=520,y=150)

Bus_No = Label(Right_frame, text="Bus No.  :", bg="green", fg="white",
font="comicsans 17 bold").place(x=370,y=200)
Dropdown_gender = ttk.Combobox(Right_frame, font="comicsans 14 bold",width=12, state="readonly")
Dropdown_gender['values'] = ("Bus No-1","Bus No-2","Bus No-3","Bus No-4","Bus No-5","Bus No-6","Bus No-7","Bus No-8","Bus No-9","Bus No-10",)
Dropdown_gender.place(x=520,y=200)

b13=Button(Right_frame,text="SUBMITT",bg='blue',command=Student_button,padx = 100,pady=20)
b13.place(x=150,y=450)




##################################################
#######################################################
#########################################################3#

def take_value():
    p1_monday_take = p1_monday_val.get()
    p2_monday_take = p2_monday_val.get()
    p3_monday_take = p3_monday_val.get()
    p4_monday_take = p4_monday_val.get()
    p5_monday_take = p5_monday_val.get()
    p6_monday_take = p6_monday_val.get()
    p7_monday_take = p7_monday_val.get()
    p8_monday_take = p8_monday_val.get()

    p1_tuesday_take = p1_tuesday_val.get()
    p2_tuesday_take = p2_tuesday_val.get()
    p3_tuesday_take = p3_tuesday_val.get()
    p4_tuesday_take = p4_tuesday_val.get()
    p5_tuesday_take = p5_tuesday_val.get()
    p6_tuesday_take = p6_tuesday_val.get()
    p7_tuesday_take = p7_tuesday_val.get()
    p8_tuesday_take = p8_tuesday_val.get()

    p1_wednesday_take = p1_wednesday_val.get()
    p2_wednesday_take = p2_wednesday_val.get()
    p3_wednesday_take = p3_wednesday_val.get()
    p4_wednesday_take = p4_wednesday_val.get()
    p5_wednesday_take = p5_wednesday_val.get()
    p6_wednesday_take = p6_wednesday_val.get()
    p7_wednesday_take = p7_wednesday_val.get()
    p8_wednesday_take = p8_wednesday_val.get()

    p1_thurshday_take = p1_thurshday_val.get()
    p2_thurshday_take = p2_thurshday_val.get()
    p3_thurshday_take = p3_thurshday_val.get()
    p4_thurshday_take = p4_thurshday_val.get()
    p5_thurshday_take = p5_thurshday_val.get()
    p6_thurshday_take = p6_thurshday_val.get()
    p7_thurshday_take = p7_thurshday_val.get()
    p8_thurshday_take = p8_thurshday_val.get()

    p1_friday_take = p1_friday_val.get()
    p2_friday_take = p2_friday_val.get()
    p3_friday_take = p3_friday_val.get()
    p4_friday_take = p4_friday_val.get()
    p5_friday_take = p5_friday_val.get()
    p6_friday_take = p6_friday_val.get()
    p7_friday_take = p7_friday_val.get()
    p8_friday_take = p8_friday_val.get()

    p1_saturday_take = p1_saturday_val.get()
    p2_saturday_take = p2_saturday_val.get()
    p3_saturday_take = p3_saturday_val.get()
    p4_saturday_take = p4_saturday_val.get()
    p5_saturday_take = p5_saturday_val.get()
    p6_saturday_take = p6_saturday_val.get()
    p7_saturday_take = p7_saturday_val.get()
    p8_saturday_take = p8_saturday_val.get()

    class_name_take = class_name.get()
    class_name_take1 = 'Class ' + class_name_take + '.txt'
    file_open = open(class_name_take1, 'x')
    file_open.write("\n\t\tMonday\t\t\tTuesday\t\t\t\tWednesday\t\t\t\tThurshday\t\t\t\tFriday\t\t\t\tSaturday\n")
    file_open.write(
        '\nPeriod 1\t' + p1_monday_take + '\t\t\t' + p1_tuesday_take + '\t\t\t\t' + p1_wednesday_take + '\t\t\t\t\t' + p1_thurshday_take + '\t\t\t\t\t' + p1_friday_take + '\t\t\t\t' + p1_saturday_take + '\n')
    file_open.write(
        '\nPeriod 2\t' + p2_monday_take + '\t\t\t' + p2_tuesday_take + '\t\t\t\t' + p2_wednesday_take + '\t\t\t\t\t' + p2_thurshday_take + '\t\t\t\t\t' + p2_friday_take + '\t\t\t\t' + p2_saturday_take + '\n')
    file_open.write(
        '\nPeriod 3\t' + p3_monday_take + '\t\t\t' + p3_tuesday_take + '\t\t\t\t' + p3_wednesday_take + '\t\t\t\t\t' + p3_thurshday_take + '\t\t\t\t\t' + p3_friday_take + '\t\t\t\t' + p3_saturday_take + '\n')
    file_open.write(
        '\nPeriod 4\t' + p4_monday_take + '\t\t\t' + p4_tuesday_take + '\t\t\t\t' + p4_wednesday_take + '\t\t\t\t\t' + p4_thurshday_take + '\t\t\t\t\t' + p4_friday_take + '\t\t\t\t' + p4_saturday_take + '\n')
    file_open.write(
        '\nPeriod 5\t' + p5_monday_take + '\t\t\t' + p5_tuesday_take + '\t\t\t\t' + p5_wednesday_take + '\t\t\t\t\t' + p5_thurshday_take + '\t\t\t\t\t' + p5_friday_take + '\t\t\t\t' + p5_saturday_take + '\n')
    file_open.write(
        '\nPeriod 6\t' + p6_monday_take + '\t\t\t' + p6_tuesday_take + '\t\t\t\t' + p6_wednesday_take + '\t\t\t\t\t' + p6_thurshday_take + '\t\t\t\t\t' + p6_friday_take + '\t\t\t\t' + p6_saturday_take + '\n')
    file_open.write(
        '\nPeriod 7\t' + p7_monday_take + '\t\t\t' + p7_tuesday_take + '\t\t\t\t' + p7_wednesday_take + '\t\t\t\t\t' + p7_thurshday_take + '\t\t\t\t\t' + p7_friday_take + '\t\t\t\t' + p7_saturday_take + '\n')
    file_open.write(
        '\nPeriod 8\t' + p8_monday_take + '\t\t\t' + p8_tuesday_take + '\t\t\t\t' + p8_wednesday_take + '\t\t\t\t\t' + p8_thurshday_take + '\t\t\t\t\t' + p8_friday_take + '\t\t\t\t' + p8_saturday_take + '\n')

    file_open.close()


##################################################################'''
class_name = StringVar()
p1_monday_val = StringVar()
p2_monday_val = StringVar()
p3_monday_val = StringVar()
p4_monday_val = StringVar()
p5_monday_val = StringVar()
p6_monday_val = StringVar()
p7_monday_val = StringVar()
p8_monday_val = StringVar()

p1_tuesday_val = StringVar()
p2_tuesday_val = StringVar()
p3_tuesday_val = StringVar()
p4_tuesday_val = StringVar()
p5_tuesday_val = StringVar()
p6_tuesday_val = StringVar()
p7_tuesday_val = StringVar()
p8_tuesday_val = StringVar()

p1_wednesday_val = StringVar()
p2_wednesday_val = StringVar()
p3_wednesday_val = StringVar()
p4_wednesday_val = StringVar()
p5_wednesday_val = StringVar()
p6_wednesday_val = StringVar()
p7_wednesday_val = StringVar()
p8_wednesday_val = StringVar()

p1_thurshday_val = StringVar()
p2_thurshday_val = StringVar()
p3_thurshday_val = StringVar()
p4_thurshday_val = StringVar()
p5_thurshday_val = StringVar()
p6_thurshday_val = StringVar()
p7_thurshday_val = StringVar()
p8_thurshday_val = StringVar()

p1_friday_val = StringVar()
p2_friday_val = StringVar()
p3_friday_val = StringVar()
p4_friday_val = StringVar()
p5_friday_val = StringVar()
p6_friday_val = StringVar()
p7_friday_val = StringVar()
p8_friday_val = StringVar()

p1_saturday_val = StringVar()
p2_saturday_val = StringVar()
p3_saturday_val = StringVar()
p4_saturday_val = StringVar()
p5_saturday_val = StringVar()
p6_saturday_val = StringVar()
p7_saturday_val = StringVar()
p8_saturday_val = StringVar()

##########################################################################
f1_timetable = Frame(page2, height=840, width=1530, bg="white").place(x=0,y=0)

l1_timetable = Label(page2, text="Enter Class :",bg="white", font=(20)).place(x=300, y=730)
e1_timetable = Entry(page2, width=6, bd=5, font=('15'), textvariable=class_name).place(x=450, y=730)
b1_timetable = Button(page2, width=15, height=2, text="Submit", bg='green', command=take_value).place(x=550, y=725)
########################################################################################################################################################

name_day1 = Label(page2, text='Monday', font=('COMICSANS 20 bold')).place(x=150, y=80)
name_day2 = Label(page2, text='Tuesday', font=('COMICSANS 20 bold')).place(x=350, y=80)
name_day3 = Label(page2, text='Wednesday', font=('COMICSANS 20 bold')).place(x=550, y=80)
name_day4 = Label(page2, text='Thurshday', font=('COMICSANS 20 bold')).place(x=800, y=80)
name_day5 = Label(page2, text='Friday', font=('COMICSANS 20 bold')).place(x=1050, y=80)
name_day6 = Label(page2, text='Saturday', font=('COMICSANS 20 bold')).place(x=1250, y=80)

#################################################################  PERIODS  #################################################################################################


l2_timetable = Label(page2, text="Period 1", font=(20)).place(x=21, y=150)

l3_timetable = Label(page2, text="Period 2", font=(20)).place(x=21, y=220)

l4_timetable = Label(page2, text="Period 3", font=(20)).place(x=21, y=290)

l5_timetable = Label(page2, text="Period 4", font=(20)).place(x=21, y=360)

l6_timetable = Label(page2, text="Period 5", font=(20)).place(x=21, y=430)

l7_timetable = Label(page2, text="Period 6", font=(20)).place(x=21, y=500)

l8_timetable = Label(page2, text="Period 7", font=(20)).place(x=21, y=570)

l9_timetable = Label(page2, text="Period 8", font=(20)).place(x=21, y=640)

#################################################################  SUBJECTS #################################################################################################
##################################################################  MONDAY  ######################################################################################

p1_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p1_monday_val).place(x=170, y=155)
p2_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p2_monday_val).place(x=170, y=220)
p3_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p3_monday_val).place(x=170, y=290)
p4_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p4_monday_val).place(x=170, y=365)
p5_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p5_monday_val).place(x=170, y=435)
p6_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p6_monday_val).place(x=170, y=505)
p7_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p7_monday_val).place(x=170, y=575)
p8_monday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p8_monday_val).place(x=170, y=645)

##################################################################  TUESDAY  ######################################################################################
p1_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p1_tuesday_val).place(x=380, y=155)
p2_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p2_tuesday_val).place(x=380, y=220)
p3_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p3_tuesday_val).place(x=380, y=290)
p4_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p4_tuesday_val).place(x=380, y=365)
p5_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p5_tuesday_val).place(x=380, y=435)
p6_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p6_tuesday_val).place(x=380, y=505)
p7_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p7_tuesday_val).place(x=380, y=575)
p8_tuesday = Spinbox(page2,
                     values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                     width=8, textvariable=p8_tuesday_val).place(x=380, y=645)

##################################################################  WEDNESDAY  ######################################################################################

p1_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p1_wednesday_val).place(x=590, y=155)
p2_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p2_wednesday_val).place(x=590, y=220)
p3_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p3_wednesday_val).place(x=590, y=290)
p4_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p4_wednesday_val).place(x=590, y=365)
p5_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p5_wednesday_val).place(x=590, y=435)
p6_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p6_wednesday_val).place(x=590, y=505)
p7_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p7_wednesday_val).place(x=590, y=575)
p8_wednesday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p8_wednesday_val).place(x=590, y=645)

##################################################################  THURHSDAY  ######################################################################################

p1_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p1_thurshday_val).place(x=830, y=155)
p2_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p2_thurshday_val).place(x=830, y=220)
p3_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p3_thurshday_val).place(x=830, y=290)
p4_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p4_thurshday_val).place(x=830, y=365)
p5_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p5_thurshday_val).place(x=830, y=435)
p6_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p6_thurshday_val).place(x=830, y=505)
p7_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p7_thurshday_val).place(x=830, y=575)
p8_thurshday = Spinbox(page2,
                       values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                       width=8, textvariable=p8_thurshday_val).place(x=830, y=645)

##################################################################  FRIDAY  ######################################################################################

p1_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p1_friday_val).place(x=1060, y=155)
p2_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p2_friday_val).place(x=1060, y=220)
p3_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p3_friday_val).place(x=1060, y=290)
p4_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p4_friday_val).place(x=1060, y=365)
p5_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p5_friday_val).place(x=1060, y=435)
p6_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p6_friday_val).place(x=1060, y=505)
p7_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p7_friday_val).place(x=1060, y=575)
p8_friday = Spinbox(page2,
                    values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                    width=8, textvariable=p8_friday_val).place(x=1060, y=645)

##################################################################  SATURDAY  ######################################################################################

p1_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p1_saturday_val).place(x=1270, y=155)
p2_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p2_saturday_val).place(x=1270, y=220)
p3_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p3_saturday_val).place(x=1270, y=290)
p4_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p4_saturday_val).place(x=1270, y=365)
p5_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p5_saturday_val).place(x=1270, y=435)
p6_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p6_saturday_val).place(x=1270, y=505)
p7_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p7_saturday_val).place(x=1270, y=575)
p8_saturday = Spinbox(page2,
                      values=("English", 'Hindi', 'Math', 'Science', 'S.S.T-', 'Drawing', 'G.K.', 'Games', 'Library'),
                      width=8, textvariable=p8_saturday_val).place(x=1270, y=645)

#####################################################
##########################################################
#######################Id card generator########################################



image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)


n1_id = StringVar()
n2_id=StringVar()
n3_id=StringVar()
n4_id=StringVar()
global t1_id
global view_id
def Card_Generator():
    t1_id = n1_id.get()
    t2_id = n2_id.get()
    t3_id = n3_id.get()
    t4_id = n4_id.get()
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
    global view_id
    view_id = t1_id+'.png'
    image.save(view_id)

    img = qrcode.make(t1_id)  # this info. is added in QR code, also add other things
    img.save('qrcode.bmp')

    til = Image.open(view_id)
    im = Image.open('qrcode.bmp')  # 25x25
    til.paste(im, (600, 550))
    til.save(view_id)

    img = ImageTk.PhotoImage(Image.open(view_id))
    img_label=Label(id_frame2,image=img)
    img_label.pack()
    root.mainloop()


l1_id1 = Label(id_frame1, text='Enter The Details', font='25', bg='red',bd=3,relief=GROOVE,fg="white").place(x=110,y=10)
Admission_no = Label(id_frame1, text="Admission no  :", bg="lime", fg="white",
font="comicsans 17 bold").place(x=10,y=50)
e1_id = Entry(id_frame1, textvariable=n1_id, font='20', width=10, bd=5).place(x=230, y=50)
b1_id = Button(id_frame1, text="GENERATE", fg='red',bg='yellow', padx=50, pady=7, command=Card_Generator).place(x=120, y=100)


id_label = Label(id_frame1,text="OR",font="comicsans 30 bold",bg="lime").place(x=150,y=170)

First_name_id = Label(id_frame1, text=" First Name :", bg="lime", fg="white",
font="comicsans 17 bold").place(x=10,y=250)
e1_id = Entry(id_frame1, textvariable=n2_id, font='20', width=12, bd=5).place(x=230, y=250)

Last_name_id = Label(id_frame1, text="Last Name :", bg="lime", fg="white",
font="comicsans 17 bold").place(x=10,y=300)
e1_id = Entry(id_frame1, textvariable=n3_id, font='20', width=12, bd=5).place(x=230, y=300)

Fathers_name = Label(id_frame1, text="Father Name :", bg="lime", fg="white",
font="comicsans 17 bold").place(x=10,y=350)
e1_id = Entry(id_frame1, textvariable=n4_id, font='20', width=12, bd=5).place(x=230, y=350)
b1_id = Button(id_frame1, text="GENERATE", bg='yellow', fg='red',padx=50, pady=20, command=Card_Generator).place(x=120, y=450)



b2_id = Button(page3, text = "PRINT ID ", font = "serif 30 italic",bg="yellow",bd="3",relief = RIDGE,padx=5,pady=5).place(x=1280,y=200)
b3_id = Button(page3, text = "PRINT NEW \n ID ", font = "serif 20 italic",bg="yellow",bd="3",relief = RIDGE,padx=10,pady=5).place(x=1280,y=400)



id_label = Label(id_frame2,text='admission.png').place(x=0,y=10)




####################################################################

jan = IntVar()
feb = IntVar()
march = IntVar()
april = IntVar()
may = IntVar()
june = IntVar()
july = IntVar()
august = IntVar()
sep = IntVar()
oct = IntVar()
nov = IntVar()
dec = IntVar()

# check buttons
jan = Checkbutton(frame2, text='Janurary', takefocus=0,bg="yellow").place(x=30, y=350)

feb = Checkbutton(frame2, text='February', takefocus=0,bg="purple").place(x=180, y=350)

mar = Checkbutton(frame2, text='March', takefocus=0,bg="orange").place(x=350, y=350)

apr = Checkbutton(frame2, text='April', takefocus=0,bg="blue").place(x=490, y=350)

may = Checkbutton(frame2, text='May', takefocus=0,bg="lime").place(x=630, y=350)

jun = Checkbutton(frame2, text='June', takefocus=0,bg="sky blue").place(x=750, y=350)

jul = Checkbutton(frame2, text='July', takefocus=0,bg="sky blue").place(x=30, y=400)

aug = Checkbutton(frame2, text='August', takefocus=0,bg="yellow").place(x=180, y=400)

sep = Checkbutton(frame2, text='September', takefocus=0,bg="orange").place(x=350, y=400)

october = Checkbutton(frame2, text='October', takefocus=0,bg="purple").place(x=490, y=400)

nov = Checkbutton(frame2, text='November', takefocus=0,bg="lime").place(x=630, y=400)

dec = Checkbutton(frame2, text='Decembr', takefocus=0,bg="blue").place(x=750, y=400)






root.mainloop()