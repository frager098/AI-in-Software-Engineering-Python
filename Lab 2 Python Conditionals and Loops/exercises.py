# LAB EXERCISES
# Exercise 1:
# (I)Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes 
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth
# After calculating volume of cube, compare it with following ranges and print the relevant label:
# Volume Range Label
# 1 cm3 – 10 cm3 Extra Small
# 11 cm3 – 25 cm3 Small
# 26 cm3 – 75 cm3 Medium
# 76 cm3 – 100 cm3 Large
# 101 cm3 – 250 cm3 Extra Large
# 251 cm3 and above Extra-Extra Large
def calcVol():
    height  = int(input("Enter Height of the Cube:"))
    width = int(input("Enter width of the Cube:"))
    depth  = int(input("Enter depth of the Cube:"))
    volume = height * width * depth 
    return volume
# volume = calcVol()
# print("Volume of the cube is:" , volume , "cm3")
    
# (II)In a company ,worker efficiency is determined on the basis of the time required for a worker 
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker 
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker 
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to 
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas 
# to leave the company, If the time taken by the worker is input through the keyboard,find the 
# efficiency of the worker.
def workerEfficiency():
    timeTaken = float(input("Enter the time taken (in hours) to complete the job: "))

    if 2 <= timeTaken < 3:
        print("The worker is highly efficient.")
    elif 3 <= timeTaken < 4:
        print("The worker is ordered to improve speed.")
    elif 4 <= timeTaken <= 5:
        print("The worker is given training to improve speed.")
    else :
        print("The worker has to leave the company.")
        
   

# workerEfficiency()
# (iii)The program must prompt the user for a username and password. The program should 
# compare the password given by the user to a known password. If the password matches, the 
# program should display “Welcome!” If it doesn’t match, the program should display “I don’t 
# know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$12
# Function to check password
def checkPassword():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checking password (case insensitive)
    if password.lower() == "abc$123":
        print("Welcome!")
        return True
    else:
        print("I don't know you.")
        return False
# checkPassword()

# Exercise 2:
# (i)What Would Python Print?
#n = 3
#while n >= 0:
#n -= 1
#print(n)

# (ii): What Would Python Print?
# n = 4
# while n > 0:
#     n += 1
#     print(n)

# Make sure your while loop condition eventually becomes false, or it'll never stop!
# (ii)Try the scenrio below:
# Make a program that lists the countries in the set
# clist = ['Canada','USA','Mexico','Australia']

def initializeList():
    cList = []
    n = 1
    while(n < 4):
        listElem = input("Enter Country:")
        cList.append(listElem)
        n += 1 
    return cList
# cList = initializeList()
# print(cList)

# 1. Create a loop that counts from 0 to 100
# 2. Make a multiplication table using a loop
# 3. Output the numbers 1 to 10 backwards using a loop
# 4. Create a loop that counts all even numbers to 10
# 5. Create a loop that sums the numbers from 100 to 200
# for i in range( 1 , 101):
#     print(i)

def multiplicationTable(multiplicand):
    for i in range (1 , 11 ):
        print(multiplicand * i) 

# multiplicand = int ( input ("Enter which Multiplication Table you want?") )
# multiplicationTable(multiplicand)
# i = 10
# while ( i > 0 ):
#     print(i)
#     i -= 1

# print("Even numbers from 1 to 10:")
# count = 0 
# for i in range(0, 11, 2):  # Start from 2, go up to 10, step by 2
#     if( i % 2 == 0 ):
#         count += 1 
# print(count)

sum = 0 
for i in range ( 100 , 201 ):
    sum += i 
print(sum)