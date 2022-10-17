# 6. COLLEGE ADDMISSION 
# WAP to check if stident is elegible for admission
# is he completed ssc ??
# if yes check elegibility criteria as per percentage

ssc = input("Do you completed SSC ? (Y/N) : ")
if ssc == "Y":
    per = float(input("Enter your percentage : "))
    if per >= 65.00:
        print("You are elegible for admission")
    else:
        print("You are not in a merit list")
else:
    print("You are not elegible for admission process")
