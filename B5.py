#Write a program that counts how many vowels are in a string entered by the user.
sentence = str(input("Enter a sentence ="))
num1 = sentence.count("a")
num2 = sentence.count("e")
num3 = sentence.count("i")
num4 = sentence.count("o")
num5 = sentence.count("u")
num = num1 + num2 + num3 + num4 + num5
if num>0:
    print("Total number of vowels in the sentence are ",num)
else:
    print("There are no vowels in the sentence")