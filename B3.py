#Write a program that prints the multiplication table for any number the user enters (1 to 12).
num = int(input("Enter a number between 1 and 12 = "))
if num<=12 and num>=1:
    for i in range (1,10):
        terms=num*i
        print(f"num * {i} = {terms}")
