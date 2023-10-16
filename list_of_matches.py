#Generate a mach list from the number of Teams joins the competetion

number_of_maches = int(input("Enter The Number of Matches>>: "))
for i in range(1,number_of_maches+1):
    for j in range(1,number_of_maches+1):
        if i == j :
            continue
        print(f"\nTeam{i} VS Team{j}\n")