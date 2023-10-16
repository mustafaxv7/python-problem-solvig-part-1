number_of_seconds = int(input("Enter The Number of Seconds >>: "))
h = number_of_seconds//3600
m = (number_of_seconds % 3600)//60
s = number_of_seconds - ((h*3600)+(m*60))
print(f"\n{h} hours : {m} minuts : {s} seconds\n")