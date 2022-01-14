print("Ques1")
number_1 = int(input("enter first number:"))
number_2 = int(input("enter second number:"))
number_3 = int(input("enter third number:"))
average = (number_1+number_2+number_3)/3
print(average)

print()
print()

print("Ques2")
# gross_income = a ,   dependents=b, standard deduction=c , dependent deduction= d
a = float(input("enter the gross income:"))

c = 10000
b = int(input("enter the no. of dependents:"))

d = 3000
taxable_income = a-c-(d * b)
print("taxable income")
print(taxable_income)
tax = (taxable_income*20)/100
print("tax")
print(tax)

print()
print()

print("Ques3")
name = input("enter student name:")
sid = input("enter student sid:")
gender = input("enter student gender:")
course_name = input("enter the students course:")
cgpa = float(input("enter the student cgpa:"))
data = [name, sid, gender, course_name, cgpa]
print(data)

print()
print()

print("Ques4")
Marks_1 = int(input("enter marks of student 1:"))
Marks_2 = int(input("enter marks of student 2:"))
Marks_3 = int(input("enter marks of student 3:"))
Marks_4 = int(input("enter marks of student 4:"))
Marks_5 = int(input("enter marks of student 5:"))

Marks_list = [Marks_1, Marks_2, Marks_3, Marks_4, Marks_5]
Marks_list.sort()
print(Marks_list)

print()
print()

print("Ques5")
print("A part")
List_color = ['Red','Green','White','Black','Pink','Yellow']
del List_color[3]
print(List_color)

print()
print("B part")
List_color=['Red','Green','White','Black','Pink','Yellow']
List_color[3]=List_color[4]='purple'
print(List_color)
