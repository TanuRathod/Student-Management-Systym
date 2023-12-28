###### STUDENT MANAGEMENT SYSTYM ######
class Student:
    def __init__(self,r,n,m):
        self.rn = r
        self.name = n
        self.marks = m

    def __str__(self):
        return f"Rn={self.rn},Name={self.name},Marks={self.marks}"


Student_list =[]
while True:      
    ch = int(input("\n\nEnter Choice: \n1. Add Student \t\t2. Show Student \n3. Update Student \t4. Delete Student  \n5. Exit:"))
    match ch:
        case 1:
            print("Add Student")
            r = int(input("Enter Roll Number:"))
            n = input("Enter Name:")
            m = int(input("Enter Marks:"))
            S3 = Student(r,n,m)
            Student_list.append(S3)
            print("Student Added Successfully")
            
        case 2:
            print("\nShow All Students")
            for stu in Student_list:
                print(stu)

        case 3:
            print("\nUPDATE STUDENT")
            r=int(input("Enter the Roll No to Update:"))
            for stu in Student_list:
                if stu.rn==r:
                    while 1:
                        ch=int(input("\nEnter the Update Choice \n1. Update Marks \t\t2. Update Name \n3. Exit :"))
                        if ch==1:
                            stu.marks=float(input("Enter the updated Marks:"))
                        elif ch==2:
                            stu.name=input("Enter the Updated Name:")
                        elif ch==3:
                            break
        case 4:
            print("\nDELETE STUDENT....")
            r = int(input("Enter Roll No to Delete:"))
            found = False

            for stu in Student_list:
                if stu.rn == r:
                    found = True
                    student_to_be_removed = stu
                    break
            if found:
                Student_list.remove(student_to_be_removed)
                print(student_to_be_removed,"REMOVED SUCCESSFULLY")

            else:
                print("Nooo.....NOT SUCH FOUND")
            
        case 5:
             print("EXITING .......")
        case _:
              print("INVALID CHOICE......")
print("\nPROGRAM ENDS")

          
