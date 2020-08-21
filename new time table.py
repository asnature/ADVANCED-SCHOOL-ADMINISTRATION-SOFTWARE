from tkinter import *

root = Tk()
root.geometry("1530x840")
root.title("Time Table")


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
    class_name_take1 = 'Class' + class_name_take + '.txt'
    file_open = open(class_name_take1, 'w')
    file_open.write("\t\t\t Monday")
    file_open.write("\t\t\t tuesdsy")
    file_open.write("\t\t\t wednesday   ")
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
f1_timetable = Frame(root, height=840, width=1530, bg="red").pack()

l1_timetable = Label(root, text="Enter Class", font=(20)).place(x=350, y=730)
e1_timetable = Entry(root, width=3, bd=5, font=('15'), textvariable=class_name).place(x=490, y=730)
b1_timetable = Button(root, width=15, height=3, text="Submit", bg='green',command=take_value).place(x=550, y=730)
########################################################################################################################################################

name_day1 = Label(root, text='Monday', font=('COMICSANS 20 bold')).place(x=150, y=80)
name_day2 = Label(root, text='Tuesday', font=('COMICSANS 20 bold')).place(x=350, y=80)
name_day3 = Label(root, text='Wednesday', font=('COMICSANS 20 bold')).place(x=550, y=80)
name_day4 = Label(root, text='Thurshday', font=('COMICSANS 20 bold')).place(x=800, y=80)
name_day5 = Label(root, text='Friday', font=('COMICSANS 20 bold')).place(x=1050, y=80)
name_day6 = Label(root, text='Saturday', font=('COMICSANS 20 bold')).place(x=1250, y=80)

#################################################################  PERIODS  #################################################################################################


l2_timetable = Label(root, text="Period 1", font=(20)).place(x=21, y=150)

l3_timetable = Label(root, text="Period 2", font=(20)).place(x=21, y=220)

l4_timetable = Label(root, text="Period 3", font=(20)).place(x=21, y=290)

l5_timetable = Label(root, text="Period 4", font=(20)).place(x=21, y=360)

l6_timetable = Label(root, text="Period 5", font=(20)).place(x=21, y=430)

l7_timetable = Label(root, text="Period 6", font=(20)).place(x=21, y=500)

l8_timetable = Label(root, text="Period 7", font=(20)).place(x=21, y=570)

l9_timetable = Label(root, text="Period 8", font=(20)).place(x=21, y=640)

#################################################################  SUBJECTS #################################################################################################
##################################################################  MONDAY  ######################################################################################

p1_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p1_monday_val).place(x=170, y=155)
p2_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p2_monday_val).place(x=170, y=220)
p3_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p3_monday_val).place(x=170, y=290)
p4_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p4_monday_val).place(x=170, y=365)
p5_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p5_monday_val).place(x=170, y=435)
p6_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p6_monday_val).place(x=170, y=505)
p7_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p7_monday_val).place(x=170, y=575)
p8_monday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p8_monday_val).place(x=170, y=645)

##################################################################  TUESDAY  ######################################################################################
p1_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p1_tuesday_val).place(x=380, y=155)
p2_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p2_tuesday_val).place(x=380, y=220)
p3_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p3_tuesday_val).place(x=380, y=290)
p4_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p4_tuesday_val).place(x=380, y=365)
p5_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p5_tuesday_val).place(x=380, y=435)
p6_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p6_tuesday_val).place(x=380, y=505)
p7_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p7_tuesday_val).place(x=380, y=575)
p8_tuesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                     textvariable=p8_tuesday_val).place(x=380, y=645)

##################################################################  WEDNESDAY  ######################################################################################

p1_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p1_wednesday_val).place(x=590, y=155)
p2_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p2_wednesday_val).place(x=590, y=220)
p3_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p3_wednesday_val).place(x=590, y=290)
p4_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p4_wednesday_val).place(x=590, y=365)
p5_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p5_wednesday_val).place(x=590, y=435)
p6_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p6_wednesday_val).place(x=590, y=505)
p7_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p7_wednesday_val).place(x=590, y=575)
p8_wednesday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p8_wednesday_val).place(x=590, y=645)

##################################################################  THURHSDAY  ######################################################################################

p1_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p1_thurshday_val).place(x=830, y=155)
p2_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p2_thurshday_val).place(x=830, y=220)
p3_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p3_thurshday_val).place(x=830, y=290)
p4_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p4_thurshday_val).place(x=830, y=365)
p5_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p5_thurshday_val).place(x=830, y=435)
p6_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p6_thurshday_val).place(x=830, y=505)
p7_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p7_thurshday_val).place(x=830, y=575)
p8_thurshday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                       textvariable=p8_thurshday_val).place(x=830, y=645)

##################################################################  FRIDAY  ######################################################################################

p1_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p1_friday_val).place(x=1060, y=155)
p2_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p2_friday_val).place(x=1060, y=220)
p3_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p3_friday_val).place(x=1060, y=290)
p4_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p4_friday_val).place(x=1060, y=365)
p5_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p5_friday_val).place(x=1060, y=435)
p6_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p6_friday_val).place(x=1060, y=505)
p7_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p7_friday_val).place(x=1060, y=575)
p8_friday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                    textvariable=p8_friday_val).place(x=1060, y=645)

##################################################################  SATURDAY  ######################################################################################

p1_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p1_saturday_val).place(x=1270, y=155)
p2_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p2_saturday_val).place(x=1270, y=220)
p3_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p3_saturday_val).place(x=1270, y=290)
p4_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p4_saturday_val).place(x=1270, y=365)
p5_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p5_saturday_val).place(x=1270, y=435)
p6_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p6_saturday_val).place(x=1270, y=505)
p7_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p7_saturday_val).place(x=1270, y=575)
p8_saturday = Spinbox(root, values=(
"English", 'Hindi', 'Math', 'Science', 'Social Science', 'Drawing', 'G.K.', 'Games', 'Library'), width=8,
                      textvariable=p8_saturday_val).place(x=1270, y=645)

root.mainloop()