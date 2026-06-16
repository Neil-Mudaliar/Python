#Create a function that checks if a number is prime and returns True or False.
num=int(input("Enter a number = "))
for i in range (2,num):
    if num%i==0:
        print("The number is not prime.")
        break
    else:
        print("The number is prime.")
        break
