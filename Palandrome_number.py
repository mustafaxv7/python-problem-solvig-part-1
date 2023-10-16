#A program to check if a Number is palandrome or not
def inverse(number):
    inversed_number = 0
    while number != 0:
        inversed_number = (inversed_number * 10) + (number % 10)
        number = number // 10
    return inversed_number

def isPalandrome(number):
    if (number == inverse(number)):
        return True
    else: return False

number = int(input("\nNumber>>: "))
if isPalandrome(number):
    print(f"\n{number} is Palandrom\n")
else:
    print(f"\n{number} is Non Palandrom\n")