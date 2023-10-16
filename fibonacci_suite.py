while True:
    n = int(input("Enter n >>: "))
    if n >= 2:
        break
a = 0
b = 1
print("\nU0 = 0\n\nU1 = 1\n")
for i in range(2,n+1):
    un = b + a
    a = b
    b = un
    print(f"U{i} = {un}\n")
