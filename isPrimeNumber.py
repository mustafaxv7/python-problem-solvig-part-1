#This program define if a number is prime or not
def isPrimeNumber(number):
    isPrime = True
    if number == 0:
        isPrime = False
    for i in range(2,int(number/2)+1):
        if number%i == 0 :
            isPrime = False
            break
    return isPrime

number = int(input("Enter a Number >>: "))
if isPrimeNumber(number):
    print(f"{number} is Prime")
else:
    print(f"{number} is Non Prime")




            