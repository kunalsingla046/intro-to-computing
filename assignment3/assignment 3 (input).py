print("ques 1")
string_user= input("Enter The desired string:")
string= string_user.split()
string_count=len(string)

dict={}
if  string_count == 1:                     # ONLY FOR ONE WORD
    for i in string[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:                                  # FOR MORE THAN TWO WORDS
    for i in string:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)

print()
print()

print("ques 2")

# let a= month with 30 days and b= month with 31 days

a = [4, 6, 9, 11]
b = [1, 3, 5, 7, 8, 10, 12]
def input_date():
    global day
    global month
    global year
    day = int(input("Please Enter The Day: "))
    month = int(input("Please Enter The Month: "))
    year = int(input("Please Enter The Year: "))
    
    #conditions given
    if year>2025 or year<1800 or month<1 or month>12 or day<1 or day>31: 
        print("invalid! please enter valid year between 1800 and 2025")
        
    if day > 28 and month == 2 and year%4 != 0: 
        print("invalid! enter valid date")
        input_date()
        
        #testing if date is in calender 
    elif ((day > 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)): 
        print("invalid! enter valid date")
        input_date()
        
    elif day > 30 and month in a: 
        print("invalid! enter valid date")
        input_date()
input_date()
#Feburary month not in leap year.
if day == 28 and month == 2 and year%4 != 0: 
    day = 1
    month = 3
    #Feburary month in leap year.
elif ((day == 28 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)): 
    day += 1
elif ((day == 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day = 1
    month = 3
    #For the end dates of month having 30 days.
elif day == 30 and month in a:  
    day = 1
    month += 1
    #For the end dates of month having 31 days.
elif day == 31: 
    day = 1
    month += 1
else:   # end of the year
    day += 1
if month == 13:
    month = 1
    year += 1
print(f"Next date is {day}/{month}/{year}")

print()
print()

print("ques 3")

user_list = list(map(int, input("Enter a list of numbers: ").split()))
#list_output is the list printed with squaring
list_output = [(user_list[i], user_list[i]**2) 
               for i in range(len(user_list))]

print(list_output)

print()
print()

print("ques 4")

# let grade_points= a
a = int(input(" enter your grade point:"))

if 4<= a <= 10:
    if a==4:
        grade, performance = "D","Poor"
    elif a == 5:
        grade,performance = 'C',"Below Average"
    elif a == 6:
        grade,performance = 'C+','Average'
    elif a == 7:
        grade,performance = 'B','Good'
    elif a == 8:
        grade,performance = 'B+','Very Good'
    elif a == 9:
        grade,performance = 'A','Excellent'
    else:
        grade,performance = 'A+','Outstanding'
        
    print("your grade is %s and %s performance "%(grade,performance))
else:
    print("error")

print()
print()

print("ques 5")
string= "ABCDEFGHIJK"

a=len(string)

for n in range(6):
     sequence = string[0:a-int(n)*2]
     
     print(" "*n + sequence )

print()
print()

print("ques 6")


student_name = input("enter your name:").upper()
SID=int(input("Enter your sid:"))

student_details={SID:student_name}

while True:
    preference= input("Do you want other student details(Y or N)").upper()
    if preference == "Y":
        student_name = input("enter your name:").upper()
        SID=int(input("Enter your sid:"))
        student_details[SID]=student_name
        
    elif preference == "N":
        break
    else:
        print("ERROR")
        
print("a part")
print(f"details stored in dictionary are {student_details}\n")

print("b part ")
final_name ={k:v for k,v in sorted(student_details.items(), key= lambda x:x[1])} #final_name = sorted name
print(f"the sorted dictionary is {final_name}\n")

print("c part")
sorted_sid=sorted((student_details.items()))
print(f"sorting done according to{sorted_sid}\n")

print("d part")
search= int(input("Enter the student sid to search"))
details = student_details[search]
print(f"the students details you want to search is {details}")

print()
print()

print("ques 7")
a=0
b=1
c=0
sum=a+b
terms= int(input("enter the numberof terms of fibonacci series:"))
print(a)
print(b)

for c in range(terms-2):
    c=a+b # C IS THE SUM OF PREVIOUS TWO TERMS
    sum += c
    print(c)
    
    a=b
    b=c
    avg=sum/terms
print(f"the average of the series is {avg}")

print()
print()

print("ques 8")
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
print("a part.")
set4 = (set1|set2)-(set1&set2)
print(set4)
print("b part.")
set5 = (set1|set2|set3)-((set1&set2)|(set2&set3)|(set1&set3))
print(set5)
print("c part.")
set6 = ((set1&set2)|(set2&set3)|(set1&set3))-(set1&set2&set3)
print(set6)
print("d part.")
set_integer = {1,2,3,4,5,6,7,8,9,10}
set7 = (set_integer-set1)
print(set7)
print("e part.")
set8 = (set_integer-(set1|set2|set3))
print(set8)
