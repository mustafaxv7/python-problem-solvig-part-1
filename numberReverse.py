#This Program Inverse Any Number You Give it
def inverse(number):
    inversed_number = 0
    while number != 0:
        inversed_number = (inversed_number * 10) + (number % 10)
        number = number // 10
    return inversed_number
    
number = int(input("Number>>: "))
print(f"The Inverse of This Number is : {inverse(number)}")
        
