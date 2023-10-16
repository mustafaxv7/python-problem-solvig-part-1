# In This Programm We Calcule The Number Of Digits In An Integer 
number = int(input("\nNumber>>: "))
number_of_digits = 0

#The Esay Way
# for i in str(number):
    # number_of_digits+=1
# print(f"\nThe Number Of Digits is: {number_of_digits}\n")

#The Hard Way
while number != 0:
    number = number // 10
    number_of_digits+=1
print(f"\nThe Number Of Digits is: {number_of_digits}\n")    