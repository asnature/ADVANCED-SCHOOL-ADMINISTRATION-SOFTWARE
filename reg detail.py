def new_registration():
    V1 = open('regg_number.txt',"r")
    V2 = V1.read(1)
    V1.close()
    V1 = open('regg_number.txt',"w")
    V2 = int(V2)
    V3 = V2
    V2 = V2 + 1
    V2 = str(V2)
    V1.write(V2)
    V1.close()



    First_name = input("Enter the first name:")
    Last_name = input("Enter the last name:")
    Mobile_no = int(input("Enter the mobile no:"))
    Email = input("Enter the email id:")
    Gender = input("Enter the gemder:")
    Specilisation = input("Enter the specialisation:")

    V4 = str(V3)
    Record_file_name = V4 + ".txt"
    Teacher_details = open(Record_file_name,"x")
    Teacher_details.close()
    Teacher_details = open(Record_file_name,"a")
    Teacher_details.write("First_name:" + First_name)
    Teacher_details.write("\nLast_name:"+ Last_name)
    Teacher_details.write("\nMobile_no:"+ str(Mobile_no))
    Teacher_details.write("\nEmail:"+ Email)
    Teacher_details.write("\nGender:" + Gender)
    Teacher_details.write("\nSpecilisation:" + Specilisation)
    Teacher_details.write("Teacher id is:"+V4)
    Teacher_details.close()
    print("Teacher Id for this detail is :" + V4)



def Old_registration_details():
    V1 = input("Enter the Teacher Id:")
    V2 = V1 + ".txt"
    V3 = open(V2,"r")

    for i in V3.readlines():
        print(i)


x = int(input("Press 1 for new registration & 2 for previous records:---"))
if (x==1):
    new_registration()
elif(x==2):
    Old_registration_details()
else:
    print("please enter the valid choice:")







