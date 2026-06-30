#Write a function that removes all duplicates from a list and returns the unique elements.
num = []
while True :
    el = int(input("ENter a number for list (0 to terminate) = "))
    if el==0 :
        print("Terminated")
        break
    else :
        num.append(el)
new_num = set(num)
num2 = list(new_num)
print(num2)