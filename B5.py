#Write a program that counts how many vowels are in a string entered by the user.
sentence = str(input("Enter a sentence or a word = "))
if sentence.count("a")>0:
    print("The number of time a has occured is ",sentence.count("a"))
else:
    print("There is no a in the sentence.")