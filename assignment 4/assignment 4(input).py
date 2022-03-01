print("ques 1")

def TOWEROFHANOI(n,start_position,end_position,helper):        #start_position=source, end_position= final destination

    # Base Case
    if n==0:
        return
# Firstly moving n-1 disc to B using C
    TOWEROFHANOI(n-1,start_position,helper,end_position)

# Moving top disc from A to C
    print(f"Move disc {n} from {start_position} to {end_position}")

# Moving n-1 disc from B TO C Using A
    TOWEROFHANOI(n-1,helper,end_position,start_position)

# calling Function For 3 Disc
TOWEROFHANOI(3,'A','C','B')
print()
print()

print("ques 2")

#asking for no. of rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

print("using recursions")

def pascal_triangle(n, original_n=n):
    if n == 0:
        return
    
    pascal_triangle(n-1,original_n)

    print('  '*(original_n-n), end='')       #print the spaces

    #first number is always 1
    count = 1
    for i in range(1, n+1):

        print(count, end ='   ')
        count = count * (n - i) // i     #use of Binomial Coefficient
    print()
pascal_triangle(n)

print("using iteratives")
for j in range(1, n+1):

    #all same as recursion
    print('  '*(n - j), end='')

    x = 1
    for i in range(1, j+1):

        print(x, end='   ')

        x = x * (j - i) // i
    print()
    

print("\nques 3")

num1=int(input("Enter the first no.:"))
while True:
    num2=int(input("enter the second no.:"))
#let a= quotient, b=remainder
    if num2!=0:
        break
    else:
        print("num 2 can't be 0 ; Enter again")

a,b=divmod(num1,num2)
print(f"the quotient is {a} and remainder is {b}\n")

print("a part") # checking callability
c=callable(divmod)
print(c,end="")
if c== True:
    print(";function is callable")
else:
    print(";function is not callable")
print()

print("b part")
if b==0:
    print("remainder is zero")
else:
    print("remainder is non zero")
if a==0:
    print("quotient is zero")
else:
    print("quotient is non zero")
print()
print("c part")

new = (a , b) + (4, 5, 6)
result = []
for i in range(len(new)):
    if new[i] > 4:
         result.append(new[i])
print(f" Filtered out numbers greater than 4: {result}")
print()

print("d part")
result_set=set(result)
print(f"the set is {result_set}")
print()

print("e part")
set_immutable=frozenset(result_set)
print(f"the immutable set is {set_immutable}")
print()

print("f part")
#let c=maximum value of set
c=max(set_immutable)
#d=hash value
d=hash(c)
print(f"the hash value of the max value from above set is {d}")
   
print()
print()

print("ques 4")

class student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def __del__(self):
        print("Object destroyed")
        
Student_1=student("Kunal Singla",21104046)     # Creating the object
print("Object created\n")
print(f"Name of Student is {Student_1.name} and Roll Number is {Student_1.roll_number}\n")

 # deleting object
del Student_1
print()
print()

print("ques 5")

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#creating employee records
employee_1 = employee("Mehak", 40000)
employee_2 = employee("Ashok", 50000)
employee_3 = employee("Viren", 60000)

print("part a")
employee_1.salary = 70000
print(f"The updated salary of the employee {employee_1.name} is {employee_1.salary}")

print("part b")
del employee_3
print("the record of viren is deleted")
print()
print()

print("ques 6")

word = input("Enter the first word: ").lower()

#asking for a meaningful word with the exact same letters
test_word = input("Enter a new meaningful word to test your friendship: ")

#defining dictionary 
def count_in_dictionary(word):
    count = {}
    list_1 = list(word)
    
    n = len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]] += 1
        else:
            count[list_1[i]] = 1
    return count

# verifying the letters of the new word
if count_in_dictionary(word) != count_in_dictionary(test_word):
    print("The letters aren't exact,so friendship is fake!")

#shopkeeper's input to verify the word's meaning
def user_input():
    ans = input("{For the Shopkeeper}\nDoes the word makes sense?(y or n)").lower()

    if ans == 'y':
        print("The friends passed the friendship test!")
    elif ans == 'n':
        print("The word doesn't have a meaning, so friendship is fake!")
    else:
        print("ERROR, try again")
        user_input()
user_input()
