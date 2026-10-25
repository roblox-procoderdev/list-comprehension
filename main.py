num=input("enter some numbers: ")
list1=[int(n) for n in num.split()]
oddlist=[int(digit) for digit in str(num) if int(digit) % 2 != 0]
print("given number = ",*list1)
print("odd digits = ",*oddlist)
fruit=input("enter some fruit: ")
fruit_list=fruit.split()
capitalized_words = [word.capitalize() for word in fruit_list if word]
print(*capitalized_words)