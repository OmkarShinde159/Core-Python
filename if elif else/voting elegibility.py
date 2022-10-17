5. VOTING ELEGIBILITY

age = int(input("Enter your age: "))
if age >= 18:
    voter = input("Do you have voter ID card (Y/N): ")
    if voter == "Y":
        print("You are elegible")
    else:
        print("You are not elegible")
else:
    print("You are not elegible")
