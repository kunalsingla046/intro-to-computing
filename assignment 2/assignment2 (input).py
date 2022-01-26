print("ques 1")
given_string ='Python is a case sensitive challenge'
print("a part")
print("length of given string is %s" % len(given_string))
print("b part")
print("reversed string order is %s" % given_string[::-1])
print("c part")
New_String = given_string[12:26]
print("new string is %s" % New_String)
print("d part")
string_replaced = given_string.replace("case sensitive", "object oriented")
print("the part of string replaced is %s" % string_replaced)
print("e part")
substring = "a"
# finding "a" when it first occurred in substring
print("index of substring  is %s" % given_string.find(substring))
print("f part")
print("string without space is %s" % given_string.replace(" ",""))

print()
print()

print("ques 2")
name = 'kunal singla'
sid = 21104046
department_name = 'EE'
cgpa=9.8

print("Hey,%s here!"%name)
print("my sid is %s"%sid)
print("I am from %s department and my cgpa is %s " %(department_name,cgpa))

print()
print()

print("ques 3")
a=56
b=10
print("a part:")
print("a & b = %s" % (a&b))
print("b part:")
print("a | b = %s"%(a|b))
print("c part:")
print("a ^ b = %s"%(a^b))
print("d part:")
print("Left shifting a and b with 2 bits: a = %s b = %s"%(a<<2,b<<2))
print("e part:")
print("Right shifting a with 2 bits and b with 4 bits: a = %s b = %s"%(a<<2,b<<4))

print()
print()

print("ques 4")
# let a, b ,c be the three number entered by user
a = input("enter the first number")
b = input("enter the second number")
c = input("enter the third number")
if (a==b==c) :
    print("The greatest number is %s" % a)
elif (a>=b) :
    if a>c :
        print("The greatest number %s"% a)
    else :
        print("The greatest number is %s"% c)
elif (b>=c) :
    if (b>c) :
        print("The greatest number is %s" % b)
    else :
        print("The greatest number is %s" % c)

print()
print()

print("ques 5")
String = input("enter the desired string:")
if "name" in String:
    print("yes")
else:
    print("no")

print()
print()

print("ques6")
# let a,b,c be the length of sides of triangle

a = int(input("Enter the length of first side:"))
b = int(input("Enter the length of second side:"))
c = int(input("Enter the length third side:"))
if a+b>c and b+c>a and a+c>b:
    print("yes")
else:
    print("no")
