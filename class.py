'''
A=input('what is your name?')
B=input('whAat is your age?')
print('my name is ',A)
print('my age is',B)

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#simple interest
p=int(input('enter a principle?'))
T=int(input('enter a time: '))
R=int(input('enter a rate: '))
i=p*T*R/100
print ("\n  The simple intrest is ",i)


#odd or even
a=int(input("enter a number: "))
if( a%2 == 0):
    print("even",a)
else:
    print("odd",a)

#maximum number between two umbers
a=int(input("enter a first number"))
b=int(input("enter a second number"))

if (a<b):
    print(b,"is maximum number")
else:
    print(a,"is maximum number")
    

 #even num upto 50 
for num in range(1, 50 + 1):
         
    if num % 2 == 0:
        print(num, end = " ")


for i in range(1, 80 , 4):
    print(i)

n = int(input("enter n: "))

print(", ".join([str(n) for n in range(1, n, 4)]))

import random
n = random.randint(5,30)
print(n)
'''
'''
result= int(input("enter your percentage: "))
if result>=70 :
    print("your result is first class")
elif result>=60 and result <70:
    print("upper second claass")
elif result>=50 and result <60:
    print("lower second class")
elif result>=40 and result <50 : 
    print("thiors class")
else:
    print("failed")

choice=2 
switch(choice){
    case 1:print("hello")
        break
    case 2:print("h1")
        break
    default:print ("out of range")
    }

choice=input("enter your choice")
match choice:
    case "1":print("hello")
    case "2":print("hi")
    #case default :print("out of range")
    case _:print("out of range")


#math
a=int(input('Enter First Number: '))
b=int(input('Enter Second Number: '))

while True:

    print('   1.Addition\n   2.Subtraction\n   3.Multiplication\n   4.Division\n   5.Exit')

    print('-------------------------------------------------------------------')

    ch=int(input('Enter your choice from 1 to 4 for Arithmetic Opeations: '))   

    if ch==1:

            print("The sum of two number  is ",a+b)   

    elif ch==2:

            print('The subtraction of two number is ',a-b)

    elif ch==3:

            print('The Multiplication of two number is ',a*b)      

    elif ch==4:

            print('The Division of two number is ',a/b)

    elif ch==5:

            break

    else:

        print('Please enter the value from 1 to 4')

    ans=input('Do you want to Continue Again(Y/N)')

    if ans.upper()=='Y':

        continue

    else:

        break


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
while True:
    hehe=int(input("select the operation \n1.add\n2.sub\n3.multi\n4.div\n5.exit: "))
    x=float(input("Enter the value of x: "))
    y=float(input("Enter the value of y: "))

    match(hehe):
        case 1:print(x,"+",y,"=",add(x,y))

        case 2:
            print(x,"-",y,"=" ,sub(x,y))

        case 3:print(x,"*",y,"=",mult(x,y))

        case 4:
            print(x,"/",y,"=",div(x,y))
        case 5:
            break
        case _:
            print("Invalid input 🙂")
    g=input("do you want to continue(y/n): ")
    if(g.lower()=='y'):
        continue
    else:
        break
f=open ("info.txt","w")
f.write("\nseweey\n")
f.write("cr\n")
f.close()
f=open("info.txt","r")
for each in f:
    print(each)

#1. wap th enter your name, age, gender, adderes, contact and email address in the file "info.txt" and display only name and email address.
f=open ("info.txt","w")
f.write ("name=alish \n gender=male \n address=siddhipur \n contact= \n gmail.com \n")
f.close()
f=open("info.txt","r")
lines= f.readlines()
for line in lines:
    if "name=alish" in line or "gmail.com" in line :
        print(line.strip())
    '''

#2. wap to enter name, occupation and address for 10 employes and display all the records.
f=open ("em.txt","w")
for i in range (10):
    name=input("\nenter a name{}:".format(i+1))
    occupation=input("enter a occupation{}: ".format(i+1))
    address=input("enter a address{}:".format(i+1))
    
    f.write("Name: {}\n Occupation: {}\n Address: {}\n".format(name, occupation, address))

f=open("em.txt","r")
contents=f.read()
print(contents)
#3. wap to create a respository or directory.
#4. wap to rename an existing directory.
#5. wap to delete the directory.

